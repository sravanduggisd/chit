import re

with open(r'd:\CHIT\MAIN\index.html', 'r', encoding='utf-8') as f:
    text = f.read()

# 1. Extract all function calls from HTML attributes
event_calls = re.findall(r'(?:onclick|onchange|oninput|onblur)=["\']([^"\']+)["\']', text)
functions_called = set()
for call in event_calls:
    for stmt in call.split(';'):
        stmt = stmt.strip()
        m = re.match(r'([a-zA-Z0-9_]+)\s*\(', stmt)
        if m:
            functions_called.add(m.group(1))

# 2. Extract defined functions
defined_funcs = set(re.findall(r'function\s+([a-zA-Z0-9_]+)\s*\(', text))
defined_vars = set(re.findall(r'(?:const|let|var)\s+([a-zA-Z0-9_]+)\s*=\s*(?:function|\([^)]*\)\s*=>)', text))
all_defined = defined_funcs | defined_vars

missing = functions_called - all_defined
print('All called functions in HTML:', sorted(list(functions_called)))
print('Total defined functions in JS:', len(all_defined))
if missing:
    print('WARNING - MISSING FUNCTIONS:', missing)
else:
    print('SUCCESS: Every single HTML event handler is properly defined!')

# 3. Check for HTML unclosed tags or syntax issues
open_divs = len(re.findall(r'<div\b', text))
close_divs = len(re.findall(r'</div>', text))
print(f'Div balance: <div ({open_divs}) vs </div> ({close_divs})')

# 4. Check Firebase initialization
assert 'https://chitsravan-default-rtdb.firebaseio.com' in text, "Firebase URL missing"
assert 'firebaseDb' in text, "firebaseDb variable missing"
assert 'attachFirebaseListener' in text, "attachFirebaseListener missing"
assert 'toggleHamburgerMenu' in text, "toggleHamburgerMenu missing"
assert 'exportDataBackup' in text, "exportDataBackup missing"
assert 'triggerRestoreBackup' in text, "triggerRestoreBackup missing"
assert 'openResetConfirm' in text, "openResetConfirm missing"

print('All 7 key integration assertions passed 100%!')
