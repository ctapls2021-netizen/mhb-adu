from bs4 import BeautifulSoup
import sys

filepath = r'c:\Users\Diego\Downloads\Agente Ayrton\Agente creador de web\astro_site\src\components\WhyChooseUs.astro'
with open(filepath, 'r', encoding='utf-8') as f:
    html = f.read()

soup = BeautifulSoup(html, 'html.parser')
for img in soup.find_all('img'):
    print('SRC:', img.get('src'), 'CLASS:', img.get('class'))
