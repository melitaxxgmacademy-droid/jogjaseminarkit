import os
import glob
from datetime import datetime

base_dir = r'c:\seminarkitjogja.web.id\seminarkitjogja'
html_files = glob.glob(os.path.join(base_dir, '**', '*.html'), recursive=True)

urls = []
for filepath in html_files:
    # Skip any templates or specific files if needed
    filename = os.path.basename(filepath)
    if filename == 'kontak.html' or filename == 'starter-page.html':
        continue
        
    # Get relative path
    rel_path = os.path.relpath(filepath, base_dir)
    # Convert windows slashes to forward slashes
    rel_path = rel_path.replace('\\', '/')
    
    # Clean URL rules for Vercel
    if rel_path == 'index.html':
        clean_path = ''
    else:
        # Remove .html extension
        if rel_path.endswith('.html'):
            clean_path = rel_path[:-5]
        else:
            clean_path = rel_path
            
    full_url = f"https://seminarkitjogja.web.id/{clean_path}"
    urls.append(full_url)

# Sort urls: root first, then main pages, then subfolders
def sort_key(url):
    if url == "https://seminarkitjogja.web.id/": return 0
    if url.count('/') == 3: return 1 # e.g. https://domain.com/produk
    return 2 # e.g. https://domain.com/detail/produk

urls.sort(key=sort_key)

xml = ['<?xml version="1.0" encoding="UTF-8"?>']
xml.append('<urlset xmlns="http://www.sitemaps.org/schemas/sitemap/0.9">')

today = datetime.now().strftime('%Y-%m-%d')

for url in urls:
    xml.append('  <url>')
    xml.append(f'    <loc>{url}</loc>')
    xml.append(f'    <lastmod>{today}</lastmod>')
    
    # Priority rules
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
    
print(f"Generated sitemap.xml with {len(urls)} URLs (clean URLs for Vercel).")
