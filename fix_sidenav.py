html = open('index.html', encoding='utf-8').read()

replacements = {
    '>Global validation<': '>Global Validation<', # Keep it or change it? Wait, let's look at the sections above.
    '>The Z-axis<': '>Proactive Defense<',
    '>01 // SLB Digital Twin<': '>01 // Executive Protection<',
    '>02 // Digital Real Estate<': '>02 // Threat Intelligence<',
    '>03 // Complex Saas UX<': '>03 // Cyber Defense<',
    '>Initiate<': '>Command Center<'
}

for old, new in replacements.items():
    html = html.replace(old, new)

with open('index.html', 'w', encoding='utf-8') as f:
    f.write(html)
    
print("Replaced all side nav items")
