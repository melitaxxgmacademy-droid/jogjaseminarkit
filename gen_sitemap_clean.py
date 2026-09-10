import os
import glob
from datetime import datetime

base_dir = r'c:\seminarkitjogja.web.id\seminarkitjogja'
html_files = glob.glob(os.path.join(base_dir, '**', '*.html'), recursive=True)

urls = []
for filepath in html_files:
    filename = os.path.basename(filepath)
    if filename in ('kontak.html', 'starter-page.html'):
        continue
        
    rel_path = os.path.relpath(filepath, base_dir).replace('\\', '/')
    
    if rel_path == 'index.html':
        full_url = "https://seminarkitjogja.web.id/"
    else:
        # Remove .html for clean URL
        clean = rel_path[:-5] if rel_path.endswith('.html') else rel_path
        full_url = f"https://seminarkitjogja.web.id/{clean}"
        
    urls.append(full_url)

def sort_key(url):
    if url == "https://seminarkitjogja.web.id/": return 0
    if url.count('/') == 3: return 1
    return 2

urls.sort(key=sort_key)

today = datetime.now().strftime('%Y-%m-%d')
xml = ['<?xml version="1.0" encoding="UTF-8"?>',
       '<urlset xmlns="http://www.sitemaps.org/schemas/sitemap/0.9">']

for url in urls:
    if url == "https://seminarkitjogja.web.id/":
        priority, freq = "1.0", "weekly"
    elif url.count('/') == 3:
        priority, freq = "0.8", "weekly"
    else:
        priority, freq = "0.6", "monthly"
    
    xml += [
        '  <url>',
        f'    <loc>{url}</loc>',
        f'    <lastmod>{today}</lastmod>',
        f'    <changefreq>{freq}</changefreq>',
        f'    <priority>{priority}</priority>',
        '  </url>'
    ]

xml.append('</urlset>')

with open(os.path.join(base_dir, 'sitemap.xml'), 'w', encoding='utf-8') as f:
    f.write('\n'.join(xml))

print(f"Done! {len(urls)} clean URLs ditulis ke sitemap.xml")
