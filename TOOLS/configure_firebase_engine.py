import re

html_path = r'd:\CHIT\MAIN\index.html'
with open(html_path, 'r', encoding='utf-8') as f:
    html = f.read()

# 1. Update Firebase Default URL
old_fb_init = """    function tryInitFirebase() {
      try {
        if (typeof firebase === 'undefined') return;
        let url = localStorage.getItem('chit_firebase_url') || '';
        let config = null;
        if (url) {
          config = { databaseURL: url };
        } else {
          const saved = localStorage.getItem('chit_firebase_config');
          if (saved) {
            try { config = JSON.parse(saved); } catch(e) {}
          }
        }
        if (!config || !config.databaseURL) return;"""

new_fb_init = """    const FIREBASE_DEFAULT_DB_URL = 'https://chitsravan-default-rtdb.firebaseio.com';

    function tryInitFirebase() {
      try {
        if (typeof firebase === 'undefined') return;
        let url = localStorage.getItem('chit_firebase_url') || FIREBASE_DEFAULT_DB_URL;
        let config = { databaseURL: url };"""

assert old_fb_init in html, "Could not find old_fb_init"
html = html.replace(old_fb_init, new_fb_init)

# 2. When Firebase connects, immediately push local data if any, and attach listener
old_listener_attach = """        if (firebase.database) {
          firebaseDb = firebase.database();
          isFirebaseConnected = true;
          attachFirebaseListener();
          const fbBadge = document.getElementById('firebaseStatusBadge');
          if (fbBadge) {
            fbBadge.innerText = '🔥 CONNECTED & ACTIVE';
            fbBadge.style.background = 'rgba(16, 185, 129, 0.3)';
          }
          updateCloudSyncStatusUI(true, "Firebase Connected");
        }"""

new_listener_attach = """        if (firebase.database) {
          firebaseDb = firebase.database();
          isFirebaseConnected = true;
          attachFirebaseListener();
          pushAllLocalToFirebase();
          const fbBadge = document.getElementById('firebaseStatusBadge');
          if (fbBadge) {
            fbBadge.innerText = '🔥 CONNECTED & ACTIVE';
            fbBadge.style.background = 'rgba(16, 185, 129, 0.3)';
          }
          updateCloudSyncStatusUI(true, "Firebase Connected");
        }"""

assert old_listener_attach in html, "Could not find old_listener_attach"
html = html.replace(old_listener_attach, new_listener_attach)

# 3. Add pushAllLocalToFirebase function
push_all_func = """    function pushAllLocalToFirebase() {
      if (!firebaseDb) return;
      try {
        const room = currentSyncRoom || 'chit_family_2026';
        const allData = {};
        for (let i = 0; i < localStorage.length; i++) {
          const k = localStorage.key(i);
          if (k && k.startsWith('chit_tracker_')) {
            try {
              allData[k] = JSON.parse(localStorage.getItem(k));
            } catch (e) {}
          }
        }
        const rName = localStorage.getItem('chit_receiver_name');
        const rPhone = localStorage.getItem('chit_receiver_phonepe');
        if (rName) allData['__receiver_name'] = rName;
        if (rPhone) allData['__receiver_phonepe'] = rPhone;

        if (Object.keys(allData).length > 0) {
          firebaseDb.ref('chit_vault/' + room).update(allData);
        }
      } catch (e) {
        console.warn("Push all error:", e);
      }
    }

    function attachFirebaseListener() {"""

assert "    function attachFirebaseListener() {" in html
html = html.replace("    function attachFirebaseListener() {", push_all_func, 1)

# 4. Make updateCloudSyncStatusUI show Firebase status proudly
old_ui_update = """      if (connected) {
        if (dot) dot.style.background = '#10b981';
        if (title) title.innerHTML = `⚡ Realtime 2-Way Cloud Sync Active!`;
        if (desc) desc.innerText = 'Payments, notes & locks sync between Phone & PC automatically.';
        if (badge) {
          badge.innerText = '✓ LIVE STREAM';
          badge.style.background = 'rgba(16, 185, 129, 0.25)';
          badge.style.color = '#34d399';
          badge.style.borderColor = 'rgba(16, 185, 129, 0.5)';
        }
        if (syncDot) syncDot.style.background = '#10b981';
        if (syncText) syncText.innerText = `☁️ Realtime Cloud: LIVE 🟢`;"""

new_ui_update = """      if (connected) {
        if (dot) dot.style.background = '#10b981';
        if (title) title.innerHTML = `🔥 Google Cloud Database Connected!`;
        if (desc) desc.innerText = 'Live 2-way sync active on Google Cloud • Updates appear across Phone & PC in 30ms';
        if (badge) {
          badge.innerText = '✓ GOOGLE LIVE';
          badge.style.background = 'rgba(16, 185, 129, 0.25)';
          badge.style.color = '#34d399';
          badge.style.borderColor = 'rgba(16, 185, 129, 0.5)';
        }
        if (syncDot) syncDot.style.background = '#10b981';
        if (syncText) syncText.innerText = `🔥 Google Cloud: LIVE 🟢`;"""

assert old_ui_update in html, "Could not find old_ui_update"
html = html.replace(old_ui_update, new_ui_update)

with open(html_path, 'w', encoding='utf-8') as f:
    f.write(html)

print("Successfully configured chitsravan-default-rtdb.firebaseio.com in index.html!")
