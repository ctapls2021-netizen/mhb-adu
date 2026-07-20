import re

def main():
    with open('src/pages/index.astro', 'r', encoding='utf-8') as f:
        content = f.read()

    start_idx = content.find('@media (max-width: 1023px)')
    end_style = content.find('</style>', start_idx)
    mobile_css = content[start_idx:end_style]

    # 1. Adjust paragraph css-v511zc to 2520px
    mobile_css = re.sub(r'#container \.css-v511zc\s*\{[^}]*\}', 
                        r'#container .css-v511zc { left: 20px !important; top: calc(50vh + 2520px) !important; width: 440px !important; text-align: center !important; position: absolute !important; }', 
                        mobile_css)

    # 2. Adjust blue background css-628mvu height to 340px
    mobile_css = re.sub(r'#container \.css-628mvu\s*\{[^}]*\}', 
                        r'#container .css-628mvu { width: 480px !important; height: 340px !important; left: 0px !important; top: calc(50vh + 2360px) !important; position: absolute !important; display: block !important; }', 
                        mobile_css)

    # 3. Adjust white background css-pj6ukt to 2700px
    mobile_css = re.sub(r'#container \.css-pj6ukt\s*\{[^}]*\}', 
                        r'#container .css-pj6ukt { width: 480px !important; height: 1800px !important; left: 0px !important; top: calc(50vh + 2700px) !important; position: absolute !important; display: block !important; }', 
                        mobile_css)

    # 4. Shift ALL ADU Types cards UP by 60px!
    # They currently start around 2770px and go up to ~4550px.
    def shift_match(match):
        prefix = match.group(1)
        val = int(match.group(2))
        suffix = match.group(3)
        if 2750 < val < 4600:
            return f"{prefix}{val-60}{suffix}"
        return match.group(0)

    mobile_css = re.sub(r'(top:\s*calc\(50vh\s*\+\s*)([0-9]+)(px\))', shift_match, mobile_css)

    content = content[:start_idx] + mobile_css + content[end_style:]

    with open('src/pages/index.astro', 'w', encoding='utf-8') as f:
        f.write(content)
        
    print('Adjusted paragraph padding and shifted layout up!')

if __name__ == '__main__':
    main()
