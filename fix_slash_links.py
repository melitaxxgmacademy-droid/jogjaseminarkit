import os
import glob

base_dir = r'c:\seminarkitjogja.web.id\seminarkitjogja'

# Root files
root_html_files = glob.glob(os.path.join(base_dir, '*.html'))
for filepath in root_html_files:
    with open(filepath, 'r', encoding='utf-8') as f:
        content = f.read()
    
    original = content
    content = content.replace('href="/"', 'href="index.html"')
    
    if content != original:
        with open(filepath, 'w', encoding='utf-8') as f:
            f.write(content)
        print(f"Updated {os.path.basename(filepath)}")

# Detail files
detail_html_files = glob.glob(os.path.join(base_dir, 'detail', '*.html'))
for filepath in detail_html_files:
    with open(filepath, 'r', encoding='utf-8') as f:
        content = f.read()
        
    original = content
    content = content.replace('href="/"', 'href="../index.html"')
    
    if content != original:
        with open(filepath, 'w', encoding='utf-8') as f:
            f.write(content)
        print(f"Updated {os.path.basename(filepath)}")

print("Successfully replaced all slash links with index.html")
