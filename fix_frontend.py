import urllib.request
import re
import os

def process():
    print("Downloading webflow.js...")
    req = urllib.request.Request('https://head-vr.pages.dev/assets/webflow.js', headers={'User-Agent': 'Mozilla/5.0'})
    with urllib.request.urlopen(req) as f:
        js_content = f.read().decode('utf-8')
    
    print("Modifying webflow.js...")
    # Replace Vertex3D in JS
    js_content = re.sub(r'Vertex3D', 'Vanguard Shield', js_content, flags=re.IGNORECASE)
    js_content = re.sub(r'Vertex 3D', 'Vanguard Shield', js_content, flags=re.IGNORECASE)
    
    with open('webflow.local.js', 'w', encoding='utf-8') as f:
        f.write(js_content)
        
    print("Modifying index.html...")
    with open('index.html', 'r', encoding='utf-8') as f:
        html = f.read()

    # Replace local JS pointing
    html = html.replace('https://head-vr.pages.dev/assets/webflow.js', './webflow.local.js')
    
    # Replace Aquila Protective with Vanguard Shield
    html = html.replace('Aquila Protective', 'Vanguard Shield')
    
    # Remove Services link from Nav
    html = re.sub(r'<a href="[^"]*" id="projectcard"[^>]*>\[ Services \]</a>', '', html)
    
    # Alternatively the user might mean the word 'Services' if it was left somewhere else, but let's replace "Explore All Services" just in case they meant the nav link 'serveses'.
    # I'll leave "Explore All Services" since that's inside the panels, and the user specifically said "rm serveses". That typically targets the top nav link that they mispelled.
    
    # Remove Address textblock in the Contactwrapper
    # <div class="text-block-23"><strong>GLOBAL HEADQUARTERS&nbsp;&nbsp;</strong><br>1 Rockefeller Plaza,<br>New York, NY 10020, USA</div>
    html = re.sub(r'<div class="text-block-23">.*?</div>', '', html)
    
    # Add Policies in Initiate/Contact section. I'll append it to text-block-25 or just as a new block
    # Existing: <div class="text-block-26"><a href="#" target="_blank" class="link-white">Licensed &amp; Insured Global Operators</a><br></div>
    # Add Privacy Policy, Terms of Service into the contactwrapper
    policies_html = '<div class="text-block-27" style="margin-top: 20px;"><a href="#" class="link-white">Privacy Policy</a> | <a href="#" class="link-white">Terms of Service</a></div>'
    html = html.replace('Licensed &amp; Insured Global Operators</a><br></div>', 'Licensed &amp; Insured Global Operators</a><br></div>' + policies_html)
    
    with open('index.html', 'w', encoding='utf-8') as f:
        f.write(html)
        
    print("Done!")

if __name__ == "__main__":
    process()
