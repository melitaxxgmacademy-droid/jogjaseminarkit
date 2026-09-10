content = open(r'c:\seminarkitjogja.web.id\seminarkitjogja\index.html', encoding='utf-8').read()
original = content

# For produk cards - change btn to use stretched-link on the title instead
# Remove the inline <a> from h4, and add stretched-link class to the existing button

replacements = [
    # Produk section - make btn use stretched-link
    (
        '<h4 class="card-title fw-bold mb-2" style="color: #1a2035; font-size: 1.2rem; font-family: \'Poppins\', sans-serif;"><a href="detail/produk-seminar-kit-premium.html" style="color:inherit; text-decoration:none;">Seminar Kit Premium</a></h4>',
        '<h4 class="card-title fw-bold mb-2" style="color: #1a2035; font-size: 1.2rem; font-family: \'Poppins\', sans-serif;">Seminar Kit Premium</h4>'
    ),
    (
        '<a class="btn mt-auto w-100" href="detail/produk-seminar-kit-premium.html"',
        '<a class="btn mt-auto w-100 stretched-link" href="detail/produk-seminar-kit-premium.html"'
    ),
    (
        '<h4 class="card-title fw-bold mb-2" style="color: #1a2035; font-size: 1.2rem; font-family: \'Poppins\', sans-serif;"><a href="detail/produk-souvenir-kantor-premium.html" style="color:inherit; text-decoration:none;">Souvenir Kantor Premium</a></h4>',
        '<h4 class="card-title fw-bold mb-2" style="color: #1a2035; font-size: 1.2rem; font-family: \'Poppins\', sans-serif;">Souvenir Kantor Premium</h4>'
    ),
    (
        '<a class="btn mt-auto w-100" href="detail/produk-souvenir-kantor-premium.html"',
        '<a class="btn mt-auto w-100 stretched-link" href="detail/produk-souvenir-kantor-premium.html"'
    ),
    (
        '<h4 class="card-title fw-bold mb-2" style="color: #1a2035; font-size: 1.2rem; font-family: \'Poppins\', sans-serif;"><a href="detail/produk-corporate-gift-vip.html" style="color:inherit; text-decoration:none;">Corporate Gift VIP</a></h4>',
        '<h4 class="card-title fw-bold mb-2" style="color: #1a2035; font-size: 1.2rem; font-family: \'Poppins\', sans-serif;">Corporate Gift VIP</h4>'
    ),
    (
        '<a class="btn mt-auto w-100" href="detail/produk-corporate-gift-vip.html"',
        '<a class="btn mt-auto w-100 stretched-link" href="detail/produk-corporate-gift-vip.html"'
    ),
    # Paket cards
    (
        '<h4 class="fw-bold mb-2" style="color:#1a2035; font-size:1.2rem; font-family: \'Poppins\', sans-serif;"><a href="detail/paket-seminar-kit-basic.html" style="color:inherit; text-decoration:none;">Paket Seminar Kit Basic</a></h4>',
        '<h4 class="fw-bold mb-2" style="color:#1a2035; font-size:1.2rem; font-family: \'Poppins\', sans-serif;">Paket Seminar Kit Basic</h4>'
    ),
    (
        '<a class="btn w-100 fw-bold py-2" href="detail/paket-seminar-kit-basic.html"',
        '<a class="btn w-100 fw-bold py-2 stretched-link" href="detail/paket-seminar-kit-basic.html"'
    ),
    (
        '<h4 class="fw-bold mb-2" style="color:#1a2035; font-size:1.2rem; font-family: \'Poppins\', sans-serif;"><a href="detail/paket-seminar-kit-standard.html" style="color:inherit; text-decoration:none;">Paket Seminar Kit Standard</a></h4>',
        '<h4 class="fw-bold mb-2" style="color:#1a2035; font-size:1.2rem; font-family: \'Poppins\', sans-serif;">Paket Seminar Kit Standard</h4>'
    ),
    (
        '<a class="btn w-100 fw-bold py-2" href="detail/paket-seminar-kit-standard.html"',
        '<a class="btn w-100 fw-bold py-2 stretched-link" href="detail/paket-seminar-kit-standard.html"'
    ),
    (
        '<h4 class="fw-bold mb-2" style="color:#1a2035; font-size:1.2rem; font-family: \'Poppins\', sans-serif;"><a href="detail/paket-seminar-kit-premium.html" style="color:inherit; text-decoration:none;">Paket Seminar Kit Premium</a></h4>',
        '<h4 class="fw-bold mb-2" style="color:#1a2035; font-size:1.2rem; font-family: \'Poppins\', sans-serif;">Paket Seminar Kit Premium</h4>'
    ),
    (
        '<a class="btn w-100 fw-bold py-2" href="detail/paket-seminar-kit-premium.html"',
        '<a class="btn w-100 fw-bold py-2 stretched-link" href="detail/paket-seminar-kit-premium.html"'
    ),
]

for old, new in replacements:
    if old in content:
        content = content.replace(old, new)
        print(f"OK: ...{old[30:80]}...")
    else:
        print(f"NOT FOUND: ...{old[30:80]}...")

# Also need card to be position:relative for stretched-link to work on produk cards
# The produk cards use class="card h-100 shadow-sm" - that needs position:relative
content = content.replace(
    'class="card h-100 shadow-sm" style="border: 1px solid #eaeaea; border-radius: 12px; overflow: hidden;"',
    'class="card h-100 shadow-sm position-relative" style="border: 1px solid #eaeaea; border-radius: 12px; overflow: hidden;"'
)

# Paket cards use class="card h-100 border-0 shadow-sm overflow-hidden"
content = content.replace(
    'class="card h-100 border-0 shadow-sm overflow-hidden" style="border-radius: 14px;"',
    'class="card h-100 border-0 shadow-sm overflow-hidden position-relative" style="border-radius: 14px;"'
)

if content != original:
    open(r'c:\seminarkitjogja.web.id\seminarkitjogja\index.html', 'w', encoding='utf-8').write(content)
    print('Saved!')
