import re

filepath = r'c:\Users\Diego\Downloads\Agente Ayrton\Agente creador de web\astro_site\src\styles\global.css'
with open(filepath, 'r', encoding='utf-8') as f:
    css = f.read()

# These 5 icon image classes all have bad positioning - fix them all
bad_classes = {
    'css-eqt5tl': r'.css-eqt5tl {width: 378.36%; height: 296.49%; top: -155.12%; left: -211.54%; max-width: none;}',
    'css-i12894': r'.css-i12894 {width: 378.36%; height: 296.49%; top: -190.76%; left: -54.73%; max-width: none;}',
    'css-1tlhgb': r'.css-1tlhgb {width: 378.36%; height: 296.49%; top: -13.4%; left: -54.73%; max-width: none;}',
    'css-f0o2nb': r'.css-f0o2nb {width: 361.26%; height: 283.1%; top: -14.78%; left: -202.57%; max-width: none;}',
    'css-u7gf77': r'.css-u7gf77 {width: 403.98%; height: 316.57%; top: -113.45%; left: -64.35%; max-width: none;}',
}

good = 'width: 100% !important; height: 100% !important; top: 0 !important; left: 0 !important; max-width: none; position: relative !important;'

for cls, old_rule in bad_classes.items():
    new_rule = f'.{cls} {{{good}}}'
    if old_rule in css:
        css = css.replace(old_rule, new_rule)
        print(f"Fixed: {cls}")
    else:
        print(f"NOT FOUND: {cls}")
        # Try flexible match
        m = re.search(r'\.' + cls + r'\s*\{[^\}]+\}', css)
        if m:
            print(f"  Found with regex: {m.group(0)}")
            css = css.replace(m.group(0), new_rule)
            print(f"  Fixed with regex")

with open(filepath, 'w', encoding='utf-8') as f:
    f.write(css)
