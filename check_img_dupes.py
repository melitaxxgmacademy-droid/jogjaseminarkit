import re
import os

base_dir = r'c:\seminarkitjogja.web.id\seminarkitjogja'
files_to_check = ['index.html', 'produk.html', 'paket.html']

image_usage = {}

for f in files_to_check:
    filepath = os.path.join(base_dir, f)
    if not os.path.exists(filepath): continue
    
    with open(filepath, 'r', encoding='utf-8') as file:
        content = file.read()
        
    # Find all <img src="..."> 
    imgs = re.findall(r'<img[^>]*src="([^"]+)"[^>]*>', content)
    for img in imgs:
        if 'assets/img/' in img and not img.endswith('.ico') and not img.endswith('.png'):
            if img not in image_usage:
                image_usage[img] = []
            image_usage[img].append(f)

for img, pages in image_usage.items():
    if len(pages) > 1 or pages.count(pages[0]) > 1:
        print(f"DUPLICATE OR REUSED: {img} -> used in {pages}")
    else:
        print(f"Single use: {img} -> used in {pages}")

