html = open('index.html', encoding='utf-8').read()

old = '<div class="nav-wrap-div-block"><img loading="lazy" src="https://cdn.prod.website-files.com/65c83fbb9f2750d119b43fb3/65dbfd98df4c613e762c8339_Vertex3d_logo.svg" alt=""></div>'
new = '<div class="nav-wrap-div-block" style="font-family: Outfit, sans-serif; font-size: 18px; font-weight: 700; letter-spacing: 3px; color: #fff; text-transform: uppercase;">VANGUARD SHIELD</div>'

print('Found old logo:', old in html)
html = html.replace(old, new)

open('index.html', 'w', encoding='utf-8').write(html)
print('Done - header now shows VANGUARD SHIELD text')
