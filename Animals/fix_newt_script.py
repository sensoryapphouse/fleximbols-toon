import os

# Read the existing v6 script
with open("/Users/paulblenkhorn/Desktop/Fleximbols/Animals/generate_fluent_svgs_v6.py", "r") as f:
    content = f.read()

# Fix the newt
old_newt = """<!-- Body Fill (no stroke yet, so belly draws over it cleanly) -->
<ellipse cx="250" cy="270" rx="80" ry="50" fill="url(#newtGrad)" stroke="none"/>
<!-- Head (Explicit distinct head shape) -->
<ellipse cx="360" cy="255" rx="50" ry="35" fill="url(#newtGrad)"/>

<!-- Belly Stripe (Clipped to body so it never spills out) -->
<!-- We deliberately make it larger so it hits the clip boundary cleanly -->
<path d="M 160 310 C 230 350, 310 350, 370 290 C 310 300, 230 300, 160 310 Z" fill="url(#bellyGrad)" stroke="none" clip-path="url(#newtBodyClip)"/>

<!-- Body Stroke (Drawn on top to ensure a clean 6px outer border over the belly) -->
<ellipse cx="250" cy="270" rx="80" ry="50" fill="none"/>"""

new_newt = """<!-- Base Strokes for Body and Head (drawn underneath to form a seamless outer border) -->
<ellipse cx="250" cy="270" rx="80" ry="50" fill="none" stroke="#1a1a1a" stroke-width="12"/>
<ellipse cx="360" cy="255" rx="50" ry="35" fill="none" stroke="#1a1a1a" stroke-width="12"/>

<!-- Body Fill (no stroke) -->
<ellipse cx="250" cy="270" rx="80" ry="50" fill="url(#newtGrad)" stroke="none"/>
<!-- Head Fill (no stroke) -->
<ellipse cx="360" cy="255" rx="50" ry="35" fill="url(#newtGrad)" stroke="none"/>

<!-- Belly Stripe (Clipped to body) -->
<path d="M 160 310 C 230 350, 310 350, 370 290 C 310 300, 230 300, 160 310 Z" fill="url(#bellyGrad)" stroke="none" clip-path="url(#newtBodyClip)"/>"""

content = content.replace(old_newt, new_newt)

# Fix Salamander just in case (same issue, head circle might not be seamlessly bordered if not drawn properly)
old_sal = """<!-- Body -->
<ellipse cx="256" cy="270" rx="90" ry="60" fill="url(#salGrad)"/>
<!-- Head (Explicit distinct head shape) -->
<ellipse cx="380" cy="260" rx="55" ry="40" fill="url(#salGrad)"/>"""

new_sal = """<!-- Base Strokes -->
<ellipse cx="256" cy="270" rx="90" ry="60" fill="none" stroke="#1a1a1a" stroke-width="12"/>
<ellipse cx="380" cy="260" rx="55" ry="40" fill="none" stroke="#1a1a1a" stroke-width="12"/>
<!-- Fills -->
<ellipse cx="256" cy="270" rx="90" ry="60" fill="url(#salGrad)" stroke="none"/>
<ellipse cx="380" cy="260" rx="55" ry="40" fill="url(#salGrad)" stroke="none"/>"""

content = content.replace(old_sal, new_sal)

with open("/Users/paulblenkhorn/Desktop/Fleximbols/Animals/generate_fluent_svgs_v7.py", "w") as f:
    f.write(content)

print("v7 script created.")
