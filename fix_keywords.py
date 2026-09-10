import os
import glob
import re

base_dir = r'c:\seminarkitjogja.web.id\seminarkitjogja'
html_files = glob.glob(os.path.join(base_dir, '*.html')) + glob.glob(os.path.join(base_dir, 'detail', '*.html'))

def deduplicate_keywords(match):
    kw_string = match.group(1)
    # Split by comma, strip whitespace, remove empty
    kws = [k.strip() for k in kw_string.split(',') if k.strip()]
    
    # Deduplicate while preserving order
    seen = set()
    unique_kws = []
    for k in kws:
        if k not in seen:
            seen.add(k)
            unique_kws.append(k)
            
    return f'<meta name="keywords" content="{", ".join(unique_kws)}">'

for filepath in html_files:
    if os.path.basename(filepath) == 'kontak.html':
        continue
        
    with open(filepath, 'r', encoding='utf-8') as f:
        content = f.read()
        
    original_content = content
    
    # 1. Fix duplicate keywords
    content = re.sub(r'<meta name="keywords" content="(.*?)">', deduplicate_keywords, content)
    
    # 2. Remove kontak.html link from footer
    # Matches <li>...<a ... href="kontak.html" ...>Kontak</a>...</li>
    # Also handles ../kontak.html
    content = re.sub(r'<li>\s*<a[^>]*href="(?:\.\./)?kontak\.html"[^>]*>.*?</a>\s*</li>\s*', '', content, flags=re.IGNORECASE | re.DOTALL)
    
    if content != original_content:
        with open(filepath, 'w', encoding='utf-8') as f:
            f.write(content)
            
# 3. Delete kontak.html
kontak_path = os.path.join(base_dir, 'kontak.html')
if os.path.exists(kontak_path):
    os.remove(kontak_path)
    print("Deleted kontak.html")
    
print("Successfully fixed keywords and removed kontak.html references.")
