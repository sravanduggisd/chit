# Main app and deployment

`index.html` is the browser app. `manifest.json`, `sw.js`, icons, and `assets/` provide its installable PWA resources. Publish the contents of this folder to a static web host, or open `index.html` locally for single-device use.

## Data and sync

- Payment state, payment mode, member notes, and month-lock state are saved in the current browser's `localStorage`.
- `server.py` serves this folder and provides `/api/sync` for devices using the same local Wi-Fi server. Start it with `Run_Server_For_Mobile.bat` and keep the server window open.
- The app also contains Firebase Realtime Database sync code. Its current configured database returns HTTP 401 to anonymous requests in the project's edge-case check. Configure database access/authentication and verify it from the app before relying on cloud sync.
- Use the app's Export Backup and Restore Backup actions for browser data. `backup_manager.py` is a separate manual utility that copies `chit_sync_data.json` if that server-side file exists; it does not automatically snapshot browser local storage.

## Deploy

Upload the complete `MAIN/` folder to a static host. Keep its relative assets alongside `index.html`. After publishing, open the site on a phone and use the browser's install/add-to-home-screen action.

For local Wi-Fi use, connect the computer and phone to the same network, run `Run_Server_For_Mobile.bat`, and visit `http://<computer-ip>:8080` on the phone.

## Important files

- `index.html`: app UI, embedded four-chit schedules, calculations, local storage, sync client, backup export/restore.
- `server.py`: static HTTP server and JSON sync API.
- `backup_manager.py`: manual backup of `chit_sync_data.json` only.
- `manifest.json`, `sw.js`, `icon-192.png`, `icon-512.png`, `app_icon.ico`: install/offline and desktop assets.
- `assets/gods/`: deity imagery used by the app.
