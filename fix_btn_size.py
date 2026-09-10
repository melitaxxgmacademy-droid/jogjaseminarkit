import os
import glob

detail_dir = 'c:\\seminarkitjogja.web.id\\seminarkitjogja\\detail'
html_files = glob.glob(os.path.join(detail_dir, '*.html'))

old_style = 'style="width: fit-content; min-width: 250px; margin: 0 auto; display: flex; justify-content: center;"'
new_style = 'style="width: fit-content; min-width: 320px; margin: 0 auto; display: flex; align-items: center; justify-content: center; padding: 12px 30px; font-size: 1.1rem; border-radius: 50px;"'

for filepath in html_files:
    with open(filepath, 'r', encoding='utf-8') as f:
        content = f.read()

    original_content = content
    content = content.replace(old_style, new_style)

    if content != original_content:
        with open(filepath, 'w', encoding='utf-8') as f:
            f.write(content)
        print(f"Updated {os.path.basename(filepath)}")

