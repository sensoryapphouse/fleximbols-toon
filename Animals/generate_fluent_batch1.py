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

# 1. ant
ant_defs = """
<linearGradient id="antGrad" x1="0%" y1="0%" x2="100%" y2="100%">
  <stop offset="0%" stop-color="#4e342e"/>
  <stop offset="100%" stop-color="#3e2723"/>
</linearGradient>
"""
ant_content = """
<!-- Legs (Black Track) -->
<path d="M 230 300 Q 210 350 200 420" fill="none" stroke="#1a1a1a" stroke-width="18"/>
<path d="M 256 300 Q 256 350 256 420" fill="none" stroke="#1a1a1a" stroke-width="18"/>
<path d="M 280 300 Q 300 350 310 420" fill="none" stroke="#1a1a1a" stroke-width="18"/>
<!-- Legs (Color) -->
<path d="M 230 300 Q 210 350 200 420" fill="none" stroke="#5d4037" stroke-width="12"/>
<path d="M 256 300 Q 256 350 256 420" fill="none" stroke="#5d4037" stroke-width="12"/>
<path d="M 280 300 Q 300 350 310 420" fill="none" stroke="#5d4037" stroke-width="12"/>

<!-- Antennae -->
<path d="M 390 230 Q 420 180 460 200" fill="none" stroke="#1a1a1a" stroke-width="10"/>
<path d="M 370 230 Q 380 180 420 160" fill="none" stroke="#1a1a1a" stroke-width="10"/>

<!-- Body Parts (Strokes behind to merge smoothly without internal lines) -->
<ellipse cx="140" cy="256" rx="80" ry="60" fill="none" stroke="#1a1a1a" stroke-width="12"/>
<ellipse cx="256" cy="270" rx="50" ry="30" fill="none" stroke="#1a1a1a" stroke-width="12"/>
<circle cx="360" cy="260" r="40" fill="none" stroke="#1a1a1a" stroke-width="12"/>

<!-- Body Parts (Fills) -->
<ellipse cx="140" cy="256" rx="80" ry="60" fill="url(#antGrad)" stroke="none"/>
<ellipse cx="256" cy="270" rx="50" ry="30" fill="url(#antGrad)" stroke="none"/>
<circle cx="360" cy="260" r="40" fill="url(#antGrad)" stroke="none"/>

<!-- Eye -->
<circle cx="370" cy="250" r="6" fill="#1a1a1a" stroke="none"/>
"""
animals['ant'] = wrap_svg(ant_defs, ant_content)

# 2. badger
badger_defs = """
<linearGradient id="badgerBody" x1="0%" y1="0%" x2="0%" y2="100%">
  <stop offset="0%" stop-color="#9e9e9e"/>
  <stop offset="100%" stop-color="#616161"/>
</linearGradient>
<linearGradient id="badgerDark" x1="0%" y1="0%" x2="0%" y2="100%">
  <stop offset="0%" stop-color="#424242"/>
  <stop offset="100%" stop-color="#212121"/>
</linearGradient>
"""
badger_content = """
<!-- Tail -->
<path d="M 100 270 L 40 320 Q 60 350 100 320 Z" fill="url(#badgerBody)"/>

<!-- Legs -->
<path d="M 140 320 L 140 400 L 170 400 L 170 320 Z" fill="url(#badgerDark)"/>
<path d="M 320 320 L 320 400 L 350 400 L 350 320 Z" fill="url(#badgerDark)"/>

<!-- Body Stroke under -->
<path d="M 100 280 C 100 200, 340 220, 360 280 C 380 340, 100 360, 100 280 Z" fill="none" stroke="#1a1a1a" stroke-width="12"/>
<!-- Head Stroke under -->
<path d="M 340 230 L 460 300 C 440 340, 350 340, 340 330 Z" fill="none" stroke="#1a1a1a" stroke-width="12"/>

<!-- Body Fill -->
<path d="M 100 280 C 100 200, 340 220, 360 280 C 380 340, 100 360, 100 280 Z" fill="url(#badgerBody)" stroke="none"/>
<!-- Head Fill -->
<path d="M 340 230 L 460 300 C 440 340, 350 340, 340 330 Z" fill="#ffffff" stroke="none"/>

<!-- Black Face Stripes -->
<path d="M 340 240 L 450 300 L 430 320 L 340 280 Z" fill="url(#badgerDark)" stroke="none"/>
<path d="M 340 310 L 410 320 L 400 340 L 340 340 Z" fill="url(#badgerDark)" stroke="none"/>

<!-- Nose -->
<circle cx="460" cy="300" r="10" fill="#1a1a1a"/>

<!-- Eye -->
<circle cx="390" cy="270" r="6" fill="#1a1a1a" stroke="none"/>
<circle cx="392" cy="268" r="2" fill="#fff" stroke="none"/>

<!-- Ear -->
<circle cx="350" cy="230" r="15" fill="url(#badgerDark)"/>
"""
animals['badger'] = wrap_svg(badger_defs, badger_content)

# 3. bat
bat_defs = """
<linearGradient id="batBody" x1="0%" y1="0%" x2="0%" y2="100%">
  <stop offset="0%" stop-color="#607d8b"/>
  <stop offset="100%" stop-color="#37474f"/>
</linearGradient>
<linearGradient id="batWing" x1="0%" y1="0%" x2="0%" y2="100%">
  <stop offset="0%" stop-color="#455a64"/>
  <stop offset="100%" stop-color="#263238"/>
</linearGradient>
"""
bat_content = """
<!-- Wings (Strokes behind) -->
<path d="M 256 256 Q 150 100 40 180 Q 90 280 140 350 Q 180 300 256 300" fill="none" stroke="#1a1a1a" stroke-width="12"/>
<path d="M 256 256 Q 362 100 472 180 Q 422 280 372 350 Q 332 300 256 300" fill="none" stroke="#1a1a1a" stroke-width="12"/>
<!-- Wings Fills -->
<path d="M 256 256 Q 150 100 40 180 Q 90 280 140 350 Q 180 300 256 300" fill="url(#batWing)" stroke="none"/>
<path d="M 256 256 Q 362 100 472 180 Q 422 280 372 350 Q 332 300 256 300" fill="url(#batWing)" stroke="none"/>

<!-- Body/Head -->
<ellipse cx="256" cy="250" rx="30" ry="50" fill="none" stroke="#1a1a1a" stroke-width="12"/>
<ellipse cx="256" cy="250" rx="30" ry="50" fill="url(#batBody)" stroke="none"/>

<!-- Ears -->
<path d="M 240 210 L 220 150 L 250 200 Z" fill="url(#batBody)"/>
<path d="M 272 210 L 292 150 L 262 200 Z" fill="url(#batBody)"/>

<!-- Eyes -->
<circle cx="245" cy="230" r="6" fill="#ffeb3b" stroke="none"/>
<circle cx="267" cy="230" r="6" fill="#ffeb3b" stroke="none"/>
"""
animals['bat'] = wrap_svg(bat_defs, bat_content)

# 4. bear
bear_defs = """
<linearGradient id="bearBody" x1="0%" y1="0%" x2="0%" y2="100%">
  <stop offset="0%" stop-color="#8d6e63"/>
  <stop offset="100%" stop-color="#5d4037"/>
</linearGradient>
<linearGradient id="bearSnout" x1="0%" y1="0%" x2="0%" y2="100%">
  <stop offset="0%" stop-color="#d7ccc8"/>
  <stop offset="100%" stop-color="#bcaaa4"/>
</linearGradient>
"""
bear_content = """
<!-- Back Legs -->
<path d="M 140 300 L 140 420 C 140 440 180 440 180 420 L 180 300 Z" fill="url(#bearBody)"/>
<path d="M 320 300 L 320 420 C 320 440 360 440 360 420 L 360 300 Z" fill="url(#bearBody)"/>

<!-- Body -->
<ellipse cx="230" cy="260" rx="120" ry="100" fill="url(#bearBody)"/>

<!-- Front Legs -->
<path d="M 280 260 L 280 420 C 280 440 320 440 320 420 L 320 260 Z" fill="url(#bearBody)"/>

<!-- Head -->
<circle cx="360" cy="180" r="60" fill="none" stroke="#1a1a1a" stroke-width="12"/>
<circle cx="360" cy="180" r="60" fill="url(#bearBody)" stroke="none"/>

<!-- Ears -->
<circle cx="320" cy="130" r="20" fill="url(#bearBody)"/>
<circle cx="400" cy="130" r="20" fill="url(#bearBody)"/>

<!-- Snout -->
<circle cx="400" cy="200" r="30" fill="url(#bearSnout)"/>
<ellipse cx="415" cy="190" rx="10" ry="8" fill="#1a1a1a"/>

<!-- Eye -->
<circle cx="360" cy="160" r="6" fill="#1a1a1a" stroke="none"/>
"""
animals['bear'] = wrap_svg(bear_defs, bear_content)

# 5. beaver
beaver_defs = """
<linearGradient id="beaverBody" x1="0%" y1="0%" x2="0%" y2="100%">
  <stop offset="0%" stop-color="#a1887f"/>
  <stop offset="100%" stop-color="#6d4c41"/>
</linearGradient>
<linearGradient id="beaverTail" x1="0%" y1="0%" x2="0%" y2="100%">
  <stop offset="0%" stop-color="#424242"/>
  <stop offset="100%" stop-color="#212121"/>
</linearGradient>
"""
beaver_content = """
<!-- Tail -->
<ellipse cx="120" cy="340" rx="80" ry="40" fill="url(#beaverTail)"/>
<!-- Tail Crosshatch -->
<path d="M 60 320 L 160 360 M 80 310 L 180 350 M 100 310 L 200 350 M 120 310 L 180 330 M 80 330 L 140 350 M 60 340 L 100 360" fill="none" stroke="#1a1a1a" stroke-width="3"/>

<!-- Body -->
<path d="M 160 340 C 140 200, 340 180, 360 280 C 380 360, 180 380, 160 340 Z" fill="url(#beaverBody)"/>

<!-- Back Leg -->
<path d="M 220 340 C 220 400, 260 400, 260 340 Z" fill="url(#beaverBody)"/>
<!-- Front Leg -->
<path d="M 320 320 C 320 380, 360 380, 360 320 Z" fill="url(#beaverBody)"/>

<!-- Head Stroke under -->
<circle cx="360" cy="240" r="45" fill="none" stroke="#1a1a1a" stroke-width="12"/>
<!-- Head Fill -->
<circle cx="360" cy="240" r="45" fill="url(#beaverBody)" stroke="none"/>

<!-- Ears -->
<circle cx="330" cy="200" r="15" fill="url(#beaverBody)"/>

<!-- Nose -->
<circle cx="400" cy="240" r="10" fill="#1a1a1a"/>

<!-- Teeth -->
<path d="M 380 270 L 380 290 L 400 290 L 400 270 Z" fill="#ffffff"/>
<path d="M 390 270 L 390 290" fill="none" stroke="#1a1a1a" stroke-width="2"/>

<!-- Eye -->
<circle cx="360" cy="220" r="6" fill="#1a1a1a" stroke="none"/>
"""
animals['beaver'] = wrap_svg(beaver_defs, beaver_content)

# 6. beetle
beetle_defs = """
<linearGradient id="beetleBody" x1="0%" y1="0%" x2="0%" y2="100%">
  <stop offset="0%" stop-color="#1976d2"/>
  <stop offset="100%" stop-color="#0d47a1"/>
</linearGradient>
<linearGradient id="beetleHead" x1="0%" y1="0%" x2="0%" y2="100%">
  <stop offset="0%" stop-color="#424242"/>
  <stop offset="100%" stop-color="#212121"/>
</linearGradient>
"""
beetle_content = """
<!-- Legs -->
<path d="M 200 240 Q 150 200 120 260 M 200 280 Q 140 280 110 320 M 210 340 Q 160 400 140 440" fill="none" stroke="#1a1a1a" stroke-width="16"/>
<path d="M 312 240 Q 362 200 392 260 M 312 280 Q 372 280 402 320 M 302 340 Q 352 400 372 440" fill="none" stroke="#1a1a1a" stroke-width="16"/>

<!-- Antennae -->
<path d="M 240 140 Q 200 80 180 100" fill="none" stroke="#1a1a1a" stroke-width="10"/>
<path d="M 272 140 Q 312 80 332 100" fill="none" stroke="#1a1a1a" stroke-width="10"/>

<!-- Body Shell Stroke under -->
<ellipse cx="256" cy="300" rx="70" ry="100" fill="none" stroke="#1a1a1a" stroke-width="12"/>
<!-- Head Stroke under -->
<ellipse cx="256" cy="160" rx="35" ry="25" fill="none" stroke="#1a1a1a" stroke-width="12"/>

<!-- Body Shell Fill -->
<ellipse cx="256" cy="300" rx="70" ry="100" fill="url(#beetleBody)" stroke="none"/>
<!-- Head Fill -->
<ellipse cx="256" cy="160" rx="35" ry="25" fill="url(#beetleHead)" stroke="none"/>

<!-- Line down middle -->
<path d="M 256 200 L 256 400" fill="none" stroke="#1a1a1a" stroke-width="6"/>

<!-- Eyes -->
<circle cx="235" cy="150" r="6" fill="#ffeb3b" stroke="none"/>
<circle cx="277" cy="150" r="6" fill="#ffeb3b" stroke="none"/>
"""
animals['beetle'] = wrap_svg(beetle_defs, beetle_content)

# 7. bison
bison_defs = """
<linearGradient id="bisonBody" x1="0%" y1="0%" x2="0%" y2="100%">
  <stop offset="0%" stop-color="#5d4037"/>
  <stop offset="100%" stop-color="#3e2723"/>
</linearGradient>
<linearGradient id="bisonHead" x1="0%" y1="0%" x2="0%" y2="100%">
  <stop offset="0%" stop-color="#4e342e"/>
  <stop offset="100%" stop-color="#212121"/>
</linearGradient>
"""
bison_content = """
<!-- Back Legs -->
<path d="M 140 280 L 140 440 L 160 440 L 160 280 Z" fill="url(#bisonBody)"/>
<path d="M 320 300 L 320 440 L 340 440 L 340 300 Z" fill="url(#bisonBody)"/>

<!-- Body (Huge front hump) -->
<path d="M 100 280 C 80 140, 360 100, 360 280 C 360 380, 100 360, 100 280 Z" fill="url(#bisonBody)"/>

<!-- Front Leg -->
<path d="M 280 280 L 280 440 L 300 440 L 300 280 Z" fill="url(#bisonHead)"/>

<!-- Head Stroke under -->
<ellipse cx="380" cy="240" rx="40" ry="60" fill="none" stroke="#1a1a1a" stroke-width="12"/>
<!-- Head Fill -->
<ellipse cx="380" cy="240" rx="40" ry="60" fill="url(#bisonHead)" stroke="none"/>

<!-- Horn -->
<path d="M 380 190 Q 420 150 440 180" fill="none" stroke="#e0e0e0" stroke-width="12" stroke-linecap="round"/>

<!-- Eye -->
<circle cx="400" cy="220" r="6" fill="#1a1a1a" stroke="none"/>
<!-- Snout -->
<ellipse cx="410" cy="280" rx="15" ry="10" fill="#212121"/>
"""
animals['bison'] = wrap_svg(bison_defs, bison_content)

# 8. blackbird
blackbird_defs = """
<linearGradient id="blackbirdBody" x1="0%" y1="0%" x2="0%" y2="100%">
  <stop offset="0%" stop-color="#424242"/>
  <stop offset="100%" stop-color="#121212"/>
</linearGradient>
"""
blackbird_content = """
<!-- Tail -->
<path d="M 360 280 Q 460 260 440 320 Q 360 320 360 280 Z" fill="url(#blackbirdBody)"/>
<!-- Legs Black Track -->
<path d="M 210 320 L 210 420 L 190 440 M 210 420 L 230 440" fill="none" stroke="#1a1a1a" stroke-width="18"/>
<path d="M 290 320 L 290 420 L 270 440 M 290 420 L 310 440" fill="none" stroke="#1a1a1a" stroke-width="18"/>
<!-- Legs Colored -->
<path d="M 210 320 L 210 420 L 190 440 M 210 420 L 230 440" fill="none" stroke="#ffb300" stroke-width="12"/>
<path d="M 290 320 L 290 420 L 270 440 M 290 420 L 310 440" fill="none" stroke="#ffb300" stroke-width="12"/>

<!-- Body -->
<ellipse cx="256" cy="280" rx="130" ry="90" fill="none" stroke="#1a1a1a" stroke-width="12"/>
<circle cx="150" cy="200" r="50" fill="none" stroke="#1a1a1a" stroke-width="12"/>

<ellipse cx="256" cy="280" rx="130" ry="90" fill="url(#blackbirdBody)" stroke="none"/>
<circle cx="150" cy="200" r="50" fill="url(#blackbirdBody)" stroke="none"/>

<!-- Beak -->
<path d="M 100 200 L 70 210 L 105 225 Z" fill="#ffb300"/>
<!-- Eye Ring -->
<circle cx="140" cy="180" r="14" fill="#ffb300" stroke="none"/>
<circle cx="140" cy="180" r="8" fill="#1a1a1a" stroke="none"/>
<circle cx="143" cy="177" r="3" fill="#fff" stroke="none"/>
<!-- Wing -->
<path d="M 256 220 C 330 220, 330 320, 256 320 C 256 270, 256 220, 256 220 Z" fill="#212121"/>
"""
animals['blackbird'] = wrap_svg(blackbird_defs, blackbird_content)

# 9. blowfish
blowfish_defs = """
<linearGradient id="blowfishBody" x1="0%" y1="0%" x2="0%" y2="100%">
  <stop offset="0%" stop-color="#fff176"/>
  <stop offset="100%" stop-color="#f57f17"/>
</linearGradient>
<linearGradient id="blowfishFin" x1="0%" y1="0%" x2="0%" y2="100%">
  <stop offset="0%" stop-color="#ffb74d"/>
  <stop offset="100%" stop-color="#e65100"/>
</linearGradient>
"""
blowfish_content = """
<!-- Fins -->
<path d="M 380 256 L 440 200 L 440 312 Z" fill="url(#blowfishFin)"/>
<path d="M 256 360 L 280 420 L 230 420 Z" fill="url(#blowfishFin)"/>
<path d="M 256 150 L 280 90 L 230 90 Z" fill="url(#blowfishFin)"/>

<!-- Body -->
<circle cx="256" cy="256" r="120" fill="url(#blowfishBody)"/>

<!-- Spikes -->
<path d="M 150 180 L 120 150 M 360 180 L 390 150 M 150 330 L 120 360 M 360 330 L 390 360 M 136 256 L 100 256" fill="none" stroke="#1a1a1a" stroke-width="6"/>

<!-- Face -->
<circle cx="180" cy="230" r="12" fill="#1a1a1a" stroke="none"/>
<circle cx="183" cy="227" r="4" fill="#fff" stroke="none"/>
<circle cx="240" cy="230" r="12" fill="#1a1a1a" stroke="none"/>
<circle cx="243" cy="227" r="4" fill="#fff" stroke="none"/>
<!-- Mouth -->
<circle cx="190" cy="280" r="15" fill="#d84315"/>
"""
animals['blowfish'] = wrap_svg(blowfish_defs, blowfish_content)

# 10. boar
boar_defs = """
<linearGradient id="boarBody" x1="0%" y1="0%" x2="0%" y2="100%">
  <stop offset="0%" stop-color="#795548"/>
  <stop offset="100%" stop-color="#3e2723"/>
</linearGradient>
<linearGradient id="boarMane" x1="0%" y1="0%" x2="0%" y2="100%">
  <stop offset="0%" stop-color="#4e342e"/>
  <stop offset="100%" stop-color="#212121"/>
</linearGradient>
"""
boar_content = """
<!-- Back Legs -->
<path d="M 140 300 L 140 400 L 160 400 L 160 300 Z" fill="url(#boarBody)"/>
<path d="M 300 300 L 300 400 L 320 400 L 320 300 Z" fill="url(#boarBody)"/>

<!-- Tail -->
<path d="M 100 260 Q 60 220 80 180" fill="none" stroke="#1a1a1a" stroke-width="8"/>

<!-- Body Stroke -->
<path d="M 100 280 C 100 150, 360 150, 360 280 C 360 380, 100 380, 100 280 Z" fill="none" stroke="#1a1a1a" stroke-width="12"/>
<!-- Head Stroke -->
<path d="M 320 220 C 420 220, 460 280, 420 320 C 380 340, 320 340, 320 340 Z" fill="none" stroke="#1a1a1a" stroke-width="12"/>

<!-- Body Fill -->
<path d="M 100 280 C 100 150, 360 150, 360 280 C 360 380, 100 380, 100 280 Z" fill="url(#boarBody)" stroke="none"/>

<!-- Mane (Spiky back) -->
<path d="M 120 180 L 140 140 L 170 170 L 200 130 L 230 170 L 260 140 L 290 170" fill="none" stroke="#212121" stroke-width="12" stroke-linejoin="round"/>

<!-- Front Leg -->
<path d="M 250 280 L 250 400 L 270 400 L 270 280 Z" fill="url(#boarBody)"/>

<!-- Head Fill -->
<path d="M 320 220 C 420 220, 460 280, 420 320 C 380 340, 320 340, 320 340 Z" fill="url(#boarBody)" stroke="none"/>

<!-- Snout Details -->
<ellipse cx="435" cy="290" rx="15" ry="25" fill="url(#boarMane)"/>
<circle cx="430" cy="285" r="4" fill="#1a1a1a"/>
<circle cx="440" cy="285" r="4" fill="#1a1a1a"/>

<!-- Tusk -->
<path d="M 400 310 Q 420 260 380 240" fill="none" stroke="#f5f5f5" stroke-width="10" stroke-linecap="round"/>

<!-- Eye -->
<circle cx="370" cy="260" r="6" fill="#1a1a1a" stroke="none"/>
<!-- Ear -->
<path d="M 340 220 L 320 160 L 360 200 Z" fill="url(#boarMane)"/>
"""
animals['boar'] = wrap_svg(boar_defs, boar_content)

out_dir = "/Users/paulblenkhorn/Desktop/Fleximbols/Animals - fluent/"
os.makedirs(out_dir, exist_ok=True)

for name, svg in animals.items():
    with open(os.path.join(out_dir, f"{name}.svg"), "w") as f:
        f.write(svg)

print("Batch 1 generated successfully.")
