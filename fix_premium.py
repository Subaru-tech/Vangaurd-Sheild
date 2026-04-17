import re

html = open('index.html', encoding='utf-8').read()

# 1. Remove the word "Premium" (with optional following space)
html = re.sub(r'(?i)\bpremium\b\s*-?\s*', '', html)

# 2. Fix the '<br>' spacing if "Premium" was right before it. 
# <h1 ...>Premium<br>...</h1> becomes <h1 ...><br>...</h1>, which is fine, but we can clean it to <h1 ...>...</h1>
# Wait, actually: `<h1 ...>Premium<br><span ...`
# Let's clean up `<br>` if it starts an element text:
html = html.replace('><br>', '>')

# 3. Remove the webcam button container
# Original starts with <div class="head-tracking-fab">
html = re.sub(r'<div class="head-tracking-fab">.*?<img[^>]*class="webcam-on"[^>]*></a></div>', '', html)

# write
with open('index.html', 'w', encoding='utf-8') as f:
    f.write(html)
    
print("Revisions successfully applied")
