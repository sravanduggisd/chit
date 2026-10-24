# Chit Fund Tracker

A local-first payment tracker and set of management tools for four 12-month chit groups: Ganapathi, Shiva, Venkateshwara, and Ranganadh.

## Start the app

- **Windows desktop:** double-click `Open_Chit_Tracker.bat`.
- **Mobile on the same Wi-Fi:** double-click `MAIN/Run_Server_For_Mobile.bat`, keep its window open, and open the displayed computer address on the phone.
- **Deploy as a website/PWA:** publish the contents of `MAIN/` with a static host. The app entry point is `MAIN/index.html`.

Payment status, mode, notes, and month locks are stored in the browser's local storage. Different browsers/devices have separate local data unless cloud or local-server sync is configured and reachable. The app's cloud connection uses Firebase Realtime Database; the configured database currently rejects anonymous reads with HTTP 401, so verify database rules/authentication before relying on cloud sync. The Wi-Fi server syncs through `MAIN/server.py` while that server is running.

Use the app's **Export Backup** action to download a JSON backup and **Restore Backup** to load one. `MAIN/backup_manager.py` only copies `MAIN/chit_sync_data.json` when manually run; it does not automatically back up browser local storage.

## Project map

| Path | Contents |
| --- | --- |
| `MAIN/` | Deployable app, PWA assets, local Wi-Fi server, and app documentation. |
| `01.GANAPATHI/` … `04.Ranganadh Chit/` | Source workbooks, reference artwork/PDFs, and 12 monthly JPG cards per chit. |
| `TOOLS/excel_maintenance/` | Scripts that generate/update workbooks and some monthly cards. The Ranganadh script rebuilds its workbook and all 12 cards. |
| `IMAGE_GENERATOR/` | Ganapathi and Shiva image-generation scripts/templates. |
| `TOOLS/` | Python validation scripts, maintenance scripts, and developer utilities. |
| `ARCHIVE/` | Older app and workbook copies retained for reference/rollback. |

The app's chit schedules and base amounts are embedded in `MAIN/index.html`. Current Ranganadh member data is also in `TOOLS/excel_maintenance/create_ranganadh_chit.py`; update both sources when changing that schedule.

## Tests

The test scripts expect this project at `D:\CHIT` and require Python packages `openpyxl` and `Pillow` for workbook/image checks. Run from PowerShell:

```powershell
python TOOLS/test_chit_suite.py
python TOOLS/test_edge_cases_comprehensive.py
python TOOLS/test_math_and_logic_simulation.py
```

These checks include static source inspections and mathematical simulations; they are not a full browser end-to-end test. The edge-case suite also performs an anonymous Firebase ping, which currently returns HTTP 401 and causes that one check to fail. A successful structural test does not verify authenticated multi-device sync.

## Before pushing to Git

This folder is not currently initialized as a Git repository. Chit workbooks and app source contain member names and financial schedules. Create a **private** remote repository and review the staged changes before pushing. `.gitignore` excludes Python cache files and local sync data, but intentionally does not exclude workbooks, images, or historical backups.
