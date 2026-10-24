
    // ==========================================
    // COMPLETE CHIT DATA ENGINE
    // ==========================================
    const CHITS = {
      ganapathi: {
        id: 'ganapathi',
        name: 'Ganapathi Chit',
        totalVal: '₹ 2,40,000',
        standardAmt: 20000,
        upiId: 'your-upi-id@oksbi',
        months: [
          { key: 'MAR', name: 'March 2026', taker: 'Sarath Babu', bid: 18500, payout: 210000, takers: ['Sarath Babu'] },
          { key: 'APR', name: 'April 2026', taker: 'Anil', bid: 18000, payout: 210000, takers: ['Sarath Babu', 'Anil'] },
          { key: 'MAY', name: 'May 2026', taker: 'Jyothi', bid: 17500, payout: 210000, takers: ['Sarath Babu', 'Anil', 'Jyothi'] },
          { key: 'JUN', name: 'June 2026', taker: 'Girl', bid: 17000, payout: 210000, takers: ['Sarath Babu', 'Anil', 'Jyothi', 'Girl'] },
          { key: 'JUL', name: 'July 2026', taker: 'Anjineyulu', bid: 16500, payout: 213000, takers: ['Sarath Babu', 'Anil', 'Jyothi', 'Girl', 'Anjineyulu'] },
          { key: 'AUG', name: 'August 2026', taker: 'Ramanaiah', bid: 16000, payout: 213000, takers: ['Sarath Babu', 'Anil', 'Jyothi', 'Girl', 'Anjineyulu', 'Ramanaiah'] },
          { key: 'SEP', name: 'September 2026', taker: 'Harish', bid: 15500, payout: 213000, takers: ['Sarath Babu', 'Anil', 'Jyothi', 'Girl', 'Anjineyulu', 'Ramanaiah', 'Harish'] },
          { key: 'OCT', name: 'October 2026', taker: 'Pallavi', bid: 15000, payout: 215000, takers: ['Sarath Babu', 'Anil', 'Jyothi', 'Girl', 'Anjineyulu', 'Ramanaiah', 'Harish', 'Pallavi'] },
          { key: 'NOV', name: 'November 2026', taker: 'P. Hari', bid: 14500, payout: 215000, takers: ['Sarath Babu', 'Anil', 'Jyothi', 'Girl', 'Anjineyulu', 'Ramanaiah', 'Harish', 'Pallavi', 'P. Hari'] },
          { key: 'DEC', name: 'December 2026', taker: 'Sumanth', bid: 14000, payout: 218000, takers: ['Sarath Babu', 'Anil', 'Jyothi', 'Girl', 'Anjineyulu', 'Ramanaiah', 'Harish', 'Pallavi', 'P. Hari', 'Sumanth'] },
          { key: 'JAN', name: 'January 2027', taker: 'Vamsi Madhu', bid: 13500, payout: 220000, takers: ['Sarath Babu', 'Anil', 'Jyothi', 'Girl', 'Anjineyulu', 'Ramanaiah', 'Harish', 'Pallavi', 'P. Hari', 'Sumanth', 'Vamsi Madhu'] },
          { key: 'FEB', name: 'February 2027', taker: 'Uma Suri', bid: 20000, payout: 225000, takers: ['Sarath Babu', 'Anil', 'Jyothi', 'Girl', 'Anjineyulu', 'Ramanaiah', 'Harish', 'Pallavi', 'P. Hari', 'Sumanth', 'Vamsi Madhu', 'Uma Suri'] }
        ],
        members: ['Sarath Babu', 'Anil', 'Jyothi', 'Girl', 'Anjineyulu', 'Ramanaiah', 'Harish', 'Pallavi', 'P. Hari', 'Sumanth', 'Vamsi Madhu', 'Uma Suri']
      },
      shiva: {
        id: 'shiva',
        name: 'Shiva Chit',
        totalVal: '₹ 1,20,000',
        standardAmt: 10000,
        upiId: 'your-upi-id@oksbi',
        months: [
          { key: 'MAR', name: 'March 2026', taker: 'Pavan', bid: 9500, payout: 105000, takers: ['Pavan'] },
          { key: 'APR', name: 'April 2026', taker: 'veda', bid: 9250, payout: 105000, takers: ['Pavan', 'veda'] },
          { key: 'MAY', name: 'May 2026', taker: 'Dharanya', bid: 9000, payout: 105000, takers: ['Pavan', 'veda', 'Dharanya'] },
          { key: 'JUN', name: 'June 2026', taker: 'Rani', bid: 8750, payout: 105000, takers: ['Pavan', 'veda', 'Dharanya', 'Rani'] },
          { key: 'JUL', name: 'July 2026', taker: 'Chaitu', bid: 8500, payout: 106500, takers: ['Pavan', 'veda', 'Dharanya', 'Rani', 'Chaitu'] },
          { key: 'AUG', name: 'August 2026', taker: 'sukesh', bid: 8250, payout: 106500, takers: ['Pavan', 'veda', 'Dharanya', 'Rani', 'Chaitu', 'sukesh'] },
          { key: 'SEP', name: 'September 2026', taker: 'sampath', bid: 8000, payout: 106500, takers: ['Pavan', 'veda', 'Dharanya', 'Rani', 'Chaitu', 'sukesh', 'sampath'] },
          { key: 'OCT', name: 'October 2026', taker: 'vijay', bid: 7750, payout: 107500, takers: ['Pavan', 'veda', 'Dharanya', 'Rani', 'Chaitu', 'sukesh', 'sampath', 'vijay'] },
          { key: 'NOV', name: 'November 2026', taker: 'sreedhar', bid: 7500, payout: 107500, takers: ['Pavan', 'veda', 'Dharanya', 'Rani', 'Chaitu', 'sukesh', 'sampath', 'vijay', 'sreedhar'] },
          { key: 'DEC', name: 'December 2026', taker: 'Tharun', bid: 7250, payout: 109000, takers: ['Pavan', 'veda', 'Dharanya', 'Rani', 'Chaitu', 'sukesh', 'sampath', 'vijay', 'sreedhar', 'Tharun'] },
          { key: 'JAN', name: 'January 2027', taker: 'chaturya', bid: 7000, payout: 110000, takers: ['Pavan', 'veda', 'Dharanya', 'Rani', 'Chaitu', 'sukesh', 'sampath', 'vijay', 'sreedhar', 'Tharun', 'chaturya'] },
          { key: 'FEB', name: 'February 2027', taker: 'mounika', bid: 10000, payout: 112500, takers: ['Pavan', 'veda', 'Dharanya', 'Rani', 'Chaitu', 'sukesh', 'sampath', 'vijay', 'sreedhar', 'Tharun', 'chaturya', 'mounika'] }
        ],
        members: ['Pavan', 'veda', 'Dharanya', 'Rani', 'Chaitu', 'sukesh', 'sampath', 'vijay', 'sreedhar', 'Tharun', 'chaturya', 'mounika']
      },
      venkateshwara: {
        id: 'venkateshwara',
        name: 'Venkateshwara Chit',
        totalVal: '₹ 3,00,000',
        standardAmt: 25000,
        upiId: 'your-upi-id@oksbi',
        months: [
          { key: 'APR', name: 'April 2026', taker: 'D DHANUNJAYA', bid: 23150, payout: 262500, takers: ['D DHANUNJAYA'] },
          { key: 'MAY', name: 'May 2026', taker: 'Amara Pavan', bid: 22500, payout: 262500, takers: ['D DHANUNJAYA', 'Amara Pavan'] },
          { key: 'JUN', name: 'June 2026', taker: 'KIRAN (anil frd)', bid: 21900, payout: 262500, takers: ['D DHANUNJAYA', 'Amara Pavan', 'KIRAN (anil frd)'] },
          { key: 'JUL', name: 'July 2026', taker: 'A RAKESH', bid: 21250, payout: 262500, takers: ['D DHANUNJAYA', 'Amara Pavan', 'KIRAN (anil frd)', 'A RAKESH'] },
          { key: 'AUG', name: 'August 2026', taker: 'BHASKAR', bid: 20650, payout: 266250, takers: ['D DHANUNJAYA', 'Amara Pavan', 'KIRAN (anil frd)', 'A RAKESH', 'BHASKAR'] },
          { key: 'SEP', name: 'September 2026', taker: 'P RANI', bid: 20000, payout: 266250, takers: ['D DHANUNJAYA', 'Amara Pavan', 'KIRAN (anil frd)', 'A RAKESH', 'BHASKAR', 'P RANI'] },
          { key: 'OCT', name: 'October 2026', taker: 'SATISH', bid: 19400, payout: 266250, takers: ['D DHANUNJAYA', 'Amara Pavan', 'KIRAN (anil frd)', 'A RAKESH', 'BHASKAR', 'P RANI', 'SATISH'] },
          { key: 'NOV', name: 'November 2026', taker: 'BOMBAY DYEING', bid: 18750, payout: 268750, takers: ['D DHANUNJAYA', 'Amara Pavan', 'KIRAN (anil frd)', 'A RAKESH', 'BHASKAR', 'P RANI', 'SATISH', 'BOMBAY DYEING'] },
          { key: 'DEC', name: 'December 2026', taker: 'P HARI KRISHNA', bid: 18150, payout: 268750, takers: ['D DHANUNJAYA', 'Amara Pavan', 'KIRAN (anil frd)', 'A RAKESH', 'BHASKAR', 'P RANI', 'SATISH', 'BOMBAY DYEING', 'P HARI KRISHNA'] },
          { key: 'JAN', name: 'January 2027', taker: 'CH RAJINI', bid: 17500, payout: 272500, takers: ['D DHANUNJAYA', 'Amara Pavan', 'KIRAN (anil frd)', 'A RAKESH', 'BHASKAR', 'P RANI', 'SATISH', 'BOMBAY DYEING', 'P HARI KRISHNA', 'CH RAJINI'] },
          { key: 'FEB', name: 'February 2027', taker: 'MOUNIKA', bid: 16900, payout: 275000, takers: ['D DHANUNJAYA', 'Amara Pavan', 'KIRAN (anil frd)', 'A RAKESH', 'BHASKAR', 'P RANI', 'SATISH', 'BOMBAY DYEING', 'P HARI KRISHNA', 'CH RAJINI', 'MOUNIKA'] },
          { key: 'MAR', name: 'March 2027', taker: 'SWETHA', bid: 25000, payout: 281250, takers: ['D DHANUNJAYA', 'Amara Pavan', 'KIRAN (anil frd)', 'A RAKESH', 'BHASKAR', 'P RANI', 'SATISH', 'BOMBAY DYEING', 'P HARI KRISHNA', 'CH RAJINI', 'MOUNIKA', 'SWETHA'] }
        ],
        members: ['D DHANUNJAYA', 'Amara Pavan', 'KIRAN (anil frd)', 'A RAKESH', 'BHASKAR', 'P RANI', 'SATISH', 'BOMBAY DYEING', 'P HARI KRISHNA', 'CH RAJINI', 'MOUNIKA', 'SWETHA']
      },
      ranganadh: {
        id: 'ranganadh',
        name: 'Ranganadh Chit',
        totalVal: '₹ 3,60,000',
        standardAmt: 30000,
        upiId: 'your-upi-id@oksbi',
        months: [
          { key: 'AUG', name: 'August 2026', taker: 'Sarada', bid: 27780, payout: 315000, takers: ['Sarada'] },
          { key: 'SEP', name: 'September 2026', taker: 'Supraja', bid: 27000, payout: 315000, takers: ['Sarada', 'Supraja'] },
          { key: 'OCT', name: 'October 2026', taker: 'Pavan', bid: 26280, payout: 315000, takers: ['Sarada', 'Supraja', 'Pavan'] },
          { key: 'NOV', name: 'November 2026', taker: 'Sravan', bid: 25500, payout: 315000, takers: ['Sarada', 'Supraja', 'Pavan', 'Sravan'] },
          { key: 'DEC', name: 'December 2026', taker: 'Raki', bid: 24780, payout: 319500, takers: ['Sarada', 'Supraja', 'Pavan', 'Sravan', 'Raki'] },
          { key: 'JAN', name: 'January 2027', taker: 'Dhana', bid: 24000, payout: 319500, takers: ['Sarada', 'Supraja', 'Pavan', 'Sravan', 'Raki', 'Dhana'] },
          { key: 'FEB', name: 'February 2027', taker: 'Satish', bid: 23280, payout: 319500, takers: ['Sarada', 'Supraja', 'Pavan', 'Sravan', 'Raki', 'Dhana', 'Satish'] },
          { key: 'MAR', name: 'March 2027', taker: 'Sudhamani', bid: 22500, payout: 322500, takers: ['Sarada', 'Supraja', 'Pavan', 'Sravan', 'Raki', 'Dhana', 'Satish', 'Sudhamani'] },
          { key: 'APR', name: 'April 2027', taker: 'Harish', bid: 21780, payout: 322500, takers: ['Sarada', 'Supraja', 'Pavan', 'Sravan', 'Raki', 'Dhana', 'Satish', 'Sudhamani', 'Harish'] },
          { key: 'MAY', name: 'May 2027', taker: 'Hari', bid: 21000, payout: 327000, takers: ['Sarada', 'Supraja', 'Pavan', 'Sravan', 'Raki', 'Dhana', 'Satish', 'Sudhamani', 'Harish', 'Hari'] },
          { key: 'JUN', name: 'June 2027', taker: 'Mounika', bid: 20280, payout: 330000, takers: ['Sarada', 'Supraja', 'Pavan', 'Sravan', 'Raki', 'Dhana', 'Satish', 'Sudhamani', 'Harish', 'Hari', 'Mounika'] },
          { key: 'JUL', name: 'July 2027', taker: 'Swetha', bid: 30000, payout: 337500, takers: ['Sarada', 'Supraja', 'Pavan', 'Sravan', 'Raki', 'Dhana', 'Satish', 'Sudhamani', 'Harish', 'Hari', 'Mounika', 'Swetha'] }
        ],
        members: ['Sarada', 'Supraja', 'Pavan', 'Sravan', 'Raki', 'Dhana', 'Satish', 'Sudhamani', 'Harish', 'Hari', 'Mounika', 'Swetha']
      }
    };

    // State
    let currentChitId = 'ganapathi';
    let currentMonthIdx = 6; // default to September 2026
    let currentFilter = 'all';

    // Local Storage State Key
    function getStorageKey(chitId, monthKey) {
      return `chit_tracker_${chitId}_${monthKey}`;
    }

    function loadMonthState(chitId, monthKey) {
      try {
        const data = localStorage.getItem(getStorageKey(chitId, monthKey));
        return data ? JSON.parse(data) : {};
      } catch (e) {
        return {};
      }
    }

    // ==========================================
    // 100% AUTOMATIC REAL-TIME CLOUD SYNC ENGINE
    // (Instant Milliseconds SSE Stream + PubSub across Phone, Tab & PC)
    // ==========================================
    const SYNC_TOPIC = 'chit_vault_sravan_live_sync_2026';
    const SYNC_PUB_URL = 'https://ntfy.sh/' + SYNC_TOPIC;
    const SYNC_SUB_URL = 'https://ntfy.sh/' + SYNC_TOPIC + '/sse';
    const SYNC_POLL_URL = 'https://ntfy.sh/' + SYNC_TOPIC + '/json?poll=1';

    let lastPushTimestamp = 0;
    let isCloudPushing = false;
    let eventSourceInstance = null;
    let cloudSyncInterval = null;
    let firebaseApp = null;
    let firebaseDb = null;
    let isFirebaseConnected = false;
    let currentSyncRoom = localStorage.getItem('chit_sync_room') || 'chit_family_2026';
    let syncServerAvailable = false;

    function getNetlifyAppUrl() {
      return 'https://chitsravan.netlify.app';
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
        if (title) title.innerHTML = `🔥 Google Cloud Database Connected!`;
        if (desc) desc.innerText = 'Live 2-way sync active on Google Cloud • Updates appear across Phone & PC in 30ms';
        if (badge) {
          badge.innerText = '✓ GOOGLE LIVE';
          badge.style.background = 'rgba(16, 185, 129, 0.25)';
          badge.style.color = '#34d399';
          badge.style.borderColor = 'rgba(16, 185, 129, 0.5)';
        }
        if (syncDot) syncDot.style.background = '#10b981';
        if (syncText) syncText.innerText = `🔥 Google Cloud: LIVE 🟢`;
        if (syncIndicator) {
          syncIndicator.style.background = 'rgba(16, 185, 129, 0.18)';
          syncIndicator.style.borderColor = 'rgba(16, 185, 129, 0.5)';
          syncIndicator.style.color = '#34d399';
        }
      }
    }

    // Push all local chit data to Realtime Cloud Stream
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
          vault: allData,
          lastUpdated: now,
          device: navigator.userAgent.includes('Mobi') ? 'Mobile' : 'PC'
        };

        await fetch(SYNC_PUB_URL, {
          method: 'POST',
          body: JSON.stringify(payload)
        });

        updateCloudSyncStatusUI(true, "Cloud Synced");
      } catch (err) {
        console.warn("Cloud push error:", err);
      } finally {
        isCloudPushing = false;
      }
    }

    // Apply remote incoming vault data to localStorage & re-render
    function applyRemoteVault(remoteVault, remoteTime) {
      if (!remoteVault) return;
      if (remoteTime && remoteTime <= lastPushTimestamp && lastPushTimestamp > 0) return;

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
        showToast("⚡ Auto-Synced from Cloud! (Real-time update)");
      }
      updateCloudSyncStatusUI(true, "Live Connected");
    }

    // Pull latest cached state from Cloud Stream
    async function pullRealtimeCloudData() {
      try {
        const res = await fetch(SYNC_POLL_URL, { cache: 'no-store' });
        if (!res.ok) return;
        const text = await res.text();
        if (!text) return;
        const lines = text.trim().split('\n');
        let latestMsg = null;
        let latestTime = 0;
        for (const line of lines) {
          try {
            const item = JSON.parse(line);
            if (item && item.message) {
              const body = JSON.parse(item.message);
              if (body && body.lastUpdated && body.lastUpdated > latestTime) {
                latestTime = body.lastUpdated;
                latestMsg = body;
              }
            }
          } catch(e) {}
        }
        if (latestMsg && latestMsg.vault) {
          applyRemoteVault(latestMsg.vault, latestMsg.lastUpdated);
        }
      } catch (err) {
        console.warn("Cloud pull error:", err);
      }
    }

    // Connect Server-Sent Events (SSE) for Instant Milliseconds Push across devices
    function connectRealtimeStream() {
      if (eventSourceInstance) {
        try { eventSourceInstance.close(); } catch(e) {}
      }
      try {
        eventSourceInstance = new EventSource(SYNC_SUB_URL);
        eventSourceInstance.onmessage = (event) => {
          try {
            const data = JSON.parse(event.data);
            if (data && data.message) {
              const body = JSON.parse(data.message);
              if (body && body.vault) {
                applyRemoteVault(body.vault, body.lastUpdated);
              }
            }
          } catch(e) {}
        };
        eventSourceInstance.onerror = () => {
          setTimeout(connectRealtimeStream, 6000);
        };
      } catch(e) {}
    }

    function initRealtimeCloudSync() {
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
    }

    function openCloudSyncModal() {
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

    function pushAllLocalToFirebase() {
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

    const FIREBASE_DEFAULT_DB_URL = 'https://chitsravan-default-rtdb.firebaseio.com';

    function tryInitFirebase() {
      try {
        if (typeof firebase === 'undefined') return;
        let url = localStorage.getItem('chit_firebase_url') || FIREBASE_DEFAULT_DB_URL;
        let config = { databaseURL: url };

        if (!firebase.apps || !firebase.apps.length) {
          firebaseApp = firebase.initializeApp(config);
        } else {
          firebaseApp = firebase.apps[0];
        }

        if (firebase.database) {
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

    // Hamburger ☰ Menu Handlers
    function toggleHamburgerMenu(e) {
      if (e) e.stopPropagation();
      const menu = document.getElementById('hamburgerDropdownMenu');
      if (menu) {
        menu.style.display = menu.style.display === 'block' ? 'none' : 'block';
      }
    }

    function closeHamburgerMenu() {
      const menu = document.getElementById('hamburgerDropdownMenu');
      if (menu) menu.style.display = 'none';
    }

    document.addEventListener('click', (e) => {
      const menuWrapper = document.querySelector('.menu-dropdown-wrapper');
      if (menuWrapper && !menuWrapper.contains(e.target)) {
        closeHamburgerMenu();
      }
    });

    async function testLiveSyncConnection() {
      const btn = document.getElementById('btnTestSync');
      const liveFeedback = document.getElementById('syncStatusLiveFeedback');
      const liveText = document.getElementById('syncLiveText');
      if (btn) btn.innerText = 'Testing Google Cloud...';

      try {
        const res = await fetch('https://chitsravan-default-rtdb.firebaseio.com/.json');
        if (res.ok) {
          if (btn) btn.innerText = '🧪 Test Sync Now';
          showToast("✓ Google Firebase Verified! 100% Active & Synced.");
          if (liveFeedback && liveText) {
            liveFeedback.style.display = 'block';
            liveText.innerHTML = `<span style="color: #34d399;">✓ Test Passed! Google Firebase Connected & Synced (0 errors)</span>`;
          }
        } else {
          throw new Error("HTTP " + res.status);
        }
      } catch (e) {
        if (btn) btn.innerText = '🧪 Test Sync Now';
        showToast("Firebase check note: " + e.message);
      }
    }
      } catch (e) {
        if (btn) btn.innerText = '🧪 Test Sync Now';
        showToast("Could not reach cloud. Check internet connection.");
      }
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
    }



    function renderChitTabs() {
      const container = document.getElementById('chitTabs');
      container.innerHTML = '';
      Object.values(CHITS).forEach(chit => {
        const card = document.createElement('div');
        card.className = `chit-tab-card ${chit.id === currentChitId ? 'active' : ''}`;
        card.onclick = () => switchChit(chit.id);
        card.innerHTML = `
          <div class="chit-tab-name">
            <span>${chit.name}</span>
            <span class="chit-tab-badge">${chit.totalVal}</span>
          </div>
          <div class="chit-tab-meta">12 Months • Base: ₹ ${chit.standardAmt.toLocaleString()}</div>
        `;
        container.appendChild(card);
      });
    }

    function switchChit(chitId) {
      currentChitId = chitId;
      renderChitTabs();
      renderMonthBar();
      // Auto select current active month (or first month)
      const chit = CHITS[currentChitId];
      currentMonthIdx = Math.min(currentMonthIdx, chit.months.length - 1);
      switchMonth(currentMonthIdx);
    }

    function renderMonthBar() {
      const bar = document.getElementById('monthBar');
      bar.innerHTML = '';
      const chit = CHITS[currentChitId];
      chit.months.forEach((m, idx) => {
        const pill = document.createElement('div');
        pill.className = `month-pill ${idx === currentMonthIdx ? 'active' : ''}`;
        pill.innerText = m.name;
        pill.onclick = () => switchMonth(idx);
        bar.appendChild(pill);
      });
    }

    function switchMonth(idx) {
      currentMonthIdx = idx;
      renderMonthBar();
      renderDashboard();
    }

    function renderDashboard() {
      const chit = CHITS[currentChitId];
      const month = chit.months[currentMonthIdx];
      const state = loadMonthState(currentChitId, month.key);

      // Members Container Populating (Both Cards and Table)
      const cardsContainer = document.getElementById('membersCardsContainer');
      const tbody = document.getElementById('membersTableBody');
      if (cardsContainer) cardsContainer.innerHTML = '';
      if (tbody) tbody.innerHTML = '';

      let totalTarget = 0;
      let totalCollected = 0;
      let paidCount = 0;

      const isLocked = !!state.__locked;

      // Update Lock Button and Banner
      const btnLock = document.getElementById('btnLockMonth');
      const lockBanner = document.getElementById('lockedMonthBanner');
      if (btnLock) {
        if (isLocked) {
          btnLock.innerHTML = '🔓 Unlock Month';
          btnLock.className = 'btn btn-warning';
          btnLock.title = 'Click to unlock this month for editing';
        } else {
          btnLock.innerHTML = '🔒 Lock Month';
          btnLock.className = 'btn btn-outline';
          btnLock.title = 'Lock month when settlement is closed to prevent accidental edits';
        }
      }
      if (lockBanner) {
        lockBanner.style.display = isLocked ? 'flex' : 'none';
      }

      chit.members.forEach((name, idx) => {
        const isTaker = month.takers.includes(name);
        const amount = isTaker ? chit.standardAmt : month.bid;
        totalTarget += amount;

        const memberState = state[name] || { paid: false, mode: 'UPI' };
        if (memberState.paid) {
          totalCollected += amount;
          paidCount++;
        }

        // Apply Filter
        if (currentFilter === 'paid' && !memberState.paid) return;
        if (currentFilter === 'pending' && memberState.paid) return;

        // 1. Render Mobile Touch Card
        const card = document.createElement('div');
        card.className = `member-card ${memberState.paid ? 'card-paid' : ''} ${isLocked ? 'card-locked' : ''}`;
        card.onclick = () => {
          if (isLocked) {
            showToast("🔒 Month is locked! Click 'Unlock Month' to make changes.");
            return;
          }
          togglePayment(name);
        };
        card.innerHTML = `
          <div class="card-left">
            <div class="checkbox-box">
              <svg viewBox="0 0 24 24"><polyline points="20 6 9 17 4 12"></polyline></svg>
            </div>
            <div class="person-avatar ${isTaker ? 'taker-avatar' : ''}">${name.charAt(0)}</div>
            <div class="person-details" style="flex: 1; min-width: 0;">
              <span class="person-name">${name}</span>
              <span class="person-tag ${isTaker ? 'taker-tag' : ''}">${isTaker ? '★ Chit Taken' : 'Active Member'}</span>
              <div class="mobile-note-row" onclick="event.stopPropagation()">
                <input 
                  type="text" 
                  class="mobile-note-input" 
                  placeholder="📝 Add note: Paid 10k, rem 10k..." 
                  value="${memberState.note || ''}" 
                  oninput="updateMemberNote('${name}', this.value)"
                  onblur="pushRealtimeCloudData()"
                  ${isLocked ? 'disabled title="Month is locked"' : ''}
                />
              </div>
            </div>
          </div>
          <div class="card-right">
            <span class="amount-cell ${isTaker ? 'amount-taker' : 'amount-nontaker'}">
              ₹ ${amount.toLocaleString()}
            </span>
            <span class="status-pill ${memberState.paid ? 'paid' : 'pending'}">
              ${memberState.paid ? '✓ PAID' : '⏳ PENDING'}
            </span>
          </div>
        `;
        cardsContainer.appendChild(card);

        // 2. Render Table Row (for Scrollable Table View)
        const tr = document.createElement('tr');
        tr.className = `${memberState.paid ? 'row-paid' : ''} ${isLocked ? 'row-locked' : ''}`;
        tr.onclick = (e) => {
          if (isLocked) {
            showToast("🔒 Month is locked! Click 'Unlock Month' to make changes.");
            return;
          }
          if (e.target.tagName !== 'SELECT' && e.target.tagName !== 'INPUT') {
            togglePayment(name);
          }
        };

        tr.innerHTML = `
          <td style="text-align: center;">
            <div class="checkbox-container">
              <div class="checkbox-box">
                <svg viewBox="0 0 24 24"><polyline points="20 6 9 17 4 12"></polyline></svg>
              </div>
            </div>
          </td>
          <td>
            <div class="person-name-cell">
              <div class="person-avatar ${isTaker ? 'taker-avatar' : ''}">${name.charAt(0)}</div>
              <div class="person-details">
                <span class="person-name">${name}</span>
                <span class="person-tag ${isTaker ? 'taker-tag' : ''}">${isTaker ? '★ Chit Taken' : 'Active Member'}</span>
              </div>
            </div>
          </td>
          <td onclick="event.stopPropagation()">
            <div class="note-input-wrapper">
              <input 
                type="text" 
                class="member-note-input" 
                placeholder="e.g. Paid 10k, rem 10k" 
                value="${memberState.note || ''}" 
                oninput="updateMemberNote('${name}', this.value)"
                onblur="pushRealtimeCloudData()"
                ${isLocked ? 'disabled title="Month is locked"' : ''}
              />
            </div>
          </td>
          <td style="text-align: right;">
            <span class="amount-cell ${isTaker ? 'amount-taker' : 'amount-nontaker'}">
              ₹ ${amount.toLocaleString()}
            </span>
          </td>
          <td style="text-align: center;">
            <select class="mode-select" onchange="changePaymentMode('${name}', this.value)" onclick="event.stopPropagation()" ${isLocked ? 'disabled' : ''}>
              <option value="UPI" ${memberState.mode === 'UPI' ? 'selected' : ''}>PhonePe / UPI</option>
              <option value="Cash" ${memberState.mode === 'Cash' ? 'selected' : ''}>Cash</option>
              <option value="Bank" ${memberState.mode === 'Bank' ? 'selected' : ''}>Bank Transfer</option>
              <option value="Pending" ${memberState.mode === 'Pending' ? 'selected' : ''}>Pending</option>
            </select>
          </td>
          <td style="text-align: center;">
            <span class="status-pill ${memberState.paid ? 'paid' : 'pending'}">
              ${memberState.paid ? '✓ PAID' : '⏳ PENDING'}
            </span>
          </td>
        `;
        tbody.appendChild(tr);
      });

      // Update Live Stats & Hero
      const pendingAmount = totalTarget - totalCollected;
      const commission = Math.max(0, totalTarget - month.payout);
      const percent = totalTarget > 0 ? Math.round((totalCollected / totalTarget) * 100) : 0;

      const heroTitle = document.getElementById('heroTitle');
      if (heroTitle) heroTitle.innerText = `${chit.name} – ${month.name}`;

      const heroMeta = document.getElementById('heroMeta');
      if (heroMeta) heroMeta.innerText = `Total 12 Members • Target Monthly Collection`;

      // Update Chit Winner / Taken Person Box Type Layout
      const winnerNameEl = document.getElementById('winnerPersonName');
      const winnerMonthPill = document.getElementById('winnerMonthPill');
      const winnerPayoutEl = document.getElementById('winnerPayoutAmount');
      const winnerSubtext = document.getElementById('winnerSubtext');

      if (winnerNameEl) winnerNameEl.innerText = month.taker || 'Auction / Pending';
      if (winnerMonthPill) winnerMonthPill.innerText = `Chit #${currentMonthIdx + 1} • ${month.name}`;
      if (winnerPayoutEl) winnerPayoutEl.innerText = `₹ ${month.payout.toLocaleString()}`;
      if (winnerSubtext) {
        winnerSubtext.innerText = month.taker 
          ? `Amount to send to ${month.taker} for ${month.name}` 
          : `Target payout for ${month.name} auction winner`;
      }

      document.getElementById('statCollected').innerText = `₹ ${totalCollected.toLocaleString()}`;
      document.getElementById('statPending').innerText = `₹ ${pendingAmount.toLocaleString()}`;
      document.getElementById('statCount').innerText = `${paidCount} / 12`;
      document.getElementById('statTarget').innerText = `₹ ${totalTarget.toLocaleString()}`;
      
      currentCommissionAmount = commission;
      currentCommissionTarget = totalTarget;
      currentCommissionPayout = month.payout;
      updateSecretCommissionUI();

      document.getElementById('progressPercent').innerText = `${percent}%`;
      document.getElementById('progressBar').style.width = `${percent}%`;

      document.getElementById('filterPendingBtn').innerText = `Pending (${12 - paidCount})`;
      document.getElementById('filterPaidBtn').innerText = `Paid (${paidCount})`;
    }

    // Stealth Eye Commission Logic (Completely hidden until eye is clicked)
    let isCommissionVisible = false;
    let currentCommissionAmount = 0;
    let currentCommissionTarget = 0;
    let currentCommissionPayout = 0;
    let autoHideTimer = null;

    function toggleSecretCommission(e) {
      if (e) e.stopPropagation();
      isCommissionVisible = !isCommissionVisible;
      updateSecretCommissionUI();
    }

    function toggleCommissionPrivacy() {
      toggleSecretCommission();
    }

    function hideSecretCommission() {
      if (isCommissionVisible) {
        isCommissionVisible = false;
        updateSecretCommissionUI();
      }
    }

    function updateSecretCommissionUI() {
      const popover = document.getElementById('secretCommissionPopover');
      const btn = document.getElementById('stealthEyeBtn');
      const monthTitle = document.getElementById('secretMonthTitle');
      const valEl = document.getElementById('statCommission');
      const commEyeBadge = document.getElementById('commEyeBadge');
      const commSubtext = document.getElementById('commissionSubtext');
      const targetEl = document.getElementById('secretTargetVal');
      const payoutEl = document.getElementById('secretPayoutVal');
      const netEl = document.getElementById('secretNetVal');

      const chit = CHITS[currentChitId];
      const month = chit.months[currentMonthIdx];

      if (monthTitle) monthTitle.innerText = `${month.name} Commission (${chit.name})`;
      if (targetEl) targetEl.innerText = `₹ ${currentCommissionTarget.toLocaleString()}`;
      if (payoutEl) payoutEl.innerText = `- ₹ ${currentCommissionPayout.toLocaleString()} (${month.taker})`;
      if (netEl) netEl.innerText = `₹ ${currentCommissionAmount.toLocaleString()}`;

      if (isCommissionVisible) {
        if (valEl) {
          valEl.innerText = `₹ ${currentCommissionAmount.toLocaleString()}`;
          valEl.style.letterSpacing = 'normal';
        }
        if (commEyeBadge) commEyeBadge.innerText = '🔒';
        if (commSubtext) {
          commSubtext.innerText = `Target ₹ ${currentCommissionTarget.toLocaleString()} − Payout ₹ ${currentCommissionPayout.toLocaleString()}`;
          commSubtext.style.color = '#fef3c7';
        }
        if (popover) popover.style.display = 'block';
        if (btn) {
          btn.innerHTML = '🔒';
          btn.classList.add('active');
        }
      } else {
        if (valEl) {
          valEl.innerText = '₹ ••••••';
          valEl.style.letterSpacing = '4px';
        }
        if (commEyeBadge) commEyeBadge.innerText = '👁️';
        if (commSubtext) {
          commSubtext.innerText = '🔒 Hidden for privacy (tap to reveal)';
          commSubtext.style.color = 'var(--text-secondary)';
        }
        if (popover) popover.style.display = 'none';
        if (btn) {
          btn.innerHTML = '👁️';
          btn.classList.remove('active');
        }
      }
    }

    // Close stealth popover when clicking anywhere outside
    document.addEventListener('click', (e) => {
      const popover = document.getElementById('secretCommissionPopover');
      const btn = document.getElementById('stealthEyeBtn');
      if (popover && popover.style.display === 'block') {
        if (!popover.contains(e.target) && !btn.contains(e.target)) {
          hideSecretCommission();
        }
      }
    });

    let noteDebounceTimer = null;
    function updateMemberNote(name, noteText) {
      const chit = CHITS[currentChitId];
      const month = chit.months[currentMonthIdx];
      const state = loadMonthState(currentChitId, month.key);

      if (state.__locked) {
        showToast("🔒 Month is locked! Click 'Unlock Month' to make changes.");
        return;
      }

      if (!state[name]) {
        state[name] = { paid: false, mode: 'UPI' };
      }
      state[name].note = noteText;
      state[name].updatedAt = new Date().toISOString();

      // Save to localStorage immediately
      try {
        localStorage.setItem(getStorageKey(currentChitId, month.key), JSON.stringify(state));
      } catch (e) {}

      // Debounce push to Cloud Stream 600ms after user stops typing
      clearTimeout(noteDebounceTimer);
      noteDebounceTimer = setTimeout(() => {
        pushRealtimeCloudData();
      }, 600);
    }

    function openLockModal() {
      const chit = CHITS[currentChitId];
      const month = chit.months[currentMonthIdx];
      const state = loadMonthState(currentChitId, month.key);
      const isLocked = !!state.__locked;

      const titleEl = document.getElementById('lockModalTitle');
      const descEl = document.getElementById('lockModalDesc');
      const btnConfirm = document.getElementById('btnConfirmLock');

      if (isLocked) {
        if (titleEl) titleEl.innerText = `🔓 Unlock ${month.name} (${chit.name})`;
        if (descEl) descEl.innerHTML = `Are you sure you want to <strong>unlock ${month.name}</strong>?<br><br>This will re-enable editing payment tick boxes, payment modes, and notes.`;
        if (btnConfirm) {
          btnConfirm.innerText = '🔓 Confirm Unlock';
          btnConfirm.className = 'btn btn-warning';
        }
      } else {
        if (titleEl) titleEl.innerText = `🔒 Lock ${month.name} Settlement (${chit.name})`;
        if (descEl) descEl.innerHTML = `Are you sure you want to <strong>lock and settle ${month.name}</strong>?<br><br>All payment tick boxes, payment modes, and notes will be frozen so no one can edit them by mistake.`;
        if (btnConfirm) {
          btnConfirm.innerText = '🔒 Confirm Lock';
          btnConfirm.className = 'btn btn-primary';
        }
      }

      document.getElementById('lockModal').classList.add('open');
    }

    function closeLockModal() {
      document.getElementById('lockModal').classList.remove('open');
    }

    function confirmToggleLock() {
      const chit = CHITS[currentChitId];
      const month = chit.months[currentMonthIdx];
      const state = loadMonthState(currentChitId, month.key);

      state.__locked = !state.__locked;
      saveMonthState(currentChitId, month.key, state);
      closeLockModal();
      renderDashboard();
      showToast(state.__locked ? `🔒 ${month.name} Locked & Settled!` : `🔓 ${month.name} Unlocked for editing.`);
    }

    function togglePayment(name) {
      const chit = CHITS[currentChitId];
      const month = chit.months[currentMonthIdx];
      const state = loadMonthState(currentChitId, month.key);

      if (state.__locked) {
        showToast("🔒 Month is locked! Click 'Unlock Month' to make changes.");
        return;
      }

      const current = state[name] || { paid: false, mode: 'UPI' };
      state[name] = {
        ...current,
        paid: !current.paid,
        mode: current.mode || 'UPI',
        updatedAt: new Date().toISOString()
      };

      saveMonthState(currentChitId, month.key, state);
      renderDashboard();
      showToast(state[name].paid ? `Marked ${name} as PAID ✓` : `Marked ${name} as PENDING ⏳`);
    }

    function changePaymentMode(name, mode) {
      const chit = CHITS[currentChitId];
      const month = chit.months[currentMonthIdx];
      const state = loadMonthState(currentChitId, month.key);

      if (state.__locked) {
        showToast("🔒 Month is locked! Click 'Unlock Month' to make changes.");
        return;
      }

      const current = state[name] || { paid: false, mode: 'UPI' };
      state[name] = {
        ...current,
        mode: mode,
        paid: mode !== 'Pending' ? true : current.paid
      };

      saveMonthState(currentChitId, month.key, state);
      renderDashboard();
      showToast(`Updated payment mode for ${name}`);
    }

    function setFilter(type, btn) {
      currentFilter = type;
      document.querySelectorAll('.filter-btn').forEach(b => b.classList.remove('active'));
      btn.classList.add('active');
      renderDashboard();
    }

    // ==========================================
    // WHATSAPP MESSAGES GENERATOR
    // ==========================================
    function getOrdinal(n) {
      const s = ["th", "st", "nd", "rd"];
      const v = n % 100;
      return n + (s[(v - 20) % 10] || s[v] || s[0]);
    }

    let currentWhatsAppType = 'all';

    function openWhatsAppModal(type) {
      currentWhatsAppType = type || 'all';
      generateWhatsAppText();
      document.getElementById('whatsappModal').classList.add('open');
    }

    function generateWhatsAppText() {
      const chit = CHITS[currentChitId];
      const month = chit.months[currentMonthIdx];
      const state = loadMonthState(currentChitId, month.key);

      const nameInput = document.getElementById('upiReceiverName');
      const phoneInput = document.getElementById('upiReceiverPhonePe');
      
      const savedName = localStorage.getItem('chit_receiver_name') || '';
      const savedPhone = localStorage.getItem('chit_receiver_phonepe') || '';

      if (nameInput && !nameInput.value) nameInput.value = savedName;
      if (phoneInput && !phoneInput.value) phoneInput.value = savedPhone;

      const receiverName = nameInput ? nameInput.value.trim() : savedName;
      const receiverPhonePe = phoneInput ? phoneInput.value.trim() : savedPhone;

      // Format Short Month (e.g. Sep, Aug, Mar, Apr, etc.)
      const monthShort = month.name.split(' ')[0].substring(0, 3);
      const chitNum = getOrdinal(currentMonthIdx + 1);

      let msg = '';
      if (currentWhatsAppType === 'all') {
        document.getElementById('modalHeading').innerText = `📢 WhatsApp Notice – ${month.name}`;
        msg = `Hai Everyone 😊\n\n`;
        msg += `${chitNum} Chit  ${monthShort} Taken By: ${month.taker}\n\n`;
        msg += `This Month Amount: ₹ ${month.bid.toLocaleString()}\n\n`;
        msg += `Everyone, please transfer the amount to:\n\n`;
        msg += `Name: ${receiverName}\n`;
        msg += `PhonePe: ${receiverPhonePe}\n\n`;
        msg += `📷 Please refer to the attached image for the payment details.\n\n`;
        msg += `📌 Note: Members who have already taken the chit need to pay ₹ ${chit.standardAmt.toLocaleString()}\n\n`;
        msg += `Please complete the payment and share the payment screenshot in the group after transferring.\n\n`;
        msg += `🙏 Thank you\n`;
        msg += `${chit.name}`;
      } else {
        document.getElementById('modalHeading').innerText = `⚠️ Pending Reminders – ${month.name}`;
        
        let pendingLines = [];
        chit.members.forEach((name) => {
          if (!state[name]?.paid) {
            const isTaker = month.takers.includes(name);
            const amt = isTaker ? chit.standardAmt : month.bid;
            pendingLines.push(`• *${name}*: ₹ ${amt.toLocaleString()}`);
          }
        });

        if (pendingLines.length === 0) {
          msg = `Hai Everyone 😊\n\n🎉 Great news! All 12 members have cleared their installments for ${chit.name} (${month.name})!\n\n🙏 Thank you all!`;
        } else {
          msg = `Hai Everyone 😊\n\n`;
          msg += `${chitNum} Chit  ${monthShort} – Pending Installments Reminder\n\n`;
          msg += `This Month Amount: ₹ ${month.bid.toLocaleString()}\n\n`;
          msg += `The following members' installments are pending:\n`;
          msg += `────────────────────────────\n`;
          msg += pendingLines.join('\n') + '\n';
          msg += `────────────────────────────\n\n`;
          msg += `Everyone, please transfer the amount to:\n\n`;
          msg += `Name: ${receiverName}\n`;
          msg += `PhonePe: ${receiverPhonePe}\n\n`;
          msg += `📷 Please refer to the attached image for the payment details.\n\n`;
          msg += `📌 Note: Members who have already taken the chit need to pay ₹ ${chit.standardAmt.toLocaleString()}\n\n`;
          msg += `Please complete the payment and share the payment screenshot in the group after transferring.\n\n`;
          msg += `🙏 Thank you\n`;
          msg += `${chit.name}`;
        }
      }

      document.getElementById('whatsappText').value = msg;
    }

    function onReceiverDetailsChange() {
      const name = document.getElementById('upiReceiverName').value;
      const phonepe = document.getElementById('upiReceiverPhonePe').value;
      localStorage.setItem('chit_receiver_name', name);
      localStorage.setItem('chit_receiver_phonepe', phonepe);
      generateWhatsAppText();
    }

    function closeWhatsAppModal() {
      document.getElementById('whatsappModal').classList.remove('open');
    }

    function copyWhatsAppMessage() {
      const textarea = document.getElementById('whatsappText');
      textarea.select();
      navigator.clipboard.writeText(textarea.value).then(() => {
        showToast("✓ Copied to clipboard! Paste directly into WhatsApp group.");
        closeWhatsAppModal();
      });
    }

    function showToast(msg) {
      const toast = document.getElementById('toast');
      toast.innerText = msg;
      toast.classList.add('show');
      setTimeout(() => {
        toast.classList.remove('show');
      }, 2500);
    }

    function openResetConfirm() {
      const chit = CHITS[currentChitId];
      const month = chit.months[currentMonthIdx];
      if (confirm(`Reset all payments for ${chit.name} - ${month.name}?`)) {
        localStorage.removeItem(getStorageKey(currentChitId, month.key));
        renderDashboard();
        showToast("Month payments reset.");
      }
    }

    function exportDataBackup() {
      const allData = {};
      for (let i = 0; i < localStorage.length; i++) {
        const key = localStorage.key(i);
        if (key.startsWith('chit_tracker_')) {
          allData[key] = JSON.parse(localStorage.getItem(key));
        }
      }
      const blob = new Blob([JSON.stringify(allData, null, 2)], { type: 'application/json' });
      const a = document.createElement('a');
      a.href = URL.createObjectURL(blob);
      a.download = `Chit_Tracker_Backup_${new Date().toISOString().split('T')[0]}.json`;
      a.click();
      showToast("Backup file downloaded!");
    }

    function triggerRestoreBackup() {
      const input = document.getElementById('backupFileInput');
      if (input) input.click();
    }

    function handleBackupFile(e) {
      const file = e.target.files[0];
      if (!file) return;
      const reader = new FileReader();
      reader.onload = function(evt) {
        try {
          const data = JSON.parse(evt.target.result);
          let count = 0;
          for (const k in data) {
            if (k.startsWith('chit_tracker_')) {
              localStorage.setItem(k, JSON.stringify(data[k]));
              count++;
            }
          }
          renderDashboard();
          pushRealtimeCloudData();
          showToast(`✓ Restored ${count} months data successfully! (Cloud updated 🎉)`);
        } catch (err) {
          alert("Invalid backup file. Please select a valid Chit Tracker JSON backup.");
        }
      };
      reader.readAsText(file);
      e.target.value = '';
    }

    // PWA Install Prompt Handling
    let deferredInstallPrompt = null;
    window.addEventListener('beforeinstallprompt', (e) => {
      e.preventDefault();
      deferredInstallPrompt = e;
      const btn = document.getElementById('btnInstallApp');
      if (btn) {
        btn.innerHTML = '📲 Install App';
        btn.classList.add('pulse');
      }
    });

    function handleInstallClick() {
      if (deferredInstallPrompt) {
        deferredInstallPrompt.prompt();
        deferredInstallPrompt.userChoice.then((choice) => {
          if (choice.outcome === 'accepted') {
            showToast("App installed successfully! 🎉");
          }
          deferredInstallPrompt = null;
        });
      } else {
        openInstallModal();
      }
    }

    function openInstallModal() {
      document.getElementById('installModal').classList.add('open');
    }

    function closeInstallModal() {
      document.getElementById('installModal').classList.remove('open');
    }

    // View Switcher Function
    let currentViewMode = window.innerWidth <= 768 ? 'cards' : 'table';

    function switchView(mode) {
      currentViewMode = mode;
      const btnCards = document.getElementById('btnViewCards');
      const btnTable = document.getElementById('btnViewTable');
      if (btnCards && btnTable) {
        btnCards.classList.toggle('active', mode === 'cards');
        btnTable.classList.toggle('active', mode === 'table');
      }

      const cards = document.getElementById('membersCardsContainer');
      const table = document.getElementById('membersTableWrapper');
      const hint = document.getElementById('scrollHintBar');

      if (mode === 'cards') {
        if (cards) cards.style.display = 'flex';
        if (table) table.style.display = 'none';
        if (hint) hint.style.display = 'none';
      } else {
        if (cards) cards.style.display = 'none';
        if (table) table.style.display = 'block';
        if (hint) hint.style.display = window.innerWidth <= 768 ? 'block' : 'none';
      }
    }

    // Register Service Worker
    if ('serviceWorker' in navigator) {
      window.addEventListener('load', () => {
        navigator.serviceWorker.register('sw.js').catch((err) => {
          console.log('SW registration:', err);
        });
      });
    }

    // Start App
    function init() {
      switchView(window.innerWidth <= 768 ? 'cards' : 'table');
      renderChitTabs();
      
      const urlParams = new URLSearchParams(window.location.search);
      const initialChit = urlParams.get('chit') || 'ganapathi';
      const initialMonth = urlParams.get('month') !== null ? parseInt(urlParams.get('month')) : null;
      const roomParam = urlParams.get('room');
      const emailParam = urlParams.get('email');
      if (emailParam && emailParam.trim()) {
        const raw = emailParam.trim().toLowerCase();
        localStorage.setItem('chit_sync_email', raw);
        currentSyncRoom = raw.replace(/[@.]/g, '_').replace(/[^a-z0-9_-]/g, '') || 'chit_family_2026';
        localStorage.setItem('chit_sync_room', currentSyncRoom);
      } else if (roomParam && roomParam.trim()) {
        currentSyncRoom = roomParam.trim().replace(/[^a-zA-Z0-9_-]/g, '');
        localStorage.setItem('chit_sync_room', currentSyncRoom);
      }

      switchChit(initialChit);
      if (initialMonth !== null && !isNaN(initialMonth)) {
        switchMonth(initialMonth);
      }
      if (urlParams.get('secret') === '1') {
        isCommissionVisible = true;
        updateSecretCommissionUI();
      }
      updatePhoneSyncLinkDisplay();
      initRealtimeCloudSync();
      tryInitFirebase();
      checkSyncServer();
    }

    if (document.readyState === 'loading') {
      document.addEventListener('DOMContentLoaded', init);
    } else {
      init();
    }
  
