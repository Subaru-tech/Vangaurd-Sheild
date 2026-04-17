import re

html = open('index.html', encoding='utf-8').read()

# 1. Remove the [ Services ] link exactly
html = re.sub(r'<a[^>]*id="projectcard"[^>]*>\[\s*Services\s*\]</a>', '', html)

# 2. Add Policies
target = '<div class="text-block-26"><a href="#" target="_blank" class="link-white">Licensed & Insured Global Operators</a><br></div>'
replacement = target + '<div class="text-block-27" style="margin-top: 15px;"><a href="#" class="link-white">Privacy Policy</a> | <a href="#" class="link-white">Terms of Service</a></div>'
html = html.replace(target, replacement)

# 3. Make sure 'Vanguard Shield' replaced 'Vertex3D' in contactus wrapper since user said "in initiate it's abt vertex so replace it with Vanguard Shield"
# Maybe Vertex3D wasn't just there but also in Initiate? The ID is 'contactus'. But wait, in previous step I replaced 'Aquila Protective' with 'Vanguard Shield'.
# Wait, did the user mean the text text-block-25 LEGAL Vertex3D? Let's aggressively replace any leftover Vertex3D.
html = re.sub(r'Vertex3D', 'Vanguard Shield', html, flags=re.IGNORECASE)

with open('index.html', 'w', encoding='utf-8') as f:
    f.write(html)
print("Fixes applied.")
