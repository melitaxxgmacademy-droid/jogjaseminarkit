import os
import re

# 1. Update sitemap.xml
sitemap_path = r'c:\seminarkitjogja.web.id\seminarkitjogja\sitemap.xml'
with open(sitemap_path, 'r', encoding='utf-8') as f:
    sitemap = f.read()

sitemap = re.sub(r'\s*<url>\s*<loc>https://seminarkitjogja\.web\.id/starter-page\.html</loc>[\s\S]*?</url>', '', sitemap)

with open(sitemap_path, 'w', encoding='utf-8') as f:
    f.write(sitemap)

# 2. Update starter-page.html
starter_path = r'c:\seminarkitjogja.web.id\seminarkitjogja\starter-page.html'
with open(starter_path, 'r', encoding='utf-8') as f:
    html = f.read()

# Replace robots tag
html = re.sub(r'<meta name="robots" content="index, follow, max-image-preview:large, max-snippet:-1"/?>', '<meta name="robots" content="noindex, nofollow">', html)

with open(starter_path, 'w', encoding='utf-8') as f:
    f.write(html)

print("Bagian 1 complete.")
