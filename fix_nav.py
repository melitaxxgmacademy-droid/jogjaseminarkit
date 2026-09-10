import os
import glob

BASE = r'c:\seminarkitjogja.web.id\seminarkitjogja'

html_files = glob.glob(os.path.join(BASE, '**', '*.html'), recursive=True)

# Strings to find and replace
OLD_NAV = '<nav class="navmenu" id="navmenu" style="flex:1;display:flex;justify-content:center;margin-right:150px;">'
OLD_UL = '<ul class="d-flex justify-content-center align-items-center">'

NEW_NAV = '<nav class="navmenu" id="navmenu">'
NEW_UL = '<ul>'

count = 0
for filepath in html_files:
    with open(filepath, 'r', encoding='utf-8') as f:
        content = f.read()
    
    if OLD_NAV in content or OLD_UL in content:
        content = content.replace(OLD_NAV, NEW_NAV)
        content = content.replace(OLD_UL, NEW_UL)
        
        with open(filepath, 'w', encoding='utf-8') as f:
            f.write(content)
        count += 1
        
print(f"Updated {count} HTML files.")
