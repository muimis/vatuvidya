import re
with open(r'c:\Users\Beginow_10\Downloads\vasthu\vastu-vidya-homes-brand-guide.html', 'r', encoding='utf-8') as f:
    html = f.read()

pattern = r'<svg[^>]*>[\s\S]*?</svg>'
def repl(m):
    content = m.group(0)
    if '<polyline points="10,15 95,180 180,15"' in content:
        class_match = re.search(r'class="([^"]+)"', content)
        class_str = f' class="{class_match.group(1)}"' if class_match else ''
        style_match = re.search(r'style="([^"]+)"', content)
        style_str = f' style="{style_match.group(1)}"' if style_match else ''
        
        # Determine the image name based on the lockup class or default to logo
        # The user has "vasthu logo.svg" and "vasthu logo.png"
        return f'<img src="vasthu%20logo.svg"{class_str}{style_str} alt="Vastu Vidya Homes Logo">'
    return content

new_html = re.sub(pattern, repl, html)

with open(r'c:\Users\Beginow_10\Downloads\vasthu\vastu-vidya-homes-brand-guide.html', 'w', encoding='utf-8') as f:
    f.write(new_html)
