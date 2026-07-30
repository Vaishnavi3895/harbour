import json

# frameKey is what actually gets a unique iframe — Brainstorm and The Plan
# share 'trip' so shortlist state stays connected between them.
page_files = {
    'home': 'pages/home.html',
    'trip': 'pages/trip.html',
    'todo': 'pages/todo.html',
    'wallet': 'pages/wallet.html',
    'budget': 'pages/budget.html',
    'faq': 'pages/faq.html',
    'bucketlist': 'pages/bucketlist.html',
    'profile': 'pages/profile.html',
    'following': 'pages/following.html',
}

contents = {}
for key, path in page_files.items():
    with open(path, 'r', encoding='utf-8') as f:
        contents[key] = f.read()

with open('index.html', 'r', encoding='utf-8') as f:
    shell = f.read()

js_map_entries = []
for key, html in contents.items():
    encoded = json.dumps(html)
    encoded = encoded.replace('</script', '<\\/script')  # prevent premature outer </script> close
    js_map_entries.append(json.dumps(key) + ': ' + encoded)
js_map = '{\n' + ',\n'.join(js_map_entries) + '\n}'

# srcdoc instead of src — same shared-instance-by-frameKey logic as index.html,
# postMessage still works fine across srcdoc iframes (same-origin by default).
# tripScoped pages can't read a URL query param from srcdoc (there's no real
# URL), so we prepend a tiny script that sets window.__PRESET_TRIP_TYPE —
# the same fallback hook added to trip/todo/wallet/budget.html — using the
# shell's actual currentTripType at the moment the frame is created.
shell = shell.replace(
    "const f = document.createElement('iframe');\n    f.src = buildSrc(tab);",
    "const f = document.createElement('iframe');\n    const presetScript = tab.tripScoped && currentTripType ? '<script>window.__PRESET_TRIP_TYPE=\"'+currentTripType+'\";<\\/script>' : '';\n    f.srcdoc = presetScript + PAGE_CONTENT[key];"
)
shell = shell.replace(
    "const tabs = [",
    "const PAGE_CONTENT = " + js_map + ";\nconst tabs = ["
)

with open('preview.html', 'w', encoding='utf-8') as f:
    f.write(shell)

print("Built preview.html —", len(shell), "bytes")
