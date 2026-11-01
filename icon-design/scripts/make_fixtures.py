#!/usr/bin/env python3
"""Generate original deterministic diagnostic art, not derived from course assets."""
import argparse, hashlib, json, platform
from pathlib import Path
from PIL import Image, __version__ as pillow_version

def generate(dest):
    dest=Path(dest);dest.mkdir(parents=True,exist_ok=False)
    specs=[]
    for name,size,fn,expect in [
        ('alpha-ramp',(16,16),lambda x,y:(240,40,120,x*17),'alpha extrema 0..255; 224 partial pixels'),
        ('empty',(16,16),lambda x,y:(0,0,0,0),'empty alpha must fail build'),
        ('one-pixel',(1,1),lambda x,y:(255,255,255,255),'valid smallest input; edge contact'),
        ('nonsquare',(16,8),lambda x,y:(255,0,0,255),'source rejected rather than distorted'),
        ('full-bleed',(16,16),lambda x,y:(20,120,90,255),'opaque; edge warning is intentional'),
        ('transparent-border',(16,16),lambda x,y:(255,255,255,255 if 3<=x<13 and 3<=y<13 else 0),'alpha bbox [3,3,13,13]; no edge'),
    ]:
        im=Image.new('RGBA',size);im.putdata([fn(x,y) for y in range(size[1]) for x in range(size[0])]);path=dest/(name+'.png');im.save(path)
        specs.append({'file':path.name,'dimensions':size,'mode':'RGBA','expected':expect,'sha256':hashlib.sha256(path.read_bytes()).hexdigest()})
    svg='<svg xmlns="http://www.w3.org/2000/svg" viewBox="0 0 64 64"><defs><filter id="b" x="-1" y="-1" width="3" height="3"><feGaussianBlur stdDeviation="3"/></filter><clipPath id="c"><rect x="34" y="10" width="20" height="44"/></clipPath></defs><g id="01-blur"><circle cx="17" cy="32" r="7" fill="#e89e36" filter="url(#b)"/></g><g id="02-clip" clip-path="url(#c)"><circle cx="40" cy="32" r="17" fill="#448fc7"/></g></svg>'
    (dest/'renderer-probe.svg').write_text(svg)
    specs.append({'file':'renderer-probe.svg','dimensions':[64,64],'expected':'soft alpha at 7,32; clip removes 33,32 but retains 34,32','sha256':hashlib.sha256(svg.encode()).hexdigest()})
    (dest/'malformed.svg').write_text('<svg><broken>')
    specs.append({'file':'malformed.svg','expected':'XML parse failure','sha256':hashlib.sha256(b'<svg><broken>').hexdigest()})
    (dest/'fixture-manifest.json').write_text(json.dumps({'generator':'scripts/make_fixtures.py','schema':1,'seed':None,'determinism':'No random operations. PNG bytes scoped to recorded Pillow version.','python':platform.python_version(),'pillow':pillow_version,'fixtures':specs},indent=2)+'\n')
    return specs
if __name__=='__main__':
    p=argparse.ArgumentParser();p.add_argument('new_directory');a=p.parse_args();generate(a.new_directory)
