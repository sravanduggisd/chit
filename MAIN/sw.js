const CACHE_NAME = 'chit-tracker-v7-settlement';

// On install, activate immediately
self.addEventListener('install', (e) => {
  self.skipWaiting();
});

// On activate, immediately purge all older caches (v1, v2, etc.)
self.addEventListener('activate', (e) => {
  e.waitUntil(
    caches.keys().then((keys) => {
      return Promise.all(
        keys.map((k) => {
          if (k !== CACHE_NAME) {
            console.log('[SW] Purging outdated cache:', k);
            return caches.delete(k);
          }
        })
      );
    })
  );
  self.clients.claim();
});

// Network-First Strategy:
// Always fetch fresh code from the internet when online so updates are seen instantly.
// Falls back to offline cache only if user is disconnected.
self.addEventListener('fetch', (e) => {
  if (e.request.method !== 'GET') return;

  e.respondWith(
    fetch(e.request)
      .then((networkRes) => {
        if (networkRes && networkRes.status === 200 && e.request.url.startsWith('http')) {
          const resClone = networkRes.clone();
          caches.open(CACHE_NAME).then((cache) => cache.put(e.request, resClone));
        }
        return networkRes;
      })
      .catch(() => caches.match(e.request))
  );
});
