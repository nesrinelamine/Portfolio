#!/usr/bin/env python3
"""Compare project 01 and project 02 structure"""

with open('portfolio.html', 'r', encoding='utf-8') as f:
    content = f.read()

# Find project 01 gallery
pos1 = content.find('gallery-projets-01')
start1 = content.rfind('<div class="gallery-container"', 0, pos1)
# Find the corresponding closing div
depth = 0
i = start1
while i < len(content):
    if '<div' in content[i:i+20]:
        depth += content[i:i+20].count('<div')
    if '</div>' in content[i:i+10]:
        depth -= 1
    if depth == 0 and i > start1:
        end1 = content.find('\n', i) + 1
        break
    i += 1

proj1_html = content[start1:end1]

# Find project 02 gallery (should be shot-grid now since I reverted)
pos2 = content.find('images MatchyKhedma')
start2 = content.rfind('<div class="shot-grid"', 0, pos2)
end2 = content.find('</div>\n          </div>\n        </div>', start2) + len('</div>')

proj2_html = content[start2:end2]

print("PROJECT 01 (first 800 chars):")
print(proj1_html[:800])
print("\n" + "="*50)
print("PROJECT 02 (first 800 chars):")
print(proj2_html[:800])
