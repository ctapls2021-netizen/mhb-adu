import re

def main():
    with open('src/pages/index.astro', 'r', encoding='utf-8') as f:
        content = f.read()

    start_idx = content.find('@media (max-width: 1023px)')
    end_style = content.find('</style>', start_idx)
    mobile_css = content[start_idx:end_style]

    # Clean up old rules if they exist
    for cls in ['css-hu9wtw', 'css-14etce']:
        pattern = r'#container \.' + cls + r'\s*{[^}]*}'
        mobile_css = re.sub(pattern, '', mobile_css)

    new_rules = ""
    new_rules += "    #container .css-hu9wtw { font-size: 24px !important; line-height: 1.2em !important; }\n"
    new_rules += "    #container .css-14etce { font-size: 24px !important; line-height: 1.2em !important; }\n"

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
        
    print('Line heights fixed!')

if __name__ == '__main__':
    main()
