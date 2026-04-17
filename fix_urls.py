import re

html = open('index.html', encoding='utf-8').read()

# Fix the CSS file link
html = re.sub(r'Vanguard Shield(\.webflow\.shared)', r'vertex3d\1', html, flags=re.IGNORECASE)

# Fix the logo
html = re.sub(r'Vanguard Shield(_logo\.svg)', r'Vertex3d\1', html, flags=re.IGNORECASE)

# Fix the domain references
html = re.sub(r'www\.Vanguard Shield\.asia', r'www.vertex3d.asia', html, flags=re.IGNORECASE)

# Fix JS webflow chunk files if any
html = re.sub(r'/js/Vanguard Shield\.', r'/js/vertex3d.', html, flags=re.IGNORECASE)

# Write it back
with open('index.html', 'w', encoding='utf-8') as f:
    f.write(html)

print("URL structure successfully repaired!")
