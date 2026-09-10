import os
import glob
import re

base_dir = r'c:\seminarkitjogja.web.id\seminarkitjogja'

# --- 1. REVERT INTERNAL LINKS (put .html back) ---
html_files = glob.glob(os.path.join(base_dir, '**', '*.html'), recursive=True)

# Define known HTML pages
known_pages = {
    'index', 'blog', 'faq', 'paket', 'produk', 'starter-page', 'tentang-kami',
    'cara-memilih-seminar-kit', 'manfaat-corporate-gift', 'panduan-rab-souvenir',
    'paket-corporate-gift-instansi', 'paket-hampers-hari-raya', 'paket-seminar-kit-basic',
    'paket-seminar-kit-premium', 'paket-seminar-kit-standard', 'paket-souvenir-onboarding',
    'produk-agenda-kerja-kulit', 'produk-agenda-kulit-custom', 'produk-agenda-magnet',
    'produk-botol-minum-custom', 'produk-buku-planner', 'produk-corporate-gift-gathering',
    'produk-corporate-gift-hardbox', 'produk-corporate-gift-pouch-kulit', 'produk-corporate-gift-set-rups',
    'produk-corporate-gift-tumbler-premium', 'produk-corporate-gift-vip', 'produk-flashdisk-kartu-custom',
    'produk-hampers-custom', 'produk-hampers-hari-guru', 'produk-hampers-imlek', 'produk-hampers-lebaran',
    'produk-hampers-natal', 'produk-hampers-ultah-perusahaan', 'produk-mug-custom', 'produk-pulpen-metal-grafir',
    'produk-seminar-kit-basic', 'produk-seminar-kit-custom-logo', 'produk-seminar-kit-kampus',
    'produk-seminar-kit-korporat', 'produk-seminar-kit-premium', 'produk-seminar-kit-standard',
    'produk-souvenir-kantor-premium', 'produk-souvenir-onboarding'
}

for filepath in html_files:
    with open(filepath, 'r', encoding='utf-8') as f:
        content = f.read()
    original = content
    
    # restore href="/" to href="index.html"
    content = content.replace('href="/"', 'href="index.html"')
    
    def restore_html(m):
        url = m.group(1)
        # if it already has .html or is an external link, skip
        if url.endswith('.html') or url.startswith('http') or url.startswith('#') or url.startswith('tel:') or url.startswith('mailto:'):
            return m.group(0)
            
        # Extract the page name from the URL path
        basename = os.path.basename(url)
        if basename in known_pages:
            return f'href="{url}.html"'
        return m.group(0)

    # find href="something"
    content = re.sub(r'href="([^"]+)"', restore_html, content)

    if content != original:
        with open(filepath, 'w', encoding='utf-8') as f:
            f.write(content)

# --- 2. UPDATE IMAGES IN DETAIL PAGES ---
# Map of old src -> new src based on previous replacements
replacements = [
    # index.html "Seminar Kit Premium" -> used seminar-kit-premium-product.webp
    # wait, detail/produk-seminar-kit-premium.html should use the new image
    ('../assets/img/paket/seminar-kit-premium.webp', '../assets/img/produk/seminar-kit-premium-product.webp'),
    ('../assets/img/paket/seminar-kit-basic.webp', '../assets/img/produk/seminar-kit-basic-product.webp'),
    ('../assets/img/paket/seminar-kit-standard.webp', '../assets/img/produk/seminar-kit-standard-product.webp'),
    ('../assets/img/paket/souvenir-onboarding.webp', '../assets/img/produk/souvenir-premium.webp'),
    ('../assets/img/paket/corporate-gift-instansi.webp', '../assets/img/produk/corporate-gift-hardbox.webp'),
    ('../assets/img/produk/corporate-gift-gathering.webp', '../assets/img/produk/botol-minum-custom.webp')
]

# Specifically update detail/produk-*.html pages
detail_dir = os.path.join(base_dir, 'detail')
if os.path.exists(detail_dir):
    for f in os.listdir(detail_dir):
        if not f.startswith('produk-'):
            continue
        filepath = os.path.join(detail_dir, f)
        
        with open(filepath, 'r', encoding='utf-8') as file:
            content = file.read()
        original = content
        
        # Apply the specific replacements
        # Only do this for the MAIN image of the page (usually first large img or in the hero section)
        # but if we just replace all, the "Terkait" (related) products will also get fixed!
        if 'produk-seminar-kit-premium.html' in f:
            content = content.replace('../assets/img/paket/seminar-kit-premium.webp', '../assets/img/produk/seminar-kit-premium-product.webp')
        elif 'produk-seminar-kit-basic.html' in f:
            content = content.replace('../assets/img/paket/seminar-kit-basic.webp', '../assets/img/produk/seminar-kit-basic-product.webp')
        elif 'produk-seminar-kit-standard.html' in f:
            content = content.replace('../assets/img/paket/seminar-kit-standard.webp', '../assets/img/produk/seminar-kit-standard-product.webp')
        elif 'produk-souvenir-kantor-premium.html' in f:
            content = content.replace('../assets/img/paket/souvenir-onboarding.webp', '../assets/img/produk/souvenir-premium.webp')
        elif 'produk-corporate-gift-vip.html' in f:
            # this used corporate-gift-vip.webp natively anyway
            pass
        elif 'produk-corporate-gift-tumbler-premium.html' in f:
            content = content.replace('../assets/img/produk/corporate-gift-gathering.webp', '../assets/img/produk/botol-minum-custom.webp')
            
        # Now fix any related products section that might reference the old duplicates
        for old, new in replacements:
            content = content.replace(old, new)
            
        if content != original:
            with open(filepath, 'w', encoding='utf-8') as file:
                file.write(content)
            print(f"Updated images in {f}")

print("Reversion & Detail Image update complete.")
