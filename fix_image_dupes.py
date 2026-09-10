import os
import re

base_dir = r'c:\seminarkitjogja.web.id\seminarkitjogja'

def update_file(filename, replacements):
    filepath = os.path.join(base_dir, filename)
    with open(filepath, 'r', encoding='utf-8') as f:
        content = f.read()
    
    original = content
    for old, new in replacements:
        content = content.replace(old, new)
        
    if content != original:
        with open(filepath, 'w', encoding='utf-8') as f:
            f.write(content)
        print(f"Updated {filename}")
    else:
        print(f"No changes made to {filename}")

# 1. index.html
update_file('index.html', [
    # Only replace the first occurrence (Produk Unggulan) not the second (Paket)
    # The first one has alt="Paket Seminar Kit Premium Yogyakarta" inside the first block
    # Actually let's be very specific:
    ('<img alt="Paket Seminar Kit Premium Yogyakarta" class="card-img-top" src="assets/img/paket/seminar-kit-premium.webp" style="border-radius: 12px 12px 0 0;',
     '<img alt="Seminar Kit Premium Yogyakarta" class="card-img-top" src="assets/img/produk/seminar-kit-premium-product.webp" style="border-radius: 12px 12px 0 0;')
])

# 2. produk.html
update_file('produk.html', [
    ('src="assets/img/paket/seminar-kit-basic.webp"', 'src="assets/img/produk/seminar-kit-custom-logo.webp"'),
    ('src="assets/img/paket/souvenir-onboarding.webp"', 'src="assets/img/produk/souvenir-premium.webp"'),
    ('src="assets/img/paket/corporate-gift-instansi.webp"', 'src="assets/img/produk/corporate-gift-hardbox.webp"')
])

# 3. produk-seminar-kit.html
update_file('produk-seminar-kit.html', [
    ('src="assets/img/paket/seminar-kit-basic.webp"', 'src="assets/img/produk/seminar-kit-basic-product.webp"'),
    ('src="assets/img/paket/seminar-kit-standard.webp"', 'src="assets/img/produk/seminar-kit-standard-product.webp"'),
    ('src="assets/img/paket/seminar-kit-premium.webp"', 'src="assets/img/produk/seminar-kit-premium-product.webp"')
])

# 4. produk-corporate-gift.html
# The first instance of corporate-gift-gathering.webp is for Tumbler Premium
filepath = os.path.join(base_dir, 'produk-corporate-gift.html')
with open(filepath, 'r', encoding='utf-8') as f:
    content = f.read()

# Replace the first occurrence
content = content.replace('src="assets/img/produk/corporate-gift-gathering.webp"', 'src="assets/img/produk/botol-minum-custom.webp"', 1)
with open(filepath, 'w', encoding='utf-8') as f:
    f.write(content)
print("Updated produk-corporate-gift.html")

