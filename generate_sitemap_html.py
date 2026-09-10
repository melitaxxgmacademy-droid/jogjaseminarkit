import os
import glob
from datetime import datetime

base_dir = r'c:\seminarkitjogja.web.id\seminarkitjogja'
html_files = glob.glob(os.path.join(base_dir, '**', '*.html'), recursive=True)

urls = []
for filepath in html_files:
    filename = os.path.basename(filepath)
    if filename == 'kontak.html' or filename == 'starter-page.html':
        continue
        
    rel_path = os.path.relpath(filepath, base_dir)
    rel_path = rel_path.replace('\\', '/')
    
    if rel_path == 'index.html':
        full_url = "https://seminarkitjogja.web.id/"
    else:
        full_url = f"https://seminarkitjogja.web.id/{rel_path}"
        
    urls.append(full_url)

def sort_key(url):
    if url == "https://seminarkitjogja.web.id/": return 0
    if url.count('/') == 3: return 1 
    return 2 

urls.sort(key=sort_key)

xml = ['<?xml version="1.0" encoding="UTF-8"?>']
xml.append('<urlset xmlns="http://www.sitemaps.org/schemas/sitemap/0.9">')

today = datetime.now().strftime('%Y-%m-%d')

for url in urls:
    xml.append('  <url>')
    xml.append(f'    <loc>{url}</loc>')
    xml.append(f'    <lastmod>{today}</lastmod>')
    
    if url == "https://seminarkitjogja.web.id/":
        priority = "1.0"
        freq = "weekly"
    elif url.count('/') == 3:
        priority = "0.8"
        freq = "weekly"
    else:
        priority = "0.6"
        freq = "monthly"
        
    xml.append(f'    <changefreq>{freq}</changefreq>')
    xml.append(f'    <priority>{priority}</priority>')
    xml.append('  </url>')
    
xml.append('</urlset>')

sitemap_path = os.path.join(base_dir, 'sitemap.xml')
with open(sitemap_path, 'w', encoding='utf-8') as f:
    f.write('\n'.join(xml))
