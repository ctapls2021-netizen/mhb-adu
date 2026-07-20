import re

def main():
    with open('src/pages/index.astro', 'r', encoding='utf-8') as f:
        content = f.read()

    start_idx = content.find('@media (max-width: 1023px)')
    end_style = content.find('</style>', start_idx)
    mobile_css = content[start_idx:end_style]

    # Classes to modify
    classes_to_remove = [
        'css-dpvz6t', 'css-628mvu', 'css-mshi22', 'css-v511zc', 'css-a49u1q', 'css-b54yok', 'css-3vgump', 'css-pj6ukt',
        'css-isagh0', 'css-rdcjzi', 'css-1tz7d0', 'css-pka6yd', 'css-dvs7qv', 'css-kaizum', 'css-c3vudm',
        'css-4jygia', 'css-c6gfuu', 'css-jizx1m', 'css-cvw59p', 'css-hry8ah', 'css-mrxjfi', 'css-h91s6s',
        'css-hoha6l', 'css-ne2xjn', 'css-e3yc09', 'css-pkcqtw', 'css-dvut5i', 'css-kazf1u', 'css-c3fu8w',
        'css-5ns3tt', 'css-ooeuwn', 'css-cvyp7t', 'css-dwatej', 'css-mruzhe', 'css-h9hquz'
    ]

    for cls in classes_to_remove:
        pattern = r'#container \.' + cls + r'\s*{[^}]*}'
        mobile_css = re.sub(pattern, '', mobile_css)

    # Blue Background starts at 2360px
    top_blue = 2360
    # Top padding = 80px
    top_title = top_blue + 80  # 2440px
    # Gap between title and paragraph = 24px
    # Title height = ~86px
    top_paragraph = top_title + 86 + 24 # 2550px
    # Paragraph height = ~100px
    bottom_paragraph = top_paragraph + 100 # 2650px
    # Bottom padding = 80px
    bottom_blue = bottom_paragraph + 80 # 2730px
    height_blue = bottom_blue - top_blue # 370px

    # White background starts at bottom_blue
    top_white = bottom_blue # 2730px

    new_rules = ""
    def add_rule(cls, rule_str):
        nonlocal new_rules
        new_rules += f"    #container .{cls} {{ {rule_str} }}\n"

    # Blue Background and text
    add_rule('css-dpvz6t', f'left: 0px !important; top: calc(50vh + {top_blue}px) !important; position: absolute !important;')
    add_rule('css-628mvu', f'width: 480px !important; height: {height_blue}px !important; left: 0px !important; top: calc(50vh + {top_blue}px) !important; position: absolute !important; display: block !important;')
    
    add_rule('css-mshi22', f'left: 20px !important; top: calc(50vh + {top_title}px) !important; width: 440px !important; text-align: center !important; font-size: 24px !important; line-height: 1.2em !important;')
    add_rule('css-a49u1q', 'font-size: 24px !important; line-height: 1.2em !important;')
    add_rule('css-b54yok', 'font-size: 24px !important; line-height: 1.2em !important;')
    
    add_rule('css-v511zc', f'left: 20px !important; top: calc(50vh + {top_paragraph}px) !important; width: 440px !important; text-align: center !important; position: absolute !important;')
    add_rule('css-3vgump', 'font-size: 14px !important; line-height: 1.4em !important;')

    # White Background (Cards Container)
    add_rule('css-pj6ukt', f'width: 480px !important; height: 1800px !important; left: 0px !important; top: calc(50vh + {top_white}px) !important; position: absolute !important; display: block !important;')

    # Helper function for cards
    # Each card takes ~450px height
    def layout_card(start_y, image_cls, title_cls, sub_cls, desc_cls, btn_box, btn_t1, btn_t2):
        # 40px padding top for each card
        y = start_y + 40
        add_rule(image_cls, f'width: 160px !important; height: 160px !important; left: 160px !important; top: calc(50vh + {y}px) !important; position: absolute !important;')
        y += 180
        add_rule(title_cls, f'width: 440px !important; left: 20px !important; top: calc(50vh + {y}px) !important; text-align: center !important; font-size: 24px !important;')
        y += 40
        if sub_cls:
            add_rule(sub_cls, f'width: 440px !important; left: 20px !important; top: calc(50vh + {y}px) !important; text-align: center !important;')
            y += 40
        add_rule(desc_cls, f'width: 440px !important; left: 20px !important; top: calc(50vh + {y}px) !important; text-align: center !important; font-size: 14px !important;')
        y += 90
        add_rule(btn_box, f'width: 240px !important; height: 50px !important; left: 120px !important; top: calc(50vh + {y}px) !important;')
        add_rule(btn_t1, f'left: 140px !important; top: calc(50vh + {y+10}px) !important; font-size: 12px !important;')
        add_rule(btn_t2, f'left: 140px !important; top: calc(50vh + {y+25}px) !important; font-size: 14px !important;')
        return y + 60 # End of card + small margin

    y_pos = top_white
    y_pos = layout_card(y_pos, 'css-isagh0', 'css-rdcjzi', 'css-1tz7d0', 'css-pka6yd', 'css-dvs7qv', 'css-kaizum', 'css-c3vudm')
    y_pos = layout_card(y_pos, 'css-4jygia', 'css-c6gfuu', 'css-jizx1m', 'css-cvw59p', 'css-hry8ah', 'css-mrxjfi', 'css-h91s6s')
    y_pos = layout_card(y_pos, 'css-hoha6l', 'css-ne2xjn', 'css-e3yc09', 'css-pkcqtw', 'css-dvut5i', 'css-kazf1u', 'css-c3fu8w')
    y_pos = layout_card(y_pos, 'css-5ns3tt', 'css-ooeuwn', None, 'css-cvyp7t', 'css-dwatej', 'css-mruzhe', 'css-h9hquz')

    # Remove extra blank lines from mobile_css cleanup
    mobile_css = re.sub(r'\n\s*\n', '\n', mobile_css)

    # Put it all together inside the mobile_css string before the closing brace
    if mobile_css.endswith('  }\n'):
        mobile_css = mobile_css[:-4] + '\n' + new_rules + '  }\n'
    elif mobile_css.endswith('  }'):
        mobile_css = mobile_css[:-3] + '\n' + new_rules + '  }\n'
    else:
        mobile_css = mobile_css + '\n' + new_rules + '  }\n'

    content = content[:start_idx] + mobile_css + content[end_style:]

    with open('src/pages/index.astro', 'w', encoding='utf-8') as f:
        f.write(content)
        
    print('Perfect Layout Updated!')

if __name__ == '__main__':
    main()
