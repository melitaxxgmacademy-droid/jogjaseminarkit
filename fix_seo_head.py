import os
import glob
import re
from bs4 import BeautifulSoup

base_dir = r'c:\seminarkitjogja.web.id\seminarkitjogja'
html_files = glob.glob(os.path.join(base_dir, '*.html')) + glob.glob(os.path.join(base_dir, 'detail', '*.html'))

for filepath in html_files:
    with open(filepath, 'r', encoding='utf-8') as f:
        content = f.read()
        
    soup = BeautifulSoup(content, 'html.parser')
    head = soup.head
    if not head:
        continue
        
    # Extract existing meta
    title_tag = head.find('title')
    title = title_tag.text.strip() if title_tag else "Vendor Seminar Kit & Souvenir Kantor Jogja Terpercaya - Seminar Kit Jogja"
    
    desc_tag = head.find('meta', attrs={'name': 'description'})
    description = desc_tag['content'].strip() if desc_tag and 'content' in desc_tag.attrs else "Layanan profesional pengadaan Seminar Kit Jogja di Yogyakarta. Kualitas premium, pengerjaan cepat, dan mendukung legalitas Faktur Pajak."
    
    canonical_tag = head.find('link', attrs={'rel': 'canonical'})
    canonical = canonical_tag['href'].strip() if canonical_tag and 'href' in canonical_tag.attrs else "https://seminarkitjogja.web.id/"
    
    og_img_tag = head.find('meta', attrs={'property': 'og:image'})
    og_image = og_img_tag['content'].strip() if og_img_tag and 'content' in og_img_tag.attrs else "https://seminarkitjogja.web.id/assets/img/hero-bg.webp"
    
    # Extract schema scripts
    schema_scripts = []
    for script in head.find_all('script'):
        if script.get('type') == 'application/ld+json':
            schema_scripts.append(str(script))
    schema_str = "\n".join(schema_scripts)
    
    # Calculate prefix
    is_detail = 'detail' in filepath.replace('\\', '/')
    prefix = '../' if is_detail else ''
    
    # Calculate keywords
    kw = f"{title.replace(' - ', ', ').replace('|', ',').lower()}, seminar kit jogja, souvenir kantor, merchandise perusahaan, corporate gift, seminar kit premium"
    
    # Construct new head
    new_head = f'''<head>
  <meta charset="utf-8">
  <meta content="width=device-width, initial-scale=1.0" name="viewport">
  <meta name="robots" content="index, follow, max-image-preview:large, max-snippet:-1">
  <link rel="canonical" href="{canonical}">

  <!-- SEO Meta Tags -->
  <title>{title}</title>
  <meta name="description" content="{description}">
  <meta name="keywords" content="{kw}">

  <!-- Favicons -->
  <link href="{prefix}assets/img/favicon.ico" rel="icon" type="image/x-icon">
  <link href="{prefix}assets/img/favicon-32x32.png" rel="icon" sizes="32x32" type="image/png">
  <link href="{prefix}assets/img/favicon-16x16.png" rel="icon" sizes="16x16" type="image/png">
  <link href="{prefix}assets/img/apple-touch-icon.png" rel="apple-touch-icon" sizes="180x180">

  <!-- Fonts -->
  <link href="https://fonts.googleapis.com" rel="preconnect">
  <link crossorigin="" href="https://fonts.gstatic.com" rel="preconnect">
  <link href="https://fonts.googleapis.com/css2?family=Poppins:ital,wght@0,300;0,400;0,500;0,600;0,700;0,800;1,400&family=Playfair+Display:wght@400;500;600;700;800&display=swap" rel="stylesheet">

  <!-- Vendor CSS Files -->
  <link href="{prefix}assets/vendor/bootstrap/css/bootstrap.min.css" rel="stylesheet">
  <link href="{prefix}assets/vendor/bootstrap-icons/bootstrap-icons.css" rel="stylesheet">
  <link href="{prefix}assets/vendor/aos/aos.css" rel="stylesheet">
  <link href="{prefix}assets/vendor/glightbox/css/glightbox.min.css" rel="stylesheet">
  <link href="{prefix}assets/vendor/swiper/swiper-bundle.min.css" rel="stylesheet">

  <!-- Main CSS File -->
  <link href="{prefix}assets/css/main.css" rel="stylesheet">

  <!-- Open Graph / Facebook -->
  <meta property="og:type" content="website">
  <meta property="og:url" content="{canonical}">
  <meta property="og:title" content="{title}">
  <meta property="og:description" content="{description}">
  <meta property="og:image" content="{og_image}">
  <meta property="og:locale" content="id_ID">
  <meta property="og:site_name" content="Seminar Kit Jogja">

  <!-- Twitter -->
  <meta name="twitter:card" content="summary_large_image">
  <meta name="twitter:url" content="{canonical}">
  <meta name="twitter:title" content="{title}">
  <meta name="twitter:description" content="{description}">
  <meta name="twitter:image" content="{og_image}">
  
  {schema_str}
</head>'''

    # Replace old head with new head
    content = re.sub(r'<head>.*?</head>', new_head, content, flags=re.DOTALL)
    
    with open(filepath, 'w', encoding='utf-8') as f:
        f.write(content)
        
print("Successfully formatted SEO tags for all HTML files.")
