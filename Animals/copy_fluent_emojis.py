import os
import re
import shutil

source_dir = "/Users/paulblenkhorn/Desktop/Fleximbols/Animals"
out_dir = "/Users/paulblenkhorn/Desktop/Fleximbols/Animals - fluent"
assets_dir = "/tmp/fluentui-emoji/assets"

os.makedirs(out_dir, exist_ok=True)

# Exclude list provided by user (non-animals)
exclude_list = {
    "chicken house", "chicken run", "comparison", "empty-nest", "feather",
    "fluent_comparison", "generate_fluent_svgs", "generate_fluent_svgs_v3",
    "generate_fluent_svgs_v4", "generate_fluent_svgs_v5", "generate_fluent_svgs_v6",
    "generate_fluent_batch1", "fix_newt_script", "hibernate", "mouth",
    "nest-with-eggs", "paw-prints", "spider-web", "wing"
}

# Collect all base animal names
animal_files = [f for f in os.listdir(source_dir) if f.endswith('.svg') and os.path.isfile(os.path.join(source_dir, f))]

base_names = set()
for f in animal_files:
    if f.startswith('test_') or f.startswith('fluent_') or f.startswith('my_') or f.startswith('original_'):
        continue
    # Extract base name by removing (number) and .svg
    base = re.sub(r'\s*\(\d+\)\.svg$', '', f)
    base = re.sub(r'\.svg$', '', base)
    
    if base not in exclude_list:
        base_names.add(base)

# Build a lowercase index of all available fluent emojis
fluent_emojis = {}
for item in os.listdir(assets_dir):
    item_path = os.path.join(assets_dir, item)
    if os.path.isdir(item_path):
        fluent_emojis[item.lower()] = item

# Custom mappings for animals that might have different names in the emoji set
mapping = {
    "blowfish": "blowfish",
    "boar": "boar",
    "butterfly": "butterfly",
    "camel": "camel",
    "two-hump-camel": "two-hump camel",
    "cat-face": "cat face",
    "cow-face": "cow face",
    "dog-face": "dog face",
    "dragon-face": "dragon face",
    "horse-face": "horse face",
    "monkey-face": "monkey face",
    "mouse-face": "mouse face",
    "pig-face": "pig face",
    "rabbit-face": "rabbit face",
    "tiger-face": "tiger face",
    "front-facing-baby-chick": "front-facing baby chick",
    "hatching-chick": "hatching chick",
    "lady-beetle": "lady beetle",
    "black-cat": "black cat",
    "guide-dog": "guide dog",
    "service-dog": "service dog",
    "see-no-evil-monkey": "see-no-evil monkey",
    "teddy-bear": "teddy bear",
    "tropical-fish": "tropical fish",
    "water-buffalo": "water buffalo",
    "peacock": "peacock",
    "phoenix-bird": "bird", # fallback
    "blackbird": "bird", # fallback
    "dodo": "dodo", 
    "flamingo": "flamingo",
    "sauropod": "sauropod",
    "t-rex": "t-rex",
    "mammoth": "mammoth",
    "sloth": "sloth",
    "kangaroo": "kangaroo",
    "llama": "llama",
    "orangutan-baby": "orangutan",
    "skunk": "skunk"
}

found_count = 0
missing = []

for base in sorted(base_names):
    search_name = mapping.get(base, base.replace('-', ' '))
    search_lower = search_name.lower()
    
    match = None
    if search_lower in fluent_emojis:
        match = fluent_emojis[search_lower]
    else:
        # Fallback searches
        for key in fluent_emojis.keys():
            if search_lower in key or key in search_lower:
                match = fluent_emojis[key]
                break
                
    if match:
        color_dir = os.path.join(assets_dir, match, "Color")
        if os.path.exists(color_dir):
            svg_files = [f for f in os.listdir(color_dir) if f.endswith('.svg')]
            if svg_files:
                src_svg = os.path.join(color_dir, svg_files[0])
                dst_svg = os.path.join(out_dir, f"{base}.svg")
                shutil.copy2(src_svg, dst_svg)
                found_count += 1
            else:
                missing.append(base)
        else:
            missing.append(base)
    else:
        missing.append(base)

print(f"Successfully copied {found_count} fluent emojis.")
if missing:
    print(f"Missing {len(missing)} animals: {', '.join(missing)}")
