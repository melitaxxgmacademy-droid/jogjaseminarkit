import os
import re

base_dir = r'c:\seminarkitjogja.web.id\seminarkitjogja'
pages = ['produk-seminar-kit.html', 'produk-souvenir-kantor.html', 'produk-corporate-gift.html', 'produk-hampers.html']

for page in pages:
    filepath = os.path.join(base_dir, page)
    with open(filepath, 'r', encoding='utf-8') as f:
        content = f.read()
    original = content

    # Pattern: h4.card-title.fw-bold.mb-2 -> ... -> <a class="btn mt-auto w-100" href="...">
    # Wrap just the title text with <a>
    pattern = r'(<h4 class="card-title fw-bold mb-2"[^>]*>)((?:(?!</h4>)(?!<a ).)*?)(</h4>)(.*?)(<a class="btn mt-auto w-100[^>]*href="([^"]+)")'
    
    def replacer(m):
        h4_open = m.group(1)
        title = m.group(2)
        h4_close = m.group(3)
        between = m.group(4)
        btn = m.group(5)
        href = m.group(6)
        return f'{h4_open}<a href="{href}" style="color:inherit;text-decoration:none;">{title}</a>{h4_close}{between}{btn}'

    new_content = re.sub(pattern, replacer, content, flags=re.DOTALL)

    if new_content != original:
        with open(filepath, 'w', encoding='utf-8') as f:
            f.write(new_content)
        print(f"Updated {page}")
    else:
        print(f"No change: {page}")
