import os
import glob
import re

base_dir = r'c:\seminarkitjogja.web.id\seminarkitjogja'
html_files = glob.glob(os.path.join(base_dir, '**', '*.html'), recursive=True)

for filepath in html_files:
    with open(filepath, 'r', encoding='utf-8') as f:
        content = f.read()
    
    original = content
    
    # 1. Change href="index.html" to href="/"
    content = content.replace('href="index.html"', 'href="/"')
    # Change href="../index.html" to href="/"
    content = content.replace('href="../index.html"', 'href="/"')
    
    # 2. Change href="detail/something.html" to href="/detail/something"
    # To be safe, we'll replace .html in internal hrefs
    # Match href="[not starting with http or mailto or tel or #][anything].html"
    def remove_html(m):
        full_match = m.group(0)
        url = m.group(1)
        if url.startswith('http') or url.startswith('mailto') or url.startswith('tel') or url.startswith('#'):
            return full_match
        
        # if it's already just "/", don't touch
        if url == '/':
            return full_match
            
        # remove .html
        new_url = url
        if new_url.endswith('.html'):
            new_url = new_url[:-5]
            
        # ensure it starts with / if it's a top-level or detail/ link for absolute routing on vercel
        # Wait, relative routing like "detail/paket.html" -> "detail/paket" works fine on Vercel.
        # But if they are inside detail/ folder and do href="../produk", that also works.
        # Let's just remove .html
        return f'href="{new_url}"'

    content = re.sub(r'href="([^"]+\.html)"', remove_html, content)

    if content != original:
        with open(filepath, 'w', encoding='utf-8') as f:
            f.write(content)
        print(f"Updated links in {os.path.basename(filepath)}")

