import re

with open('src/pages/index.astro', 'r', encoding='utf-8') as f:
    content = f.read()

start_idx = content.find('@media (max-width: 1023px)')
end_style = content.find('</style>', start_idx)
mobile_css = content[start_idx:end_style]

def replace_rule(cls, new_rule, css):
    pattern = r'(#container \.' + cls + r'\s*{)[^}]*(})'
    if re.search(pattern, css):
        return re.sub(pattern, r'\g<1>\n      ' + new_rule + r'\n    \g<2>', css)
    else:
        return css + f'\n    #container .{cls} {{\n      {new_rule}\n    }}\n'

# Push ADU Types text down to leave 30px gap after Financing
mobile_css = replace_rule('css-mshi22', 'left: 20px !important; top: calc(50vh + 2440px) !important; width: 440px !important; text-align: center !important; font-size: 32px !important; line-height: 1.2em !important;', mobile_css)
mobile_css = replace_rule('css-v511zc', 'left: 20px !important; top: calc(50vh + 2580px) !important; width: 440px !important; text-align: center !important; position: absolute !important;', mobile_css)

# Bring the ADU Types blue background to mobile!
# Financing gray text ends around 2330px.
# 30px padding -> blue background starts at 2360px.
mobile_css = replace_rule('css-dpvz6t', 'left: 0px !important; top: calc(50vh + 2360px) !important; position: absolute !important;', mobile_css)
mobile_css = replace_rule('css-628mvu', 'width: 480px !important; height: 750px !important; left: 0px !important; top: calc(50vh + 2360px) !important; position: absolute !important; display: block !important;', mobile_css)

content = content[:start_idx] + mobile_css + content[end_style:]

with open('src/pages/index.astro', 'w', encoding='utf-8') as f:
    f.write(content)

print('Updated ADUTypes background and text positions!')
