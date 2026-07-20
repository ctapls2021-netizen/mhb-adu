import re

def main():
    with open('src/pages/index.astro', 'r', encoding='utf-8') as f:
        content = f.read()

    start_idx = content.find('@media (max-width: 1023px)')
    end_style = content.find('</style>', start_idx)
    mobile_css = content[start_idx:end_style]

    # Classes to remove from mobile_css
    classes_to_remove = [
        'css-isagh0', 'css-rdcjzi', 'css-1tz7d0', 'css-pka6yd', 'css-dvs7qv', 'css-kaizum', 'css-c3vudm',
        'css-4jygia', 'css-c6gfuu', 'css-jizx1m', 'css-cvw59p', 'css-hry8ah', 'css-mrxjfi', 'css-h91s6s',
        'css-hoha6l', 'css-ne2xjn', 'css-e3yc09', 'css-pkcqtw', 'css-dvut5i', 'css-kazf1u', 'css-c3fu8w',
        'css-5ns3tt', 'css-ooeuwn', 'css-cvyp7t', 'css-dwatej', 'css-mruzhe', 'css-h9hquz',
        'css-pj6ukt' # We will redefine the white background height!
    ]

    for cls in classes_to_remove:
        pattern = r'#container \.' + cls + r'\s*{[^}]*}'
        mobile_css = re.sub(pattern, '', mobile_css)
        # Also remove if it has height: auto !important from the fix_height script
        # Wait, fix_height script only added height auto to mshi22 and v511zc, which are NOT in this list.

    # Slider CSS rules
    new_rules = """
    #container .css-pj6ukt { width: 480px !important; height: 560px !important; left: 0px !important; top: calc(50vh + 2700px) !important; position: absolute !important; display: block !important; }
    
    #container .adu-slider-wrapper { position: absolute !important; top: calc(50vh + 2700px) !important; left: 0px !important; width: 480px !important; height: 560px !important; overflow: hidden !important; z-index: 10 !important; }
    #container .adu-slider-track { display: flex !important; width: 400% !important; height: 100% !important; transition: transform 0.5s ease-in-out !important; }
    #container .adu-slide { width: 480px !important; height: 100% !important; position: relative !important; flex-shrink: 0 !important; }
    
    #container .adu-slider-dots { position: absolute !important; bottom: 20px !important; left: 0 !important; width: 100% !important; display: flex !important; justify-content: center !important; gap: 10px !important; z-index: 20 !important; }
    #container .adu-dot { width: 12px !important; height: 12px !important; border-radius: 50% !important; background-color: #ccc !important; cursor: pointer !important; transition: background-color 0.3s !important; }
    #container .adu-dot.active { background-color: #0077c8 !important; }

    /* Unified Card Element Styles inside .adu-slide */
    #container .adu-slide .css-isagh0, #container .adu-slide .css-4jygia, #container .adu-slide .css-hoha6l, #container .adu-slide .css-5ns3tt {
        width: 160px !important; height: 160px !important; left: 160px !important; top: 40px !important; position: absolute !important;
    }
    
    #container .adu-slide .css-rdcjzi, #container .adu-slide .css-c6gfuu, #container .adu-slide .css-ne2xjn, #container .adu-slide .css-ooeuwn {
        width: 440px !important; left: 20px !important; top: 220px !important; text-align: center !important; font-size: 24px !important; position: absolute !important;
    }
    
    #container .adu-slide .css-1tz7d0, #container .adu-slide .css-jizx1m, #container .adu-slide .css-e3yc09 {
        width: 440px !important; left: 20px !important; top: 260px !important; text-align: center !important; position: absolute !important;
    }
    
    #container .adu-slide .css-pka6yd, #container .adu-slide .css-cvw59p, #container .adu-slide .css-pkcqtw, #container .adu-slide .css-cvyp7t {
        width: 440px !important; left: 20px !important; top: 310px !important; text-align: center !important; font-size: 14px !important; position: absolute !important;
    }
    
    #container .adu-slide .css-dvs7qv, #container .adu-slide .css-hry8ah, #container .adu-slide .css-dvut5i, #container .adu-slide .css-dwatej {
        width: 240px !important; height: 50px !important; left: 120px !important; top: 410px !important; position: absolute !important;
    }
    
    #container .adu-slide .css-kaizum, #container .adu-slide .css-mrxjfi, #container .adu-slide .css-kazf1u, #container .adu-slide .css-mruzhe {
        left: 140px !important; top: 420px !important; font-size: 12px !important; position: absolute !important; z-index: 100 !important;
    }
    
    #container .adu-slide .css-c3vudm, #container .adu-slide .css-h91s6s, #container .adu-slide .css-c3fu8w, #container .adu-slide .css-h9hquz {
        left: 140px !important; top: 435px !important; font-size: 14px !important; position: absolute !important; z-index: 100 !important;
    }
"""

    mobile_css = re.sub(r'\n\s*\n', '\n', mobile_css)

    if mobile_css.endswith('  }\n'):
        mobile_css = mobile_css[:-4] + '\n' + new_rules + '  }\n'
    elif mobile_css.endswith('  }'):
        mobile_css = mobile_css[:-3] + '\n' + new_rules + '  }\n'
    else:
        mobile_css = mobile_css + '\n' + new_rules + '  }\n'

    content = content[:start_idx] + mobile_css + content[end_style:]

    # Now let's inject the JavaScript!
    js_code = """
<script is:inline>
  document.addEventListener('DOMContentLoaded', () => {
    if (window.innerWidth >= 1024) return; // Only mobile

    const container = document.getElementById('container');
    if (!container) return;

    // Check if already injected
    if (document.querySelector('.adu-slider-wrapper')) return;

    const sliderWrapper = document.createElement('div');
    sliderWrapper.className = 'adu-slider-wrapper';
    
    const sliderTrack = document.createElement('div');
    sliderTrack.className = 'adu-slider-track';
    sliderWrapper.appendChild(sliderTrack);
    
    const cards = [
        ['css-isagh0', 'css-rdcjzi', 'css-1tz7d0', 'css-pka6yd', 'css-dvs7qv', 'css-kaizum', 'css-c3vudm'],
        ['css-4jygia', 'css-c6gfuu', 'css-jizx1m', 'css-cvw59p', 'css-hry8ah', 'css-mrxjfi', 'css-h91s6s'],
        ['css-hoha6l', 'css-ne2xjn', 'css-e3yc09', 'css-pkcqtw', 'css-dvut5i', 'css-kazf1u', 'css-c3fu8w'],
        ['css-5ns3tt', 'css-ooeuwn', 'css-cvyp7t', 'css-dwatej', 'css-mruzhe', 'css-h9hquz']
    ];

    cards.forEach((cardClasses, index) => {
        const slide = document.createElement('div');
        slide.className = 'adu-slide';
        
        cardClasses.forEach(cls => {
            const elements = container.querySelectorAll('.' + cls);
            elements.forEach(el => {
                slide.appendChild(el);
            });
        });
        
        sliderTrack.appendChild(slide);
    });

    const dotsContainer = document.createElement('div');
    dotsContainer.className = 'adu-slider-dots';
    cards.forEach((_, i) => {
        const dot = document.createElement('div');
        dot.className = 'adu-dot' + (i === 0 ? ' active' : '');
        dot.addEventListener('click', () => goToSlide(i));
        dotsContainer.appendChild(dot);
    });
    sliderWrapper.appendChild(dotsContainer);

    container.appendChild(sliderWrapper);

    let currentSlide = 0;
    const totalSlides = cards.length;
    let autoPlayInterval;

    function goToSlide(index) {
        currentSlide = index;
        sliderTrack.style.transform = `translateX(-${currentSlide * 25}%)`;
        
        Array.from(dotsContainer.children).forEach((dot, i) => {
            dot.className = 'adu-dot' + (i === currentSlide ? ' active' : '');
        });
        
        resetAutoPlay();
    }

    function nextSlide() {
        goToSlide((currentSlide + 1) % totalSlides);
    }

    function resetAutoPlay() {
        clearInterval(autoPlayInterval);
        autoPlayInterval = setInterval(nextSlide, 3500);
    }

    resetAutoPlay();
  });
</script>
"""
    
    # Inject before </body>
    if '</body>' in content:
        content = content.replace('</body>', js_code + '\n</body>')
    else:
        content += js_code

    with open('src/pages/index.astro', 'w', encoding='utf-8') as f:
        f.write(content)
        
    print('Carousel injected successfully!')

if __name__ == '__main__':
    main()
