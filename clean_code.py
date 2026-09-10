import os
import glob
import re

css_path = 'c:\\seminarkitjogja.web.id\\seminarkitjogja\\assets\\css\\main.css'
with open(css_path, 'r', encoding='utf-8') as f:
    css_content = f.read()

cta_css = '''
/* WhatsApp CTA Button */
.btn-whatsapp-cta {
  width: fit-content;
  min-width: 320px;
  margin: 0 auto;
  display: flex;
  align-items: center;
  justify-content: center;
  padding: 12px 30px;
  font-size: 1.1rem;
  border-radius: 50px;
}

@media (max-width: 768px) {
  .btn-whatsapp-cta {
    width: 100% !important;
    min-width: unset;
  }
}
'''

if 'btn-whatsapp-cta' not in css_content:
    # Insert after btn-whatsapp:hover
    css_content = css_content.replace('.btn-whatsapp:hover {\n  background-color: transparent;\n  color: #25D366 !important;\n}', '.btn-whatsapp:hover {\n  background-color: transparent;\n  color: #25D366 !important;\n}\n' + cta_css)
    with open(css_path, 'w', encoding='utf-8') as f:
        f.write(css_content)
    print("Updated main.css")


detail_dir = 'c:\\seminarkitjogja.web.id\\seminarkitjogja\\detail'
html_files = glob.glob(os.path.join(detail_dir, '*.html'))

old_string = 'class="btn btn-whatsapp btn-lg shadow-sm" style="width: fit-content; min-width: 320px; margin: 0 auto; display: flex; align-items: center; justify-content: center; padding: 12px 30px; font-size: 1.1rem; border-radius: 50px;"'
new_string = 'class="btn btn-whatsapp btn-whatsapp-cta shadow-sm"'

# Handle any minor whitespace variations
pattern = r'class="btn btn-whatsapp btn-lg shadow-sm" style="[^"]*width: fit-content; min-width: 320px[^"]*"'

for filepath in html_files:
    with open(filepath, 'r', encoding='utf-8') as f:
        content = f.read()

    original_content = content
    content = content.replace(old_string, new_string)
    content = re.sub(pattern, new_string, content)

    if content != original_content:
        with open(filepath, 'w', encoding='utf-8') as f:
            f.write(content)
        print(f"Cleaned {os.path.basename(filepath)}")

