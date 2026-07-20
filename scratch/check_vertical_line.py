with open('src/styles/global.css', 'a', encoding='utf-8') as f:
    f.write('''

/* Smooth Scroll & Fade In Animations */
html {
  scroll-behavior: smooth;
}

.reveal-on-scroll {
  opacity: 0;
  transform: translateY(24px);
  transition: opacity 0.8s cubic-bezier(0.16, 1, 0.3, 1), transform 0.8s cubic-bezier(0.16, 1, 0.3, 1);
  will-change: opacity, transform;
}

.reveal-on-scroll.is-visible {
  opacity: 1;
  transform: translateY(0);
}

/* Button & Card Hover Micro-animations */
a[href^="#"], button, .adu-card-slide, .header-desktop-btn {
  transition: transform 0.25s cubic-bezier(0.16, 1, 0.3, 1), box-shadow 0.25s ease, background-color 0.25s ease, filter 0.25s ease;
}

a[href^="#"]:hover, button:hover {
  transform: translateY(-2px);
  filter: brightness(1.06);
}

a[href^="#"]:active, button:active {
  transform: translateY(0);
}
''')

print("Appended smooth animation CSS to global.css")
