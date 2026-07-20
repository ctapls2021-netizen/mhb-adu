import os
from bs4 import BeautifulSoup

filepath = r'c:\Users\Diego\Downloads\Agente Ayrton\Agente creador de web\astro_site\src\components\HeaderAndHero.astro'
with open(filepath, 'r', encoding='utf-8') as f:
    html = f.read()

soup = BeautifulSoup(html, 'html.parser')

style_topbar = 'color: #F5F9FA !important; text-align: center !important; font-family: Inter, sans-serif !important; font-size: 18px !important; font-style: normal !important; font-weight: 700 !important; line-height: 37.694px !important;'
style_hero_title = 'color: #FFF !important; font-family: "Playfair Display", serif !important; font-size: 60px !important; font-style: normal !important; font-weight: 700 !important; line-height: 75px !important;'
style_hero_sub = 'color: #F5F9FA !important; font-family: Inter, sans-serif !important; font-size: 26px !important; font-style: normal !important; font-weight: 500 !important; line-height: 34px !important;'
style_icon_title = 'color: #F5F9FA !important; text-align: center !important; font-family: "Playfair Display", serif !important; font-size: 23px !important; font-style: normal !important; font-weight: 700 !important; line-height: 37.694px !important;'
style_icon_text = 'color: #F5F9FA !important; text-align: center !important; font-family: Inter, sans-serif !important; font-size: 18px !important; font-style: normal !important; font-weight: 400 !important; line-height: 17px !important;'

for p in soup.find_all('p'):
    text = p.get_text()
    if 'CA Lic' in text:
        p['style'] = style_topbar
    elif 'Los Angeles ADU Builders' in text:
        p['style'] = style_hero_title
    elif 'From expedited city permits' in text:
        p['style'] = style_hero_sub
    elif 'We Handle All City Permits' in text or 'Fixed-Price Guarantee' in text or '0% Interest' in text:
        p['style'] = style_icon_title
    elif 'No City Hall trips' in text or 'Your written quote' in text or 'Build now, pay over time' in text:
        p['style'] = style_icon_text

# Write back
content = "---\n---\n" + "".join([str(c) for c in soup.children])
with open(filepath, 'w', encoding='utf-8') as f:
    f.write(content)
