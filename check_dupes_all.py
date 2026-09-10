import re
import os
import glob
from collections import defaultdict

base_dir = r'c:\seminarkitjogja.web.id\seminarkitjogja'
html_files = glob.glob(os.path.join(base_dir, '*.html'))

# mapping of image -> list of (file, section_or_alt)
usage = defaultdict(list)

for filepath in html_files:
    fname = os.path.basename(filepath)
    with open(filepath, 'r', encoding='utf-8') as file:
        content = file.read()
        
    # Find all <img alt="..." src="..."> 
    imgs = re.findall(r'<img[^>]*alt="([^"]*)"[^>]*src="([^"]+)"[^>]*>', content)
    for alt, src in imgs:
        if 'assets/img/' in src and not src.endswith('.ico') and not src.endswith('.png'):
            usage[src].append(f"{fname} (alt: {alt})")

print("Checking for Reused Images Across Different Concepts:")
for img, places in usage.items():
    if len(places) > 1:
        # If it's used in index and in its own detail page, that's normal.
        # We're looking for images used in multiple DIFFERENT product listings.
        print(f"\n--- {img} ---")
        for p in places:
            print(f"  {p}")

