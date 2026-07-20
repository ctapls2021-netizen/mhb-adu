with open('src/components/Process.astro', 'r', encoding='utf-8') as f:
    c = f.read()

# Replace line-height: 32px with line-height: 20px for the Inter font spans (City names)
old_style = "font-family: 'Inter', sans-serif; font-size: 20px; font-weight: 400; line-height: 32px;"
new_style = "font-family: 'Inter', sans-serif; font-size: 20px; font-weight: 400; line-height: 20px;"

c = c.replace(old_style, new_style)

with open('src/components/Process.astro', 'w', encoding='utf-8') as f:
    f.write(c)

print('Updated font styles successfully!')
