import os
import glob
import re

base_dir = r'c:\seminarkitjogja.web.id\seminarkitjogja'
html_files = glob.glob(os.path.join(base_dir, 'produk-*.html'))

for filepath in html_files:
    fname = os.path.basename(filepath)
    with open(filepath, 'r', encoding='utf-8') as f:
        content = f.read()
    
    print(f"\n--- {fname} ---")
    cards = re.findall(r'<h4 class="card-title fw-bold[^>]*>.*?<a[^>]*>(.*?)</a></h4>\s*<p[^>]*>(.*?)</p>', content, re.DOTALL)
    for title, desc in cards:
        print(f"Title: {title.strip()}\nDesc:  {desc.strip()}\n")

