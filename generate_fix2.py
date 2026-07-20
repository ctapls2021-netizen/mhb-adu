import re

def main():
    with open('src/styles/global.css', 'r', encoding='utf-8') as f:
        css = f.read()

    cards = [[] for _ in range(4)]
    
    blocks = css.split('}')
    for block in blocks:
        if '{' not in block: continue
        selectors_str, rules = block.split('{', 1)
        
        top_m = re.search(r'top:\s*([0-9]+(?:\.[0-9]+)?)px', rules)
        if top_m:
            top = float(top_m.group(1))
            if 3200 <= top <= 4100:
                left_m = re.search(r'left:\s*([0-9]+(?:\.[0-9]+)?)px', rules)
                left = float(left_m.group(1)) if left_m else 0
                width_m = re.search(r'width:\s*([0-9]+(?:\.[0-9]+)?)px', rules)
                width = float(width_m.group(1)) if width_m else 0
                height_m = re.search(r'height:\s*([0-9]+(?:\.[0-9]+)?)px', rules)
                height = float(height_m.group(1)) if height_m else 0
                
                if width > 1000 or height == 0: continue
                
                card_idx = -1
                if top < 3700:
                    if left < 900: card_idx = 0
                    else: card_idx = 1
                else:
                    if left < 900: card_idx = 2
                    else: card_idx = 3
                    
                if card_idx != -1:
                    classes = re.findall(r'\.(css-[a-z0-9]+)', selectors_str)
                    for cls in classes:
                        if cls not in cards[card_idx]:
                            cards[card_idx].append(cls)

    print("Card classes perfectly mapped:")
    for i, c in enumerate(cards):
        print(f"Card {i+1}: {c}")

    js_array = "[\n"
    for c in cards:
        js_array += "        [" + ", ".join([f"'{cls}'" for cls in c]) + "],\n"
    js_array += "    ]"
    
    fix_slider_code = f"""
import re

def main():
    with open('src/pages/index.astro', 'r', encoding='utf-8') as f:
        content = f.read()

    start_idx = content.find('@media (max-width: 1023px)')
    end_style = content.find('</style>', start_idx)
    mobile_css = content[start_idx:end_style]

    js_array_code = '''{js_array}'''
    content = re.sub(
        r'const cards = \\[[^\\]]+\\];',
        f'const cards = {{js_array_code}};',
        content,
        flags=re.DOTALL
    )

    start_unified = content.find('/* Unified Card Element Styles inside .adu-slide */')
    end_unified = content.find('</style>', start_unified)
    
    new_css = '''
    /* Unified Card Element Styles inside .adu-slide */
    #container .adu-slide * {{ transform: none !important; margin: 0 !important; }}
    
    /* 1. Image */
    #container .adu-slide .css-isagh0, #container .adu-slide .css-4jygia, #container .adu-slide .css-hoha6l, #container .adu-slide .css-5ns3tt {{
        width: 240px !important; height: 240px !important; left: 120px !important; top: 20px !important; position: absolute !important;
    }}
    
    /* 2. Title */
    #container .adu-slide .css-rdcjzi, #container .adu-slide .css-c6gfuu, #container .adu-slide .css-ne2xjn, #container .adu-slide .css-ooeuwn {{
        width: 440px !important; left: 20px !important; top: 260px !important; text-align: center !important; font-size: 24px !important; position: absolute !important; height: auto !important;
    }}
    
    /* 3. Subtitle (only cards 1, 2, 3 have it usually) */
    #container .adu-slide .css-1tz7d0, #container .adu-slide .css-jizx1m, #container .adu-slide .css-e3yc09 {{
        width: 360px !important; left: 60px !important; top: 310px !important; text-align: center !important; position: absolute !important; height: auto !important;
    }}
    
    /* 4. Description */
    #container .adu-slide .css-pka6yd, #container .adu-slide .css-cvw59p, #container .adu-slide .css-pkcqtw, #container .adu-slide .css-cvyp7t {{
        width: 360px !important; left: 60px !important; top: 370px !important; text-align: center !important; font-size: 14px !important; position: absolute !important; height: auto !important;
    }}
    
    /* 5. Blue Box */
    #container .adu-slide .css-dvs7qv, #container .adu-slide .css-hry8ah, #container .adu-slide .css-dvut5i, #container .adu-slide .css-hrvocd {{
        width: 380px !important; height: 100px !important; left: 50px !important; top: 480px !important; position: absolute !important;
    }}
    
    /* 6. Best For: text */
    #container .adu-slide .css-kaizum, #container .adu-slide .css-mrxjfi, #container .adu-slide .css-kazf1u, #container .adu-slide .css-mruzhe {{
        width: auto !important; left: 70px !important; top: 500px !important; font-size: 20px !important; position: absolute !important; z-index: 100 !important; color: white !important; font-weight: bold !important; font-style: italic !important;
    }}
    
    /* 7. SVG Arrow */
    #container .adu-slide .css-c3vudm, #container .adu-slide .css-h91s6s, #container .adu-slide .css-c3fu8w, #container .adu-slide .css-odriau {{
        left: 70px !important; top: 540px !important; width: 40px !important; height: auto !important; position: absolute !important; z-index: 100 !important;
    }}
    
    /* 8. Text on right of button */
    #container .adu-slide .css-sqgevl, #container .adu-slide .css-lhwfyv, #container .adu-slide .css-zf3ss0, #container .adu-slide .css-ne2xjn, #container .adu-slide .css-cwerfg, #container .adu-slide .css-oe7gz1 {{
        width: 220px !important; left: 200px !important; top: 500px !important; font-size: 14px !important; position: absolute !important; z-index: 100 !important; color: white !important; text-align: left !important; line-height: 1.2 !important; height: auto !important;
    }}
'''
    content = content[:start_unified] + new_css + content[end_unified:]

    with open('src/pages/index.astro', 'w', encoding='utf-8') as f:
        f.write(content)
        
    print('Styles updated!')

if __name__ == '__main__':
    main()
"""
    
    with open('fix_slider_styling.py', 'w', encoding='utf-8') as f:
        f.write(fix_slider_code)

if __name__ == '__main__':
    main()
