import os
import re

count = 0
for root, dirs, files in os.walk('src'):
    for f in files:
        if f.endswith('.astro'):
            path = os.path.join(root, f)
            with open(path, 'r', encoding='utf-8') as file:
                content = file.read()

            # Replace "images/... or 'images/... or "./images/... with "/images/...
            new_content = re.sub(r'([\'"])(?:\./)?(images|index Adu_files)/', r'\1/\2/', content)

            if new_content != content:
                with open(path, 'w', encoding='utf-8') as file:
                    file.write(new_content)
                print(f"Fixed relative JS image paths in: {path}")
                count += 1

print(f"Fixed {count} files!")
