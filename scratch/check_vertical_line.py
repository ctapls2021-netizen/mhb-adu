path_proc = 'src/components/Process.astro'
with open(path_proc, 'r', encoding='utf-8') as f:
    c = f.read()

# Fix See If I Qualify in Process.astro
old_q = '<div class="css-bz2tic css-o2k3h2">'
new_q = '<div class="css-bz2tic css-o2k3h2" data-cta="form" style="cursor: pointer !important;">'
c = c.replace(old_q, new_q)

# Remove outer <a> tag from Check My Property in Process.astro
old_c = '<a href="#estimate" style="text-decoration: none; cursor: pointer;"><div class="css-bz2tic css-orhuyv" data-cta="form" style="cursor: pointer;"><div class="css-5u23lp css-roiesn css-rqi8kd"></div><div class="css-ys5lqv css-x7xdan css-8zrmd9 css-caq160 textContents" style="display: flex !important; flex-direction: row !important; align-items: center !important; justify-content: center !important; gap: 14px !important; width: max-content !important; height: 91px !important; top: 6399px !important; left: 50% !important; transform: translateX(-50%) !important; z-index: 50;"><img src="/images/icon-qualify-white.svg" style="width: 33px; height: 33px; flex-shrink: 0;" alt=""/><p style="margin: 0; padding: 0; white-space: nowrap !important; text-align: center;"><span style="color: #FFF; font-family: Inter, sans-serif; font-size: 22px; font-style: normal; font-weight: 600; line-height: 26px;">Check My Property\'s ADU Eligibility - </span><span style="color: #FFF; font-family: Inter, sans-serif; font-size: 22px; font-style: italic; font-weight: 800; line-height: 26px;">It\'s Free</span></p></div></div></a>'

new_c = '<div class="css-bz2tic css-orhuyv" data-cta="form" style="cursor: pointer !important;"><div class="css-5u23lp css-roiesn css-rqi8kd"></div><div class="css-ys5lqv css-x7xdan css-8zrmd9 css-caq160 textContents" style="display: flex !important; flex-direction: row !important; align-items: center !important; justify-content: center !important; gap: 14px !important; width: max-content !important; height: 91px !important; top: 6399px !important; left: 50% !important; transform: translateX(-50%) !important; z-index: 50; cursor: pointer !important;"><img src="/images/icon-qualify-white.svg" style="width: 33px; height: 33px; flex-shrink: 0;" alt=""/><p style="margin: 0; padding: 0; white-space: nowrap !important; text-align: center; cursor: pointer !important;"><span style="color: #FFF; font-family: Inter, sans-serif; font-size: 22px; font-style: normal; font-weight: 600; line-height: 26px;">Check My Property\'s ADU Eligibility - </span><span style="color: #FFF; font-family: Inter, sans-serif; font-size: 22px; font-style: italic; font-weight: 800; line-height: 26px;">It\'s Free</span></p></div></div>'

c = c.replace(old_c, new_c)

with open(path_proc, 'w', encoding='utf-8') as f:
    f.write(c)

print("Process.astro cleaned and fixed successfully!")
