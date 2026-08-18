#!/usr/bin/env python3
"""Fix image paths by URL encoding them"""
import urllib.parse

# Read file
with open('portfolio.html', 'r', encoding='utf-8') as f:
    content = f.read()

# Function to encode path
def encode_path(path):
    parts = path.split('/')
    encoded_parts = [urllib.parse.quote(part, safe='') for part in parts]
    return '/'.join(encoded_parts)

# List of all image paths to fix
image_paths = [
    # Projet 02 - MatchyKhedma
    "images MatchyKhedma/Capture d'écran 2026-08-17 124536.png",
    "images MatchyKhedma/Capture d'écran 2026-08-17 124559.png",
    "images MatchyKhedma/Capture d'écran 2026-08-17 124623.png",
    "images MatchyKhedma/Capture d'écran 2026-08-17 124644.png",
    "images MatchyKhedma/Capture d'écran 2026-08-17 124705.png",
    "images MatchyKhedma/Capture d'écran 2026-08-17 124721.png",
    "images MatchyKhedma/Capture d'écran 2026-08-17 124742.png",
    "images MatchyKhedma/Capture d'écran 2026-08-17 124805.png",
    # Projet 03 - Chicago
    "images chicago/Capture d'écran 2026-08-15 214202.png",
    "images chicago/Capture d'écran 2026-08-15 214236.png",
    "images chicago/Capture d'écran 2026-08-15 214256.png",
    "images chicago/Capture d'écran 2026-08-15 214315.png",
    # Projet 04 - Agriplanner
    "images Agriplanner/Capture d'écran 2026-08-17 125604.png",
    "images Agriplanner/Capture d'écran 2026-08-17 125641.png",
    "images Agriplanner/Capture d'écran 2026-08-17 125700.png",
    "images Agriplanner/Capture d'écran 2026-08-17 125720.png",
    "images Agriplanner/Capture d'écran 2026-08-17 125735.png",
    "images Agriplanner/Capture d'écran 2026-08-17 125752.png",
    # Projet 05 - Mobilité
    "images mobilité internationnale/Capture d'écran 2026-08-09 152746.png",
    "images mobilité internationnale/Capture d'écran 2026-08-09 152950.png",
    "images mobilité internationnale/Capture d'écran 2026-08-09 153114.png",
    "images mobilité internationnale/Capture d'écran 2026-08-09 153143.png",
    "images mobilité internationnale/Capture d'écran 2026-08-09 153240.png",
    # Projet 06 - Banque
    "images de l application de banque centrale/Capture d'écran 2026-08-09 143941.png",
    "images de l application de banque centrale/Capture d'écran 2026-08-09 144003.png",
    "images de l application de banque centrale/Capture d'écran 2026-08-09 144024.png",
    "images de l application de banque centrale/Capture d'écran 2026-08-09 144848.png",
    "images de l application de banque centrale/Capture d'écran 2026-08-09 145041.png",
    "images de l application de banque centrale/Capture d'écran 2026-08-09 145118.png",
    "images de l application de banque centrale/Capture d'écran 2026-08-09 145223.png",
    "images de l application de banque centrale/Capture d'écran 2026-08-09 145306.png",
    # Dashboard (Projet 01)
    "images dashboard/dashboard-01.png",
    "images dashboard/dashboard-02.png",
    "images dashboard/dashboard-03.png",
    "images dashboard/dashboard-04.png",
    "images dashboard/preview.webp",
]

# Replace each path with encoded version
for path in image_paths:
    encoded_path = encode_path(path)
    # Replace in src attributes
    search = f'src="{path}"'
    replace = f'src="{encoded_path}"'
    if search in content:
        content = content.replace(search, replace)
        print(f"✓ Fixed: {path} -> {encoded_path}")
    else:
        print(f"✗ Not found: {path}")

# Write back
with open('portfolio.html', 'w', encoding='utf-8') as f:
    f.write(content)

print("\n✓ All image paths have been URL encoded!")
