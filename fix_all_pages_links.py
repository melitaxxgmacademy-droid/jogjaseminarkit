import os
import glob
import re

base_dir = r'c:\seminarkitjogja.web.id\seminarkitjogja'

# All listing pages
target_files = [
    os.path.join(base_dir, 'blog.html'),
    os.path.join(base_dir, 'paket.html'),
    os.path.join(base_dir, 'produk.html'),
    os.path.join(base_dir, 'produk-seminar-kit.html'),
    os.path.join(base_dir, 'produk-souvenir-kantor.html'),
    os.path.join(base_dir, 'produk-corporate-gift.html'),
    os.path.join(base_dir, 'produk-hampers.html'),
]

for filepath in target_files:
    if not os.path.exists(filepath):
        continue
    with open(filepath, 'r', encoding='utf-8') as f:
        content = f.read()
    original = content

    # 1. Add position-relative to card containers (so stretched-link works)
    content = re.sub(
        r'class="card h-100 (border-0 |)shadow-sm (overflow-hidden |)"',
        lambda m: m.group(0).replace('class="card h-100 ', 'class="card h-100 position-relative '),
        content
    )
    content = re.sub(
        r'class="card h-100 shadow-sm" style="border:',
        'class="card h-100 shadow-sm position-relative" style="border:',
        content
    )

    # 2. Add stretched-link to all Lihat Detail / Baca Selengkapnya buttons
    content = re.sub(
        r'class="btn w-100 fw-bold(?: py-2)?"(?! [^>]*stretched)',
        lambda m: m.group(0).replace('class="btn w-100 fw-bold', 'class="btn w-100 fw-bold stretched-link'),
        content
    )
    content = re.sub(
        r'class="btn w-100 fw-bold stretched-link py-2"',
        'class="btn w-100 fw-bold py-2 stretched-link"',
        content
    )
    # Blog "Baca Selengkapnya" buttons
    content = re.sub(
        r'class="btn w-100 fw-bold"(?! [^>]*stretched)',
        'class="btn w-100 fw-bold stretched-link"',
        content
    )

    if content != original:
        with open(filepath, 'w', encoding='utf-8') as f:
            f.write(content)
        print(f"Updated {os.path.basename(filepath)}")
    else:
        print(f"No changes: {os.path.basename(filepath)}")

print("Done!")
