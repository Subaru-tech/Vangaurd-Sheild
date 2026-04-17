import re

def process():
    html = open('index.html', encoding='utf-8').read()

    # 1. REMOVE POPUP-VR DIV AND ITS CHILDREN
    # Since popup-vr is a huge block, we can reliably match it until the next major block
    # It starts with <div class="popup-vr"> and ends right before <div class="carousel-3d">
    html = re.sub(r'<div class="popup-vr">.*?<div class="carousel-3d">', '<div class="carousel-3d">', html, flags=re.DOTALL)
    
    # Also ensure head-tracking-fab is gone (was removed previously but to be absolutely sure)
    html = re.sub(r'<div class="head-tracking-fab">.*?</div>', '', html, flags=re.DOTALL)

    # 2. REMOVE ML AND TRACKING EXTERNAL SCRIPTS
    html = re.sub(r'<script src="https://cdn.jsdelivr.net/npm/@mediapipe/[^>]+></script>', '', html)
    html = re.sub(r'<script src="https://head-vr.pages.dev/assets/headtracking.js"[^>]*></script>', '', html)
    html = re.sub(r'<script src="https://head-vr.pages.dev/assets/handtracking.js"[^>]*></script>', '', html)
    
    # 3. REMOVE POPUP INLINE SCRIPT
    # This script starts with <!-- HEAD TRACKING POPUP --> and goes to the end
    html = re.sub(r'<!-- HEAD TRACKING POPUP -->\s*<script>.*?</script>', '', html, flags=re.DOTALL)
    
    # 4. FIX CONTACT EMAIL AND ADD MORE CONTACT INFO
    # The previous regex might have missed 'aquilaprotective' if it wasn't strictly matching. Current email is contact@aquilaprotective.com
    html = re.sub(r'contact@aquilaprotective\.com', 'operations@vanguard-shield.com', html)
    html = re.sub(r'contact@vanguard shield\.com', 'operations@vanguard-shield.com', html, flags=re.IGNORECASE)
    
    # Let's add the contact stuff: Phone number and emergency line.
    target_contact = '<div class="text-block-24"><strong>COMMAND CENTER<br></strong>'
    # We will inject a new block or append to this block
    if target_contact in html:
        # Instead of finding and replacing the exact whole block, we inject right after the email anchor tag.
        # Find the end of the text-block-24
        # Existing structure: <div class="text-block-24"><strong>COMMAND CENTER<br></strong><a href="#" target="_blank" class="link-white">operations@vanguard-shield.com</a></div>
        new_info = '<br><br><strong>GLOBAL DISPATCH:</strong> +1 (800) 555-VGRD<br><strong>SECURE LINE:</strong> +44 20 7946 0958'
        html = re.sub(r'(<div class="text-block-24"><strong>COMMAND CENTER<br></strong><a [^>]+>.*?</a>)', r'\1' + new_info, html)
        
    with open('index.html', 'w', encoding='utf-8') as f:
        f.write(html)
        
    print("Done")

if __name__ == "__main__":
    process()
