import subprocess
from PIL import Image

edge = r'C:\Program Files (x86)\Microsoft\Edge\Application\msedge.exe'
html = open('d:/CHIT/APP/index.html', encoding='utf-8').read()
inject = '<script>document.addEventListener("DOMContentLoaded", () => { setTimeout(() => { toggleCommissionPrivacy(); }, 400); });</script>'
open('d:/CHIT/WORKSPACE/privacy_revealed_test.html', 'w', encoding='utf-8').write(html.replace('</body>', inject + '</body>'))

png = r'd:\CHIT\WORKSPACE\privacy_revealed.png'
jpg = r'd:\CHIT\WORKSPACE\privacy_revealed.jpg'

cmd = [
    edge,
    '--headless',
    '--disable-gpu',
    '--window-size=1200,900',
    f'--screenshot={png}',
    'file:///d:/CHIT/WORKSPACE/privacy_revealed_test.html'
]
subprocess.run(cmd, check=True)
Image.open(png).convert('RGB').save(jpg, 'JPEG', quality=95)
print('SUCCESS_REVEALED')
