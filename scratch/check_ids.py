import re
with open('dist/index.html', 'r', encoding='utf-8') as f:
    c = f.read()
print('lead-form:', len(re.findall(r'id="lead-form"', c)))
print('estimate:', len(re.findall(r'id="estimate"', c)))
