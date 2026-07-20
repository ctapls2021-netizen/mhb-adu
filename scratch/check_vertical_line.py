import os
import re

# Update Process.astro
path_proc = 'src/components/Process.astro'
with open(path_proc, 'r', encoding='utf-8') as f:
    c_proc = f.read()

# Add data-cta="form" and cursor: pointer to See If I Qualify
c_proc = c_proc.replace('See If I Qualify for 0% Financing', 'See If I Qualify for 0% Financing')
# Ensure css-h7jh0h and css-orhuyv have cursor: pointer and data-cta="form"
c_proc = c_proc.replace('class="css-bz2tic css-h7jh0h"', 'class="css-bz2tic css-h7jh0h" data-cta="form" style="cursor: pointer;"')
c_proc = c_proc.replace('class="css-bz2tic css-orhuyv"', 'class="css-bz2tic css-orhuyv" data-cta="form" style="cursor: pointer;"')

with open(path_proc, 'w', encoding='utf-8') as f:
    f.write(c_proc)
print("Updated Process.astro with data-cta='form'")

# Update MobileADUEligibilityCTA.astro
path_elig = 'src/components/mobile/MobileADUEligibilityCTA.astro'
with open(path_elig, 'r', encoding='utf-8') as f:
    c_elig = f.read()

c_elig = c_elig.replace(
    'See If I Qualify for 0% Financing',
    'See If I Qualify for 0% Financing'
)
# Add data-cta="form" to both top bar and bottom button
c_elig = re.sub(r'(<a [^>]*href="#lead-form"[^>]*>)', r'\1', c_elig)
c_elig = c_elig.replace('background-color: #000000;', 'background-color: #000000; cursor: pointer;')

with open(path_elig, 'w', encoding='utf-8') as f:
    f.write(c_elig)
print("Updated MobileADUEligibilityCTA.astro")

# Update MobileBottomCTA.astro
path_bot = 'src/components/mobile/MobileBottomCTA.astro'
with open(path_bot, 'r', encoding='utf-8') as f:
    c_bot = f.read()

c_bot = c_bot.replace('background-color: #007BC3;', 'background-color: #007BC3; cursor: pointer;')

with open(path_bot, 'w', encoding='utf-8') as f:
    f.write(c_bot)
print("Updated MobileBottomCTA.astro")
