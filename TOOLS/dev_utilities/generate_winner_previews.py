import subprocess
import os
import time
from PIL import Image

edge_exe = r'C:\Program Files (x86)\Microsoft\Edge\Application\msedge.exe'
html_path = r'd:\CHIT\APP\index.html'

with open(html_path, 'r', encoding='utf-8') as f:
    orig_html = f.read()

# 1. Normal View for Ranganadh Chit September
inject_ranganadh = '''
<script>
window.addEventListener('load', () => {
    setTimeout(() => {
        switchChit('ranganadh');
        switchMonth(5); // September
    }, 200);
});
</script>
'''
ranganadh_html = orig_html.replace('</body>', inject_ranganadh + '</body>')
temp_path1 = r'd:\CHIT\WORKSPACE\temp_view1.html'
with open(temp_path1, 'w', encoding='utf-8') as f:
    f.write(ranganadh_html)

png_path1 = r'd:\CHIT\WORKSPACE\dashboard_winner_preview.png'
jpg_path1 = r'd:\CHIT\WORKSPACE\dashboard_winner_preview.jpg'
cmd1 = [
    edge_exe,
    '--headless',
    '--disable-gpu',
    '--force-device-scale-factor=1',
    f'--screenshot={png_path1}',
    '--window-size=1280,1100',
    'file:///' + temp_path1.replace('\\', '/')
]
subprocess.run(cmd1, check=True)
if os.path.exists(png_path1):
    Image.open(png_path1).convert('RGB').save(jpg_path1, 'JPEG', quality=95)
    print("Saved normal view:", jpg_path1)

# 2. Secret Commission Revealed View (Eye clicked)
inject_eye_clicked = '''
<script>
window.addEventListener('load', () => {
    setTimeout(() => {
        switchChit('ranganadh');
        switchMonth(5); // September
        setTimeout(() => {
            toggleSecretCommission();
        }, 300);
    }, 200);
});
</script>
'''
revealed_html = orig_html.replace('</body>', inject_eye_clicked + '</body>')
temp_path2 = r'd:\CHIT\WORKSPACE\temp_view2.html'
with open(temp_path2, 'w', encoding='utf-8') as f:
    f.write(revealed_html)

png_path2 = r'd:\CHIT\WORKSPACE\secret_commission_revealed.png'
jpg_path2 = r'd:\CHIT\WORKSPACE\secret_commission_revealed.jpg'
cmd2 = [
    edge_exe,
    '--headless',
    '--disable-gpu',
    '--force-device-scale-factor=1',
    f'--screenshot={png_path2}',
    '--window-size=1280,1100',
    'file:///' + temp_path2.replace('\\', '/')
]
subprocess.run(cmd2, check=True)
if os.path.exists(png_path2):
    Image.open(png_path2).convert('RGB').save(jpg_path2, 'JPEG', quality=95)
    print("Saved revealed view:", jpg_path2)

# 3. Mobile View (400x850)
png_path3 = r'd:\CHIT\WORKSPACE\mobile_winner_preview.png'
jpg_path3 = r'd:\CHIT\WORKSPACE\mobile_winner_preview.jpg'
cmd3 = [
    edge_exe,
    '--headless',
    '--disable-gpu',
    '--force-device-scale-factor=1',
    f'--screenshot={png_path3}',
    '--window-size=400,900',
    'file:///' + temp_path1.replace('\\', '/')
]
subprocess.run(cmd3, check=True)
if os.path.exists(png_path3):
    Image.open(png_path3).convert('RGB').save(jpg_path3, 'JPEG', quality=95)
    print("Saved mobile view:", jpg_path3)

# Clean up temp files
for p in [temp_path1, temp_path2]:
    if os.path.exists(p): os.remove(p)

print("ALL_PREVIEWS_GENERATED_SUCCESSFULLY")
