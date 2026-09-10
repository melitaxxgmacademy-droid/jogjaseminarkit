from PIL import Image
import os

images = [
    (r'C:\Users\Dell\.gemini\antigravity-ide\brain\6cab9b98-2fa9-45cb-8e00-49ce5c59a6b0\seminar_kit_basic_product_1788179746338.jpg', r'c:\seminarkitjogja.web.id\seminarkitjogja\assets\img\produk\seminar-kit-basic-product.webp'),
    (r'C:\Users\Dell\.gemini\antigravity-ide\brain\6cab9b98-2fa9-45cb-8e00-49ce5c59a6b0\seminar_kit_standard_product_1788179772145.jpg', r'c:\seminarkitjogja.web.id\seminarkitjogja\assets\img\produk\seminar-kit-standard-product.webp'),
    (r'C:\Users\Dell\.gemini\antigravity-ide\brain\6cab9b98-2fa9-45cb-8e00-49ce5c59a6b0\seminar_kit_premium_product_1788179798107.jpg', r'c:\seminarkitjogja.web.id\seminarkitjogja\assets\img\produk\seminar-kit-premium-product.webp')
]

for src, dest in images:
    try:
        img = Image.open(src)
        # resize down if it's 1024x1024 to something like 600x600 to ensure < 100kb easily
        img = img.resize((600, 600), Image.Resampling.LANCZOS)
        img.save(dest, 'WEBP', quality=75)
        size = os.path.getsize(dest)
        print(f"Saved {os.path.basename(dest)} - {size/1024:.1f} KB")
    except Exception as e:
        print(f"Failed to process {src}: {e}")

