with open(r'd:\CHIT\MAIN\index.html', 'r', encoding='utf-8') as f:
    text = f.read()

import re
m = re.search(r'id=["\']cloudSyncModal["\']', text)
if m:
    line_no = text[:m.start()].count('\n') + 1
    print('cloudSyncModal line:', line_no)
    lines = text.splitlines()
    print('\n'.join(lines[line_no-1:line_no+65]))
