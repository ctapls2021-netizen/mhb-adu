
import re

def main():
    with open('src/pages/index.astro', 'r', encoding='utf-8') as f:
        content = f.read()

    start_idx = content.find('@media (max-width: 1023px)')
    end_style = content.find('</style>', start_idx)
    mobile_css = content[start_idx:end_style]

    js_array_code = '''[
        ['css-dvs7qv', 'css-pka6yd', 'css-isagh0', 'css-rdcjzi', 'css-1tz7d0', 'css-sqgevl', 'css-kaizum', 'css-c3vudm'],
        ['css-hry8ah', 'css-cvw59p', 'css-c6gfuu', 'css-lhwfyv', 'css-mrxjfi', 'css-4jygia', 'css-jizx1m', 'css-h91s6s'],
        ['css-dvut5i', 'css-pkcqtw', 'css-2lywx', 'css-gjp8cy', 'css-kazf1u', 'css-hoha6l', 'css-e3yc09', 'css-c3fu8w'],
        ['css-hrvocd', 'css-cvyp7t', 'css-e2mxfm', 'css-ne2xjn', 'css-mruzhe', 'css-5ns3tt', 'css-ooeuwn', 'css-h9hquz'],
    ]'''
    content = re.sub(
        r'const cards = \[[^\]]+\];',
        f'const cards = {js_array_code};',
        content,
        flags=re.DOTALL
    )

    start_unified = content.find('/* Unified Card Element Styles inside .adu-slide */')
    end_unified = content.find('</style>', start_unified)
    
    new_css = '''
    /* Unified Card Element Styles inside .adu-slide */
    #container .adu-slide * { transform: none !important; margin: 0 !important; }
    
    /* 1. Image */
    #container .adu-slide .css-isagh0, #container .adu-slide .css-4jygia, #container .adu-slide .css-hoha6l, #container .adu-slide .css-5ns3tt {
        width: 240px !important; height: 240px !important; left: 120px !important; top: 20px !important; position: absolute !important;
    }
    
    /* 2. Title */
    #container .adu-slide .css-rdcjzi, #container .adu-slide .css-c6gfuu, #container .adu-slide .css-ne2xjn, #container .adu-slide .css-ooeuwn {
        width: 440px !important; left: 20px !important; top: 260px !important; text-align: center !important; font-size: 24px !important; position: absolute !important; height: auto !important;
    }
    
    /* 3. Subtitle (only cards 1, 2, 3 have it usually) */
    #container .adu-slide .css-1tz7d0, #container .adu-slide .css-jizx1m, #container .adu-slide .css-e3yc09 {
        width: 360px !important; left: 60px !important; top: 310px !important; text-align: center !important; position: absolute !important; height: auto !important;
    }
    
    /* 4. Description */
    #container .adu-slide .css-pka6yd, #container .adu-slide .css-cvw59p, #container .adu-slide .css-pkcqtw, #container .adu-slide .css-cvyp7t {
        width: 360px !important; left: 60px !important; top: 370px !important; text-align: center !important; font-size: 14px !important; position: absolute !important; height: auto !important;
    }
    
    /* 5. Blue Box */
    #container .adu-slide .css-dvs7qv, #container .adu-slide .css-hry8ah, #container .adu-slide .css-dvut5i, #container .adu-slide .css-hrvocd {
        width: 380px !important; height: 100px !important; left: 50px !important; top: 480px !important; position: absolute !important;
    }
    
    /* 6. Best For: text */
    #container .adu-slide .css-kaizum, #container .adu-slide .css-mrxjfi, #container .adu-slide .css-kazf1u, #container .adu-slide .css-mruzhe {
        width: auto !important; left: 70px !important; top: 500px !important; font-size: 20px !important; position: absolute !important; z-index: 100 !important; color: white !important; font-weight: bold !important; font-style: italic !important;
    }
    
    /* 7. SVG Arrow */
    #container .adu-slide .css-c3vudm, #container .adu-slide .css-h91s6s, #container .adu-slide .css-c3fu8w, #container .adu-slide .css-odriau {
        left: 70px !important; top: 540px !important; width: 40px !important; height: auto !important; position: absolute !important; z-index: 100 !important;
    }
    
    /* 8. Text on right of button */
    #container .adu-slide .css-sqgevl, #container .adu-slide .css-lhwfyv, #container .adu-slide .css-zf3ss0, #container .adu-slide .css-ne2xjn, #container .adu-slide .css-cwerfg, #container .adu-slide .css-oe7gz1 {
        width: 220px !important; left: 200px !important; top: 500px !important; font-size: 14px !important; position: absolute !important; z-index: 100 !important; color: white !important; text-align: left !important; line-height: 1.2 !important; height: auto !important;
    }
'''
    content = content[:start_unified] + new_css + content[end_unified:]

    with open('src/pages/index.astro', 'w', encoding='utf-8') as f:
        f.write(content)
        
    print('Styles updated!')

if __name__ == '__main__':
    main()
