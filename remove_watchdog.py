import re

html = open('index.html', encoding='utf-8').read()

# Delete the Watchdog script block
html = re.sub(r'<!-- Watchdog for Firewalled Asset Connections -->\s*<script>.*?</script>', '', html, flags=re.DOTALL)

# Delete any remnant watchdog lines if they weren't wrapped
html = re.sub(r'<script>\s*\(function\(\)\s*\{\s*// Watchdog.*?\}\)\(\);\s*</script>', '', html, flags=re.DOTALL)

with open('index.html', 'w', encoding='utf-8') as f:
    f.write(html)
    
print("Watchdog excised")
