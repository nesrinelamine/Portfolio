#!/usr/bin/env python3
"""Rename image files to remove apostrophes and update HTML"""
import os
import re

# Mapping old names to new names (removing apostrophes)
file_mappings = {}

# Directories to process
directories = [
    'images MatchyKhedma',
    'images chicago', 
    'images Agriplanner',
    'images mobilité internationnale',
    'images de l application de banque centrale'
]

# Rename files
for dir_name in directories:
    if os.path.exists(dir_name):
        files = os.listdir(dir_name)
        for old_name in files:
            # Create new name by removing apostrophe
            new_name = old_name.replace("'", "")
            old_path = os.path.join(dir_name, old_name)
            new_path = os.path.join(dir_name, new_name)
            
            if old_name != new_name:
                os.rename(old_path, new_path)
                file_mappings[f"{dir_name}/{old_name}"] = f"{dir_name}/{new_name}"
                print(f"✓ Renamed: {old_name} → {new_name}")

# Now update the HTML
with open('portfolio.html', 'r', encoding='utf-8') as f:
    content = f.read()

# Replace all old paths with new paths
replacements = 0
for old_path, new_path in file_mappings.items():
    old_src = f'src="{old_path}"'
    new_src = f'src="{new_path}"'
    if old_src in content:
        content = content.replace(old_src, new_src)
        replacements += 1

# Write back
with open('portfolio.html', 'w', encoding='utf-8') as f:
    f.write(content)

print(f"\n✓ Updated HTML: {replacements} paths fixed!")
