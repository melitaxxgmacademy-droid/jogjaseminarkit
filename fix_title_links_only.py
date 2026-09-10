import os
import re

base_dir = r'c:\seminarkitjogja.web.id\seminarkitjogja'

# ---- produk.html: category cards -> link to category pages ----
produk_path = os.path.join(base_dir, 'produk.html')
with open(produk_path, 'r', encoding='utf-8') as f:
    content = f.read()
original = content

category_map = {
    '>Seminar Kit</h4>': ' href="produk-seminar-kit.html"',
    '>Souvenir Kantor</h4>': ' href="produk-souvenir-kantor.html"',
    '>Corporate Gift</h4>': ' href="produk-corporate-gift.html"',
    '>Hampers</h4>': ' href="produk-hampers.html"',
}
for title_end, link in category_map.items():
    # Wrap title with an <a>
    content = content.replace(
        '<h4 class="card-title fw-bold"' + title_end,
        '<h4 class="card-title fw-bold"><a' + link + ' style="color:inherit;text-decoration:none;"' + title_end + '</a></h4>'
    )

if content != original:
    with open(produk_path, 'w', encoding='utf-8') as f:
        f.write(content)
    print("Updated produk.html")

# ---- paket.html + produk-*.html: check if stretched-link is missing from card ----
# For these pages, add <a> wrapper around just the <h4> title, pointing to the detail link nearby

def add_title_link(filepath):
    with open(filepath, 'r', encoding='utf-8') as f:
        content = f.read()
    original = content

    # Pattern: find h4 with fw-bold mb-2 that is NOT already wrapped in <a>, followed somewhere by btn href
    def wrap_title(m):
        h4_open = m.group(1)   # e.g. <h4 class="fw-bold mb-2" ...>
        title = m.group(2)     # e.g. Paket Seminar Kit Basic
        h4_close = m.group(3)  # </h4>
        after = m.group(4)     # content between h4 and button
        btn_href = m.group(5)  # href value from the nearby button
        button_all = m.group(6) # full button
        
        # If title already has <a>, skip
        if '<a ' in title:
            return m.group(0)
        
        wrapped_title = f'{h4_open}<a href="{btn_href}" style="color:inherit;text-decoration:none;">{title}</a>{h4_close}'
        return wrapped_title + after + button_all

    # Pattern for paket-style: h4.fw-bold.mb-2 title then some content then button with href
    pattern = r'(<h4 class="fw-bold mb-2"[^>]*>)((?:(?!<a ).)*?)(</h4>)(.*?)(<a class="btn w-100[^>]*href="([^"]+)")'
    content = re.sub(pattern, 
        lambda m: (m.group(1) + '<a href="' + m.group(6) + '" style="color:inherit;text-decoration:none;">' + m.group(2) + '</a>' + m.group(3) + m.group(4) + m.group(5)),
        content, flags=re.DOTALL)

    # Pattern for produk-style: h4.card-title.fw-bold.mb-2 or mb-3
    pattern2 = r'(<h4 class="card-title fw-bold mb-[23]"[^>]*>)((?:(?!</h4>)(?!<a ).)*?)(</h4>)(.*?)(<a class="btn w-100[^>]*href="([^"]+)")'
    content = re.sub(pattern2,
        lambda m: (m.group(1) + '<a href="' + m.group(6) + '" style="color:inherit;text-decoration:none;">' + m.group(2) + '</a>' + m.group(3) + m.group(4) + m.group(5)),
        content, flags=re.DOTALL)

    if content != original:
        with open(filepath, 'w', encoding='utf-8') as f:
            f.write(content)
        print(f"Updated {os.path.basename(filepath)}")
    else:
        print(f"No change: {os.path.basename(filepath)}")

pages = ['paket.html', 'blog.html', 'produk-seminar-kit.html', 'produk-souvenir-kantor.html', 'produk-corporate-gift.html', 'produk-hampers.html']
for page in pages:
    add_title_link(os.path.join(base_dir, page))

print("Done!")
