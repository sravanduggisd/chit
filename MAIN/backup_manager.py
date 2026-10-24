"""
================================================================================
CHIT FUND TRACKER - AUTOMATIC BACKUP UTILITY
================================================================================
Usage:
  python backup_manager.py

What it does:
  - Takes a timestamped snapshot of your `chit_sync_data.json`
  - Saves it safely in `d:/CHIT/MAIN/backups/chit_backup_YYYYMMDD_HHMMSS.json`
  - Allows you to easily restore if you ever need to roll back
================================================================================
"""

import os
import shutil
from datetime import datetime

BASE_DIR = os.path.dirname(os.path.abspath(__file__))
DATA_FILE = os.path.join(BASE_DIR, 'chit_sync_data.json')
BACKUP_DIR = os.path.join(BASE_DIR, 'backups')


def create_backup():
    if not os.path.exists(BACKUP_DIR):
        os.makedirs(BACKUP_DIR)

    if not os.path.exists(DATA_FILE):
        print(f"[INFO] No sync data file found yet at: {DATA_FILE}")
        print("Once you make changes in the app or run server.py, data will be created.")
        return

    timestamp = datetime.now().strftime('%Y%m%d_%H%M%S')
    backup_filename = f"chit_backup_{timestamp}.json"
    dest_path = os.path.join(BACKUP_DIR, backup_filename)

    shutil.copy2(DATA_FILE, dest_path)
    file_size = os.path.getsize(dest_path)
    print("=" * 60)
    print("[SUCCESS] CHIT FUND DATA BACKUP COMPLETED!")
    print("=" * 60)
    print(f" Source : {DATA_FILE}")
    print(f" Backup : {dest_path}")
    print(f" Size   : {file_size} bytes")
    print("=" * 60)


def list_backups():
    if not os.path.exists(BACKUP_DIR):
        print("No backups directory found yet.")
        return

    files = sorted([f for f in os.listdir(BACKUP_DIR) if f.endswith('.json')])
    if not files:
        print("No previous backups found.")
        return

    print("\nRecent Backups:")
    for f in files[-10:]:
        fpath = os.path.join(BACKUP_DIR, f)
        print(f" - {f} ({os.path.getsize(fpath)} bytes)")


if __name__ == '__main__':
    create_backup()
    list_backups()
