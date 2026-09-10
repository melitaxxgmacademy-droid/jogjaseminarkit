content = open(r'c:\seminarkitjogja.web.id\seminarkitjogja\index.html', encoding='utf-8').read()
original = content

# Produk cards (line 285, 298, 311) - card-title fw-bold mb-2
replacements = [
    # Produk section
    (
        '<h4 class="card-title fw-bold mb-2" style="color: #1a2035; font-size: 1.2rem; font-family: \'Poppins\', sans-serif;">Seminar Kit Premium</h4>',
        '<h4 class="card-title fw-bold mb-2" style="color: #1a2035; font-size: 1.2rem; font-family: \'Poppins\', sans-serif;"><a href="detail/produk-seminar-kit-premium.html" style="color:inherit; text-decoration:none;">Seminar Kit Premium</a></h4>'
    ),
    (
        '<h4 class="card-title fw-bold mb-2" style="color: #1a2035; font-size: 1.2rem; font-family: \'Poppins\', sans-serif;">Souvenir Kantor Premium</h4>',
        '<h4 class="card-title fw-bold mb-2" style="color: #1a2035; font-size: 1.2rem; font-family: \'Poppins\', sans-serif;"><a href="detail/produk-souvenir-kantor-premium.html" style="color:inherit; text-decoration:none;">Souvenir Kantor Premium</a></h4>'
    ),
    (
        '<h4 class="card-title fw-bold mb-2" style="color: #1a2035; font-size: 1.2rem; font-family: \'Poppins\', sans-serif;">Corporate Gift VIP</h4>',
        '<h4 class="card-title fw-bold mb-2" style="color: #1a2035; font-size: 1.2rem; font-family: \'Poppins\', sans-serif;"><a href="detail/produk-corporate-gift-vip.html" style="color:inherit; text-decoration:none;">Corporate Gift VIP</a></h4>'
    ),
    # Paket cards
    (
        '<h4 class="fw-bold mb-2" style="color:#1a2035; font-size:1.2rem; font-family: \'Poppins\', sans-serif;">Paket Seminar Kit Basic</h4>',
        '<h4 class="fw-bold mb-2" style="color:#1a2035; font-size:1.2rem; font-family: \'Poppins\', sans-serif;"><a href="detail/paket-seminar-kit-basic.html" style="color:inherit; text-decoration:none;">Paket Seminar Kit Basic</a></h4>'
    ),
    (
        '<h4 class="fw-bold mb-2" style="color:#1a2035; font-size:1.2rem; font-family: \'Poppins\', sans-serif;">Paket Seminar Kit Standard</h4>',
        '<h4 class="fw-bold mb-2" style="color:#1a2035; font-size:1.2rem; font-family: \'Poppins\', sans-serif;"><a href="detail/paket-seminar-kit-standard.html" style="color:inherit; text-decoration:none;">Paket Seminar Kit Standard</a></h4>'
    ),
    (
        '<h4 class="fw-bold mb-2" style="color:#1a2035; font-size:1.2rem; font-family: \'Poppins\', sans-serif;">Paket Seminar Kit Premium</h4>',
        '<h4 class="fw-bold mb-2" style="color:#1a2035; font-size:1.2rem; font-family: \'Poppins\', sans-serif;"><a href="detail/paket-seminar-kit-premium.html" style="color:inherit; text-decoration:none;">Paket Seminar Kit Premium</a></h4>'
    ),
]

for old, new in replacements:
    if old in content:
        content = content.replace(old, new)
        print(f"Replaced: {old[:60]}...")
    else:
        print(f"NOT FOUND: {old[:60]}...")

if content != original:
    open(r'c:\seminarkitjogja.web.id\seminarkitjogja\index.html', 'w', encoding='utf-8').write(content)
    print('Saved.')
