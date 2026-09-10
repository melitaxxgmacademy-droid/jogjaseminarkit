import os
import re

filepath = r'c:\seminarkitjogja.web.id\seminarkitjogja\index.html'

with open(filepath, 'r', encoding='utf-8') as f:
    content = f.read()
original = content

# Pattern for paket-style: h4.fw-bold.mb-2 title then some content then button with href
pattern = r'(<h4 class="fw-bold mb-2"[^>]*>)((?:(?!<a ).)*?)(</h4>)(.*?)(<a class="btn w-100[^>]*href="([^"]+)")'
content = re.sub(pattern, 
    lambda m: (m.group(1) + '<a href="' + m.group(6) + '" style="color:inherit;text-decoration:none;">' + m.group(2) + '</a>' + m.group(3) + m.group(4) + m.group(5)),
    content, flags=re.DOTALL)

# Pattern for produk-style: h4.card-title.fw-bold.mb-2 or mb-3 followed by btn mt-auto w-100
pattern2 = r'(<h4 class="card-title fw-bold mb-[23]"[^>]*>)((?:(?!</h4>)(?!<a ).)*?)(</h4>)(.*?)(<a class="btn mt-auto w-100[^>]*href="([^"]+)")'
content = re.sub(pattern2,
    lambda m: (m.group(1) + '<a href="' + m.group(6) + '" style="color:inherit;text-decoration:none;">' + m.group(2) + '</a>' + m.group(3) + m.group(4) + m.group(5)),
    content, flags=re.DOTALL)

if content != original:
    with open(filepath, 'w', encoding='utf-8') as f:
        f.write(content)
    print("Updated index.html")
else:
    print("No change: index.html")

