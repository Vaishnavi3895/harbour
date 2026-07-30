import glob

files = ['index.html'] + glob.glob('pages/*.html')
old = '<meta name="viewport" content="width=device-width, initial-scale=1.0">'
new = '<meta name="viewport" content="width=device-width, initial-scale=1.0, viewport-fit=cover">'

for path in files:
    with open(path, 'r', encoding='utf-8') as f:
        content = f.read()
    if old not in content:
        print('SKIP (not found):', path)
        continue
    content = content.replace(old, new, 1)
    with open(path, 'w', encoding='utf-8') as f:
        f.write(content)
    print('Fixed:', path)
