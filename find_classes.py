import re

def main():
    with open('src/components/ADUTypes.astro', 'r', encoding='utf-8') as f:
        content = f.read()

    classes = set(re.findall(r'class="([^"]+)"', content))
    all_classes = set()
    for c in classes:
        all_classes.update(c.split(' '))
    
    known = {
        'css-isagh0', 'css-rdcjzi', 'css-1tz7d0', 'css-pka6yd', 'css-dvs7qv', 'css-kaizum', 'css-c3vudm',
        'css-4jygia', 'css-c6gfuu', 'css-jizx1m', 'css-cvw59p', 'css-hry8ah', 'css-mrxjfi', 'css-h91s6s',
        'css-hoha6l', 'css-ne2xjn', 'css-e3yc09', 'css-pkcqtw', 'css-dvut5i', 'css-kazf1u', 'css-c3fu8w',
        'css-5ns3tt', 'css-ooeuwn', 'css-cvyp7t', 'css-dwatej', 'css-mruzhe', 'css-h9hquz',
        
        # Other known structural ones
        'css-pj6ukt', 'css-dqbxpu', 'css-bz2tic', 'css-roiesn', 'css-628mvu', 'css-mshi22', 'css-v511zc',
        'css-a49u1q', 'css-b54yok', 'css-3vgump', 'css-v4058c', 'css-14etce', 'textContents', 'css-hu9wtw',
        'css-lla91', 'css-8zrmd9', 'css-ki8et9', 'css-8zr56v'
    }
    
    unknown = all_classes - known
    
    with open('src/styles/global.css', 'r', encoding='utf-8') as f:
        css = f.read()
        
    for c in unknown:
        if c.startswith('css-'):
            match = re.search(r'#' + c + r'[^}]*top:\s*([0-9]+)px', css)
            if match:
                top = int(match.group(1))
                if 3200 <= top <= 4600:
                    print(f'{c}: top {top}')
            else:
                match = re.search(r'\.' + c + r'\s*\{[^}]*top:\s*([0-9]+)px', css)
                if match:
                    top = int(match.group(1))
                    if 3200 <= top <= 4600:
                        left = re.search(r'left:\s*([0-9]+(?:\.[0-9]+)?)px', css[match.start():match.end()])
                        left_val = left.group(1) if left else 'N/A'
                        print(f'{c}: top {top}, left {left_val}')

if __name__ == '__main__':
    main()
