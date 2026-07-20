import os
import re

count_src = 0
count_url = 0

for root, dirs, files in os.walk('src'):
    for f in files:
        if f.endswith('.astro') or f.endswith('.css'):
            path = os.path.join(root, f)
            with open(path, 'r', encoding='utf-8') as file:
                content = file.read()

            # 1. Convert src="images/... -> src="/images/...
            new_content = re.sub(r'src="(?:\./)?images/', 'src="/images/', content)
            # 2. Convert src="index Adu_files/... -> src="/index Adu_files/...
            new_content = re.sub(r'src="(?:\./)?index Adu_files/', 'src="/index Adu_files/', new_content)
            # 3. Convert src="./index opacity-05.svg -> src="/index opacity-05.svg
            new_content = re.sub(r'src="(?:\./)?index opacity-05\.svg"', 'src="/index opacity-05.svg"', new_content)
            
            # 4. Convert url("./index Adu_files/...") or url('index Adu_files/...') -> url('/index Adu_files/...')
            new_content = re.sub(r'url\(([\'"]?)(?:\./)?index Adu_files/', r'url(\1/index Adu_files/', new_content)
            new_content = re.sub(r'url\(([\'"]?)(?:\./)?images/', r'url(\1/images/', new_content)

            if new_content != content:
                with open(path, 'w', encoding='utf-8') as file:
                    file.write(new_content)
                print(f"Updated absolute asset paths in: {path}")

print("Path conversion complete!")
