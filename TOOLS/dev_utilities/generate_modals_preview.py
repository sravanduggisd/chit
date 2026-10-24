import subprocess
import os
from PIL import Image

edge_exe = r'C:\Program Files (x86)\Microsoft\Edge\Application\msedge.exe'
artifacts_dir = r"C:\Users\Sravan Duggi\.gemini\antigravity-ide\brain\80ab0e40-91c0-4aca-9ab1-151489e84b2d"

with open(r'd:\CHIT\MAIN\index.html', 'r', encoding='utf-8') as f:
    h = f.read()

# 3. Locked Banner State Preview
h_locked_state = h.replace('id="lockedMonthBanner" style="display: none;"', 'id="lockedMonthBanner" style="display: flex !important;"')
h_locked_state = h_locked_state.replace('id="btnLockMonth" onclick="openLockModal()" title="Lock month when settlement is closed to prevent accidental edits">\n          🔒 Lock Month', 'id="btnLockMonth" class="btn btn-warning" onclick="openLockModal()">\n          🔓 Unlock Month')

temp_banner = r'd:\CHIT\WORKSPACE\snap_banner.html'
with open(temp_banner, 'w', encoding='utf-8') as f:
    f.write(h_locked_state)

png_banner = os.path.join(artifacts_dir, 'preview_locked_state.png')
jpg_banner = os.path.join(artifacts_dir, 'preview_locked_state.jpg')
subprocess.run([edge_exe, '--headless', '--disable-gpu', '--force-device-scale-factor=1', f'--screenshot={png_banner}', '--window-size=1280,950', 'file:///' + temp_banner.replace('\\', '/')], check=True)
if os.path.exists(png_banner):
    Image.open(png_banner).convert('RGB').save(jpg_banner, 'JPEG', quality=92)
    print("Saved locked state banner:", jpg_banner)
