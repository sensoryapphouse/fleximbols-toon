import os

def wrap_svg(defs, content):
    return f"""<svg xmlns="http://www.w3.org/2000/svg" viewBox="0 0 512 512">
  <defs>
    {defs}
  </defs>
  <g stroke="#1a1a1a" stroke-width="6" stroke-linejoin="round" stroke-linecap="round">
    {content}
  </g>
</svg>"""

animals = {}

# 1. Salamander
salamander_defs = """
<linearGradient id="salGrad" x1="0%" y1="0%" x2="100%" y2="100%">
  <stop offset="0%" stop-color="#424242"/>
  <stop offset="100%" stop-color="#212121"/>
</linearGradient>
<radialGradient id="spotGrad" cx="50%" cy="50%" r="50%">
  <stop offset="0%" stop-color="#ffeb3b"/>
  <stop offset="100%" stop-color="#f57f17"/>
</radialGradient>
"""
salamander_content = """
<!-- Legs (drawn behind body) -->
<path d="M 190 270 L 120 380 Q 110 400 130 400 L 150 410 L 160 380 L 210 270 Z" fill="url(#salGrad)"/>
<path d="M 330 270 L 290 380 Q 280 400 300 400 L 320 410 L 330 380 L 350 270 Z" fill="url(#salGrad)"/>
<path d="M 190 230 L 110 180 Q 100 160 120 160 L 140 150 L 150 180 L 210 230 Z" fill="url(#salGrad)"/>
<path d="M 350 230 L 390 180 Q 400 160 380 160 L 360 150 L 350 180 L 330 230 Z" fill="url(#salGrad)"/>
<!-- Tail -->
<path d="M 220 280 C 80 200, 20 300, 60 300 C 80 340, 160 340, 220 320 Z" fill="url(#salGrad)"/>
<!-- Body -->
<ellipse cx="256" cy="270" rx="90" ry="60" fill="url(#salGrad)"/>
<!-- Head (Explicit distinct head shape) -->
<ellipse cx="380" cy="260" rx="55" ry="40" fill="url(#salGrad)"/>
<!-- Spots (No stroke on spots to keep them clean) -->
<circle cx="220" cy="240" r="18" fill="url(#spotGrad)" stroke="none"/>
<circle cx="290" cy="230" r="14" fill="url(#spotGrad)" stroke="none"/>
<circle cx="260" cy="290" r="16" fill="url(#spotGrad)" stroke="none"/>
<circle cx="340" cy="280" r="12" fill="url(#spotGrad)" stroke="none"/>
<circle cx="180" cy="290" r="12" fill="url(#spotGrad)" stroke="none"/>
<!-- Eye -->
<circle cx="390" cy="245" r="10" fill="#ffeb3b" stroke="none"/>
<circle cx="390" cy="245" r="5" fill="#1a1a1a" stroke="none"/>
<circle cx="392" cy="243" r="2" fill="#fff" stroke="none"/>
"""
animals['salamander'] = wrap_svg(salamander_defs, salamander_content)

# 2. Newt
newt_defs = """
<linearGradient id="newtGrad" x1="0%" y1="0%" x2="0%" y2="100%">
  <stop offset="0%" stop-color="#66bb6a"/>
  <stop offset="100%" stop-color="#2e7d32"/>
</linearGradient>
<linearGradient id="bellyGrad" x1="0%" y1="0%" x2="0%" y2="100%">
  <stop offset="0%" stop-color="#ffa726"/>
  <stop offset="100%" stop-color="#ef6c00"/>
</linearGradient>
"""
newt_content = """
<!-- Tail -->
<path d="M 180 260 C 60 220, 40 320, 80 320 C 120 320, 160 320, 180 300 Z" fill="url(#newtGrad)"/>
<!-- Legs (drawn behind body) -->
<path d="M 190 270 L 140 360 Q 130 380 150 380 L 170 390 L 180 360 L 210 270 Z" fill="url(#newtGrad)"/>
<path d="M 330 270 L 300 360 Q 290 380 310 380 L 330 390 L 340 360 L 350 270 Z" fill="url(#newtGrad)"/>
<path d="M 190 240 L 140 180 Q 130 160 150 160 L 170 170 L 180 190 L 210 240 Z" fill="url(#newtGrad)"/>
<path d="M 330 240 L 380 180 Q 390 160 370 160 L 350 170 L 340 190 L 310 240 Z" fill="url(#newtGrad)"/>
<!-- Body -->
<ellipse cx="250" cy="270" rx="80" ry="50" fill="url(#newtGrad)"/>
<!-- Head (Explicit distinct head shape) -->
<ellipse cx="360" cy="255" rx="50" ry="35" fill="url(#newtGrad)"/>
<!-- Belly Stripe (No stroke) -->
<path d="M 180 310 C 230 330, 310 330, 350 290 C 310 315, 230 315, 180 310 Z" fill="url(#bellyGrad)" stroke="none"/>
<!-- Eye -->
<circle cx="370" cy="245" r="8" fill="#1a1a1a" stroke="none"/>
<circle cx="372" cy="243" r="2" fill="#fff" stroke="none"/>
"""
animals['newt'] = wrap_svg(newt_defs, newt_content)

# 3. Quail
quail_defs = """
<linearGradient id="quailBody" x1="0%" y1="0%" x2="100%" y2="100%">
  <stop offset="0%" stop-color="#8d6e63"/>
  <stop offset="100%" stop-color="#4e342e"/>
</linearGradient>
<linearGradient id="quailBelly" x1="0%" y1="0%" x2="0%" y2="100%">
  <stop offset="0%" stop-color="#d7ccc8"/>
  <stop offset="100%" stop-color="#8d6e63"/>
</linearGradient>
"""
quail_content = """
<!-- Legs (Buried into body at y=320) -->
<path d="M 230 320 L 230 410 L 210 430 M 230 410 L 250 430" fill="none" stroke="#ffb300" stroke-width="12"/>
<path d="M 310 320 L 310 410 L 290 430 M 310 410 L 330 430" fill="none" stroke="#ffb300" stroke-width="12"/>
<!-- Body -->
<path d="M 160 280 C 160 180, 380 180, 380 280 C 380 380, 160 380, 160 280 Z" fill="url(#quailBody)"/>
<!-- Belly (Drawn with stroke=none to avoid internal lines) -->
<path d="M 190 280 C 190 350, 350 350, 350 280 C 350 330, 190 330, 190 280 Z" fill="url(#quailBelly)" stroke="none"/>
<!-- Head -->
<circle cx="160" cy="200" r="50" fill="url(#quailBody)"/>
<!-- Plume -->
<path d="M 150 150 Q 140 80 180 100 Q 160 120 160 150 Z" fill="#212121"/>
<!-- Beak -->
<path d="M 110 200 L 80 210 L 115 220 Z" fill="#ffb300"/>
<!-- Eye -->
<circle cx="140" cy="190" r="12" fill="#1a1a1a" stroke="none"/>
<circle cx="143" cy="187" r="4" fill="#fff" stroke="none"/>
<!-- Wing -->
<path d="M 240 240 C 340 240, 340 320, 240 320 C 210 320, 210 240, 240 240 Z" fill="url(#quailBelly)"/>
"""
animals['quail'] = wrap_svg(quail_defs, quail_content)

# 4. Bird (Green)
bird_defs = """
<linearGradient id="birdGrad" x1="0%" y1="0%" x2="100%" y2="100%">
  <stop offset="0%" stop-color="#43a047"/>
  <stop offset="100%" stop-color="#1b5e20"/>
</linearGradient>
<linearGradient id="birdBelly" x1="0%" y1="0%" x2="0%" y2="100%">
  <stop offset="0%" stop-color="#fdd835"/>
  <stop offset="100%" stop-color="#f57f17"/>
</linearGradient>
"""
bird_content = """
<!-- Tail -->
<path d="M 360 280 Q 460 260 440 320 Q 360 320 360 280 Z" fill="url(#birdGrad)"/>
<!-- Legs -->
<path d="M 210 320 L 210 420 L 190 440 M 210 420 L 230 440" fill="none" stroke="#1a1a1a" stroke-width="12"/>
<path d="M 290 320 L 290 420 L 270 440 M 290 420 L 310 440" fill="none" stroke="#1a1a1a" stroke-width="12"/>
<!-- Body -->
<ellipse cx="256" cy="280" rx="130" ry="90" fill="url(#birdGrad)"/>
<!-- Belly -->
<path d="M 170 320 C 220 390, 310 390, 340 320 Z" fill="url(#birdBelly)" stroke="none"/>
<!-- Head -->
<circle cx="150" cy="200" r="50" fill="url(#birdGrad)"/>
<!-- Beak -->
<path d="M 100 200 L 70 210 L 105 225 Z" fill="#ffb300"/>
<!-- Eye -->
<circle cx="140" cy="180" r="10" fill="#1a1a1a" stroke="none"/>
<circle cx="143" cy="177" r="3" fill="#fff" stroke="none"/>
<!-- Wing -->
<path d="M 256 220 C 330 220, 330 320, 256 320 C 256 270, 256 220, 256 220 Z" fill="#2e7d32"/>
"""
animals['bird'] = wrap_svg(bird_defs, bird_content)

# 5. Partridge
part_defs = """
<linearGradient id="partBody" x1="0%" y1="0%" x2="100%" y2="100%">
  <stop offset="0%" stop-color="#795548"/>
  <stop offset="100%" stop-color="#4e342e"/>
</linearGradient>
<radialGradient id="partPatch" cx="50%" cy="50%" r="50%">
  <stop offset="0%" stop-color="#ff7043"/>
  <stop offset="100%" stop-color="#d84315"/>
</radialGradient>
"""
part_content = """
<!-- Tail -->
<path d="M 340 300 Q 420 280 400 360 Q 340 360 340 300 Z" fill="url(#partPatch)"/>
<!-- Legs -->
<path d="M 210 320 L 210 430 L 190 450 M 210 430 L 230 450" fill="none" stroke="#ffca28" stroke-width="12"/>
<path d="M 300 320 L 300 430 L 280 450 M 300 430 L 320 450" fill="none" stroke="#ffca28" stroke-width="12"/>
<!-- Body -->
<ellipse cx="256" cy="300" rx="110" ry="85" fill="url(#partBody)"/>
<!-- Rust patch -->
<path d="M 190 310 C 190 370, 290 370, 290 310 C 290 350, 190 350, 190 310 Z" fill="url(#partPatch)" stroke="none"/>
<!-- Head -->
<circle cx="160" cy="220" r="45" fill="url(#partBody)"/>
<!-- Beak -->
<path d="M 115 220 L 85 230 L 120 245 Z" fill="#1a1a1a"/>
<!-- Eye -->
<circle cx="150" cy="205" r="12" fill="#ffca28" stroke="none"/>
<circle cx="150" cy="205" r="6" fill="#e64a19" stroke="none"/>
<circle cx="150" cy="205" r="3" fill="#1a1a1a" stroke="none"/>
<!-- Wing -->
<path d="M 250 250 C 340 250, 340 330, 250 330 C 210 330, 210 250, 250 250 Z" fill="#5d4037"/>
"""
animals['partridge'] = wrap_svg(part_defs, part_content)

# 6. Shark
shark_defs = """
<linearGradient id="sharkBody" x1="0%" y1="0%" x2="0%" y2="100%">
  <stop offset="0%" stop-color="#78909c"/>
  <stop offset="100%" stop-color="#455a64"/>
</linearGradient>
<linearGradient id="sharkBelly" x1="0%" y1="0%" x2="0%" y2="100%">
  <stop offset="0%" stop-color="#eceff1"/>
  <stop offset="100%" stop-color="#b0bec5"/>
</linearGradient>
"""
shark_content = """
<!-- Top Fin -->
<path d="M 220 250 C 240 140, 250 100, 260 80 C 270 140, 280 180, 300 250 Z" fill="url(#sharkBody)"/>
<!-- Bottom Fin -->
<path d="M 240 330 C 260 410, 270 440, 280 460 C 290 410, 300 380, 320 330 Z" fill="url(#sharkBody)"/>
<!-- Tail -->
<path d="M 380 280 C 440 220, 470 180, 480 160 C 460 250, 460 310, 480 400 C 470 380, 440 340, 380 280 Z" fill="url(#sharkBody)"/>
<!-- Body -->
<path d="M 60 280 C 60 180, 420 200, 420 280 C 420 360, 60 380, 60 280 Z" fill="url(#sharkBody)"/>
<!-- Belly -->
<path d="M 120 340 C 220 380, 360 360, 410 310 C 340 370, 200 390, 120 340 Z" fill="url(#sharkBelly)" stroke="none"/>
<!-- Gills -->
<path d="M 180 260 Q 170 280 180 300 M 200 260 Q 190 280 200 300 M 220 260 Q 210 280 220 300" fill="none" stroke="#1a1a1a" stroke-width="4"/>
<!-- Eye -->
<circle cx="120" cy="240" r="8" fill="#1a1a1a" stroke="none"/>
<circle cx="123" cy="237" r="2" fill="#fff" stroke="none"/>
<!-- Mouth/Teeth -->
<path d="M 70 300 Q 120 320 150 300" fill="none" stroke="#1a1a1a" stroke-width="6"/>
<polygon points="80,305 85,295 90,307" fill="#fff" stroke="#1a1a1a" stroke-width="2"/>
<polygon points="95,309 100,299 105,311" fill="#fff" stroke="#1a1a1a" stroke-width="2"/>
<polygon points="110,312 115,302 120,313" fill="#fff" stroke="#1a1a1a" stroke-width="2"/>
"""
animals['shark'] = wrap_svg(shark_defs, shark_content)

# 7. Pterodactyl 1
ptero1_defs = """
<linearGradient id="pteroBody" x1="0%" y1="0%" x2="0%" y2="100%">
  <stop offset="0%" stop-color="#8d6e63"/>
  <stop offset="100%" stop-color="#4e342e"/>
</linearGradient>
<linearGradient id="pteroWing" x1="0%" y1="0%" x2="0%" y2="100%">
  <stop offset="0%" stop-color="#a1887f"/>
  <stop offset="100%" stop-color="#5d4037"/>
</linearGradient>
"""
ptero1_content = """
<!-- Back Wing -->
<path d="M 256 256 L 452 120 C 412 280, 332 300, 256 300 Z" fill="url(#pteroWing)"/>
<!-- Legs -->
<path d="M 220 270 L 190 380 Q 180 400 190 420 L 210 440 M 190 420 L 170 440" fill="none" stroke="url(#pteroBody)" stroke-width="14"/>
<path d="M 290 270 L 320 380 Q 330 400 320 420 L 300 440 M 320 420 L 340 440" fill="none" stroke="url(#pteroBody)" stroke-width="14"/>
<!-- Body (Now correctly ordered to show its stroke clearly over back wing) -->
<ellipse cx="256" cy="270" rx="50" ry="40" fill="url(#pteroBody)"/>
<!-- Head/Neck -->
<path d="M 290 250 C 350 250, 380 250, 420 260 C 420 280, 380 280, 290 270 Z" fill="url(#pteroBody)"/>
<!-- Front Wing -->
<path d="M 256 256 L 60 120 C 100 280, 180 300, 256 300 Z" fill="url(#pteroWing)"/>
<!-- Eye -->
<circle cx="360" cy="255" r="6" fill="#1a1a1a" stroke="none"/>
<circle cx="361" cy="254" r="2" fill="#fff" stroke="none"/>
"""
animals['pterodactyl1'] = wrap_svg(ptero1_defs, ptero1_content)

# 8. Pterodactyl 2
ptero2_defs = """
<linearGradient id="ptero2Body" x1="0%" y1="0%" x2="0%" y2="100%">
  <stop offset="0%" stop-color="#6d4c41"/>
  <stop offset="100%" stop-color="#3e2723"/>
</linearGradient>
<linearGradient id="ptero2Wing" x1="0%" y1="0%" x2="0%" y2="100%">
  <stop offset="0%" stop-color="#512da8"/>
  <stop offset="100%" stop-color="#311b92"/>
</linearGradient>
"""
ptero2_content = """
<!-- Back Wing Outer -->
<path d="M 256 256 L 452 120 C 412 280, 332 300, 256 300 Z" fill="url(#ptero2Wing)"/>
<!-- Back Wing Inner (Removed stroke="none" so border appears properly) -->
<path d="M 256 260 L 437 140 C 402 270, 332 290, 256 290 Z" fill="url(#pteroBody)"/>

<!-- Legs -->
<path d="M 220 270 L 190 380 Q 180 400 190 420 L 210 440 M 190 420 L 170 440" fill="none" stroke="url(#ptero2Body)" stroke-width="14"/>
<path d="M 290 270 L 320 380 Q 330 400 320 420 L 300 440 M 320 420 L 340 440" fill="none" stroke="url(#ptero2Body)" stroke-width="14"/>

<!-- Head crest -->
<path d="M 280 250 C 260 180, 250 160, 240 140 C 260 180, 280 220, 290 250 Z" fill="url(#ptero2Body)"/>
<!-- Body -->
<ellipse cx="256" cy="270" rx="50" ry="40" fill="url(#ptero2Body)"/>
<!-- Head/Neck -->
<path d="M 290 250 C 350 250, 380 250, 420 260 C 420 280, 380 280, 290 270 Z" fill="url(#ptero2Body)"/>

<!-- Front Wing Outer -->
<path d="M 256 256 L 60 120 C 100 280, 180 300, 256 300 Z" fill="url(#ptero2Wing)"/>
<!-- Front Wing Inner (Removed stroke="none") -->
<path d="M 256 260 L 75 140 C 110 270, 180 290, 256 290 Z" fill="url(#pteroBody)"/>

<!-- Beak Highlight -->
<path d="M 380 255 Q 420 260 420 265 Q 380 270 380 255 Z" fill="#a1887f" stroke="none"/>
<!-- Eye -->
<circle cx="360" cy="255" r="6" fill="#1a1a1a" stroke="none"/>
<circle cx="361" cy="254" r="2" fill="#fff" stroke="none"/>
"""
animals['pterodactyl2'] = wrap_svg(ptero2_defs, ptero2_content)

# 9. Sheep
sheep_defs = """
<linearGradient id="sheepWool" x1="0%" y1="0%" x2="0%" y2="100%">
  <stop offset="0%" stop-color="#ffffff"/>
  <stop offset="100%" stop-color="#e0e0e0"/>
</linearGradient>
<linearGradient id="sheepFace" x1="0%" y1="0%" x2="0%" y2="100%">
  <stop offset="0%" stop-color="#bcaaa4"/>
  <stop offset="100%" stop-color="#795548"/>
</linearGradient>
"""
sheep_content = """
<!-- Legs -->
<path d="M 180 280 C 180 390, 170 410, 170 430 C 170 440, 190 440, 190 430 C 190 410, 195 390, 195 280 Z" fill="#1a1a1a"/>
<path d="M 240 280 C 240 390, 230 410, 230 430 C 230 440, 250 440, 250 430 C 250 410, 255 390, 255 280 Z" fill="#1a1a1a"/>
<path d="M 300 280 C 300 390, 290 410, 290 430 C 290 440, 310 440, 310 430 C 310 410, 315 390, 315 280 Z" fill="#1a1a1a"/>
<!-- Wool Body -->
<path d="M 160 280 C 120 280, 100 240, 140 200 C 140 140, 220 120, 260 160 C 320 120, 380 180, 340 240 C 380 280, 340 340, 280 340 C 240 380, 160 380, 140 320 C 100 320, 100 280, 160 280 Z" fill="url(#sheepWool)"/>
<!-- Head -->
<circle cx="330" cy="250" r="45" fill="url(#sheepFace)"/>
<!-- Horns -->
<path d="M 310 220 C 260 180, 220 280, 280 280" fill="none" stroke="#5d4037" stroke-width="16"/>
<path d="M 350 220 C 400 180, 440 280, 380 280" fill="none" stroke="#5d4037" stroke-width="16"/>
<!-- Ears -->
<ellipse cx="280" cy="270" rx="16" ry="10" fill="url(#sheepFace)"/>
<ellipse cx="380" cy="270" rx="16" ry="10" fill="url(#sheepFace)"/>
<!-- Eyes & Nose -->
<circle cx="310" cy="240" r="6" fill="#1a1a1a" stroke="none"/>
<circle cx="350" cy="240" r="6" fill="#1a1a1a" stroke="none"/>
<circle cx="330" cy="270" r="5" fill="#1a1a1a" stroke="none"/>
"""
animals['sheep'] = wrap_svg(sheep_defs, sheep_content)

# 10. Worm (Snake)
worm_defs = """
<linearGradient id="wormGrad" x1="0%" y1="0%" x2="100%" y2="100%">
  <stop offset="0%" stop-color="#f48fb1"/>
  <stop offset="100%" stop-color="#ad1457"/>
</linearGradient>
<linearGradient id="wormGlow" x1="0%" y1="0%" x2="100%" y2="100%">
  <stop offset="0%" stop-color="#f8bbd0"/>
  <stop offset="100%" stop-color="#e91e63"/>
</linearGradient>
"""
worm_content = """
<!-- Explicit Solid Black Border Track for Worm -->
<!-- We stroke it with 72 width, and then the colored body with 60 width goes on top. -->
<!-- 72 - 60 = 12, so there's a 6px border sticking out perfectly! -->
<path d="M 120 250 C 180 180, 280 180, 320 220 C 400 300, 420 180, 360 140 C 300 100, 200 120, 160 200 C 120 280, 220 380, 280 340 C 340 300, 380 400, 300 440 C 220 480, 140 400, 180 340" fill="none" stroke="#1a1a1a" stroke-width="72" stroke-linecap="round"/>

<!-- Core Body -->
<path d="M 120 250 C 180 180, 280 180, 320 220 C 400 300, 420 180, 360 140 C 300 100, 200 120, 160 200 C 120 280, 220 380, 280 340 C 340 300, 380 400, 300 440 C 220 480, 140 400, 180 340" fill="none" stroke="url(#wormGrad)" stroke-width="60" stroke-linecap="round"/>

<!-- Highlight core -->
<path d="M 120 250 C 180 180, 280 180, 320 220 C 400 300, 420 180, 360 140 C 300 100, 200 120, 160 200 C 120 280, 220 380, 280 340 C 340 300, 380 400, 300 440 C 220 480, 140 400, 180 340" fill="none" stroke="url(#wormGlow)" stroke-width="40" stroke-linecap="round" stroke="none"/>

<!-- Eye -->
<circle cx="110" cy="240" r="8" fill="#fff" stroke="none"/>
<circle cx="108" cy="238" r="4" fill="#1a1a1a" stroke="none"/>
<!-- Smile -->
<path d="M 100 260 Q 120 270 130 250" fill="none" stroke="#880e4f" stroke-width="6"/>
"""
animals['worm'] = wrap_svg(worm_defs, worm_content)

filenames = {
    'salamander': 'salamander.svg',
    'newt': 'newt.svg',
    'quail': 'quail.svg',
    'bird': 'bird (1).svg',
    'partridge': 'partridge.svg',
    'shark': 'shark.svg',
    'pterodactyl1': 'pterodactyl.svg', 
    'pterodactyl2': 'pterodactyl2.svg',
    'sheep': 'sheep.svg',
    'worm': 'worm.svg'
}

out_dir = "/Users/paulblenkhorn/Desktop/Fleximbols/Animals - fluent/"
os.makedirs(out_dir, exist_ok=True)

for name, svg in animals.items():
    with open(os.path.join(out_dir, filenames[name]), "w") as f:
        f.write(svg)

print("Generated SVGs successfully with specific detail fixes.")
