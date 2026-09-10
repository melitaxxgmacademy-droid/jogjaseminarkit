import os
import glob

base_dir = r'c:\seminarkitjogja.web.id\seminarkitjogja'
html_files = glob.glob(os.path.join(base_dir, '*.html'))

for filepath in html_files:
    with open(filepath, 'r', encoding='utf-8') as f:
        content = f.read()
    original = content

    # Remove stretched-link class
    content = content.replace(' stretched-link', '')
    content = content.replace('stretched-link ', '')
    content = content.replace('stretched-link', '')

    if content != original:
        with open(filepath, 'w', encoding='utf-8') as f:
            f.write(content)
        print(f"Removed stretched-link from {os.path.basename(filepath)}")

