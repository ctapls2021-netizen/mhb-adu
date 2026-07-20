import os

# 1. Update HeaderAndHero.astro (Desktop)
hh_path = 'src/components/HeaderAndHero.astro'
with open(hh_path, 'r', encoding='utf-8') as f:
    hh_content = f.read()

old_options = """<option value="conversion">Garage Conversion</option>"""
new_options = """<option value="conversion">Garage Conversion</option>
        <option value="junior">Junior ADU</option>
        <option value="notsure">Not Sure Yet</option>"""

hh_content = hh_content.replace(old_options, new_options)

with open(hh_path, 'w', encoding='utf-8') as f:
    f.write(hh_content)


# 2. Update MobileHeroForm.astro (Mobile)
mh_path = 'src/components/mobile/MobileHeroForm.astro'
with open(mh_path, 'r', encoding='utf-8') as f:
    mh_content = f.read()

# Replace <div id="lead-form"> with <form id="lead-form">
mh_content = mh_content.replace('<div id="lead-form"', '<form id="lead-form"')
mh_content = mh_content.replace('</div>\n', '</form>\n')

# Full Name
mh_content = mh_content.replace(
    '''<div style="width: 400px; height: 48px; border: 1px solid #c3c3c3 !important; border-left: 1px solid #c3c3c3 !important; background-color: #ffffff; border-radius: 0px; margin-bottom: 12px; display: flex; align-items: center; justify-content: center; box-sizing: border-box;">
    <span style="color: #777777; font-family: Inter, sans-serif; font-size: 20px; font-weight: 500;">Full Name</span>
  </div>''',
    '''<input type="text" name="name" placeholder="Full Name" style="width: 400px; height: 48px; border: 1px solid #c3c3c3 !important; background-color: #ffffff; border-radius: 0px; margin-bottom: 12px; box-sizing: border-box; color: #333; font-family: Inter, sans-serif; font-size: 20px; font-weight: 500; text-align: center; outline: none;" required />'''
)

# Phone Number
mh_content = mh_content.replace(
    '''<div style="width: 400px; height: 48px; border: 1px solid #c3c3c3 !important; border-left: 1px solid #c3c3c3 !important; background-color: #ffffff; border-radius: 0px; margin-bottom: 12px; display: flex; align-items: center; justify-content: center; box-sizing: border-box;">
    <span style="color: #777777; font-family: Inter, sans-serif; font-size: 20px; font-weight: 500;">Phone Number</span>
  </div>''',
    '''<input type="tel" name="phone" placeholder="Phone Number" style="width: 400px; height: 48px; border: 1px solid #c3c3c3 !important; background-color: #ffffff; border-radius: 0px; margin-bottom: 12px; box-sizing: border-box; color: #333; font-family: Inter, sans-serif; font-size: 20px; font-weight: 500; text-align: center; outline: none;" required />'''
)

# Zip Code
mh_content = mh_content.replace(
    '''<div style="width: 400px; height: 48px; border: 1px solid #c3c3c3 !important; border-left: 1px solid #c3c3c3 !important; background-color: #ffffff; border-radius: 0px; margin-bottom: 12px; display: flex; align-items: center; justify-content: center; box-sizing: border-box;">
    <span style="color: #777777; font-family: Inter, sans-serif; font-size: 20px; font-weight: 500;">Zip Code</span>
  </div>''',
    '''<input type="text" name="zip" placeholder="Zip Code" style="width: 400px; height: 48px; border: 1px solid #c3c3c3 !important; background-color: #ffffff; border-radius: 0px; margin-bottom: 12px; box-sizing: border-box; color: #333; font-family: Inter, sans-serif; font-size: 20px; font-weight: 500; text-align: center; outline: none;" required />'''
)

# Project Type
mh_content = mh_content.replace(
    '''<div style="width: 400px; height: 48px; border: 1px solid #c3c3c3 !important; border-left: 1px solid #c3c3c3 !important; background-color: #ffffff; border-radius: 0px; margin-bottom: 20px; display: flex; align-items: center; justify-content: center; box-sizing: border-box;">
    <span style="color: #777777; font-family: Inter, sans-serif; font-size: 20px; font-weight: 500;">Project Type</span>
  </div>''',
    '''<div style="position: relative; width: 400px; margin-bottom: 20px;">
    <select name="projectType" style="width: 100%; height: 48px; border: 1px solid #c3c3c3 !important; background-color: #ffffff; border-radius: 0px; box-sizing: border-box; color: #777777; font-family: Inter, sans-serif; font-size: 20px; font-weight: 500; text-align: center; text-align-last: center; appearance: none; outline: none; cursor: pointer;" required>
      <option value="" disabled selected>Project Type</option>
      <option value="detached">Detached ADU</option>
      <option value="attached">Attached ADU</option>
      <option value="conversion">Garage Conversion</option>
      <option value="junior">Junior ADU</option>
      <option value="notsure">Not Sure Yet</option>
    </select>
    <div style="position: absolute; right: 20px; top: 50%; transform: translateY(-50%); pointer-events: none; width: 0; height: 0; border-left: 6px solid transparent; border-right: 6px solid transparent; border-top: 6px solid #777;"></div>
  </div>'''
)

# Submit Button
mh_content = mh_content.replace(
    '''<div style="width: 400px; height: 50px; background-color: #007bc3; border-radius: 0px; display: flex; align-items: center; justify-content: center; cursor: pointer; box-sizing: border-box;">
    <span style="color: #ffffff; font-family: Inter, sans-serif; font-size: 20px; font-weight: 700; text-transform: uppercase; text-align: center;">
      Get My Free ADU Estimate
    </span>
  </div>''',
    '''<button type="submit" style="width: 400px; height: 50px; background-color: #007bc3; border: none; border-radius: 0px; display: flex; align-items: center; justify-content: center; cursor: pointer; box-sizing: border-box; color: #ffffff; font-family: Inter, sans-serif; font-size: 20px; font-weight: 700; text-transform: uppercase;">
    Get My Free ADU Estimate
  </button>'''
)

with open(mh_path, 'w', encoding='utf-8') as f:
    f.write(mh_content)

print('Forms updated successfully!')
