with open(r'd:\CHIT\MAIN\index.html', 'r', encoding='utf-8') as f:
    text = f.read()

import re

# 1. Check catch around btn.innerText
for m in re.finditer(r'catch\s*\(.*?\)\s*\{[^}]*btn\.innerText', text):
    start = text[:m.start()].count('\n') + 1
    print("Found btn catch at line:", start, m.group(0))

# 2. Check chit keys in CHITS
chits_match = re.search(r'const CHITS\s*=\s*(\{.*?\n    \};)', text, re.DOTALL)
if chits_match:
    keys = re.findall(r'(\w+):\s*\{\s*id:\s*[\'"](\w+)[\'"]', chits_match.group(1))
    print("CHITS keys:", keys)

# 3. Check paid amount calculation in renderDashboard
for line in text.splitlines():
    if 'statPaid' in line or 'paidAmount' in line or 'paidCount' in line:
        if any(w in line for w in ['=', '*', '+']):
            print("Paid calculation line:", line.strip())

# 4. Check exportDataBackup
for m in re.finditer(r'function exportDataBackup.*?\n    \}', text, re.DOTALL):
    print("exportDataBackup:", m.group(0))

# 5. Check commEyeBadge / commission reveal
for line in text.splitlines():
    if 'commEye' in line or 'statCommission' in line or 'Commission' in line:
        if 'onclick' in line or 'function' in line or 'let ' in line:
            print("Commission line:", line.strip())
