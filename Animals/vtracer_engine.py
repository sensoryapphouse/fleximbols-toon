#!/usr/bin/env python3
import sys
import os
import subprocess
from PIL import Image

def process_image(jpg_path, animal_name, target_dir=None):
    out_dir = target_dir if target_dir else "/Users/paulblenkhorn/Desktop/Fleximbols/Animals - fluent"
    os.makedirs(out_dir, exist_ok=True)
    
    # Canonical on-disk name: lowercased, hyphen-separated. This MUST match the
    # dedup check in worker_1A/1B - previously this wrote "chilli crab.svg" while
    # the workers looked for "chilli-crab.svg", so every multiword symbol was
    # regenerated on each pass and piled up as " (1)", " (2)" copies.
    safe_name = animal_name.strip().lower().replace(" ", "-")

    png_path = os.path.join(out_dir, f"{safe_name}.png")
    svg_path = os.path.join(out_dir, f"{safe_name}.svg")

    # Handle duplicate collisions using (1), (2) naming convention
    if os.path.exists(svg_path):
        counter = 1
        while os.path.exists(os.path.join(out_dir, f"{safe_name} ({counter}).svg")):
            counter += 1
        svg_path = os.path.join(out_dir, f"{safe_name} ({counter}).svg")
        png_path = os.path.join(out_dir, f"{safe_name} ({counter}).png")
    
    # 1. Convert to transparent PNG
    try:
        img = Image.open(jpg_path).convert("RGBA")
        width, height = img.size
        
        # We use a custom flood fill to only remove the contiguous white background.
        # This prevents internal white areas (like teeth or eyes) from being removed.
        from collections import deque
        pixels = img.load()
        
        # Threshold for considering a pixel "white"
        def is_bg(c):
            return c[0] > 240 and c[1] > 240 and c[2] > 240
            
        visited = set()
        queue = deque()
        
        # Seed the edges
        for x in range(width):
            queue.append((x, 0))
            queue.append((x, height - 1))
        for y in range(height):
            queue.append((0, y))
            queue.append((width - 1, y))
            
        while queue:
            x, y = queue.popleft()
            if (x, y) in visited:
                continue
            visited.add((x, y))
            
            if x < 0 or x >= width or y < 0 or y >= height:
                continue
                
            if is_bg(pixels[x, y]):
                pixels[x, y] = (255, 255, 255, 0) # Make transparent
                queue.append((x + 1, y))
                queue.append((x - 1, y))
                queue.append((x, y + 1))
                queue.append((x, y - 1))
                
        img.save(png_path, "PNG")
        print(f"Saved PNG to {png_path}")
    except Exception as e:
        print(f"Error processing image for {animal_name}: {e}")
        return False

    # 2. Run vtracer
    vtracer_bin = "/Users/paulblenkhorn/Downloads/flux.macos.arm64/vtracer"
    cmd = [
        vtracer_bin,
        "--input", png_path,
        "--output", svg_path,
        "--colormode", "color",
        "--mode", "spline",
        "--hierarchical", "stacked",
        "--filter_speckle", "16",
        "--corner_threshold", "60",
        "--segment_length", "10"
    ]
    
    result = subprocess.run(cmd, capture_output=True, text=True)
    if result.returncode == 0:
        print(f"Successfully vectorized {animal_name} to {svg_path}")
        
        # Clean up intermediate files to save space
        try:
            if os.path.exists(png_path):
                os.remove(png_path)
            if os.path.exists(jpg_path):
                os.remove(jpg_path)
        except Exception as cleanup_err:
            print(f"Cleanup warning: {cleanup_err}")
            
        return True
    else:
        print(f"vtracer failed for {animal_name}: {result.stderr}")
        return False

if __name__ == "__main__":
    if len(sys.argv) < 3:
        print("Usage: python3 vtracer_engine.py <path_to_jpg> <animal_name> [optional_target_dir]")
        sys.exit(1)
        
    target = sys.argv[3] if len(sys.argv) > 3 else None
    process_image(sys.argv[1], sys.argv[2], target)
