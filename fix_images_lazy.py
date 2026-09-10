import os
import re

dir_path = r'c:\seminar kit jogja tinggal mobile\seminarkitjogja.web.id\seminarkitjogja'

def fix_images_in_html(filepath):
    try:
        with open(filepath, 'r', encoding='utf-8') as f:
            content = f.read()
    except UnicodeDecodeError:
        with open(filepath, 'r', encoding='cp1252') as f:
            content = f.read()

    original_content = content
    
    def repl(m):
        img_tag = m.group(0)
        # Skip if already has loading=
        if re.search(r'\bloading=', img_tag, re.IGNORECASE):
            return img_tag
        # Skip if fetchpriority=high
        if re.search(r'\bfetchpriority=[\"\']high[\"\']', img_tag, re.IGNORECASE):
            return img_tag
        
        # Add loading='lazy' before closing bracket
        if img_tag.endswith('/>'):
            return img_tag[:-2] + ' loading=\"lazy\"/>'
        elif img_tag.endswith('>'):
            return img_tag[:-1] + ' loading=\"lazy\">'
        return img_tag

    # Match img tags
    content = re.sub(r'<img\s+[^>]+>', repl, content, flags=re.IGNORECASE)

    if content != original_content:
        # Write back with the same encoding that worked
        # Since we might have read with cp1252, let's write with utf-8 to standardize, or keep utf-8.
        # Actually it's safer to write with utf-8
        with open(filepath, 'w', encoding='utf-8') as f:
            f.write(content)
        return True
    return False

modified_count = 0
for root, dirs, files in os.walk(dir_path):
    for file in files:
        if file.endswith('.html'):
            if fix_images_in_html(os.path.join(root, file)):
                modified_count += 1

print(f"Modified {modified_count} HTML files.")
