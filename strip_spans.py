import os
from bs4 import BeautifulSoup

filepath = r'c:\Users\Diego\Downloads\Agente Ayrton\Agente creador de web\astro_site\src\components\HeaderAndHero.astro'
with open(filepath, 'r', encoding='utf-8') as f:
    html = f.read()

soup = BeautifulSoup(html, 'html.parser')

for p in soup.find_all('p'):
    text = p.get_text()
    if 'No City Hall trips' in text:
        p.string = 'No City Hall trips. No confusing zoning paperwork.'
    elif 'Your written quote' in text:
        p.string = 'Your written quote is your final price. No hidden fees, no surprise change orders.'
    elif 'Build now, pay over time' in text:
        p.string = 'Build now, pay over time.'
    elif 'We Handle All City Permits' in text:
        p.string = 'We Handle All City Permits & Plans'
    elif 'Fixed-Price Guarantee' in text:
        p.string = 'Fixed-Price Guarantee'
    elif '0% Interest' in text:
        p.string = '0% Interest for 18 Months Available'
    elif 'Los Angeles ADU Builders' in text:
        p.string = 'Los Angeles ADU Builders You Can Actually Trust'
    elif 'From expedited city permits' in text:
        p.string = 'From expedited city permits to flawless construction, we handle 100% of your ADU project so you generate passive income or house family members without the typical contractor headaches.'
    elif 'CA Lic' in text:
        p.string = 'CA Lic. #1002927  |  Licensed, Bonded & Insured  |  100% Financing Available  |  📞 (818) 914-4900'

# Write back
content = "---\n---\n" + "".join([str(c) for c in soup.children])
with open(filepath, 'w', encoding='utf-8') as f:
    f.write(content)
