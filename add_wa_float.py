import os
import glob

html_files = []
for root, dirs, files in os.walk(r'c:\seminarkitjogja.web.id\seminarkitjogja'):
    for file in files:
        if file.endswith('.html'):
            html_files.append(os.path.join(root, file))

wa_html = """
<!-- WhatsApp Float -->
<a href="https://wa.me/6288989643555?text=Halo%20Seminar%20Kit%20Jogja,%20saya%20ingin%20konsultasi%20pengadaan%20souvenir." target="_blank" class="whatsapp-float d-flex align-items-center justify-content-center"><i class="bi bi-whatsapp"></i></a>
"""

for file_path in html_files:
    with open(file_path, 'r', encoding='utf-8') as f:
        content = f.read()

    if 'class="whatsapp-float"' in content:
        continue # Already added

    # Find <!-- Scroll Top --> and insert before it
    if '<!-- Scroll Top -->' in content:
        content = content.replace('<!-- Scroll Top -->', wa_html + '<!-- Scroll Top -->')
        with open(file_path, 'w', encoding='utf-8') as f:
            f.write(content)
        print(f"Added to {file_path}")
    else:
        print(f"Skipped {file_path} (Scroll Top comment not found)")
