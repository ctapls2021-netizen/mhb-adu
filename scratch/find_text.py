with open('src/components/Process.astro', 'r', encoding='utf-8') as f:
    content = f.read()

import re
for match in re.finditer(r'<[^>]*class=[^>]*textContents[^>]*>(.*?)</[^>]*>', content):
    print(match.group(0))
