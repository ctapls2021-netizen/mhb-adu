import re
import os

filepath = r'c:\Users\Diego\Downloads\Agente Ayrton\Agente creador de web\astro_site\src\components\HeaderAndHero.astro'
with open(filepath, 'r', encoding='utf-8') as f:
    html = f.read()

# 1. Top Bar text
style_topbar = 'style="color: #F5F9FA; text-align: center; font-family: Inter, sans-serif; font-size: 18px; font-style: normal; font-weight: 700; line-height: 37.694px;"'
html = re.sub(r'(<p[^>]*)(>.*?CA Lic\..*?</p>)', r'\1 ' + style_topbar + r'\2', html, flags=re.DOTALL)

# 2. Main Title
style_title = 'style="color: #FFF; font-family: \'Playfair Display\', serif; font-size: 60px; font-style: normal; font-weight: 700; line-height: 75px;"'
html = re.sub(r'(<p[^>]*)(>.*?Los Angeles ADU Builders.*?You Can Actually Trust.*?</p>)', r'\1 ' + style_title + r'\2', html, flags=re.DOTALL)

# 3. Subtitle
style_subtitle = 'style="color: #F5F9FA; font-family: Inter, sans-serif; font-size: 26px; font-style: normal; font-weight: 500; line-height: 34px;"'
html = re.sub(r'(<p[^>]*)(>.*?From expedited city permits.*?contractor headaches\..*?</p>)', r'\1 ' + style_subtitle + r'\2', html, flags=re.DOTALL)

with open(filepath, 'w', encoding='utf-8') as f:
    f.write(html)
