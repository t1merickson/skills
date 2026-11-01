#!/usr/bin/env python3
"""From-scratch study of Sebastiaan de With's Icon Resource course composition.
No reference-image pixels or PSD paths are imported. Deterministic SVG construction.
"""
from pathlib import Path
import random,json
OUT=Path(__file__).resolve().parent
rng=random.Random(19)
DEFS='''
<linearGradient id="backPaper" x1="0" y1="0" x2="1" y2="1"><stop stop-color="#e8dcbb"/><stop offset=".55" stop-color="#dbcb9f"/><stop offset="1" stop-color="#f2e8ca"/></linearGradient>
<linearGradient id="blueBase" x1="0" y1=".4" x2="1" y2=".55"><stop stop-color="#559bda"/><stop offset=".45" stop-color="#3976bf"/><stop offset="1" stop-color="#294b86"/></linearGradient>
<linearGradient id="blueSweep" x1="0" y1="1" x2="1" y2="0"><stop stop-color="#a5c9e7"/><stop offset="1" stop-color="#5b96d5"/></linearGradient>
<linearGradient id="paperEdge" x1="0" y1="0" x2="1" y2="1"><stop stop-color="#ffffff"/><stop offset=".6" stop-color="#e5e6e6"/><stop offset="1" stop-color="#f9fbfe"/></linearGradient>
<linearGradient id="curl" gradientUnits="userSpaceOnUse" x1="370" y1="24" x2="337" y2="76"><stop stop-color="#7f7f7b"/><stop offset=".27" stop-color="#ddddda"/><stop offset=".68" stop-color="#f9f9f7"/><stop offset="1" stop-color="#ffffff"/></linearGradient>
<linearGradient id="curlEdge" x1="0" y1="0" x2="0" y2="1"><stop stop-color="#fafaf6"/><stop offset="1" stop-color="#92948f"/></linearGradient>
<linearGradient id="pencilYellow" x1="0" y1="0" x2="0" y2="1"><stop stop-color="#fbd247"/><stop offset=".2" stop-color="#ffd945"/><stop offset=".43" stop-color="#f4b900"/><stop offset=".63" stop-color="#ecad00"/><stop offset=".8" stop-color="#d69500"/><stop offset="1" stop-color="#8d5900"/></linearGradient>
<linearGradient id="wood" x1="0" y1="0" x2="0" y2="1"><stop stop-color="#d6b46f"/><stop offset=".28" stop-color="#fae2a9"/><stop offset=".5" stop-color="#e1bd7c"/><stop offset="1" stop-color="#9a743b"/></linearGradient>
<linearGradient id="graphite" x1="0" y1="0" x2="0" y2="1"><stop stop-color="#686c60"/><stop offset=".35" stop-color="#41453b"/><stop offset=".6" stop-color="#101812"/><stop offset="1" stop-color="#090c08"/></linearGradient>
<linearGradient id="silver" x1="0" y1="0" x2="0" y2="1"><stop stop-color="#737975"/><stop offset=".19" stop-color="#d7dad6"/><stop offset=".4" stop-color="#fcfff9"/><stop offset=".56" stop-color="#d0d4cf"/><stop offset=".8" stop-color="#b1b6b1"/><stop offset="1" stop-color="#707773"/></linearGradient>
<radialGradient id="eraser" cx=".55" cy=".16" r="1"><stop stop-color="#f6c0ed"/><stop offset=".46" stop-color="#e184d2"/><stop offset="1" stop-color="#b851ae"/></radialGradient>
<linearGradient id="redPaint" x1="0" y1="0" x2="0" y2="1"><stop stop-color="#b72e09"/><stop offset=".16" stop-color="#f36437"/><stop offset=".29" stop-color="#ff7643"/><stop offset=".5" stop-color="#e7370b"/><stop offset=".74" stop-color="#c41d04"/><stop offset="1" stop-color="#720d02"/></linearGradient>
<linearGradient id="redHighlight" x1="0" y1="0" x2="1" y2="0"><stop stop-color="#fff8dc" stop-opacity=".98"/><stop offset=".67" stop-color="#ffe2c3" stop-opacity=".9"/><stop offset="1" stop-color="#ffca92" stop-opacity=".12"/></linearGradient>
<linearGradient id="bristles" x1="0" y1="0" x2="0" y2="1"><stop stop-color="#a87526"/><stop offset=".2" stop-color="#e3be73"/><stop offset=".5" stop-color="#d4a64e"/><stop offset=".78" stop-color="#f1ce8e"/><stop offset="1" stop-color="#a57222"/></linearGradient>
<linearGradient id="bristleRoot" x1="0" y1="0" x2="1" y2="0"><stop stop-color="#73511e" stop-opacity="0"/><stop offset=".7" stop-color="#684819" stop-opacity="0"/><stop offset="1" stop-color="#684819" stop-opacity=".6"/></linearGradient>
<filter id="broadShadow" x="-.2" y="-.2" width="1.4" height="1.4"><feGaussianBlur stdDeviation="4"/></filter>
<filter id="toolShadow" x="-.25" y="-1" width="1.5" height="3"><feGaussianBlur stdDeviation="2.6"/></filter>
<filter id="contact" x="-.2" y="-.5" width="1.4" height="2"><feGaussianBlur stdDeviation=".8"/></filter>
<filter id="foldShadow" x="-.4" y="-.6" width="1.8" height="2.2"><feGaussianBlur stdDeviation="5"/></filter>
<clipPath id="pageClip"><path d="M73 48 L290 10 C308 7 313 23 320 79 C350 72 374 65 385 67 C403 67 409 75 414 94 L475 410 L140 470Z"/></clipPath>
<clipPath id="woodClip"><path d="M12 0 L51-12 Q55-9 52-6 Q58-3 54 0 Q58 4 53 6 Q56 10 51 12Z"/></clipPath>
<path id="brushHair" d="M2-10 Q5-15 11-14 C32-13 53-11 80-9 L80 9 C50 10 29 15 10 15 Q4 14 2 10 L0 5 L1 1 L0-3Z"/>
<clipPath id="hairClip"><use href="#brushHair"/></clipPath>
'''
PAGE_SHAPE='M69 44 L290 6 Q305 3 318 12 L398 58 Q409 64 414 91 L480 414 L137 476Z'
BACK='M26 108 L287 14 L494 365 L184 501Z'
BACK_GROUP=f'''<g id="01-back-paper"><path d="{BACK}" transform="translate(2 3)" fill="#000" opacity=".38" filter="url(#broadShadow)"/><path d="{BACK}" fill="url(#backPaper)" stroke="#b9aa83" stroke-width="1.5"/></g>'''
PAGE_GROUP=f'''<g id="02-document"><path d="{PAGE_SHAPE}" transform="translate(1 5)" fill="#000" opacity=".5" filter="url(#broadShadow)"/><path d="{PAGE_SHAPE}" fill="#737775"/><path d="M70 44 L291 7 Q305 4 318 13 L397 59 Q408 65 413 91 L479 413 L138 474Z" fill="url(#paperEdge)"/>
<g clip-path="url(#pageClip)"><path d="M64-5 H440 L492 474 H112Z" fill="url(#blueBase)"/>
<path d="M258 5 C237 68 226 111 237 175 C254 279 221 357 128 397 L137 470 C246 458 299 379 283 277 C266 165 275 90 315 37 L316-3Z" fill="url(#blueSweep)" opacity=".65"/>
<path d="M317 22 C277 79 270 131 279 186 C297 276 316 325 289 392 C310 355 342 318 337 264 C333 215 310 171 313 140 C313 103 342 83 366 66Z" fill="#2458ad" opacity=".52"/>
<path d="M322 81 Q375 61 393 72 Q409 81 415 99 L401 68 Q383 52 320 74Z" fill="#081c38" opacity=".46" filter="url(#foldShadow)"/>
</g>
<path d="M287 8 C309 1 314 25 320 79 C341 75 365 68 379 66 C399 62 410 73 415 95 L409 72 Q407 62 397 57 L316 10 Q305 3 287 8Z" fill="url(#curl)"/>
<path d="M299 7 Q308 4 319 12 L397 58 Q407 65 410 78" fill="none" stroke="url(#curlEdge)" stroke-width="1.1"/>
</g>'''
# Pencil body stays in one coordinate frame; wood and paint share the same cut.
wood_lines=[]
for i in range(27):
 y=-12+i*24/26;end=rng.uniform(3,16);wood_lines.append(f'<path d="M{end:.2f} {y*.08:.2f} Q31 {y*.55:.2f} 57 {y:.2f}" stroke="{rng.choice(["#795628","#fff0bc","#aa803f"])}" stroke-opacity="{rng.uniform(.08,.25):.3f}" stroke-width="{rng.uniform(.25,.65):.3f}" fill="none"/>')
PENCIL='''<path d="M0 0 L51-12 H345 Q368-12 368 0 Q368 12 345 12 H51Z" fill="#000" opacity=".33" filter="url(#toolShadow)" transform="translate(-1 4)"/>
<path d="M12 0 L51-12 Q55-9 52-6 Q58-3 54 0 Q58 4 53 6 Q56 10 51 12Z" fill="url(#wood)"/>
<g clip-path="url(#woodClip)">'''+''.join(wood_lines)+'''</g>
<path d="M51-12 H323 V12 H51 Q56 10 53 6 Q58 4 54 0 Q58-3 52-6 Q55-9 51-12Z" fill="url(#pencilYellow)"/>
<path d="M53-7 H323 V-4 H55Z" fill="#ffe563" opacity=".75"/>
<path d="M54 4 H323 V12 H51 Q56 10 53 6Z" fill="#986600" opacity=".33"/>
<path d="M0 0 L15-3.8 L13 1.4 L15 3.8Z" fill="url(#graphite)"/>
<path d="M2-.2 L14-3.5 L13-1.9Z" fill="#bcc0a0" opacity=".65"/>
<path d="M322-12 H344 V12 H322Z" fill="url(#silver)"/>
<path d="M325-11 V11 M340-11 V11" fill="none" stroke="#777f77" stroke-opacity=".15" stroke-width=".6"/>
<path d="M344-12 H355 Q368-12 368 0 Q368 12 355 12 H344Z" fill="url(#eraser)"/>
<path d="M344-11 H355 Q365-11 366-3" fill="none" stroke="#f9d5f1" stroke-opacity=".38" stroke-width=".8"/>
'''
# Individual fibers fan from ferrule to tip; bounded deterministic irregularity.
hairs=[]
for i in range(52):
 v=(i+.5)/52;end=-13+v*27;root=-8.6+v*17.2
 x0=rng.uniform(.2,5);bend=end+rng.uniform(-1,1)
 hairs.append(f'<path d="M{x0:.2f} {end:.2f} C23 {bend:.2f} 53 {root:.2f} 81 {root:.2f}" stroke="{rng.choice(["#865119","#fff1c6","#a77327","#eac782","#bf8c38"])}" stroke-opacity="{rng.uniform(.48,.92):.3f}" stroke-width="{rng.uniform(.35,.8):.3f}" fill="none"/>')
HANDLE='M103-12 C188-13 352-9 447-6 Q460-5 458 2 Q457 7 448 7 C331 10 193 15 104 12 Q98 6 103-12Z'
BRUSH=f'''<path d="M0-13 L79-9 L105-12 L451-6 Q461 0 451 7 L104 12 L79 9 L8 15Z" fill="#000" opacity=".38" filter="url(#toolShadow)" transform="translate(0 4)"/>
<use href="#brushHair" fill="url(#bristles)"/><g clip-path="url(#hairClip)">{''.join(hairs)}<use href="#brushHair" fill="url(#bristleRoot)"/></g>
<path d="M78-9 Q90-11 103-12 Q106-5 108 10 Q94 11 78 9Z" fill="url(#silver)"/>
<path d="M79-8 Q91-10 101-11" fill="none" stroke="#f5f7ed" stroke-opacity=".8" stroke-width=".8"/>
<path d="{HANDLE}" fill="url(#redPaint)" stroke="#991900" stroke-width=".5"/>
<path d="M115-8 C206-8 353-6 448-3 C355-2 215-1 118 1 Q108 1 109-4 Q110-7 115-8Z" fill="url(#redHighlight)"/>
<path d="M111 10 C203 12 349 8 448 5" fill="none" stroke="#720e03" stroke-opacity=".55" stroke-width="1.1"/>
'''

def svg(body,title):return f'<svg xmlns="http://www.w3.org/2000/svg" width="512" height="512" viewBox="0 0 512 512"><title>{title}</title><defs>{DEFS}</defs>{body}</svg>\n'
full=BACK_GROUP+PAGE_GROUP+f'<g id="03-brush" transform="translate(143 403) rotate(-44.7)">{BRUSH}</g>'+f'<g id="04-pencil" transform="translate(264 438) rotate(-56.6)">{PENCIL}</g>'
(OUT/'course-icon.svg').write_text(svg(full,'Icon Resource course reconstruction — independently authored SVG'))
(OUT/'pencil.svg').write_text(svg(f'<g id="pencil" transform="translate(52 256) scale(1.1)">{PENCIL}</g>','Course pencil construction study'))
(OUT/'brush.svg').write_text(svg(f'<g id="brush" transform="translate(26 256)">{BRUSH}</g>','Course red brush construction study'))
(OUT/'document.svg').write_text(svg(PAGE_GROUP,'Course curled document construction study'))
# Separate optical redraws: upright page, enlarged fold, no rear sheet.
# The course changes construction at small sizes; do not just scale the full composition.
for n in (32,16):
    k=n/32
    body='''<g id="small-document"><path d="M5.5 2.5H21L27.5 9V29.5H5.5Z" fill="#3978bd" stroke="#e9eef3"/>
    <path d="M18 3C13 10 21 22 6 27V29H13C26 24 17 13 23 7Z" fill="#79a5d5" opacity=".7"/>
    <path d="M21 3V9H27" fill="#fff" stroke="#c4cbd2" stroke-width=".6"/></g>
    <g id="small-brush" transform="translate(7 25) rotate(-45)">
    <path d="M0-1.2H5V1.2H0Z" fill="#d7ae61" stroke="#8f6b2d" stroke-width=".4"/>
    <path d="M1-.5H5M1 .5H5" stroke="#fff0b4" stroke-width=".35"/>
    <path d="M5-1.15H7.5V1.15H5Z" fill="#dbe0df" stroke="#6e7a7e" stroke-width=".35"/>
    <path d="M7.5-1.25L31-.7Q32 0 31 .7L7.5 1.25Z" fill="#d7320b" stroke="#802003" stroke-width=".4"/>
    <path d="M8-.6L30-.2" stroke="#ffce94" stroke-width=".7"/></g>
    <g id="small-pencil" transform="translate(17 27) rotate(-56.6)">
    <path d="M0 0L3.5-1H20V1H3.5Z" fill="#efb51b" stroke="#956314" stroke-width=".4"/>
    <path d="M0 0L3.5-1V1Z" fill="#e8ca91"/><path d="M0 0L1.2-.35V.35Z" fill="#202b25"/>
    <path d="M4-.5H18" stroke="#fff188" stroke-width=".55"/>
    <path d="M18-1H20V1H18Z" fill="#e2e6df"/><path d="M20-1H21Q22 0 21 1H20Z" fill="#df82ca"/></g>'''
    if n==16:
        body=body.replace('stroke-width=".4"','stroke-width=".65"').replace('stroke-width=".35"','stroke-width=".6"')
    (OUT/f'course-{n}.svg').write_text(f'<svg xmlns="http://www.w3.org/2000/svg" width="{n}" height="{n}" viewBox="0 0 32 32"><title>Course exercise — optical redraw {n}px</title>{body}</svg>\n')
rows=[]
for n in (512,256,128,32,16):rows.append({'id':f'course-{n}','pixels':n,'source':f'course-{n}.svg' if n<128 else 'course-icon.svg','alpha':'allowed'})
for name in ('pencil','brush','document'):rows.append({'id':name+'-512','pixels':512,'source':name+'.svg','alpha':'allowed','appearance':name})
(OUT/'manifest.json').write_text(json.dumps({'schema':1,'attribution':'From-scratch study of Sebastiaan de With, Icon Resource; reference supplied by user. No embedded course pixels or extracted paths.','resources':rows},indent=2)+'\n')
print('wrote full icon, optical redraws, and three component studies')
