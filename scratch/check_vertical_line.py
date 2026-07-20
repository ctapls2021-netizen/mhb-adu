import os
import re

print("CTA candidates in desktop components:")
for root, dirs, files in os.walk('src/components'):
    if 'mobile' in root:
        continue
    for f in files:
        if f.endswith('.astro') and f != 'HeaderAndHero.astro':
            path = os.path.join(root, f)
            with open(path, 'r', encoding='utf-8') as file:
                content = file.read()
                # Find buttons, inputs of type button, or divs/spans with click handlers/cursor pointer
                matches = re.finditer(r'<[a-zA-Z]+[^>]*estimate[^>]*>', content, re.IGNORECASE)
                for m in matches:
                    print(f"{f}: {m.group(0)}")
                
                # Check for any button tags
                matches_btn = re.finditer(r'<button[^>]*>.*?</button>', content, re.DOTALL | re.IGNORECASE)
                for m in matches_btn:
                    print(f"{f} (button): {m.group(0).strip()}")
