import re
import os

filepath = r'c:\Users\Diego\Downloads\Agente Ayrton\Agente creador de web\astro_site\src\components\HeaderAndHero.astro'
with open(filepath, 'r', encoding='utf-8') as f:
    html = f.read()

style_title = 'style="color: #F5F9FA; text-align: center; font-family: \'Playfair Display\', serif; font-size: 23px; font-style: normal; font-weight: 700; line-height: 37.694px;"'
style_text = 'style="color: #F5F9FA; text-align: center; font-family: Inter, sans-serif; font-size: 18px; font-style: normal; font-weight: 400; line-height: 17px;"'

# 1. We Handle All City Permits & Plans
html = re.sub(r'(<p[^>]*)(>.*?We Handle All City Permits.*?(?:&|&amp;) Plans.*?</p>)', r'\1 ' + style_title + r'\2', html, flags=re.DOTALL)
html = re.sub(r'(<p[^>]*)(>.*?No City Hall trips.*?confusing zoning paperwork\..*?</p>)', r'\1 ' + style_text + r'\2', html, flags=re.DOTALL)

# 2. Fixed-Price Guarantee
html = re.sub(r'(<p[^>]*)(>.*?Fixed-Price Guarantee.*?</p>)', r'\1 ' + style_title + r'\2', html, flags=re.DOTALL)
html = re.sub(r'(<p[^>]*)(>.*?Your written quote is your final price.*?surprise change orders\..*?</p>)', r'\1 ' + style_text + r'\2', html, flags=re.DOTALL)

# 3. 0% Interest for 18 Months Available
html = re.sub(r'(<p[^>]*)(>.*?0% Interest for 18 Months Available.*?</p>)', r'\1 ' + style_title + r'\2', html, flags=re.DOTALL)
html = re.sub(r'(<p[^>]*)(>.*?Build now, pay over time\..*?</p>)', r'\1 ' + style_text + r'\2', html, flags=re.DOTALL)

with open(filepath, 'w', encoding='utf-8') as f:
    f.write(html)
