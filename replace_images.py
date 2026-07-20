import os
import re

comps_dir = r'c:\Users\Diego\Downloads\Agente Ayrton\Agente creador de web\astro_site\src\components'

# Exact string replacements for known image tags based on extracted sizes and contexts
# We will use re.sub on the content of the files.
# For multiple instances of the same hash (like ADUTypes), we will replace them sequentially.

replacements = {
    'ADUTypes.astro': [
        # Detached ADU is 68ee8daa
        (r'/index Adu_files/68ee8daa4b4f07cd9c7fdae5cdba562f009d56f8.png', '/images/Detached ADU.png'),
        # Above-Garage ADU is 33b1e841
        (r'/index Adu_files/33b1e841b8892abbec41e0e129c52fe6a745adea.png', '/images/Above-Garage ADU.png'),
        # Two-Story ADU is e01bf69b but wait, there are many e01bf69b. Let's map it based on order.
        # Attached, Garage, JADU use 7c110fe7.
    ],
    'HeaderAndHero.astro': [
        (r'/index Adu_files/2fb779fabc00a002a183c69724fe58cc4df65a88.png', '/images/Los Angeles ADU Builders.webp'),
    ],
    'Process.astro': [
        (r'/index Adu_files/9b939839ff80178263170408151d8b52c5447381.png', '/images/Not sure which type fits your property.webp'),
        (r'/index Adu_files/3bb93d8ae3460faf1a5e816ded8479deacee189e.svg', '/images/See If I Qualify for 0% Financing.svg'),
        # Gallery images
        (r'/index Adu_files/f01095a3a26e2ca352ac40ea5a1d5f44cce4aaf9.png', '/images/Reseda, CA.jpg'),
        (r'/index Adu_files/2162cd77ea296ccbf8c86db05f96cc21197ec27c.png', '/images/Sherman Oaks.jpg'),
        (r'/index Adu_files/3b15f2c6eaae78c283d06ff561b47392f0abe2f1.png', '/images/Studio City.jpg'),
        (r'/index Adu_files/00e4534258f32ed0560a5e11eaf4ac6aa637ade2.png', '/images/Woodland Hills, CA.jpg'),
    ],
    'TestimonialsAndFooter.astro': [
        (r'/index Adu_files/d11e208b0bdde5cd7ed59e71737af8d6475456aa.png', '/images/Ready to Unlock Your Property Hidden Potential.webp'),
        (r'/index Adu_files/8011cbdde3d80edff0505d503ddc8d3c20c4389d.svg', '/images/google.svg'),
        (r'/index Adu_files/0bd7b0f330cbb53917847311d23015f7400e9e67.svg', '/images/Just Take Our Word For It..png'),
    ],
    'WhyChooseUs.astro': [
        (r'/index Adu_files/12152694e89d57a645f69630ce30dfbcc7dce633.png', '/images/Fully Licensed & Insured.png'),
        (r'/index Adu_files/a2ac1660928341d2a544d272f62b9156e3648e46.png', '/images/Iron-Clad Fixed Pricing.png'),
        (r'/index Adu_files/346e77b44feb524f58e355dd6bf04dcbae626ba6.png', '/images/Dedicated Project Manager.png'),
    ]
}

# For 7c110fe7, we will replace sequentially in ADUTypes.astro
adu_types_seq = ['/images/Attached ADU.png', '/images/Garage Conversion.png', '/images/JADU.png']

# For eb5eb0c4 (5 icons) in Process.astro
proc_icons_seq = [
    '/images/Speed to Completion.png', 
    '/images/Permit Experts.png',
    '/images/Everything Under One Roof.png',
    '/images/Free 3D Design Rendering.png',
    '/images/25+ Years of Local Experience.png'
]

# For 8fc2e45a (4 icons) in Process.astro
proc_icons_2 = [
    '/images/Generate Rental Income.png',
    '/images/Keep Family Close.png',
    '/images/Boost Property Value.png',
    '/images/The Ultimate Home Office.png'
]

# For e01bf69b in ADUTypes.astro
# For 22e194fc in Process.astro

for file in os.listdir(comps_dir):
    if not file.endswith('.astro'): continue
    path = os.path.join(comps_dir, file)
    with open(path, 'r', encoding='utf-8') as f:
        content = f.read()
    
    # Apply standard replacements
    if file in replacements:
        for old, new in replacements[file]:
            content = re.sub(old, new, content)
            
    # Apply sequential replacements
    if file == 'ADUTypes.astro':
        for rep in adu_types_seq:
            content = re.sub(r'/index Adu_files/7c110fe76c38e1bc5d8672c2900f33c368eac93f.png', rep, content, count=1)
    
    if file == 'Process.astro':
        for rep in proc_icons_seq:
            content = re.sub(r'/index Adu_files/eb5eb0c4c101746bb231c9308e10427bb935299f.png', rep, content, count=1)
        for rep in proc_icons_2:
            content = re.sub(r'/index Adu_files/8fc2e45a827f35093be9bdfb939c1ae2c3eb10a2.png', rep, content, count=1)
            
    # Remove srcset globally so new images are forced
    content = re.sub(r'srcset=[\"\'][^\"\']+[\"\']', '', content)
    
    with open(path, 'w', encoding='utf-8') as f:
        f.write(content)

print('Replaced known images successfully.')
