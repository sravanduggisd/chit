import subprocess
import os
from PIL import Image

edge_exe = r'C:\Program Files (x86)\Microsoft\Edge\Application\msedge.exe'
html_path = r'd:/CHIT/APP/index.html'

# 1. Normal View for Ranganadh Chit September (Winner: Supraja, Payout ₹ 3,15,000)
url1 = f'file:///{html_path}?chit=ranganadh&month=1'
png_path1 = r'd:\CHIT\WORKSPACE\ranganadh_winner_box.png'
jpg_path1 = r'd:\CHIT\WORKSPACE\ranganadh_winner_box.jpg'
cmd1 = [
    edge_exe,
    '--headless',
    '--disable-gpu',
    '--force-device-scale-factor=1',
    f'--screenshot={png_path1}',
    '--window-size=1280,1100',
    url1
]
subprocess.run(cmd1, check=True)
if os.path.exists(png_path1):
    Image.open(png_path1).convert('RGB').save(jpg_path1, 'JPEG', quality=95)
    print("Saved Ranganadh Winner Box:", jpg_path1)

# 2. Secret Commission Revealed View (Secret Popover Open)
url2 = f'file:///{html_path}?chit=ranganadh&month=1&secret=1'
png_path2 = r'd:\CHIT\WORKSPACE\ranganadh_commission_revealed.png'
jpg_path2 = r'd:\CHIT\WORKSPACE\ranganadh_commission_revealed.jpg'
cmd2 = [
    edge_exe,
    '--headless',
    '--disable-gpu',
    '--force-device-scale-factor=1',
    f'--screenshot={png_path2}',
    '--window-size=1280,1100',
    url2
]
subprocess.run(cmd2, check=True)
if os.path.exists(png_path2):
    Image.open(png_path2).convert('RGB').save(jpg_path2, 'JPEG', quality=95)
    print("Saved Ranganadh Commission Revealed:", jpg_path2)

# 3. Mobile View of Ranganadh Chit September (Cards View)
png_path3 = r'd:\CHIT\WORKSPACE\ranganadh_mobile_winner.png'
jpg_path3 = r'd:\CHIT\WORKSPACE\ranganadh_mobile_winner.jpg'
cmd3 = [
    edge_exe,
    '--headless',
    '--disable-gpu',
    '--force-device-scale-factor=1',
    f'--screenshot={png_path3}',
    '--window-size=412,915',
    url1
]
subprocess.run(cmd3, check=True)
if os.path.exists(png_path3):
    Image.open(png_path3).convert('RGB').save(jpg_path3, 'JPEG', quality=95)
    print("Saved Ranganadh Mobile Winner:", jpg_path3)

print("PREVIEWS_GENERATED_SUCCESSFULLY")
