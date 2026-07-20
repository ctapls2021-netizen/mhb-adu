import re

def main():
    with open('src/pages/index.astro', 'r', encoding='utf-8') as f:
        content = f.read()

    # 1. Update scaleDesign script to run immediately if DOM is ready
    old_scale_script = """<script is:inline>
  function scaleDesign() {
    var container = document.getElementById('container');
    if (!container) return;
    
    if (window.innerWidth < 1024) {
      var scale = window.innerWidth / 480;
      container.style.transform = 'scale(' + scale + ')';
    } else {
      container.style.transform = 'none';
    }
  }

  window.addEventListener('resize', scaleDesign);
  window.addEventListener('DOMContentLoaded', scaleDesign);
</script>"""

    new_scale_script = """<script is:inline>
  function scaleDesign() {
    var container = document.getElementById('container');
    if (!container) return;
    
    if (window.innerWidth < 1024) {
      var scale = window.innerWidth / 480;
      container.style.transform = 'scale(' + scale + ')';
    } else {
      container.style.transform = 'none';
    }
  }

  window.addEventListener('resize', scaleDesign);
  if (document.readyState === 'loading') {
    window.addEventListener('DOMContentLoaded', scaleDesign);
  } else {
    scaleDesign();
  }
</script>"""

    # 2. Update slider script to run immediately if DOM is ready
    old_slider_script_start = """<script is:inline>
  document.addEventListener('DOMContentLoaded', () => {
    if (window.innerWidth >= 1024) return; // Only mobile"""

    new_slider_script_start = """<script is:inline>
  function initSlider() {
    if (window.innerWidth >= 1024) return; // Only mobile

    const container = document.getElementById('container');
    if (!container) return;

    if (document.querySelector('.adu-slider-wrapper')) return;

    const sliderWrapper = document.createElement('div');
    sliderWrapper.className = 'adu-slider-wrapper';
    
    const sliderTrack = document.createElement('div');
    sliderTrack.className = 'adu-slider-track';
    sliderWrapper.appendChild(sliderTrack);
    
    const cards = [
        ['css-dvs7qv', 'css-pka6yd', 'css-isagh0', 'css-rdcjzi', 'css-1tz7d0', 'css-sqgevl', 'css-kaizum', 'css-c3vudm'],
        ['css-hry8ah', 'css-cvw59p', 'css-c6gfuu', 'css-lhwfyv', 'css-mrxjfi', 'css-4jygia', 'css-jizx1m', 'css-h91s6s'],
        ['css-dvut5i', 'css-pkcqtw', 'css-2lywx', 'css-gjp8cy', 'css-kazf1u', 'css-hoha6l', 'css-e3yc09', 'css-c3fu8w'],
        ['css-hrvocd', 'css-cvyp7t', 'css-e2mxfm', 'css-ne2xjn', 'css-mruzhe', 'css-5ns3tt', 'css-ooeuwn', 'css-h9hquz'],
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
  }

  if (document.readyState === 'loading') {
    window.addEventListener('DOMContentLoaded', initSlider);
  } else {
    initSlider();
  }
</script>"""

    # We can replace the whole second script block.
    # Let's find the second script block in content.
    slider_pattern = r'<script is:inline>\s*document\.addEventListener\(\'DOMContentLoaded\', \(\) => \{.*?</script>'
    
    content = content.replace(old_scale_script, new_scale_script)
    content = re.sub(slider_pattern, new_slider_script_start, content, flags=re.DOTALL)

    with open('src/pages/index.astro', 'w', encoding='utf-8') as f:
        f.write(content)
        
    print('Updated scripts to avoid race conditions!')

if __name__ == '__main__':
    main()
