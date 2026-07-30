import re

# Exact rules found via audit — replacing only the font-size value within
# each specific input/select/textarea rule, nothing else in the rule.
fixes = [
    ('pages/bucketlist.html', '.modal input{ width:100%; padding:9px 10px; border:1px solid #E9D8DC; background:#fff; font-size:13px;',
                               '.modal input{ width:100%; padding:9px 10px; border:1px solid #E9D8DC; background:#fff; font-size:16px;'),
    ('pages/budget.html', '.modal input, .modal select{ width:100%; padding:9px 10px; border:1px solid #E9E1DA; border-radius:8px; font-size:12px;',
                           '.modal input, .modal select{ width:100%; padding:9px 10px; border:1px solid #E9E1DA; border-radius:8px; font-size:16px;'),
    ('pages/budget.html', '.converter-row input{ flex:1; padding:9px 10px; border:1px solid #E9E1DA; border-radius:8px; font-size:12px;',
                           '.converter-row input{ flex:1; padding:9px 10px; border:1px solid #E9E1DA; border-radius:8px; font-size:16px;'),
    ('pages/budget.html', '.converter-row select{ padding:9px 8px; border:1px solid #E9E1DA; border-radius:8px; font-size:12px;',
                           '.converter-row select{ padding:9px 8px; border:1px solid #E9E1DA; border-radius:8px; font-size:16px;'),
    ('pages/faq.html', '.modal input,.modal textarea{ width:100%; padding:9px 10px; border:1px solid #E9E1DA; border-radius:8px; font-size:12px;',
                        '.modal input,.modal textarea{ width:100%; padding:9px 10px; border:1px solid #E9E1DA; border-radius:8px; font-size:16px;'),
    ('pages/home.html', '.setup-card input{ padding:10px 12px; border:1px solid #E9E1DA; border-radius:10px; font-size:13px;',
                         '.setup-card input{ padding:10px 12px; border:1px solid #E9E1DA; border-radius:10px; font-size:16px;'),
    ('pages/home.html', '.chat-input-row input{ flex:1; padding:10px 12px; border:1px solid #E9E1DA; border-radius:10px; font-size:13px;',
                         '.chat-input-row input{ flex:1; padding:10px 12px; border:1px solid #E9E1DA; border-radius:10px; font-size:16px;'),
    ('pages/trip.html', '.input-row input{ flex:1; padding:9px 12px; border:1px solid #E9E1DA; border-radius:20px; font-size:12.5px;',
                         '.input-row input{ flex:1; padding:9px 12px; border:1px solid #E9E1DA; border-radius:20px; font-size:16px;'),
    ('pages/trip.html', '.modal input{ width:100%; padding:9px 10px; border:1px solid #E9E1DA; border-radius:8px; font-size:12px;',
                         '.modal input{ width:100%; padding:9px 10px; border:1px solid #E9E1DA; border-radius:8px; font-size:16px;'),
    ('pages/trip.html', 'select{ width:100%; padding:9px 10px; border:1px solid #E9E1DA; border-radius:8px; font-size:12px;',
                         'select{ width:100%; padding:9px 10px; border:1px solid #E9E1DA; border-radius:8px; font-size:16px;'),
    ('pages/wallet.html', '.modal input{ width:100%; padding:9px 10px; border:1px solid #E9E1DA; border-radius:8px; font-size:12px;',
                           '.modal input{ width:100%; padding:9px 10px; border:1px solid #E9E1DA; border-radius:8px; font-size:16px;'),
    ('pages/todo.html', '.add-item-row input{ flex:1; padding:8px 10px; border:1px solid #E9E1DA; border-radius:8px; font-size:11.5px;',
                         '.add-item-row input{ flex:1; padding:8px 10px; border:1px solid #E9E1DA; border-radius:8px; font-size:16px;'),
]

for path, old, new in fixes:
    with open(path, 'r', encoding='utf-8') as f:
        content = f.read()
    if old not in content:
        print('NOT FOUND in', path, '->', old[:60])
        continue
    content = content.replace(old, new, 1)
    with open(path, 'w', encoding='utf-8') as f:
        f.write(content)
    print('Fixed:', path)
