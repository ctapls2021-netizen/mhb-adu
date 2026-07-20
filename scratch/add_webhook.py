import os

webhook_attr = ' action="https://hooks.zapier.com/hooks/catch/14076185/44dmeuv/" method="POST" '

# 1. Update HeaderAndHero.astro
hh_path = 'src/components/HeaderAndHero.astro'
if os.path.exists(hh_path):
    with open(hh_path, 'r', encoding='utf-8') as f:
        c = f.read()
    c = c.replace('<form id="estimate" ', f'<form id="estimate"{webhook_attr}')
    with open(hh_path, 'w', encoding='utf-8') as f:
        f.write(c)
    print("Updated HeaderAndHero.astro")

# 2. Update MobileHeroForm.astro
mh_path = 'src/components/mobile/MobileHeroForm.astro'
if os.path.exists(mh_path):
    with open(mh_path, 'r', encoding='utf-8') as f:
        c = f.read()
    c = c.replace('<form id="lead-form" ', f'<form id="lead-form"{webhook_attr}')
    with open(mh_path, 'w', encoding='utf-8') as f:
        f.write(c)
    print("Updated MobileHeroForm.astro")
