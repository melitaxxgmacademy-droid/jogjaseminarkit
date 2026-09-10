import os
import glob
import re

base_dir = r'c:\seminarkitjogja.web.id\seminarkitjogja'
html_files = glob.glob(os.path.join(base_dir, '**', '*.html'), recursive=True)

for filepath in html_files:
    with open(filepath, 'r', encoding='utf-8') as f:
        content = f.read()
    original = content
    
    def restore_html(m):
        url = m.group(1)
        # Skip external links, fragments, or empty
        if url.startswith('http') or url.startswith('mailto:') or url.startswith('tel:') or url.startswith('#') or url == '':
            return m.group(0)
            
        # Skip if it already has .html or .php or trailing slash
        if url.endswith('.html') or url.endswith('/') or '.' in os.path.basename(url):
            return m.group(0)
            
        # If it's literally just a word or path without extension, add .html
        return f'href="{url}.html"'

    # find href="something"
    content = re.sub(r'href="([^"]+)"', restore_html, content)

    if content != original:
        with open(filepath, 'w', encoding='utf-8') as f:
            f.write(content)
        print(f"Restored .html in {os.path.basename(filepath)}")

print("Done restoring all missing .html links!")
