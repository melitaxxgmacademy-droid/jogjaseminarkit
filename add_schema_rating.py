import os
import glob
import json
import random
import re

base_dir = r'c:\seminarkitjogja.web.id\seminarkitjogja\detail'
html_files = glob.glob(os.path.join(base_dir, '*.html'))

for filepath in html_files:
    with open(filepath, 'r', encoding='utf-8') as f:
        content = f.read()

    # Find the JSON LD script block
    match = re.search(r'<script type="application/ld\+json">(.*?)</script>', content, re.DOTALL)
    if not match:
        continue
        
    json_str = match.group(1)
    
    try:
        data = json.loads(json_str)
        changed = False
        
        if '@graph' in data:
            for item in data['@graph']:
                if item.get('@type') == 'Product':
                    if 'aggregateRating' not in item:
                        rating = str(round(random.uniform(4.8, 5.0), 1))
                        if rating == '5.0': rating = '5'
                        count = str(random.randint(80, 250))
                        
                        item['aggregateRating'] = {
                            "@type": "AggregateRating",
                            "ratingValue": rating,
                            "reviewCount": count
                        }
                        changed = True
        
        if changed:
            new_json_str = json.dumps(data, indent=2)
            # Replace the old script block with the new one
            new_script = f'<script type="application/ld+json">\n{new_json_str}\n</script>'
            content = content[:match.start()] + new_script + content[match.end():]
            
            with open(filepath, 'w', encoding='utf-8') as f:
                f.write(content)
            print(f"Added aggregate rating to {os.path.basename(filepath)}")
            
    except Exception as e:
        print(f"Error parsing JSON in {filepath}: {e}")

print("Completed adding aggregate ratings.")
