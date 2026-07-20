import re

def main():
    with open('src/pages/index.astro', 'r', encoding='utf-8') as f:
        content = f.read()

    # The exact string to remove:
    str_to_remove = "/* Fixing the Maximize Your Space overlap */\n    #container .css-mshi22, #container .css-mshi22 span { font-size: 32px !important; line-height: 1.2em !important; }"
    
    if str_to_remove in content:
        content = content.replace(str_to_remove, '')
        with open('src/pages/index.astro', 'w', encoding='utf-8') as f:
            f.write(content)
        print('REMOVED THE OFFENDING RULE!')
    else:
        # Try a more forgiving replacement
        pattern = r'\/\* Fixing the Maximize Your Space overlap \*\/[\s\n]*#container \.css-mshi22, #container \.css-mshi22 span \{[^}]*\}'
        new_content = re.sub(pattern, '', content)
        if new_content != content:
            with open('src/pages/index.astro', 'w', encoding='utf-8') as f:
                f.write(new_content)
            print('REMOVED THE OFFENDING RULE VIA REGEX!')
        else:
            print('STILL COULD NOT FIND IT!')

if __name__ == '__main__':
    main()
