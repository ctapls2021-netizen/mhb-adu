import os
import re

# Update MobileADUEligibilityCTA.astro
path_elig = 'src/components/mobile/MobileADUEligibilityCTA.astro'
with open(path_elig, 'r', encoding='utf-8') as f:
    c_elig = f.read()

c_elig = c_elig.replace(
    '<div style="width: 480px; height: 50px; background-color: #000000; display: flex; align-items: center; justify-content: center; gap: 10px; box-sizing: border-box;">',
    '<a href="#lead-form" style="width: 480px; height: 50px; background-color: #000000; display: flex; align-items: center; justify-content: center; gap: 10px; box-sizing: border-box; text-decoration: none; cursor: pointer;">'
).replace(
    '</span>\n  </div>',
    '</span>\n  </a>'
)

with open(path_elig, 'w', encoding='utf-8') as f:
    f.write(c_elig)
print("Updated MobileADUEligibilityCTA.astro")

# Update MobileBottomCTA.astro
path_bot = 'src/components/mobile/MobileBottomCTA.astro'
with open(path_bot, 'r', encoding='utf-8') as f:
    c_bot = f.read()

c_bot = c_bot.replace(
    '<div style="width: 480px; height: 50px; background-color: #007BC3; display: flex; align-items: center; justify-content: center; gap: 10px; box-sizing: border-box;">',
    '<a href="#lead-form" style="width: 480px; height: 50px; background-color: #007BC3; display: flex; align-items: center; justify-content: center; gap: 10px; box-sizing: border-box; text-decoration: none; cursor: pointer;">'
).replace(
    '</span>\n  </div>',
    '</span>\n  </a>'
)

with open(path_bot, 'w', encoding='utf-8') as f:
    f.write(c_bot)
print("Updated MobileBottomCTA.astro")

# Update Process.astro (Desktop)
path_proc = 'src/components/Process.astro'
with open(path_proc, 'r', encoding='utf-8') as f:
    c_proc = f.read()

# Wrap See If I Qualify in Process.astro
old_q = '<div class="css-bz2tic css-h7jh0h"><div class="css-nit1yh css-roiesn css-bo4u3g"></div><div class="css-h7jh0h css-lla91 css-8zrmd9 css-tsm8h9 textContents" style="display: flex !important; flex-direction: row !important; align-items: center !important; justify-content: center !important; gap: 14px !important; width: max-content !important; height: 62px !important; top: 5539px !important; left: 50% !important; transform: translateX(-50%) !important; z-index: 50;"><img src="/images/icon-qualify.svg" style="width: 33px; height: 33px; flex-shrink: 0;" alt=""/><p class="css-8zr56v css-304kt4" style="margin: 0; padding: 0; white-space: nowrap !important; color: #FFF; text-align: center; font-family: Montserrat, sans-serif; font-size: 22px; font-weight: 600; line-height: 41px;">See If I Qualify for 0% Financing</p></div></div>'

new_q = '<a href="#estimate" style="text-decoration: none; cursor: pointer;"><div class="css-bz2tic css-h7jh0h"><div class="css-nit1yh css-roiesn css-bo4u3g"></div><div class="css-h7jh0h css-lla91 css-8zrmd9 css-tsm8h9 textContents" style="display: flex !important; flex-direction: row !important; align-items: center !important; justify-content: center !important; gap: 14px !important; width: max-content !important; height: 62px !important; top: 5539px !important; left: 50% !important; transform: translateX(-50%) !important; z-index: 50;"><img src="/images/icon-qualify.svg" style="width: 33px; height: 33px; flex-shrink: 0;" alt=""/><p class="css-8zr56v css-304kt4" style="margin: 0; padding: 0; white-space: nowrap !important; color: #FFF; text-align: center; font-family: Montserrat, sans-serif; font-size: 22px; font-weight: 600; line-height: 41px;">See If I Qualify for 0% Financing</p></div></div></a>'

# Wrap Check My Property in Process.astro
old_c = '<div class="css-bz2tic css-orhuyv"><div class="css-5u23lp css-roiesn css-rqi8kd"></div><div class="css-ys5lqv css-x7xdan css-8zrmd9 css-caq160 textContents" style="display: flex !important; flex-direction: row !important; align-items: center !important; justify-content: center !important; gap: 14px !important; width: max-content !important; height: 91px !important; top: 6399px !important; left: 50% !important; transform: translateX(-50%) !important; z-index: 50;"><img src="/images/icon-qualify-white.svg" style="width: 33px; height: 33px; flex-shrink: 0;" alt=""/><p style="margin: 0; padding: 0; white-space: nowrap !important; text-align: center;"><span style="color: #FFF; font-family: Inter, sans-serif; font-size: 22px; font-style: normal; font-weight: 600; line-height: 26px;">Check My Property\'s ADU Eligibility - </span><span style="color: #FFF; font-family: Inter, sans-serif; font-size: 22px; font-style: italic; font-weight: 800; line-height: 26px;">It\'s Free</span></p></div></div>'

new_c = '<a href="#estimate" style="text-decoration: none; cursor: pointer;"><div class="css-bz2tic css-orhuyv"><div class="css-5u23lp css-roiesn css-rqi8kd"></div><div class="css-ys5lqv css-x7xdan css-8zrmd9 css-caq160 textContents" style="display: flex !important; flex-direction: row !important; align-items: center !important; justify-content: center !important; gap: 14px !important; width: max-content !important; height: 91px !important; top: 6399px !important; left: 50% !important; transform: translateX(-50%) !important; z-index: 50;"><img src="/images/icon-qualify-white.svg" style="width: 33px; height: 33px; flex-shrink: 0;" alt=""/><p style="margin: 0; padding: 0; white-space: nowrap !important; text-align: center;"><span style="color: #FFF; font-family: Inter, sans-serif; font-size: 22px; font-style: normal; font-weight: 600; line-height: 26px;">Check My Property\'s ADU Eligibility - </span><span style="color: #FFF; font-family: Inter, sans-serif; font-size: 22px; font-style: italic; font-weight: 800; line-height: 26px;">It\'s Free</span></p></div></div></a>'

c_proc = c_proc.replace(old_q, new_q).replace(old_c, new_c)

with open(path_proc, 'w', encoding='utf-8') as f:
    f.write(c_proc)
print("Updated Process.astro")
