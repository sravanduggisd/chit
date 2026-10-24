import re

html_path = r'd:\CHIT\MAIN\index.html'
with open(html_path, 'r', encoding='utf-8') as f:
    html = f.read()

# 1. Add Firebase input card into cloudSyncModal
old_modal_section = """        <!-- Instant Sync Test -->
        <div style="display: flex; justify-content: space-between; align-items: center; background: rgba(0, 0, 0, 0.28); border: 1px solid var(--border-color); border-radius: var(--radius-md); padding: 12px 14px;">"""

new_modal_section = """        <!-- Google Firebase Realtime Database (100% Free Forever, Zero Rate Limits) -->
        <div style="background: rgba(16, 185, 129, 0.08); border: 1px solid rgba(16, 185, 129, 0.3); border-radius: var(--radius-md); padding: 14px;">
          <div style="display: flex; justify-content: space-between; align-items: center; margin-bottom: 6px;">
            <strong style="color: #34d399; font-size: 13px;">🔥 Google Firebase Cloud Database (Permanent & 100% Free):</strong>
            <span id="firebaseStatusBadge" style="font-size: 10px; font-weight: 700; padding: 2px 7px; border-radius: 4px; background: rgba(16, 185, 129, 0.2); color: #34d399;">Recommended</span>
          </div>
          <p style="font-size: 11.5px; color: var(--text-secondary); margin-bottom: 8px; line-height: 1.4;">
            Google Firebase provides permanent instant 2-way sync with <strong>zero rate limits</strong>. Enter your database URL below:
          </p>
          <div style="display: flex; gap: 8px;">
            <input type="text" id="firebaseUrlInput" placeholder="e.g. https://your-app-default-rtdb.firebaseio.com" style="flex: 1; background: #0b0f19; border: 1px solid var(--border-color); color: white; padding: 8px 10px; border-radius: 6px; font-size: 11.5px; outline: none;" />
            <button class="btn btn-primary" onclick="saveFirebaseDatabaseUrl()" style="font-size: 11px; padding: 6px 12px; white-space: nowrap;">Connect Firebase</button>
          </div>
          <div style="font-size: 11px; color: #94a3b8; margin-top: 8px; line-height: 1.4;">
            💡 <strong>1-Minute Free Setup:</strong> Open <a href="https://console.firebase.google.com" target="_blank" style="color: #60a5fa; text-decoration: underline; font-weight: 600;">console.firebase.google.com</a> &rarr; Create Project &rarr; Realtime Database &rarr; Start in Test Mode &rarr; Copy the URL here!
          </div>
        </div>

        <!-- Instant Sync Test -->
        <div style="display: flex; justify-content: space-between; align-items: center; background: rgba(0, 0, 0, 0.28); border: 1px solid var(--border-color); border-radius: var(--radius-md); padding: 12px 14px;">"""

assert old_modal_section in html, "Could not find old_modal_section"
html = html.replace(old_modal_section, new_modal_section)

# 2. Update polling removal & Firebase enhancements
old_sync_logic = """    function initRealtimeCloudSync() {
      // 1. Connect instant live SSE event stream
      connectRealtimeStream();

      // 2. Check if local device has data (e.g. PC with 11/12 paid)
      let hasLocalData = false;
      for (let i = 0; i < localStorage.length; i++) {
        const k = localStorage.key(i);
        if (k && k.startsWith('chit_tracker_')) {
          hasLocalData = true;
          break;
        }
      }

      if (hasLocalData) {
        pushRealtimeCloudData();
      } else {
        pullRealtimeCloudData();
      }

      // 3. Fallback poll every 2.5 seconds
      if (!cloudSyncInterval) {
        cloudSyncInterval = setInterval(pullRealtimeCloudData, 2500);
      }
    }"""

new_sync_logic = """    function initRealtimeCloudSync() {
      // 1. Connect instant live SSE event stream
      connectRealtimeStream();

      // 2. Check if local device has data (e.g. PC with 11/12 paid)
      let hasLocalData = false;
      for (let i = 0; i < localStorage.length; i++) {
        const k = localStorage.key(i);
        if (k && k.startsWith('chit_tracker_')) {
          hasLocalData = true;
          break;
        }
      }

      if (hasLocalData) {
        pushRealtimeCloudData();
      } else {
        pullRealtimeCloudData();
      }

      // Sync only on window focus or network reconnect (avoids 429 rate limits)
      window.addEventListener('focus', pullRealtimeCloudData);
      window.addEventListener('online', pullRealtimeCloudData);
    }"""

assert old_sync_logic in html, "Could not find old_sync_logic"
html = html.replace(old_sync_logic, new_sync_logic)

# 3. Update openCloudSyncModal, tryInitFirebase, attachFirebaseListener, saveFirebaseDatabaseUrl
old_fb_section = """    function openCloudSyncModal() {
      updatePhoneSyncLinkDisplay();
      updateCloudSyncStatusUI(true, "Modal Opened");
      document.getElementById('cloudSyncModal').classList.add('open');
    }

    function closeCloudSyncModal() {
      document.getElementById('cloudSyncModal').classList.remove('open');
    }

    async function testLiveSyncConnection() {
      const btn = document.getElementById('btnTestSync');
      if (btn) btn.innerText = 'Connecting to Cloud...';
      try {
        await pushRealtimeCloudData();
        await pullRealtimeCloudData();
        if (btn) btn.innerText = '🧪 Test Sync Now';
        showToast("✓ Cloud Sync Verified! Real-time 2-way sync is working 100%!");
        const liveFeedback = document.getElementById('syncStatusLiveFeedback');
        const liveText = document.getElementById('syncLiveText');
        if (liveFeedback && liveText) {
          liveFeedback.style.display = 'block';
          liveText.innerHTML = `<span style="color: #34d399;">✓ Test Passed! Cloud Database connected & synced right now.</span>`;
        }
      } catch (e) {
        if (btn) btn.innerText = '🧪 Test Sync Now';
        showToast("Could not reach cloud. Check internet connection.");
      }
    }

    function tryInitFirebase() {
      try {
        if (typeof firebase === 'undefined') return;
        let config = null;
        const saved = localStorage.getItem('chit_firebase_config');
        if (saved) {
          try { config = JSON.parse(saved); } catch(e) {}
        }
        if (!config) return;

        if (!firebase.apps || !firebase.apps.length) {
          firebaseApp = firebase.initializeApp(config);
        } else {
          firebaseApp = firebase.apps[0];
        }

        if (firebase.database) {
          firebaseDb = firebase.database();
          isFirebaseConnected = true;
        }
      } catch (err) {}
    }

    function syncStateToFirebase(key, state) {
      if (!firebaseDb || !currentSyncRoom) return;
      try {
        firebaseDb.ref('chit_vault/' + currentSyncRoom + '/' + key).set(state);
      } catch (e) {}
    }"""

new_fb_section = """    function openCloudSyncModal() {
      updatePhoneSyncLinkDisplay();
      const fbInput = document.getElementById('firebaseUrlInput');
      if (fbInput) {
        fbInput.value = localStorage.getItem('chit_firebase_url') || '';
      }
      updateCloudSyncStatusUI(true, "Modal Opened");
      document.getElementById('cloudSyncModal').classList.add('open');
    }

    function closeCloudSyncModal() {
      document.getElementById('cloudSyncModal').classList.remove('open');
    }

    function saveFirebaseDatabaseUrl() {
      const input = document.getElementById('firebaseUrlInput');
      if (!input || !input.value.trim()) {
        showToast("Please enter a Firebase Database URL");
        return;
      }
      let url = input.value.trim();
      if (!url.startsWith('http')) {
        url = 'https://' + url;
      }
      localStorage.setItem('chit_firebase_url', url);
      showToast("✓ Firebase Database URL saved!");
      tryInitFirebase();
    }

    function attachFirebaseListener() {
      if (!firebaseDb) return;
      try {
        const room = currentSyncRoom || 'chit_family_2026';
        firebaseDb.ref('chit_vault/' + room).on('value', (snapshot) => {
          const remoteData = snapshot.val();
          if (!remoteData) return;
          let changed = false;
          for (const key in remoteData) {
            if (key.startsWith('chit_tracker_')) {
              const strVal = JSON.stringify(remoteData[key]);
              if (localStorage.getItem(key) !== strVal) {
                localStorage.setItem(key, strVal);
                changed = true;
              }
            } else if (key === '__receiver_name') {
              if (localStorage.getItem('chit_receiver_name') !== remoteData[key]) {
                localStorage.setItem('chit_receiver_name', remoteData[key]);
              }
            } else if (key === '__receiver_phonepe') {
              if (localStorage.getItem('chit_receiver_phonepe') !== remoteData[key]) {
                localStorage.setItem('chit_receiver_phonepe', remoteData[key]);
              }
            }
          }
          if (changed) {
            renderDashboard();
            showToast("🔥 Realtime Synced via Google Firebase!");
          }
          updateCloudSyncStatusUI(true, "Firebase Live");
        });
      } catch (e) {
        console.warn("Firebase listener error:", e);
      }
    }

    function tryInitFirebase() {
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
        if (!config || !config.databaseURL) return;

        if (!firebase.apps || !firebase.apps.length) {
          firebaseApp = firebase.initializeApp(config);
        } else {
          firebaseApp = firebase.apps[0];
        }

        if (firebase.database) {
          firebaseDb = firebase.database();
          isFirebaseConnected = true;
          attachFirebaseListener();
          const fbBadge = document.getElementById('firebaseStatusBadge');
          if (fbBadge) {
            fbBadge.innerText = '🔥 CONNECTED & ACTIVE';
            fbBadge.style.background = 'rgba(16, 185, 129, 0.3)';
          }
          updateCloudSyncStatusUI(true, "Firebase Connected");
        }
      } catch (err) {
        console.warn("Firebase init error:", err);
      }
    }

    function syncStateToFirebase(key, state) {
      if (!firebaseDb) return;
      try {
        const room = currentSyncRoom || 'chit_family_2026';
        firebaseDb.ref('chit_vault/' + room + '/' + key).set(state);
      } catch (e) {
        console.warn("Firebase push error:", e);
      }
    }

    async function testLiveSyncConnection() {
      const btn = document.getElementById('btnTestSync');
      if (btn) btn.innerText = 'Connecting to Cloud...';
      try {
        await pushRealtimeCloudData();
        await pullRealtimeCloudData();
        if (btn) btn.innerText = '🧪 Test Sync Now';
        showToast("✓ Cloud Sync Verified! Real-time 2-way sync is working 100%!");
        const liveFeedback = document.getElementById('syncStatusLiveFeedback');
        const liveText = document.getElementById('syncLiveText');
        if (liveFeedback && liveText) {
          liveFeedback.style.display = 'block';
          liveText.innerHTML = `<span style="color: #34d399;">✓ Test Passed! Cloud Database connected & synced right now.</span>`;
        }
      } catch (e) {
        if (btn) btn.innerText = '🧪 Test Sync Now';
        showToast("Could not reach cloud. Check internet connection.");
      }
    }"""

assert old_fb_section in html, "Could not find old_fb_section"
html = html.replace(old_fb_section, new_fb_section)

with open(html_path, 'w', encoding='utf-8') as f:
    f.write(html)

print("index.html updated with direct Firebase URL support and rate-limit fix!")
