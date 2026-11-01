// Adapter kept separate so Python owns manifest validation and output policy.
const fs = require('node:fs');
const sharp = require(process.env.ICON_SHARP_MODULE || 'sharp');
(async () => {
  if (process.argv[2] === '--versions') { console.log(JSON.stringify(sharp.versions)); return; }
  const [src, dst, size] = process.argv.slice(2);
  await sharp(fs.readFileSync(src), {density: 72, limitInputPixels: 67108864})
    .resize(Number(size), Number(size), {fit:'fill', kernel:'lanczos3'})
    .toColourspace('srgb').ensureAlpha().png().toFile(dst);
})().catch(e => { console.error(e.message); process.exit(1); });
