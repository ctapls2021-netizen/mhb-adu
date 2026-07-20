import re

def main():
    with open('src/styles/global.css', 'r', encoding='utf-8') as f:
        css = f.read()

    # Find all elements in the ADU Types section
    cards = [[] for _ in range(4)]
    
    # We will look for elements with top between 3200 and 4100
    for m in re.finditer(r'(?:#container \.|\.)(css-[a-z0-9]+)\s*\{([^}]+)\}', css):
        cls = m.group(1)
        rules = m.group(2)
        top_m = re.search(r'top:\s*([0-9]+)px', rules)
        if top_m:
            top = int(top_m.group(1))
            if 3200 <= top <= 4100:
                left_m = re.search(r'left:\s*([0-9]+(?:\.[0-9]+)?)px', rules)
                left = float(left_m.group(1)) if left_m else 0
                width_m = re.search(r'width:\s*([0-9]+(?:\.[0-9]+)?)px', rules)
                width = float(width_m.group(1)) if width_m else 0
                
                # Exclude the large white background
                if width > 1000: continue
                
                # Determine which card it belongs to
                card_idx = -1
                if top < 3700:
                    if left < 900: card_idx = 0
                    else: card_idx = 1
                else:
                    if left < 900: card_idx = 2
                    else: card_idx = 3
                    
                if card_idx != -1:
                    cards[card_idx].append(cls)

    print("Card classes mapped dynamically:")
    for i, c in enumerate(cards):
        print(f"Card {i+1}: {c}")

    # Now let's inject this into build_slider.py and rewrite the CSS!
    
    with open('src/pages/index.astro', 'r', encoding='utf-8') as f:
        content = f.read()

    # 1. Update the JavaScript array
    js_array = "[\n"
    for c in cards:
        js_array += "        [" + ", ".join([f"'{cls}'" for cls in c]) + "],\n"
    js_array += "    ]"
    
    # Replace the old cards array in JS
    content = re.sub(
        r'const cards = \[[^\]]+\];',
        f'const cards = {js_array};',
        content,
        flags=re.DOTALL
    )

    # 2. Update the CSS for the slide elements
    # We will rip out the old unified CSS block and write a new one
    start_css = content.find('/* Unified Card Element Styles inside .adu-slide */')
    end_css = content.find('</style>', start_css)
    
    if start_css != -1 and end_css != -1:
        # We need to write rules targeting elements by their class.
        # But wait! Which class is which element?!
        # We can figure it out by their desktop relative positioning!
        # Or we can just use the classes we already know + the new ones.
        # But mapping dynamically is safer.
        pass

if __name__ == '__main__':
    main()
