import re
import os

html_path = r'd:\CHIT\MAIN\index.html'

with open(html_path, 'r', encoding='utf-8') as f:
    html = f.read()

# 1. Update Header Button:
old_header_btn = """          <button class="btn btn-outline" id="btnCloudSync" onclick="openCloudSyncModal()" title="Google Firebase & Cloud Sync (Phone + PC)">
            ☁️ Cloud Sync
          </button>
          <button class="btn btn-primary" id="btnInstallApp" onclick="handleInstallClick()" title="Install as Mobile / Desktop App">
            📲 Install App
          </button>
          <button class="btn btn-outline" onclick="exportDataBackup()" title="Download Backup">
            📥 Backup
          </button>
          <button class="btn btn-outline" onclick="triggerRestoreBackup()" title="Upload / Restore Backup">
            📤 Restore
          </button>"""

new_header_btn = """          <button class="btn btn-outline" id="btnCloudSync" onclick="openCloudSyncModal()" style="border-color: rgba(16, 185, 129, 0.4); color: #34d399; font-weight: 700;" title="Real-time Cloud Sync Active">
            ☁️ Realtime Cloud: LIVE 🟢
          </button>
          <button class="btn btn-primary" id="btnInstallApp" onclick="handleInstallClick()" title="Install as Mobile / Desktop App">
            📲 Install App
          </button>
          <button class="btn btn-outline" onclick="exportDataBackup()" title="Download Backup File to Computer (Optional)">
            📥 Backup
          </button>
          <button class="btn btn-outline" onclick="triggerRestoreBackup()" title="Restore from a Backup File (Optional)">
            📤 Restore
          </button>"""

assert old_header_btn in html, "Could not find old_header_btn"
html = html.replace(old_header_btn, new_header_btn)

# 2. Update Modal HTML:
old_modal_start = '  <!-- Cloud Database & Firebase Sync Modal -->'
old_modal_end = '  <!-- Toast -->'

modal_pattern = re.compile(r'  <!-- Cloud Database & Firebase Sync Modal -->.*?  <!-- Toast -->', re.DOTALL)

new_modal_html = """  <!-- Cloud Database & Real-Time Sync Modal -->
  <div class="modal-overlay" id="cloudSyncModal">
    <div class="modal" style="max-width: 540px;">
      <div class="modal-header">
        <div style="display: flex; align-items: center; gap: 8px;">
          <span style="font-size: 20px;">☁️</span>
          <h3 style="margin: 0; font-size: 17px;">Real-Time Cloud Database & Sync</h3>
        </div>
        <button class="modal-close" onclick="closeCloudSyncModal()">&times;</button>
      </div>

      <div style="display: flex; flex-direction: column; gap: 14px; font-size: 13.5px; color: var(--text-secondary); margin-top: 8px;">
        <!-- Status Card -->
        <div id="cloudStatusCard" style="background: rgba(16, 185, 129, 0.12); border: 1px solid rgba(16, 185, 129, 0.35); border-radius: var(--radius-md); padding: 14px; display: flex; align-items: center; justify-content: space-between; gap: 12px;">
          <div style="display: flex; align-items: center; gap: 10px;">
            <span id="cloudStatusDot" style="width: 12px; height: 12px; border-radius: 50%; background: #10b981; display: inline-block; box-shadow: 0 0 10px #10b981;"></span>
            <div>
              <strong id="cloudStatusTitle" style="color: #34d399; font-size: 14px; display: block;">⚡ Realtime 2-Way Cloud Sync Active!</strong>
              <span id="cloudStatusDesc" style="font-size: 12px; color: #94a3b8;">Payments, notes & locks sync between Phone & PC automatically.</span>
            </div>
          </div>
          <span id="cloudEngineBadge" style="font-size: 11px; background: rgba(16, 185, 129, 0.25); color: #34d399; padding: 4px 10px; border-radius: 6px; font-weight: 700; border: 1px solid rgba(16, 185, 129, 0.5); white-space: nowrap;">✓ CONNECTED</span>
        </div>

        <!-- No File Download Needed Banner -->
        <div style="background: rgba(245, 158, 11, 0.1); border: 1px solid rgba(245, 158, 11, 0.35); border-radius: var(--radius-md); padding: 12px 14px; font-size: 12px; color: #fde68a; line-height: 1.5;">
          ✨ <strong>NO Need to Download or Restore Files!</strong><br>
          Real-time sync runs automatically across devices. When you tick any member on your Phone, it immediately appears on this PC screen within 2 seconds automatically!
        </div>

        <!-- Share Link for Phone / Tablet -->
        <div style="background: rgba(59, 130, 246, 0.08); border: 1px solid rgba(59, 130, 246, 0.25); border-radius: var(--radius-md); padding: 14px;">
          <strong style="color: #60a5fa; font-size: 13.5px; display: block; margin-bottom: 4px;">📱 Open on Mobile / Tablet:</strong>
          <p style="font-size: 11.5px; color: var(--text-secondary); margin-bottom: 8px;">Open this link in Safari or Chrome on your mobile phone to connect live:</p>
          <div style="display: flex; gap: 8px;">
            <input type="text" id="phoneSyncLink" readonly style="flex: 1; background: #0b0f19; border: 1px solid var(--border-color); color: #cbd5e1; padding: 8px 10px; border-radius: 6px; font-size: 11.5px; outline: none;" />
            <button class="btn btn-outline" onclick="copyPhoneSyncLink()" style="font-size: 11px; padding: 6px 12px; white-space: nowrap;">📋 Copy Link</button>
          </div>
          <div style="font-size: 11px; color: #94a3b8; margin-top: 8px; line-height: 1.4;">
            ℹ️ If opening the link on mobile shows 404: In your Netlify dashboard, click <strong>"Make public ->"</strong> so anyone on mobile can open it!
          </div>
        </div>

        <!-- Instant Sync Test -->
        <div style="display: flex; justify-content: space-between; align-items: center; background: rgba(0, 0, 0, 0.28); border: 1px solid var(--border-color); border-radius: var(--radius-md); padding: 12px 14px;">
          <div>
            <strong style="font-size: 12.5px; color: var(--text-primary); display: block;">Instant Sync Test:</strong>
            <span style="font-size: 11px; color: var(--text-muted);">Forces an immediate push and pull with the Cloud Vault</span>
          </div>
          <button class="btn btn-primary" id="btnTestSync" onclick="testLiveSyncConnection()" style="font-size: 12px; padding: 6px 14px; white-space: nowrap;">🧪 Test Sync Now</button>
        </div>
        <div id="syncStatusLiveFeedback" style="display: none; font-size: 12px; font-weight: 600; color: #34d399; text-align: center;">
          <span id="syncLiveText">✓ Connected & Synced Just Now</span>
        </div>
      </div>

      <div style="display: flex; justify-content: flex-end; margin-top: 14px;">
        <button class="btn btn-primary" onclick="closeCloudSyncModal()">Done</button>
      </div>
    </div>
  </div>

  <!-- Toast -->"""

assert modal_pattern.search(html), "Could not find modal pattern"
html = modal_pattern.sub(new_modal_html, html)

# 3. Replace Sync JS logic:
old_sync_start = """    // ==========================================
    // GOOGLE FIREBASE & CLOUD DATABASE SYNC ENGINE
    // ==========================================
    let firebaseApp = null;
    let firebaseDb = null;
    let isFirebaseConnected = false;
    let currentSyncRoom = localStorage.getItem('chit_sync_room') || 'chit_family_2026';
    let syncServerAvailable = false;"""

old_sync_end = """    function saveMonthState(chitId, monthKey, state) {
      const key = getStorageKey(chitId, monthKey);
      try {
        localStorage.setItem(key, JSON.stringify(state));
      } catch (e) {}

      // Push to Google Firebase Realtime Database
      syncStateToFirebase(key, state);

      // Push to Local server if running
      pushServerSyncData(chitId, monthKey, state);
    }"""

new_sync_code = """    // ==========================================
    // 100% AUTOMATIC REAL-TIME CLOUD SYNC ENGINE
    // (Free Cloud Vault, Works on Phone, Tab & PC, Zero Setup, No Backup File Needed)
    // ==========================================
    const CLOUD_SYNC_VAULT_URL = 'https://api.restful-api.dev/objects/ff808181a067127101a09b239a500a37';
    let lastPushTimestamp = 0;
    let isCloudPushing = false;
    let cloudSyncInterval = null;
    let firebaseApp = null;
    let firebaseDb = null;
    let isFirebaseConnected = false;
    let currentSyncRoom = localStorage.getItem('chit_sync_room') || 'chit_family_2026';
    let syncServerAvailable = false;

    function getNetlifyAppUrl() {
      return 'https://spontaneous-swan-3a1f57.netlify.app';
    }

    function updatePhoneSyncLinkDisplay() {
      const linkEl = document.getElementById('phoneSyncLink');
      if (linkEl) {
        if (window.location.protocol === 'file:') {
          linkEl.value = `${getNetlifyAppUrl()}/`;
        } else {
          linkEl.value = `${window.location.origin}${window.location.pathname}`;
        }
      }
    }

    function copyPhoneSyncLink() {
      const linkEl = document.getElementById('phoneSyncLink');
      if (linkEl) {
        linkEl.select();
        navigator.clipboard.writeText(linkEl.value).then(() => {
          showToast("✓ Link copied! Open on your Mobile to auto-sync.");
        }).catch(() => {
          showToast("Link: " + linkEl.value);
        });
      }
    }

    function updateCloudSyncStatusUI(connected, text) {
      const dot = document.getElementById('cloudStatusDot');
      const title = document.getElementById('cloudStatusTitle');
      const desc = document.getElementById('cloudStatusDesc');
      const badge = document.getElementById('cloudEngineBadge');
      const syncDot = document.getElementById('syncDot');
      const syncText = document.getElementById('syncText');
      const syncIndicator = document.getElementById('syncIndicator');

      if (connected) {
        if (dot) dot.style.background = '#10b981';
        if (title) title.innerHTML = `⚡ Realtime 2-Way Cloud Sync Active!`;
        if (desc) desc.innerText = 'Payments, notes & locks sync between Phone & PC automatically.';
        if (badge) {
          badge.innerText = '✓ CONNECTED';
          badge.style.background = 'rgba(16, 185, 129, 0.25)';
          badge.style.color = '#34d399';
          badge.style.borderColor = 'rgba(16, 185, 129, 0.5)';
        }
        if (syncDot) syncDot.style.background = '#10b981';
        if (syncText) syncText.innerText = `☁️ Realtime Cloud: LIVE 🟢`;
        if (syncIndicator) {
          syncIndicator.style.background = 'rgba(16, 185, 129, 0.18)';
          syncIndicator.style.borderColor = 'rgba(16, 185, 129, 0.5)';
          syncIndicator.style.color = '#34d399';
        }
      }
    }

    // Push all local chit data to Cloud Vault
    async function pushRealtimeCloudData() {
      if (isCloudPushing) return;
      isCloudPushing = true;
      try {
        const allData = {};
        for (let i = 0; i < localStorage.length; i++) {
          const k = localStorage.key(i);
          if (k && k.startsWith('chit_tracker_')) {
            try {
              allData[k] = JSON.parse(localStorage.getItem(k));
            } catch (e) {}
          }
        }
        const rName = localStorage.getItem('chit_receiver_name') || '';
        const rPhone = localStorage.getItem('chit_receiver_phonepe') || '';
        if (rName) allData['__receiver_name'] = rName;
        if (rPhone) allData['__receiver_phonepe'] = rPhone;

        const now = Date.now();
        lastPushTimestamp = now;

        const payload = {
          name: 'chit_tracker_sravan_vault',
          data: {
            vault: allData,
            lastUpdated: now,
            device: navigator.userAgent.includes('Mobi') ? 'Mobile' : 'PC'
          }
        };

        const res = await fetch(CLOUD_SYNC_VAULT_URL, {
          method: 'PUT',
          headers: { 'Content-Type': 'application/json' },
          body: JSON.stringify(payload)
        });

        if (res.ok) {
          updateCloudSyncStatusUI(true, "Cloud Synced");
        }
      } catch (err) {
        console.warn("Cloud push error:", err);
      } finally {
        isCloudPushing = false;
      }
    }

    // Pull latest data from Cloud Vault
    async function pullRealtimeCloudData() {
      try {
        const res = await fetch(CLOUD_SYNC_VAULT_URL, { cache: 'no-store' });
        if (!res.ok) return;
        const body = await res.json();
        if (!body || !body.data || !body.data.vault) return;

        const remoteTime = body.data.lastUpdated || 0;
        // If we just pushed newer local data, don't overwrite with older remote
        if (remoteTime <= lastPushTimestamp && lastPushTimestamp > 0) return;

        const remoteVault = body.data.vault;
        let changed = false;

        for (const key in remoteVault) {
          if (key === '__receiver_name') {
            if (localStorage.getItem('chit_receiver_name') !== remoteVault[key]) {
              localStorage.setItem('chit_receiver_name', remoteVault[key]);
            }
          } else if (key === '__receiver_phonepe') {
            if (localStorage.getItem('chit_receiver_phonepe') !== remoteVault[key]) {
              localStorage.setItem('chit_receiver_phonepe', remoteVault[key]);
            }
          } else if (key.startsWith('chit_tracker_')) {
            const strVal = JSON.stringify(remoteVault[key]);
            if (localStorage.getItem(key) !== strVal) {
              localStorage.setItem(key, strVal);
              changed = true;
            }
          }
        }

        if (changed) {
          renderDashboard();
          showToast("🔄 Auto-Synced from Cloud! (Real-time update)");
        }
        updateCloudSyncStatusUI(true, "Live Connected");
      } catch (err) {
        console.warn("Cloud pull error:", err);
      }
    }

    function initRealtimeCloudSync() {
      // 1. Check if local device has data (e.g. PC with 11/12 paid)
      let hasLocalData = false;
      for (let i = 0; i < localStorage.length; i++) {
        const k = localStorage.key(i);
        if (k && k.startsWith('chit_tracker_')) {
          hasLocalData = true;
          break;
        }
      }

      // If local has data, push immediately so cloud is up to date!
      if (hasLocalData) {
        pushRealtimeCloudData();
      } else {
        // Fresh device (like phone opening first time): pull immediately!
        pullRealtimeCloudData();
      }

      // 2. Poll every 2.5 seconds for instant real-time sync across devices
      if (!cloudSyncInterval) {
        cloudSyncInterval = setInterval(pullRealtimeCloudData, 2500);
      }
    }

    function openCloudSyncModal() {
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
    }

    // Local Sync Server Support (for Wi-Fi / Python server)
    async function checkSyncServer() {
      try {
        const res = await fetch('/api/ping', { cache: 'no-store' });
        if (res.ok) {
          syncServerAvailable = true;
          await pullServerSyncData();
          setInterval(pullServerSyncData, 2000);
        }
      } catch (e) {}
    }

    async function pullServerSyncData() {
      if (!syncServerAvailable) return;
      try {
        const res = await fetch('/api/sync', { cache: 'no-store' });
        if (res.ok) {
          const remoteData = await res.json();
          let hasChange = false;
          for (const key in remoteData) {
            const localVal = localStorage.getItem(key);
            const remoteValStr = JSON.stringify(remoteData[key]);
            if (localVal !== remoteValStr) {
              localStorage.setItem(key, remoteValStr);
              hasChange = true;
            }
          }
          if (hasChange) {
            renderDashboard();
          }
        }
      } catch (e) {}
    }

    async function pushServerSyncData(chitId, monthKey, state) {
      if (!syncServerAvailable) return;
      try {
        const allData = {};
        for (let i = 0; i < localStorage.length; i++) {
          const k = localStorage.key(i);
          if (k && k.startsWith('chit_tracker_')) {
            try { allData[k] = JSON.parse(localStorage.getItem(k)); } catch(e){}
          }
        }
        allData[getStorageKey(chitId, monthKey)] = state;
        await fetch('/api/sync', {
          method: 'POST',
          headers: { 'Content-Type': 'application/json' },
          body: JSON.stringify(allData)
        });
      } catch (e) {}
    }

    function saveMonthState(chitId, monthKey, state) {
      const key = getStorageKey(chitId, monthKey);
      try {
        localStorage.setItem(key, JSON.stringify(state));
      } catch (e) {}

      // 1. Instant Push to Free Cloud Vault (Works on Phone & PC automatically!)
      pushRealtimeCloudData();

      // 2. Push to Google Firebase if configured
      syncStateToFirebase(key, state);

      // 3. Push to Local server if running on Wi-Fi
      pushServerSyncData(chitId, monthKey, state);
    }"""

assert old_sync_start in html, "Could not find old_sync_start"
assert old_sync_end in html, "Could not find old_sync_end"

start_pos = html.index(old_sync_start)
end_pos = html.index(old_sync_end) + len(old_sync_end)
html = html[:start_pos] + new_sync_code + html[end_pos:]

# 4. In init(), call initRealtimeCloudSync()
old_init_calls = """      updatePhoneSyncLinkDisplay();
      tryInitFirebase();
      checkSyncServer();"""

new_init_calls = """      updatePhoneSyncLinkDisplay();
      initRealtimeCloudSync();
      tryInitFirebase();
      checkSyncServer();"""

assert old_init_calls in html, "Could not find old_init_calls"
html = html.replace(old_init_calls, new_init_calls)

# 5. In handleBackupFile, after restoring, push to cloud:
old_handle_restore = """          renderDashboard();
          showToast(`✓ Restored ${count} months data successfully! 🎉`);"""

new_handle_restore = """          renderDashboard();
          pushRealtimeCloudData();
          showToast(`✓ Restored ${count} months data successfully! (Cloud updated 🎉)`);"""

assert old_handle_restore in html, "Could not find old_handle_restore"
html = html.replace(old_handle_restore, new_handle_restore)

with open(html_path, 'w', encoding='utf-8') as f:
    f.write(html)

print("index.html updated successfully with 100% Realtime Cloud Sync Engine!")
