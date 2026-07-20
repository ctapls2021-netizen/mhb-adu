import re

filepath = r'c:\Users\Diego\Downloads\Agente Ayrton\Agente creador de web\astro_site\src\styles\global.css'
with open(filepath, 'r', encoding='utf-8') as f:
    css = f.read()

# These classes have bad positioning (overflow would clip them wrong or show them twice)
# Replace their positioning to be proper cover within their container
bad_classes = {
    'css-qw3zwa': '.css-qw3zwa {width: 301.02%; height: 200.68%; top: 1.3%; left: 1.62%; max-width: none;}',
    'css-z3as1s': '.css-z3as1s {width: 301.02%; height: 200.68%; top: 1.3%; left: -97.73%; max-width: none;}',
    'css-9edryz': '.css-9edryz {width: 74.27%; height: 86.3%; top: 9.11%; left: 13.02%; max-width: none;}',
    'css-y9pif0': '.css-y9pif0 {width: 85.24%; height: 82.43%; top: 8.91%; left: 5.48%; max-width: none;}',
    'css-baon7m': '.css-baon7m {width: 306.34%; height: 204.23%; top: -98.83%; left: -1.32%; max-width: none;}',
    'css-j8fkso': '.css-j8fkso {width: 301.02%; height: 200.68%; top: -97.79%; left: -96.66%; max-width: none;}',
}

good_rule = 'width: 100% !important; height: 100% !important; top: 0 !important; left: 0 !important; max-width: none; position: relative !important;'

for cls, old_rule in bad_classes.items():
    new_rule = f'.{cls} {{{good_rule}}}'
    css = css.replace(old_rule, new_rule)

with open(filepath, 'w', encoding='utf-8') as f:
    f.write(css)

print("Done - fixed bad CSS positioning")
