#!/usr/bin/env python3
"""Explicit optical sources -> sRGB PNGs -> offline inspection -> optional ICNS.
Requires Pillow, Node and sharp. No source mutation; every output directory is new.
"""
import argparse, base64, hashlib, html, json, math, os, re, shutil, subprocess, sys, tempfile, struct
from pathlib import Path
from xml.etree import ElementTree as ET
from PIL import Image, ImageCms, ImageChops

HERE = Path(__file__).resolve().parent
SCHEMA = 1
ET.register_namespace("", "http://www.w3.org/2000/svg")

def digest(path):
    return hashlib.sha256(Path(path).read_bytes()).hexdigest()

def write_json(path, data):
    Path(path).write_text(json.dumps(data, indent=2, ensure_ascii=False)+'\n')

def fresh(path):
    p=Path(path).resolve()
    p.mkdir(parents=True, exist_ok=False)
    return p

def safe_name(name):
    if not isinstance(name,str) or not re.fullmatch(r'[A-Za-z0-9][A-Za-z0-9_-]{0,79}',name):
        raise ValueError('id must be a short ASCII filename stem')
    return name

def svg_check(path):
    raw=Path(path).read_text()
    if re.search(r'<!DOCTYPE|<!ENTITY',raw,re.I): raise ValueError('SVG entities/DOCTYPE are unsupported')
    root=ET.fromstring(raw)
    if root.tag.split('}')[-1]!='svg': raise ValueError('expected SVG root')
    vb=[float(x) for x in re.split(r'[\s,]+',root.get('viewBox','').strip()) if x]
    if len(vb)!=4 or not all(math.isfinite(x) for x in vb) or vb[2]<=0 or vb[2]!=vb[3]:
        raise ValueError('SVG needs finite positive square viewBox; do not distort nonsquare art')
    allowed={'svg','defs','g','path','rect','circle','ellipse','line','polyline','polygon',
             'linearGradient','radialGradient','stop','clipPath','mask','filter','feGaussianBlur',
             'feOffset','feMerge','feMergeNode','feColorMatrix','feComposite','feBlend','feFlood',
             'use','title','desc'}
    for e in root.iter():
        tag=e.tag.split('}')[-1]
        if tag not in allowed: raise ValueError(f'unsupported SVG element {tag}; outline text or flatten explicitly')
        for key,val in e.attrib.items():
            k=key.split('}')[-1]
            if k.startswith('on'):raise ValueError('SVG event handlers unsupported')
            if k=='href' and not val.startswith('#'): raise ValueError('external SVG references unsupported')
            if 'url(' in val and re.search(r'url\(\s*[\x22\x27]?(?!#)[^\s]',val):
                raise ValueError('only local fragment URLs supported')
    return root

def source_check(path):
    if path.suffix.lower()=='.svg': svg_check(path)
    elif path.suffix.lower()=='.png':
        with Image.open(path) as im:
            if im.width!=im.height or im.width<1: raise ValueError('PNG source must be square')
            if im.width*im.height>67108864:raise ValueError('source exceeds pixel limit')
    else: raise ValueError('source must be SVG or PNG')

def load_manifest(path):
    path=Path(path).resolve();m=json.loads(path.read_text())
    if m.get('schema')!=SCHEMA:raise ValueError('unsupported schema')
    rows=m.get('resources',[])
    if not rows or len(rows)>100:raise ValueError('require 1..100 resources')
    ids=set(); slots=set()
    for r in rows:
        rid=safe_name(r['id'])
        if rid.casefold() in ids:raise ValueError('duplicate id')
        ids.add(rid.casefold())
        size=r['pixels']
        if type(size)!=int or not 1<=size<=4096:raise ValueError('pixels must be integer 1..4096')
        points=r.get('points');scale=r.get('scale')
        if points is not None or scale is not None:
            if type(points) not in (int,float) or type(scale) not in (int,float) or points<=0 or scale not in (1,2,3) or points*scale!=size:
                raise ValueError('points * scale must equal pixels; scale 1,2,3')
        slot=(r.get('platform','study'),r.get('appearance','default'),points,scale,size)
        if slot in slots:raise ValueError('duplicate platform/appearance/size/scale slot')
        slots.add(slot)
        if r.get('alpha','allowed') not in ('allowed','opaque'):raise ValueError('alpha must be allowed or opaque')
        src=(path.parent/r['source']).resolve()
        if not src.is_relative_to(path.parent):raise ValueError('source must stay within manifest directory')
        source_check(src);r['_source']=src
    return m

def inspect(path):
    with Image.open(path) as src:
        fmt=src.format; im=src.convert('RGBA');alpha=im.getchannel('A'); hist=alpha.histogram();bbox=alpha.getbbox()
        px=list(alpha.tobytes());total=sum(px);w,h=im.size
        centroid=[sum((i%w)*a for i,a in enumerate(px))/total,sum((i//w)*a for i,a in enumerate(px))/total] if total else None
        edge=max(list(alpha.crop((0,0,w,1)).tobytes())+list(alpha.crop((0,h-1,w,h)).tobytes())+list(alpha.crop((0,0,1,h)).tobytes())+list(alpha.crop((w-1,0,w,h)).tobytes()))
        return {'format':fmt,'pixels':[w,h],'mode':src.mode,'sha256':digest(path),'alpha_bbox':bbox,
                'alpha_extrema':alpha.getextrema(),'alpha_coverage':round(total/(255*w*h),6),
                'alpha_centroid':centroid,'edge_alpha_max':edge,'partial_alpha_pixels':sum(hist[1:255]),
                'icc_profile':bool(src.info.get('icc_profile')),
                'warnings':(['empty alpha'] if not total else [])+(['edge contact: inspect clipping or intended full bleed'] if edge else [])}

def build(manifest,out):
    m=load_manifest(manifest);node=os.environ.get('ICON_NODE','node')
    versions=json.loads(subprocess.check_output([node,str(HERE/'render.cjs'),'--versions'],text=True))
    dest=fresh(out);results=[]
    try:
        for r in m['resources']:
            src=r.pop('_source');target=dest/(r['id']+'.png')
            with tempfile.TemporaryDirectory(prefix='icon-render-') as temp:
                render_source=src
                if src.suffix.lower()=='.svg':
                    tree=svg_check(src);tree.set('width',str(r['pixels']));tree.set('height',str(r['pixels']))
                    render_source=Path(temp)/'source.svg'
                    ET.ElementTree(tree).write(render_source,encoding='utf-8',xml_declaration=True)
                subprocess.run([node,str(HERE/'render.cjs'),str(render_source),str(target),str(r['pixels'])],check=True)
            # Tag predictable sRGB; decoder output is already converted by sharp.
            with Image.open(target) as im:
                im.save(target,icc_profile=ImageCms.ImageCmsProfile(ImageCms.createProfile('sRGB')).tobytes())
            checks=inspect(target)
            if not checks['alpha_bbox']:raise ValueError(r['id']+': empty alpha')
            if r.get('alpha')=='opaque' and checks['alpha_extrema'][0]!=255:raise ValueError(r['id']+': opaque contract failed')
            if checks['pixels']!=[r['pixels']]*2:raise ValueError('renderer dimensions mismatch')
            results.append({**r,'file':target.name,'source_sha256':digest(src),'checks':checks})
        receipt={'schema':SCHEMA,'manifest_sha256':digest(manifest),'renderer':versions,'resources':results}
        write_json(dest/'receipt.json',receipt);gallery(dest/'receipt.json',dest/'review.html')
        return receipt
    except Exception as e:
        write_json(dest/'FAILED.json',{'error':str(e),'completed':results})
        raise

def verify(manifest,receipt):
    m=load_manifest(manifest);p=Path(receipt);r=json.loads(p.read_text())
    if r['manifest_sha256']!=digest(manifest):raise ValueError('manifest changed since build')
    if len(m['resources'])!=len(r['resources']):raise ValueError('receipt resource count mismatch')
    for spec,built in zip(m['resources'],r['resources']):
        if spec['id']!=built['id'] or digest(spec['_source'])!=built['source_sha256']:raise ValueError('source changed since build')
        name=built['file']
        if Path(name).name!=name:raise ValueError('unsafe receipt filename')
        checks=inspect(p.parent/name)
        if checks['sha256']!=built['checks']['sha256'] or checks['pixels']!=[spec['pixels']]*2:raise ValueError('output changed since build')
    return {'verified':True,'resources':len(r['resources'])}

def gallery(receipt,out):
    p=Path(receipt);r=json.loads(p.read_text());cards=[]
    for row in r['resources']:
        name=row['file']
        if Path(name).name!=name:raise ValueError('unsafe receipt filename')
        raw=(p.parent/name).read_bytes();uri='data:image/png;base64,'+base64.b64encode(raw).decode();n=row['pixels'];pt=row.get('points',n)
        with Image.open(p.parent/name) as im:
            import io
            b=io.BytesIO();im.convert('RGBA').getchannel('A').save(b,format='PNG');a='data:image/png;base64,'+base64.b64encode(b.getvalue()).decode()
        title=html.escape(row['id']);detail=html.escape(json.dumps(row['checks'],indent=2))
        cards.append(f'<article><h2>{title}</h2><p>{n}px; intended {pt}pt. Source: {html.escape(row["source"])}</p><div class="well"><img alt="{title} at intended size" src="{uri}" width="{pt}" height="{pt}"></div><details><summary>Pixels and alpha</summary><div class="pixel well"><img alt="magnified color" src="{uri}" width="{min(n*8,512)}"><img alt="alpha, white opaque" src="{a}" width="{min(n*8,512)}"></div><pre>{detail}</pre></details></article>')
    page='''<!doctype html><meta charset="utf-8"><meta name="viewport" content="width=device-width"><meta http-equiv="Content-Security-Policy" content="default-src 'none'; img-src data:; style-src 'unsafe-inline'; script-src 'unsafe-inline'"><title>Icon inspection</title><style>body{font:15px system-ui;margin:24px;background:#eee;color:#222}header{position:sticky;top:0;background:#eee;padding:12px;border-bottom:1px solid #aaa}main{display:flex;flex-wrap:wrap;gap:16px}article{background:white;padding:16px;border:1px solid #aaa;max-width:1100px;overflow:auto}h2{font-size:16px}.well{background:var(--bg,#888);padding:20px;display:flex;align-items:center;justify-content:center;min-width:80px;min-height:80px}.pixel img{image-rendering:pixelated}pre{font-size:11px;white-space:pre-wrap}button,input{font:inherit;margin:4px}</style><header><h1>Icon inspection</h1><p>Actual CSS size first. Browser zoom and display density affect physical pixels. Alpha metrics are diagnostics, not taste scores. This is a static raster preview, not Apple's material renderer.</p><label>Background <input type="color" value="#888888" id="bg"></label><button data-color="#ffffff">White</button><button data-color="#161616">Dark</button><button data-color="#ef00c8">Magenta</button><button data-color="#888888">Gray</button></header><main>'''+''.join(cards)+'''</main><script>const set=c=>document.documentElement.style.setProperty('--bg',c);document.getElementById('bg').oninput=e=>set(e.target.value);document.querySelectorAll('button').forEach(b=>b.onclick=()=>set(b.dataset.color));</script>'''
    Path(out).write_text(page)

def icns(manifest,receipt,out,encoding="png"):
    verify(manifest,receipt);p=Path(receipt);r=json.loads(p.read_text());slots={}
    for row in r['resources']:
        if row.get('platform')=='macos' and row.get('appearance','default')=='default':slots[(row.get('points'),row.get('scale'))]=row
    need=[(pt,s) for pt in (16,32,128,256,512) for s in (1,2)]
    if any(k not in slots for k in need):raise ValueError('ICNS requires macos default slots: 16,32,128,256,512 points each at 1x and 2x')
    dest=fresh(out);iset=dest/'AppIcon.iconset';iset.mkdir()
    for pt,s in need:shutil.copyfile(p.parent/slots[(pt,s)]['file'],iset/f'icon_{pt}x{pt}{"@2x" if s==2 else ""}.png')
    if encoding=='native':
        subprocess.run(['iconutil','-c','icns',str(iset),'-o',str(dest/'AppIcon.icns')],check=True)
    else:
        # Modern PNG resource codes, independently represented logical slots.
        codes={(16,1):b'icp4',(16,2):b'ic11',(32,1):b'icp5',(32,2):b'ic12',
               (128,1):b'ic07',(128,2):b'ic13',(256,1):b'ic08',(256,2):b'ic14',
               (512,1):b'ic09',(512,2):b'ic10'}
        chunks=[]
        for slot in need:
            data=(p.parent/slots[slot]['file']).read_bytes()
            chunks.append(struct.pack('>4sI',codes[slot],len(data)+8)+data)
        payload=b''.join(chunks)
        (dest/'AppIcon.icns').write_bytes(struct.pack('>4sI',b'icns',len(payload)+8)+payload)
    subprocess.run(['iconutil','-c','iconset',str(dest/'AppIcon.icns'),'-o',str(dest/'roundtrip.iconset')],check=True)
    # Container round-trip may choose one representation where logical slots share a pixel size.
    decoded=[]
    for q in sorted((dest/'roundtrip.iconset').glob('*.png')):decoded.append({'file':q.name,**inspect(q)})
    expected={q.name for q in iset.glob('*.png')}
    actual={q.name for q in (dest/'roundtrip.iconset').glob('*.png')}
    if expected!=actual:raise ValueError('ICNS roundtrip slot mismatch')
    differences=[]
    for name in sorted(expected):
        with Image.open(iset/name) as a, Image.open(dest/'roundtrip.iconset'/name) as b:
            if a.size!=b.size:raise ValueError('ICNS roundtrip dimension mismatch: '+name)
            extrema=ImageChops.difference(a.convert('RGBA'),b.convert('RGBA')).getextrema()
            if any(hi for lo,hi in extrema):differences.append({'file':name,'rgba_max_delta':[hi for lo,hi in extrema]})
    # Independent decoder verifies each logical resource, including equal-pixel-size slots.
    if encoding=='png':
        from PIL.IcnsImagePlugin import IcnsFile
        with open(dest/'AppIcon.icns','rb') as f:
            decoder=IcnsFile(f)
            for pt,scale in need:
                got=decoder.getimage((pt,pt,scale)).convert('RGBA')
                with Image.open(p.parent/slots[(pt,scale)]['file']) as wanted:
                    if got.size!=wanted.size or any(hi for lo,hi in ImageChops.difference(got,wanted.convert('RGBA')).getextrema()):
                        raise ValueError('independent ICNS decode mismatch')
    write_json(dest/'package-receipt.json',{'encoding':encoding,'sha256':digest(dest/'AppIcon.icns'),'decoded':decoded,'native_rgba_differences':differences,'independent_png_decode':'exact' if encoding=='png' else 'not run','context_acceptance':'not tested'})
    return {'icns':str(dest/'AppIcon.icns'),'decoded':len(decoded),'native_rgba_differences':len(differences),'context_acceptance':'not tested'}

def layers(source,out):
    root=svg_check(source);ns='{http://www.w3.org/2000/svg}';groups=[e for e in root if e.tag==ns+'g']
    if not groups:raise ValueError('need top-level named groups')
    names=[safe_name(e.get('id')) for e in groups]
    if len(set(names))!=len(names):raise ValueError('duplicate layer names')
    dest=fresh(out)
    import copy
    rows=[]
    for n,g in zip(names,groups):
        new=ET.Element(root.tag,root.attrib)
        for d in root:
            if d.tag in (ns+'defs',ns+'title',ns+'desc'):new.append(copy.deepcopy(d))
        new.append(copy.deepcopy(g));q=dest/(n+'.svg');ET.ElementTree(new).write(q,encoding='utf-8',xml_declaration=True)
        rows.append({'file':q.name,'sha256':digest(q)})
    write_json(dest/'layers.json',{'source_sha256':digest(source),'layers':rows,'note':'Same canvas preserved. Tool does not remove baked effects or create .icon files. Review layer dependencies and import into Icon Composer.'})
    return {'layers':len(rows)}

def main():
    p=argparse.ArgumentParser(description=__doc__);s=p.add_subparsers(dest='cmd',required=True)
    for name in ['build','verify','icns']:
        q=s.add_parser(name);q.add_argument('manifest');q.add_argument('receipt' if name!='build' else 'out')
        if name=='icns':
            q.add_argument('out');q.add_argument('--encoding',choices=['png','native'],default='png')
    q=s.add_parser('inspect');q.add_argument('png')
    q=s.add_parser('layers');q.add_argument('svg');q.add_argument('out')
    a=p.parse_args()
    try:
        if a.cmd=='build':r=build(a.manifest,a.out);r={'built':len(r['resources']),'out':a.out}
        elif a.cmd=='verify':r=verify(a.manifest,a.receipt)
        elif a.cmd=='icns':r=icns(a.manifest,a.receipt,a.out,a.encoding)
        elif a.cmd=='layers':r=layers(a.svg,a.out)
        else:r=inspect(a.png)
        print(json.dumps(r,indent=2))
    except (ValueError,OSError,KeyError,ET.ParseError,subprocess.CalledProcessError) as e:
        print('iconkit: '+str(e),file=sys.stderr);return 1
    return 0
if __name__=='__main__':sys.exit(main())
