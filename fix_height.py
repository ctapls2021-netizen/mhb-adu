import re

def main():
    with open('src/pages/index.astro', 'r', encoding='utf-8') as f:
        content = f.read()

    start_idx = content.find('@media (max-width: 1023px)')
    end_style = content.find('</style>', start_idx)
    mobile_css = content[start_idx:end_style]

    # Add height: auto !important to css-mshi22
    mobile_css = re.sub(
        r'(#container \.css-mshi22\s*\{[^}]*)(text-align:\s*center\s*!important;)',
        r'\1\2 height: auto !important;',
        mobile_css
    )

    # Add height: auto !important to css-v511zc
    mobile_css = re.sub(
        r'(#container \.css-v511zc\s*\{[^}]*)(text-align:\s*center\s*!important;)',
        r'\1\2 height: auto !important;',
        mobile_css
    )

    # In case the regex above failed because the order of properties is different, let's just append them to the end!
    if 'height: auto !important;' not in mobile_css:
        new_rules = "\n    #container .css-mshi22 { height: auto !important; display: flex !important; align-items: flex-start !important; flex-direction: column !important; justify-content: flex-start !important; }\n    #container .css-v511zc { height: auto !important; }\n"
        if mobile_css.endswith('  }\n'):
            mobile_css = mobile_css[:-4] + '\n' + new_rules + '  }\n'
        elif mobile_css.endswith('  }'):
            mobile_css = mobile_css[:-3] + '\n' + new_rules + '  }\n'
        else:
            mobile_css = mobile_css + '\n' + new_rules + '  }\n'

    content = content[:start_idx] + mobile_css + content[end_style:]

    with open('src/pages/index.astro', 'w', encoding='utf-8') as f:
        f.write(content)
        
    print('Added height: auto to title and paragraph!')

if __name__ == '__main__':
    main()
