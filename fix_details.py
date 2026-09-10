import os
import glob
import re

detail_dir = 'c:\\seminarkitjogja.web.id\\seminarkitjogja\\detail'
html_files = glob.glob(os.path.join(detail_dir, '*.html'))

premium_card_html = '''<div class="col-md-4 mb-4" data-aos="fade-up" data-aos-delay="100">
<div class="card h-100 border-0 shadow-sm overflow-hidden" style="border-radius: 14px;">
<div class="position-relative">
<img alt="Paket Seminar Kit Premium Yogyakarta" class="card-img-top" src="../assets/img/paket/seminar-kit-premium.webp" style="object-fit:cover; height:200px;"/>
</div>
<div class="card-body p-4 d-flex flex-column">
<h4 class="card-title fw-bold mb-3" style="color:#1a2035; font-size:1.2rem; font-family: 'Poppins', sans-serif;">Seminar Kit Premium</h4>
<p class="card-text text-muted mb-4" style="font-size:0.9rem; line-height:1.6;">Pouch kulit eksklusif, agenda magnet, tumbler premium grafir, flashdisk, dan pulpen metal.</p>
<div class="mt-auto">
<a class="btn w-100 fw-bold py-2 btn-glass-outline" href="produk-seminar-kit-premium.html" style="border-radius:30px;">Lihat Detail</a>
</div>
</div>
</div>
</div>'''

for filepath in html_files:
    with open(filepath, 'r', encoding='utf-8') as f:
        content = f.read()

    original_content = content

    # 1. Fix CTA button: replace w-100 with centered inline styles to avoid cache issues
    content = content.replace('class="btn btn-whatsapp btn-lg w-100 shadow-sm"', 'class="btn btn-whatsapp btn-lg shadow-sm" style="width: fit-content; min-width: 250px; margin: 0 auto; display: flex; justify-content: center;"')
    
    # 2. If it's a paket file, fix "Produk Seminar Kit Terkait" to "Paket Seminar Kit Terkait"
    basename = os.path.basename(filepath)
    if basename.startswith('paket-'):
        content = content.replace('<h3 class="mb-4">Produk Seminar Kit Terkait</h3>', '<h3 class="mb-4">Paket Seminar Kit Terkait</h3>')
        content = content.replace('<h3 class="mb-4">Produk Souvenir Kantor Terkait</h3>', '<h3 class="mb-4">Paket Souvenir Kantor Terkait</h3>')
        content = content.replace('<h3 class="mb-4">Produk Corporate Gift Terkait</h3>', '<h3 class="mb-4">Paket Corporate Gift Terkait</h3>')

    # 3. Prevent current product from showing in related products
    # We will use regex to find and replace the specific card DIV if it matches the current file
    
    if 'seminar-kit-basic.html' in basename:
        # Regex to match the Basic card
        pattern = r'<div class="col-md-4 mb-4"[^>]*>.*?<h4 class="card-title[^>]*>Seminar Kit Basic</h4>.*?</div>\s*</div>\s*</div>\s*</div>'
        content = re.sub(pattern, premium_card_html, content, flags=re.DOTALL)
        
    elif 'seminar-kit-standard.html' in basename:
        # Regex to match the Standard card
        pattern = r'<div class="col-md-4 mb-4"[^>]*>.*?<h4 class="card-title[^>]*>Seminar Kit Standard</h4>.*?</div>\s*</div>\s*</div>\s*</div>'
        content = re.sub(pattern, premium_card_html, content, flags=re.DOTALL)
        
    elif 'seminar-kit-kampus.html' in basename:
        # Regex to match the Kampus card
        pattern = r'<div class="col-md-4 mb-4"[^>]*>.*?<h4 class="card-title[^>]*>Seminar Kit Kampus \(Mahasiswa\)</h4>.*?</div>\s*</div>\s*</div>\s*</div>'
        content = re.sub(pattern, premium_card_html, content, flags=re.DOTALL)

    if content != original_content:
        with open(filepath, 'w', encoding='utf-8') as f:
            f.write(content)
        print(f"Updated {basename}")

