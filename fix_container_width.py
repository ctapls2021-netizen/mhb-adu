import re

def main():
    with open('src/pages/index.astro', 'r', encoding='utf-8') as f:
        content = f.read()

    # The broken CSS:
    # @media (max-width: 1023px) {
    #   body { margin: 0; padding: 0; overflow-x: hidden; }
    #   #container { transform-origin: top left !important; }
    
    old_css = """@media (max-width: 1023px) {
  body { margin: 0; padding: 0; overflow-x: hidden; }
  #container { transform-origin: top left !important; }"""
  
    new_css = """@media (max-width: 1023px) {
  body { margin: 0; padding: 0; overflow-x: hidden; }
  #container { 
    transform-origin: top left !important; 
    width: 480px !important; 
    overflow-x: hidden !important; 
    height: auto !important;
  }"""
    
    if old_css in content:
        content = content.replace(old_css, new_css)
        with open('src/pages/index.astro', 'w', encoding='utf-8') as f:
            f.write(content)
        print('Fixed the container width!')
    else:
        print('Could not find the exact string!')

if __name__ == '__main__':
    main()
