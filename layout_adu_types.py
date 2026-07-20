import re

def main():
    with open('src/pages/index.astro', 'r', encoding='utf-8') as f:
        content = f.read()

    start_idx = content.find('@media (max-width: 1023px)')
    end_style = content.find('</style>', start_idx)
    mobile_css = content[start_idx:end_style]

    # Classes to modify
    classes_to_remove = [
        'css-pj6ukt',
        'css-isagh0', 'css-rdcjzi', 'css-1tz7d0', 'css-pka6yd', 'css-dvs7qv', 'css-kaizum', 'css-c3vudm',
        'css-4jygia', 'css-c6gfuu', 'css-jizx1m', 'css-cvw59p', 'css-hry8ah', 'css-mrxjfi', 'css-h91s6s',
        'css-hoha6l', 'css-ne2xjn', 'css-e3yc09', 'css-pkcqtw', 'css-dvut5i', 'css-kazf1u', 'css-c3fu8w',
        'css-5ns3tt', 'css-ooeuwn', 'css-cvyp7t', 'css-dwatej', 'css-mruzhe', 'css-h9hquz'
    ]

    for cls in classes_to_remove:
        pattern = r'#container \.' + cls + r'\s*{[^}]*}'
        mobile_css = re.sub(pattern, '', mobile_css)

    # Now we build the new rules
    new_rules = ""
    def add_rule(cls, rule_str):
        nonlocal new_rules
        new_rules += f"    #container .{cls} {{ {rule_str} }}\n"
        
    add_rule('css-pj6ukt', 'width: 480px !important; height: 1800px !important; left: 0px !important; top: calc(50vh + 2820px) !important; position: absolute !important; display: block !important;')

    # Card 1
    add_rule('css-isagh0', 'width: 160px !important; height: 160px !important; left: 160px !important; top: calc(50vh + 2860px) !important; position: absolute !important;')
    add_rule('css-rdcjzi', 'width: 440px !important; left: 20px !important; top: calc(50vh + 3040px) !important; text-align: center !important; font-size: 24px !important;')
    add_rule('css-1tz7d0', 'width: 440px !important; left: 20px !important; top: calc(50vh + 3080px) !important; text-align: center !important;')
    add_rule('css-pka6yd', 'width: 440px !important; left: 20px !important; top: calc(50vh + 3130px) !important; text-align: center !important; font-size: 14px !important;')
    add_rule('css-dvs7qv', 'width: 240px !important; height: 50px !important; left: 120px !important; top: calc(50vh + 3220px) !important;')
    add_rule('css-kaizum', 'left: 140px !important; top: calc(50vh + 3230px) !important; font-size: 12px !important;')
    add_rule('css-c3vudm', 'left: 140px !important; top: calc(50vh + 3245px) !important; font-size: 14px !important;')

    # Card 2
    add_rule('css-4jygia', 'width: 160px !important; height: 160px !important; left: 160px !important; top: calc(50vh + 3300px) !important; position: absolute !important;')
    add_rule('css-c6gfuu', 'width: 440px !important; left: 20px !important; top: calc(50vh + 3480px) !important; text-align: center !important; font-size: 24px !important;')
    add_rule('css-jizx1m', 'width: 440px !important; left: 20px !important; top: calc(50vh + 3520px) !important; text-align: center !important;')
    add_rule('css-cvw59p', 'width: 440px !important; left: 20px !important; top: calc(50vh + 3570px) !important; text-align: center !important; font-size: 14px !important;')
    add_rule('css-hry8ah', 'width: 240px !important; height: 50px !important; left: 120px !important; top: calc(50vh + 3660px) !important;')
    add_rule('css-mrxjfi', 'left: 140px !important; top: calc(50vh + 3670px) !important; font-size: 12px !important;')
    add_rule('css-h91s6s', 'left: 140px !important; top: calc(50vh + 3685px) !important; font-size: 14px !important;')

    # Card 3
    add_rule('css-hoha6l', 'width: 160px !important; height: 160px !important; left: 160px !important; top: calc(50vh + 3740px) !important; position: absolute !important;')
    add_rule('css-ne2xjn', 'width: 440px !important; left: 20px !important; top: calc(50vh + 3920px) !important; text-align: center !important; font-size: 24px !important;')
    add_rule('css-e3yc09', 'width: 440px !important; left: 20px !important; top: calc(50vh + 3960px) !important; text-align: center !important;')
    add_rule('css-pkcqtw', 'width: 440px !important; left: 20px !important; top: calc(50vh + 4010px) !important; text-align: center !important; font-size: 14px !important;')
    add_rule('css-dvut5i', 'width: 240px !important; height: 50px !important; left: 120px !important; top: calc(50vh + 4100px) !important;')
    add_rule('css-kazf1u', 'left: 140px !important; top: calc(50vh + 4110px) !important; font-size: 12px !important;')
    add_rule('css-c3fu8w', 'left: 140px !important; top: calc(50vh + 4125px) !important; font-size: 14px !important;')

    # Card 4
    add_rule('css-5ns3tt', 'width: 160px !important; height: 160px !important; left: 160px !important; top: calc(50vh + 4180px) !important; position: absolute !important;')
    add_rule('css-ooeuwn', 'width: 440px !important; left: 20px !important; top: calc(50vh + 4360px) !important; text-align: center !important; font-size: 24px !important;')
    add_rule('css-cvyp7t', 'width: 440px !important; left: 20px !important; top: calc(50vh + 4400px) !important; text-align: center !important; font-size: 14px !important;')
    add_rule('css-dwatej', 'width: 240px !important; height: 50px !important; left: 120px !important; top: calc(50vh + 4490px) !important;')
    add_rule('css-mruzhe', 'left: 140px !important; top: calc(50vh + 4500px) !important; font-size: 12px !important;')
    add_rule('css-h9hquz', 'left: 140px !important; top: calc(50vh + 4515px) !important; font-size: 14px !important;')

    # Put it all together inside the mobile_css string before the closing brace
    # Assuming mobile_css ends with `  }`
    if mobile_css.endswith('  }\n'):
        mobile_css = mobile_css[:-4] + '\n' + new_rules + '  }\n'
    else:
        mobile_css = mobile_css.replace('  }\n', '\n' + new_rules + '  }\n')

    content = content[:start_idx] + mobile_css + content[end_style:]

    with open('src/pages/index.astro', 'w', encoding='utf-8') as f:
        f.write(content)
        
    print('ADU Types Layout Updated!')

if __name__ == '__main__':
    main()
