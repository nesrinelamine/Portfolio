#!/usr/bin/env python3
"""Rename files and directories to remove problematic characters"""
import os
import shutil

# Mapping of old folder names to new names
folder_mappings = {
    'images MatchyKhedma': 'images-matchykhedma',
    'images chicago': 'images-chicago',
    'images Agriplanner': 'images-agriplanner',
    'images mobilité internationnale': 'images-mobilite',
    'images de l application de banque centrale': 'images-banque',
    'images dashboard': 'images-dashboard'  # No need to rename but included for consistency
}

# Rename directories and files
for old_dir, new_dir in folder_mappings.items():
    if os.path.exists(old_dir):
        # Rename directory
        if not os.path.exists(new_dir):
            shutil.move(old_dir, new_dir)
            print(f"✓ Renamed directory: {old_dir} → {new_dir}")
        
        # Rename files inside to remove apostrophes
        for filename in os.listdir(new_dir):
            if "'" in filename:
                new_filename = filename.replace("'", "")
                old_path = os.path.join(new_dir, filename)
                new_path = os.path.join(new_dir, new_filename)
                os.rename(old_path, new_path)
                print(f"  ✓ Renamed file: {filename} → {new_filename}")

# Now update the HTML
with open('portfolio.html', 'r', encoding='utf-8') as f:
    content = f.read()

# Replace all old paths with new paths
replacements = [
    ('images MatchyKhedma/', 'images-matchykhedma/'),
    ('images chicago/', 'images-chicago/'),
    ('images Agriplanner/', 'images-agriplanner/'),
    ('images mobilité internationnale/', 'images-mobilite/'),
    ('images de l application de banque centrale/', 'images-banque/'),
    ("Capture d'écran", "Capture décran"),  # Replace apostrophe in filenames
]

for old, new in replacements:
    content = content.replace(old, new)
    print(f"✓ Updated HTML: {old} → {new}")

# Write back
with open('portfolio.html', 'w', encoding='utf-8') as f:
    f.write(content)

print("\n✓ All files and HTML updated successfully!")
