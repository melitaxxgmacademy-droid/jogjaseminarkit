import os
import glob
import re

detail_dir = 'c:\\seminarkitjogja.web.id\\seminarkitjogja\\detail'
html_files = glob.glob(os.path.join(detail_dir, '*.html'))

old_button_pattern = r'<a class="btn w-100 fw-bold py-2 btn-glass-outline" href="([^"]+)" style="border-radius:30px;">Lihat Detail</a>'
new_button_template = r'<a class="btn w-100 fw-bold py-2" href="\1" style="background-color:#1a2035; color:#fff; border-radius:30px;">Lihat Detail</a>'

for filepath in html_files:
    with open(filepath, 'r', encoding='utf-8') as f:
        content = f.read()

    original_content = content
    content = re.sub(old_button_pattern, new_button_template, content)

    if content != original_content:
        with open(filepath, 'w', encoding='utf-8') as f:
            f.write(content)
        print(f"Updated {os.path.basename(filepath)}")

