import os

filepath = r'c:\seminarkitjogja.web.id\seminarkitjogja\index.html'
with open(filepath, 'r', encoding='utf-8') as f:
    content = f.read()
    
# Remove border-0 and add a very thin border style
old_str = 'class="card h-100 border-0 shadow-sm p-4 text-center"'
new_str = 'class="card h-100 shadow-sm p-4 text-center" style="border: 1px solid rgba(0,0,0,0.08);"'

if old_str in content:
    content = content.replace(old_str, new_str)
    with open(filepath, 'w', encoding='utf-8') as f:
        f.write(content)
    print("Updated index.html feature cards")
else:
    print("String not found")
