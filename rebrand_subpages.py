import re

# ========================
# PATCH 1: slb-digitalfield -> Executive Protection Case Study
# ========================
with open('project/slb-digitalfield/index.html', encoding='utf-8') as f:
    slb = f.read()

slb = slb.replace('<title>real-time 3D solution for Schlumberger SLB</title>',
                  '<title>Executive Protection — Vanguard Shield</title>')
slb = slb.replace('content="Immersive real-time 3D solution for Schlumberger\'s Digital Oilfield. Interactive visualization of integrated energy systems across land, sea, and subsurface."',
                  'content="Vanguard Shield deploys elite executive protection operators to safeguard corporate leaders, high-value individuals, and critical assets globally."')
slb = slb.replace('<div class="subheading-playcanvas">Real-time 3D</div>',
                  '<div class="subheading-playcanvas">Executive Protection</div>')
slb = slb.replace('<h2 class="a-h1-heading">Schlumberger <br>Digital Oilfield</h2>',
                  '<h2 class="a-h1-heading">Vanguard Shield<br>Elite Protection</h2>')
slb = slb.replace('<p class="rl-text-style-medium-2 projectpage">Elevating key presentations <br>with real-time 3D environment.</p>',
                  '<p class="rl-text-style-medium-2 projectpage">Safeguarding lives and assets through military-grade executive security.</p>')
slb = slb.replace('<div class="destitleproject">Client</div><p class="descontentproject">SLB</p>',
                  '<div class="destitleproject">Clients</div><p class="descontentproject">Fortune 500 Executives<br>Diplomats &amp; HNWIs</p>')
slb = slb.replace('<div class="destitleproject">Service Provided</div><p class="descontentproject">3D Rendering<br>Real-time 3D<br>Frontend Development<br>UI/UX Design<br></p>',
                  '<div class="destitleproject">Services</div><p class="descontentproject">Close Protection<br>Secure Transport<br>Threat Assessment<br>Intelligence Briefings<br></p>')
slb = slb.replace('<h1 data-w-id="280674b4-a469-3ba0-5e1f-40983bda145c" style="opacity:0" class="projectheadingw">An Immersive Solution</h1>',
                  '<h1 data-w-id="280674b4-a469-3ba0-5e1f-40983bda145c" style="opacity:0" class="projectheadingw">Uncompromising Protection</h1>')
slb = slb.replace(
    'We collaborated with SLB, a renowned leader in the Oil and Gas industry, to establish a comprehensive hub for accessing all presentations and media content during their global SLB Forum event held in Switzerland. <br><br>One of their stipulations was to ensure online accessibility, prompting us to opt for 3D real-time rendering technology to meticulously reconstruct a miniature ecosystem showcasing their various domains.',
    'Vanguard Shield provides elite executive protection to Fortune 500 executives, diplomats, and high-net-worth individuals across 40+ countries. Our operators are former special forces and intelligence personnel, trained to neutralize threats at every level.<br><br>Every principal receives a bespoke protection plan built on continuous threat intelligence, secure transportation logistics, and advance security protocols — ensuring their safety is never left to chance.'
)
slb = slb.replace(
    '<h1 data-w-id="c7a5124c-c41f-d96c-fa5c-d71e7b9ead35" style="opacity:0" class="projectheadingb">Shaping the World</h1>',
    '<h1 data-w-id="c7a5124c-c41f-d96c-fa5c-d71e7b9ead35" style="opacity:0" class="projectheadingb">Intel-Driven Operations</h1>'
)
slb = slb.replace(
    'To craft this virtual environment, our initial step involved comprehensively understanding the specifications and intricacies of the equipment and surroundings. We opted to segment the map into three distinct sections: land, sea, and subsurface.',
    'Every protection detail begins with rigorous intelligence gathering. We analyse geopolitical risk, venue threat profiles, and adversary patterns before personnel ever deploy. Our analysts provide continuous threat updates in real-time so operators can adapt instantly to evolving situations.'
)
slb = slb.replace('<h1 data-w-id="efb33682-c4f9-51fc-91c7-3229c1f188ed" style="opacity:0" class="projectheadingb">Visual Design</h1>',
                  '<h1 data-w-id="efb33682-c4f9-51fc-91c7-3229c1f188ed" style="opacity:0" class="projectheadingb">Layered Security Zones</h1>')
slb = slb.replace(
    'Significant emphasis was placed on the art direction to offer a visually striking and captivating interface. With the mandate to convey the concept of a Digital Twin, we ingeniously crafted a visual narrative that seamlessly bridges the gap between the real and digital worlds. <br><br>The UI/UX was meticulously designed to align with the 3D aesthetic, maintaining consistent adherence to the overarching art direction throughout the entirety of the project.',
    'Protection is structured in concentric rings — outer perimeter, middle layer, and close protection. Each layer operates with distinct protocols and communication channels, ensuring redundancy and resilience against penetration. Teams undergo continuous scenario training and live-fire exercises to maintain peak operational readiness.'
)
slb = slb.replace('<h1 data-w-id="3a915ce2-2912-dd27-94d2-dfeb47d4028d" style="opacity:0" class="projectheadingw">Attention to Detail</h1>',
                  '<h1 data-w-id="3a915ce2-2912-dd27-94d2-dfeb47d4028d" style="opacity:0" class="projectheadingw">Precision Planning</h1>')
slb = slb.replace(
    'We collaborated closely with the SLB team to ensure precision in the 3D elements, leaving no room for error.',
    'No detail is overlooked. From advance route reconnaissance to medical contingency planning, Vanguard Shield operators leave nothing to chance — because in protection, there are no second chances.'
)
slb = slb.replace('<h1 data-w-id="aa24a043-f83b-0f0b-0f2f-9af110104796" style="opacity:0" class="projectheadingw">Custom Iconography</h1>',
                  '<h1 data-w-id="aa24a043-f83b-0f0b-0f2f-9af110104796" style="opacity:0" class="projectheadingw">Global Footprint</h1>')
slb = slb.replace(
    'Custom icons were meticulously designed for this project to enhance visual clarity and facilitate clear comprehension.',
    'With operational teams stationed across North America, Europe, the Middle East, and Southeast Asia, Vanguard Shield delivers seamless protection wherever our clients need us — ensuring continuity of safety across every time zone and every jurisdiction.'
)

with open('project/slb-digitalfield/index.html', 'w', encoding='utf-8') as f:
    f.write(slb)

print("Page 1 (Executive Protection) done.")

# ========================
# PATCH 2: real-estate -> Threat Intelligence Case Study
# ========================
with open('web/real-estate/index.html', encoding='utf-8') as f:
    re_html = f.read()

re_html = re_html.replace('<title>Real-estate</title>',
                          '<title>Threat Intelligence — Vanguard Shield</title>')
re_html = re_html.replace('<div class="subheading-playcanvas">3D Rendering</div>',
                          '<div class="subheading-playcanvas">Threat Intelligence</div>')
re_html = re_html.replace('<h2 class="a-h1-heading">Architectural 3D Rendering Services</h2>',
                          '<h2 class="a-h1-heading">Global Risk<br>Intelligence</h2>')
re_html = re_html.replace('<p class="rl-text-style-medium-2 projectpage">Delivering immersive 3D rendering experiences for real estate projects.</p>',
                          '<p class="rl-text-style-medium-2 projectpage">Actionable intelligence to neutralise threats before they materialise.</p>')
re_html = re_html.replace('<div class="destitleproject">Service Provided</div><p class="descontentproject">3D Rendering (video/image)<br>Real-time 3D<br>Website Design<br>UI/UX Design<br>VR&amp;AR Experiences<br></p>',
                          '<div class="destitleproject">Capabilities</div><p class="descontentproject">Open Source Intelligence<br>Corporate Espionage Detection<br>Geopolitical Risk Analysis<br>Dark Web Monitoring<br>Counter-Surveillance<br></p>')
re_html = re_html.replace('<h1 data-w-id="59ed3458-396f-7ab1-6a09-a856feb0a5a4" style="opacity:0" class="projectheadingb">360° Interactive Video</h1>',
                          '<h1 data-w-id="59ed3458-396f-7ab1-6a09-a856feb0a5a4" style="opacity:0" class="projectheadingb">Intelligence That Protects</h1>')
re_html = re_html.replace(
    'Vertex3D delivers unique and immersive 3D visualization solutions for the real estate market, assisting clients worldwide. <br><br>The 360° interactive video allows your customers to navigate through the house while controlling the camera with the mouse or finger.',
    'Vanguard Shield\'s intelligence division operates a global network of analysts and field operatives who gather, verify, and synthesise threat data across every sector.<br><br>Our clients receive structured intelligence briefings, adversary profiles, and real-time alerts, giving them the operational clarity to make decisive protective decisions before threats escalate.'
)
re_html = re_html.replace('<h1 data-w-id="7265b05f-ad15-3742-e450-7502d6ccd35e" style="opacity:0" class="projectheadingb">360° Virtual Model</h1>',
                          '<h1 data-w-id="7265b05f-ad15-3742-e450-7502d6ccd35e" style="opacity:0" class="projectheadingb">Persistent Threat Monitoring</h1>')
re_html = re_html.replace(
    'This innovative solution allows customers to explore the project in an immersive, interactive environment, navigating through the entire space as if they were physically there. <br><br>With full control over their experience, users can select specific units within the project to access detailed information, such as floor plans, pricing, and availability. <br><br>This tool transforms the way potential buyers engage with real estate, offering an enhanced, hands-on approach to exploring and evaluating properties remotely.',
    'Our 24/7 monitoring infrastructure tracks threat actors across open web, social platforms, and deep-web forums. Machine-learning models combined with human analyst review ensure zero false negatives on high-priority alerts.<br><br>Threat intelligence is delivered through a secure client portal with tiered access controls, ensuring only authorised personnel receive sensitive assessments. Reports are structured for both executive decision-makers and operational security teams.'
)
re_html = re_html.replace('<h1 data-w-id="eb4b4b88-46e5-621b-a9a4-9acfb0c11984" style="opacity:0" class="projectheadingb">360° 3D Image</h1>',
                          '<h1 data-w-id="eb4b4b88-46e5-621b-a9a4-9acfb0c11984" style="opacity:0" class="projectheadingb">Corporate Espionage Counter-Ops</h1>')
re_html = re_html.replace('<h1 data-w-id="31576ba4-39f3-e897-7194-67ef5063c29e" style="opacity:0" class="projectheadingb">Real Time 3D</h1>',
                          '<h1 data-w-id="31576ba4-39f3-e897-7194-67ef5063c29e" style="opacity:0" class="projectheadingb">Geopolitical Risk Advisory</h1>')
re_html = re_html.replace(
    'We specialize in real-time 3D solutions tailored for the real estate market.<br><br>Our expertise lies in creating immersive, interactive 3D models and visualizations that allow developers, agents, and buyers to explore properties like never before. <br>‍<br>From virtual walkthroughs to detailed real-time renderings of Projects, possibilities are limitless!',
    'Operating in over 65 countries, our geopolitical risk analysts provide clients with country-specific stability assessments, sanction risk screening, and in-territory threat briefings.<br><br>Whether you are expanding operations into an emerging market or managing existing assets in a volatile region, Vanguard Shield intelligence ensures your decisions are grounded in verified, actionable data.'
)
re_html = re_html.replace('<h1 data-w-id="62f8ac79-3fa8-e467-001e-ba0d296f7404" style="opacity:0" class="projectheadingb">A rich portfolio with over 150+ Clients worldwide </h1>',
                          '<h1 data-w-id="62f8ac79-3fa8-e467-001e-ba0d296f7404" style="opacity:0" class="projectheadingb">Trusted by Global Enterprises</h1>')
re_html = re_html.replace(
    'We are a global leader in 3D rendering for the real estate industry, serving clients worldwide. <br><br>Whether you need high-quality visualizations, interactive virtual tours, or detailed architectural models, we respond quickly and efficiently to meet your unique needs. <br><br>Our team is dedicated to delivering top-tier solutions that help developers, architects, and real estate professionals showcase their projects with precision and impact, no matter where they\'re located.',
    'From multinational banking institutions to sovereign wealth funds and critical infrastructure operators, Vanguard Shield\'s intelligence clients represent some of the most asset-rich and threat-exposed organisations on the planet.<br><br>Our team responds with urgency and precision — because when geopolitical events unfold, decision windows are measured in hours, not days.'
)

with open('web/real-estate/index.html', 'w', encoding='utf-8') as f:
    f.write(re_html)

print("Page 2 (Threat Intelligence) done.")

# ========================
# PATCH 3: mysepstudio6 -> Cyber Defense Case Study
# ========================
with open('project/mysepstudio6/index.html', encoding='utf-8') as f:
    mysep = f.read()

mysep = mysep.replace('<title>MySep - Studio interface UI-UX</title>',
                      '<title>Cyber Defense — Vanguard Shield</title>')
mysep = mysep.replace('content="Complete UI/UX redesign of MySep Studio V6 separation software. Modern interface with dark and light themes, custom iconography, and reimagined user experience."',
                      'content="Vanguard Shield\'s military-grade cybersecurity services protect enterprise networks, critical data, and digital infrastructure against sophisticated threat actors."')
mysep = mysep.replace('<div class="subheading-playcanvas">UI/UX</div>',
                      '<div class="subheading-playcanvas">Cyber Defense</div>')
mysep = mysep.replace('<h2 class="a-h1-heading">MySep Studio V6</h2>',
                      '<h2 class="a-h1-heading">Vanguard Shield<br>CyberOps</h2>')
mysep = mysep.replace('<p class="rl-text-style-medium-2 projectpage">Revolutionizing the experience of separation software.</p>',
                      '<p class="rl-text-style-medium-2 projectpage">Military-grade cybersecurity architecture for enterprise-critical infrastructure.</p>')
mysep = mysep.replace('<div class="destitleproject">Client</div><p class="descontentproject">MySep Ltd</p>',
                      '<div class="destitleproject">Sectors Served</div><p class="descontentproject">Financial Services<br>Critical Infrastructure<br>Government &amp; Defence</p>')
mysep = mysep.replace('<div class="destitleproject">Service Provided</div><p class="descontentproject">UX Analysis<br>UI/UX Design<br>Design System<br></p>',
                      '<div class="destitleproject">Services</div><p class="descontentproject">Penetration Testing<br>SOC Monitoring 24/7<br>Incident Response<br>Zero-Trust Architecture</p>')
mysep = mysep.replace('<h1 data-w-id="c7a5124c-c41f-d96c-fa5c-d71e7b9ead35" class="projectheadingb">Task</h1><h1 class="projectheadingb">Challenge</h1><h1 class="projectheadingb">Solution</h1>',
                      '<h1 data-w-id="c7a5124c-c41f-d96c-fa5c-d71e7b9ead35" class="projectheadingb">Mission</h1><h1 class="projectheadingb">Threat</h1><h1 class="projectheadingb">Response</h1>')
mysep = mysep.replace(
    'MySep requested a redesign of their outdated software user interface for the next generation. They sought a modern and updated look and feel.',
    'A global financial institution required continuous protection of its trading infrastructure and client data across 12 global data centres spanning three continents.'
)
mysep = mysep.replace(
    'Understanding the intricacies of separation software is challenging, and discerning the needs of their users adds another layer of complexity.',
    'Advanced persistent threat (APT) groups had been conducting reconnaissance against the client\'s network perimeter for 14 months, seeking to exfiltrate sensitive client financial data.'
)
mysep = mysep.replace(
    'We completely reimagined the user experience of their software from the ground up, reinventing both navigation and interaction.',
    'Vanguard Shield deployed a zero-trust network architecture, established a 24/7 security operations centre, and conducted three rounds of red team penetration testing — neutralising the threat and hardening the defences permanently.'
)
mysep = mysep.replace('<h1 data-w-id="219dfbbc-e006-13c4-d7af-cd84fa6ee852" style="opacity:0" class="projectheadingb">Discovery</h1>',
                      '<h1 data-w-id="219dfbbc-e006-13c4-d7af-cd84fa6ee852" style="opacity:0" class="projectheadingb">Threat Assessment</h1>')
mysep = mysep.replace(
    'Our initial encounter was marked by a sudden realization of an outdated interface cluttered with numerous tabs, pop-ups, windows, and tables. Our thorough examination of each window ensured a complete grasp of the software.',
    'Vanguard Shield\'s cyber analysts conducted a comprehensive threat assessment across all 12 data centres. Vulnerability scanning, network traffic analysis, and endpoint forensics revealed 37 unpatched critical CVEs and three active intrusion chains that had persisted undetected for over a year.'
)
mysep = mysep.replace('<h1 data-w-id="ba2b5862-9261-f4a9-e650-fddc572155d6" style="opacity:0" class="projectheadingw designprocess">Design Process</h1>',
                      '<h1 data-w-id="ba2b5862-9261-f4a9-e650-fddc572155d6" style="opacity:0" class="projectheadingw designprocess">Response Methodology</h1>')
mysep = mysep.replace('<h1 data-w-id="962a8711-09b2-bbe5-4e08-cab9e4c97461" style="opacity:0" class="projectheadingb">Rethinking the UI/UX</h1>',
                      '<h1 data-w-id="962a8711-09b2-bbe5-4e08-cab9e4c97461" style="opacity:0" class="projectheadingb">Zero-Trust Architecture</h1>')
mysep = mysep.replace(
    'We commenced by reevaluating the information architecture and presented various iterations of the UX workflow. Once approved by the team, we proceeded to the visual design phase. Two themes were requested: Dark and White. We crafted a user interface with a contemporary aesthetic, ensuring ease of navigation and interaction.',
    'We implemented a strict zero-trust framework: verify every user, every device, every request — every time. Micro-segmentation isolated each trading system from lateral movement. Multi-factor authentication and privileged access management were enforced organisation-wide, eliminating over 90% of the attack surface within 30 days of deployment.'
)
mysep = mysep.replace('<h1 data-w-id="c4e31770-0f94-8e46-22ab-b2c1ebe4c4d1" style="opacity:0" class="projectheadingw">Component-Based Design System</h1>',
                      '<h1 data-w-id="c4e31770-0f94-8e46-22ab-b2c1ebe4c4d1" style="opacity:0" class="projectheadingw">SOC Operations Centre</h1>')
mysep = mysep.replace(
    'Two sets of components were developed for both themes. MySep Studio, being a complex software handling extensive data, required the creation of numerous data-related components, along with all interactions and animations.',
    'Vanguard Shield\'s Security Operations Centre monitors the client environment 24 hours a day, 365 days a year. Mean time to detect (MTTD) was reduced from 22 days to under 4 hours. Mean time to respond (MTTR) dropped to under 15 minutes with automated playbook execution for the 40 most common attack scenarios.'
)
mysep = mysep.replace('<h1 data-w-id="6d0cee3e-9fb1-b5b1-b5f2-a9664b22ee72" style="opacity:0" class="projectheadingw">Custom Iconography</h1>',
                      '<h1 data-w-id="6d0cee3e-9fb1-b5b1-b5f2-a9664b22ee72" style="opacity:0" class="projectheadingw">Measurable Outcomes</h1>')
mysep = mysep.replace(
    'Designing icons for complex domain software poses a considerable challenge due to the lack of common understanding. Our objective was to create icons that are comprehensible to domain experts, facilitating intuitive navigation within the software.',
    '99.98% network uptime maintained throughout the engagement. Zero successful data exfiltration events in 18 months post-deployment. Three attempted APT intrusions detected and neutralised within minutes. The client achieved full regulatory compliance with ISO 27001 and PCI-DSS within six months.'
)

with open('project/mysepstudio6/index.html', 'w', encoding='utf-8') as f:
    f.write(mysep)

print("Page 3 (Cyber Defense) done.")
print("All 3 sub-pages successfully rebranded!")
