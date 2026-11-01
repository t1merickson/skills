#!/usr/bin/env python3
import copy,json,os,tempfile,unittest
from pathlib import Path
from PIL import Image
import iconkit as kit
from make_fixtures import generate

class Contracts(unittest.TestCase):
 def setUp(self):
  self.t=tempfile.TemporaryDirectory();self.p=Path(self.t.name)/'fixtures';generate(self.p)
 def tearDown(self):self.t.cleanup()
 def manifest(self,source='transparent-border.png',**extra):
  m={'schema':1,'resources':[{'id':'test','source':source,'pixels':16,**extra}]};p=self.p/'m.json';kit.write_json(p,m);return p
 def test_alpha_metrics(self):
  x=kit.inspect(self.p/'alpha-ramp.png');self.assertEqual(x['alpha_extrema'],(0,255));self.assertEqual(x['partial_alpha_pixels'],224)
  x=kit.inspect(self.p/'transparent-border.png');self.assertEqual(x['alpha_bbox'],(3,3,13,13));self.assertEqual(x['edge_alpha_max'],0)
 def test_boundaries(self):
  kit.source_check(self.p/'one-pixel.png')
  for f in ('nonsquare.png','malformed.svg'):
   with self.assertRaises(Exception):kit.source_check(self.p/f)
 def test_external_and_script(self):
  for content in ('<script/>','<image href="https://example.com/a.png"/>','<use href="file:///tmp/a.svg"/>','<rect fill="url(https://example.com/a)"/>'):
   p=self.p/'bad.svg';p.write_text('<svg xmlns="http://www.w3.org/2000/svg" viewBox="0 0 16 16">'+content+'</svg>')
   with self.assertRaises(ValueError):kit.svg_check(p)
 def test_slots_and_escape(self):
  p=self.manifest();m=json.loads(p.read_text());m['resources'].append({**m['resources'][0],'id':'different'});kit.write_json(p,m)
  with self.assertRaises(ValueError):kit.load_manifest(p)
  p=self.manifest(points=16,scale=2)
  with self.assertRaises(ValueError):kit.load_manifest(p)
  p=self.manifest(source='../outside.png')
  with self.assertRaises(ValueError):kit.load_manifest(p)
  p=self.manifest();m=json.loads(p.read_text());m['resources'][0]['pixels']=4097;kit.write_json(p,m)
  with self.assertRaises(ValueError):kit.load_manifest(p)
 def test_build_stale_and_collision(self):
  p=self.manifest();out=self.p/'build';kit.build(p,out);kit.verify(p,out/'receipt.json')
  with self.assertRaises(FileExistsError):kit.build(p,out)
  im=Image.new('RGBA',(16,16),'red');im.save(self.p/'transparent-border.png')
  with self.assertRaisesRegex(ValueError,'source changed'):kit.verify(p,out/'receipt.json')
 def test_output_tamper(self):
  p=self.manifest();out=self.p/'build';kit.build(p,out);Image.new('RGBA',(16,16),'blue').save(out/'test.png')
  with self.assertRaisesRegex(ValueError,'output changed'):kit.verify(p,out/'receipt.json')
 def test_alpha_contract(self):
  for name,extra in [('empty.png',{}),('alpha-ramp.png',{'alpha':'opaque'})]:
   with self.assertRaises(ValueError):kit.build(self.manifest(name,**extra),self.p/name.replace('.png','-out'))
 def test_renderer_features(self):
  p=self.manifest('renderer-probe.svg');m=json.loads(p.read_text());m['resources'][0]['pixels']=64;kit.write_json(p,m);out=self.p/'probe';kit.build(p,out)
  with Image.open(out/'test.png') as im:
   a=im.getchannel('A');self.assertTrue(0<a.getpixel((7,32))<255);self.assertEqual(a.getpixel((33,32)),0);self.assertGreater(a.getpixel((34,32)),200)
 def test_layers_preserve_canvas(self):
  out=self.p/'layers';kit.layers(self.p/'renderer-probe.svg',out)
  x=kit.svg_check(out/'02-clip.svg');self.assertEqual(x.get('viewBox'),'0 0 64 64');self.assertEqual(len(list(out.glob('*.svg'))),2)
 def test_fixture_hashes(self):
  x=json.loads((self.p/'fixture-manifest.json').read_text())
  for f in x['fixtures']:self.assertEqual(kit.digest(self.p/f['file']),f['sha256'])
if __name__=='__main__':unittest.main()
