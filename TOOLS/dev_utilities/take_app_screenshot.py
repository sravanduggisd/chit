import subprocess
import os
from PIL import Image

edge_exe = r'C:\Program Files (x86)\Microsoft\Edge\Application\msedge.exe'
html_path = r'd:\CHIT\APP\index.html'
png_path = r'd:\CHIT\WORKSPACE\app_preview.png'
jpg_path = r'd:\CHIT\WORKSPACE\app_preview.jpg'

url = 'file:///' + html_path.replace('\\', '/')
cmd = [
    edge_exe,
    '--headless',
    '--disable-gpu',
    '--force-device-scale-factor=1',
    f'--screenshot={png_path}',
    '--window-size=1280,1100',
    url
]
subprocess.run(cmd, check=True)
print('Screenshot generated:', os.path.exists(png_path))

if os.path.exists(png_path):
    img = Image.open(png_path)
    img.convert('RGB').save(jpg_path, 'JPEG', quality=95)
    print('JPG saved:', jpg_path)
