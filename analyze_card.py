import re

def main():
    with open('src/styles/global.css', 'r', encoding='utf-8') as f:
        css = f.read()

    classes = set()
    for m in re.finditer(r'(?:#container \.|\.)(css-[a-z0-9]+)\s*\{([^}]+)\}', css):
        cls = m.group(1)
        rules = m.group(2)
        top_m = re.search(r'top:\s*([0-9]+)px', rules)
        if top_m:
            top = int(top_m.group(1))
            if 3200 <= top <= 4600:
                left_m = re.search(r'left:\s*([0-9]+(?:\.[0-9]+)?)px', rules)
                left = float(left_m.group(1)) if left_m else 0
                width_m = re.search(r'width:\s*([0-9]+(?:\.[0-9]+)?)px', rules)
                width = float(width_m.group(1)) if width_m else 0
                height_m = re.search(r'height:\s*([0-9]+(?:\.[0-9]+)?)px', rules)
                height = float(height_m.group(1)) if height_m else 0
                
                # Card 1 is top < 3700 and left < 700
                if top < 3700 and left < 700:
                    # Ignore the white background which is width 1920
                    if width > 1000: continue
                    print(f'{cls}: top {top}, left {left}, width {width}, height {height}')

if __name__ == '__main__':
    main()
