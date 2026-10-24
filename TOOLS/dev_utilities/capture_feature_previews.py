import subprocess
import os
import time
from PIL import Image

edge_exe = r'C:\Program Files (x86)\Microsoft\Edge\Application\msedge.exe'
html_path = r'd:\CHIT\MAIN\index.html'
artifacts_dir = r"C:\Users\Sravan Duggi\.gemini\antigravity-ide\brain\80ab0e40-91c0-4aca-9ab1-151489e84b2d"

with open(html_path, 'r', encoding='utf-8') as f:
    orig_html = f.read()

# 1. Desktop Table View with Notes Column & August Month
script1 = '''
<script>
window.addEventListener('load', () => {
    setTimeout(() => {
        switchChit('ganapathi');
        switchMonth(4); // August
        switchView('table');
        setTimeout(() => {
            const inputs = document.querySelectorAll('.member-note-input');
            if (inputs.length > 0) inputs[0].value = "Paid 10k, rem 10k";
            if (inputs.length > 1) inputs[1].value = "GPay done 20k";
            if (inputs.length > 2) inputs[2].value = "Will clear tomorrow";
        }, 300);
    }, 200);
});
</script>
'''
html1 = orig_html.replace('</body>', script1 + '</body>')
temp1 = r'd:\CHIT\WORKSPACE\temp_notes.html'
with open(temp1, 'w', encoding='utf-8') as f:
    f.write(html1)

png1 = os.path.join(artifacts_dir, 'preview_notes_table.png')
jpg1 = os.path.join(artifacts_dir, 'preview_notes_table.jpg')
cmd1 = [
    edge_exe, '--headless', '--disable-gpu', '--force-device-scale-factor=1',
    f'--screenshot={png1}', '--window-size=1280,1100',
    'file:///' + temp1.replace('\\', '/')
]
subprocess.run(cmd1, check=True)
if os.path.exists(png1):
    Image.open(png1).convert('RGB').save(jpg1, 'JPEG', quality=90)
    print("Generated:", jpg1)

# 2. Lock Month Popup Modal
script2 = '''
<script>
window.addEventListener('load', () => {
    setTimeout(() => {
        switchChit('ganapathi');
        switchMonth(4); // August
        openLockModal();
    }, 300);
});
</script>
'''
html2 = orig_html.replace('</body>', script2 + '</body>')
temp2 = r'd:\CHIT\WORKSPACE\temp_lock_popup.html'
with open(temp2, 'w', encoding='utf-8') as f:
    f.write(html2)

png2 = os.path.join(artifacts_dir, 'preview_lock_modal.png')
jpg2 = os.path.join(artifacts_dir, 'preview_lock_modal.jpg')
cmd2 = [
    edge_exe, '--headless', '--disable-gpu', '--force-device-scale-factor=1',
    f'--screenshot={png2}', '--window-size=1280,1050',
    'file:///' + temp2.replace('\\', '/')
]
subprocess.run(cmd2, check=True)
if os.path.exists(png2):
    Image.open(png2).convert('RGB').save(jpg2, 'JPEG', quality=90)
    print("Generated:", jpg2)

# 3. Locked Month Banner & Disabled State
script3 = '''
<script>
window.addEventListener('load', () => {
    setTimeout(() => {
        switchChit('ganapathi');
        switchMonth(4); // August
        const chit = CHITS['ganapathi'];
        const month = chit.months[4];
        const state = loadMonthState('ganapathi', month.key);
        state.__locked = true;
        saveMonthState('ganapathi', month.key, state);
        renderDashboard();
        switchView('table');
    }, 300);
});
</script>
'''
html3 = orig_html.replace('</body>', script3 + '</body>')
temp3 = r'd:\CHIT\WORKSPACE\temp_locked_state.html'
with open(temp3, 'w', encoding='utf-8') as f:
    f.write(html3)

png3 = os.path.join(artifacts_dir, 'preview_locked_state.png')
jpg3 = os.path.join(artifacts_dir, 'preview_locked_state.jpg')
cmd3 = [
    edge_exe, '--headless', '--disable-gpu', '--force-device-scale-factor=1',
    f'--screenshot={png3}', '--window-size=1280,1100',
    'file:///' + temp3.replace('\\', '/')
]
subprocess.run(cmd3, check=True)
if os.path.exists(png3):
    Image.open(png3).convert('RGB').save(jpg3, 'JPEG', quality=90)
    print("Generated:", jpg3)

# 4. Cloud Database & Firebase Sync Modal
script4 = '''
<script>
window.addEventListener('load', () => {
    setTimeout(() => {
        openCloudSyncModal();
    }, 300);
});
</script>
'''
html4 = orig_html.replace('</body>', script4 + '</body>')
temp4 = r'd:\CHIT\WORKSPACE\temp_cloud_modal.html'
with open(temp4, 'w', encoding='utf-8') as f:
    f.write(html4)

png4 = os.path.join(artifacts_dir, 'preview_cloud_modal.png')
jpg4 = os.path.join(artifacts_dir, 'preview_cloud_modal.jpg')
cmd4 = [
    edge_exe, '--headless', '--disable-gpu', '--force-device-scale-factor=1',
    f'--screenshot={png4}', '--window-size=1280,1050',
    'file:///' + temp4.replace('\\', '/')
]
subprocess.run(cmd4, check=True)
if os.path.exists(png4):
    Image.open(png4).convert('RGB').save(jpg4, 'JPEG', quality=90)
    print("Generated:", jpg4)
