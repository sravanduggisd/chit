import urllib.request
import json

topic = 'chit_vault_sravan_live_sync_2026'
req = urllib.request.Request(f'https://ntfy.sh/{topic}/json?poll=1')
res = urllib.request.urlopen(req)
lines = [json.loads(l) for l in res.read().decode('utf-8').strip().split('\n') if l]
print(f"Total messages in stream: {len(lines)}")

latest = None
latest_time = 0
for item in lines:
    if 'message' in item:
        try:
            m = json.loads(item['message'])
            if m.get('lastUpdated', 0) > latest_time:
                latest_time = m.get('lastUpdated')
                latest = m
        except Exception:
            pass

if latest and 'vault' in latest:
    print('Latest Stream Update Device:', latest.get('device'))
    print('Vault keys:', list(latest['vault'].keys()))
    notes_found = 0
    for k, v in latest['vault'].items():
        if isinstance(v, dict):
            for mk, mv in v.items():
                if isinstance(mv, dict) and mv.get('note'):
                    print(f"  -> [NOTE] Month: {k}, Member: {mk}, Note: '{mv.get('note')}'")
                    notes_found += 1
    if notes_found == 0:
        print("No member notes in the latest vault payload yet.")
else:
    print("No valid vault payload in stream yet.")
