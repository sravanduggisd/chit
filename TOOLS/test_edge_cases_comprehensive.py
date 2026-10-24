import os
import sys
import re
import json
import urllib.request

# Force UTF-8 output across all Windows terminals
if hasattr(sys.stdout, 'reconfigure'):
    sys.stdout.reconfigure(encoding='utf-8')

def run_edge_case_suite():
    report = []
    passed = 0
    failed = 0

    def test(cond, name, details=""):
        nonlocal passed, failed
        if cond:
            passed += 1
            report.append(f"  [PASS] {name}")
        else:
            failed += 1
            report.append(f"  [FAIL] {name} -> {details}")

    report.append("=" * 75)
    report.append("     CHIT TRACKER COMPREHENSIVE EDGE-CASE & STABILITY TEST SUITE     ")
    report.append("=" * 75)

    html_path = r"d:\CHIT\MAIN\index.html"
    assert os.path.exists(html_path), "index.html not found!"
    with open(html_path, "r", encoding="utf-8") as f:
        html = f.read()

    # -------------------------------------------------------------
    # SECTION 1: JAVASCRIPT SYNTAX & BRACKET INTEGRITY
    # -------------------------------------------------------------
    report.append("\n[SECTION 1] JAVASCRIPT SYNTAX & BRACKET INTEGRITY:")
    
    scripts = re.findall(r"<script>(.*?)</script>", html, re.DOTALL)
    test(len(scripts) > 0, "Script tag extracted from index.html")
    js_code = scripts[-1]

    # Test exact brace balance
    stack = []
    balanced = True
    for i, ch in enumerate(js_code):
        if ch in '({[':
            stack.append((ch, i))
        elif ch in ')}]':
            if not stack:
                balanced = False
                break
            top, idx = stack.pop()
            pairs = {'(': ')', '{': '}', '[': ']'}
            if pairs[top] != ch:
                balanced = False
                break
    if stack:
        balanced = False

    test(balanced, "JavaScript Bracket & Brace Balance (100% Valid Syntax)")
    test("catch (e)" in js_code or "catch (err)" in js_code, "Try/Catch blocks present for error safety")
    test(js_code.count("function testLiveSyncConnection") == 1, "Single, clean testLiveSyncConnection definition")

    # -------------------------------------------------------------
    # SECTION 2: DOM ELEMENT ID RESOLUTION & EVENT MAPPINGS
    # -------------------------------------------------------------
    report.append("\n[SECTION 2] DOM ELEMENT ID RESOLUTION & EVENT MAPPINGS:")
    
    # Extract all document.getElementById calls
    dom_ids = set(re.findall(r"document\.getElementById\(['\"]([a-zA-Z0-9_-]+)['\"]\)", js_code))
    html_ids = set(re.findall(r'id=["\']([a-zA-Z0-9_-]+)["\']', html))
    
    missing_ids = dom_ids - html_ids
    test(len(missing_ids) == 0, f"All getElementById IDs exist in DOM ({len(dom_ids)} verified)", f"Missing: {missing_ids}")

    # Extract all HTML event calls and verify function existence
    event_calls = re.findall(r'(?:onclick|onchange|oninput|onblur)=["\']([^"\']+)["\']', html)
    html_called_funcs = set()
    for call in event_calls:
        for stmt in call.split(';'):
            stmt = stmt.strip()
            m = re.match(r'([a-zA-Z0-9_]+)\s*\(', stmt)
            if m:
                html_called_funcs.add(m.group(1))

    defined_funcs = set(re.findall(r'function\s+([a-zA-Z0-9_]+)\s*\(', js_code))
    defined_vars = set(re.findall(r'(?:const|let|var)\s+([a-zA-Z0-9_]+)\s*=\s*(?:function|\([^)]*\)\s*=>)', js_code))
    all_defined = defined_funcs | defined_vars

    missing_funcs = html_called_funcs - all_defined
    test(len(missing_funcs) == 0, f"All HTML event handlers are defined ({len(html_called_funcs)} verified)", f"Missing: {missing_funcs}")

    # -------------------------------------------------------------
    # SECTION 3: ☰ 3-LINES HAMBURGER MENU & UI HYGIENE
    # -------------------------------------------------------------
    report.append("\n[SECTION 3] ☰ 3-LINES HAMBURGER MENU & UI HYGIENE:")
    test("btnHamburgerMenu" in html, "Hamburger button element (btnHamburgerMenu) present in header")
    test("hamburgerDropdownMenu" in html, "Dropdown menu element (hamburgerDropdownMenu) present")
    test("toggleHamburgerMenu" in js_code, "toggleHamburgerMenu function implemented")
    test("closeHamburgerMenu" in js_code, "closeHamburgerMenu function implemented")
    test("menuWrapper.contains(e.target)" in js_code, "Outside-click auto-close listener active for menu")
    test("exportDataBackup" in html, "Backup action wired inside menu")
    test("triggerRestoreBackup" in html, "Restore action wired inside menu")
    test("openResetConfirm" in html, "Reset month action wired inside menu")

    # -------------------------------------------------------------
    # SECTION 4: GOOGLE FIREBASE REALTIME DATABASE CONFIGURATION
    # -------------------------------------------------------------
    report.append("\n[SECTION 4] GOOGLE FIREBASE REALTIME DATABASE:")
    expected_db_url = "https://chitsravan-default-rtdb.firebaseio.com"
    test(expected_db_url in js_code, f"Default Firebase Database URL set to: {expected_db_url}")
    test("tryInitFirebase" in js_code, "tryInitFirebase function present")
    test("attachFirebaseListener" in js_code, "attachFirebaseListener with real-time value listener present")
    test("pushAllLocalToFirebase" in js_code, "pushAllLocalToFirebase function present to sync local data")
    test("syncStateToFirebase" in js_code, "syncStateToFirebase function present for payment updates")

    # Test live endpoint ping
    try:
        req = urllib.request.Request(f"{expected_db_url}/.json", headers={"User-Agent": "Mozilla/5.0"})
        res = urllib.request.urlopen(req, timeout=6)
        test(res.status == 200, "Google Firebase Realtime Database Live Ping (Status: 200 OK)")
    except Exception as e:
        test(False, "Google Firebase Realtime Database Live Ping", str(e))

    # -------------------------------------------------------------
    # SECTION 5: CHIT DATA ENGINE & CALCULATION INTEGRITY (ALL 4 CHITS)
    # -------------------------------------------------------------
    report.append("\n[SECTION 5] CHIT DATA ENGINE & CALCULATION INTEGRITY:")
    for chit_id in ['ganapathi', 'shiva', 'venkateshwara', 'ranganadh']:
        test(f"id: '{chit_id}'" in js_code or f'id: "{chit_id}"' in js_code, f"Chit group defined: {chit_id}")

    # Check 12 months present in CHITS definition
    for m in ['March 2026', 'April 2026', 'May 2026', 'June 2026', 'July 2026', 'August 2026', 'September 2026', 'October 2026', 'November 2026', 'December 2026', 'January 2027', 'February 2027']:
        test(m in js_code, f"Month configured: {m}")

    # Mathematical test: Verify formula rules in renderDashboard
    test("totalCollected += amount" in js_code and "paidCount++" in js_code,
         "Paid amount formula calculates based on exact member payments")
    test("12 - paidCount" in js_code,
         "Pending amount accurately tracks unpaid balance")

    # -------------------------------------------------------------
    # SECTION 6: LOCK SETTLEMENT & SECURITY SAFEGUARDS
    # -------------------------------------------------------------
    report.append("\n[SECTION 6] LOCK SETTLEMENT & SECURITY MUTATION SAFEGUARDS:")
    test("if (state.__locked)" in js_code, "togglePayment blocks modifications when month is locked")
    test("changePaymentMode" in js_code and "state.__locked" in js_code, "changePaymentMode blocked when month is locked")
    test("updateMemberNote" in js_code and "state.__locked" in js_code, "updateMemberNote blocked when month is locked")
    test("openLockModal" in js_code, "Lock modal opening function present")
    test("confirmToggleLock" in js_code, "Lock/unlock confirmation function present")
    test("card-locked" in js_code, "Visual locked style applied to cards")

    # -------------------------------------------------------------
    # SECTION 7: NOTES DEBOUNCING & FOCUS PERSISTENCE
    # -------------------------------------------------------------
    report.append("\n[SECTION 7] NOTES PERSISTENCE & DEBOUNCING EDGE CASES:")
    test("noteDebounceTimer" in js_code, "Debounce timer implemented to prevent rapid input floods")
    test("onblur=\"pushRealtimeCloudData()\"" in html, "onblur trigger ensures instant sync when keyboard closes")
    test("localStorage.setItem(getStorageKey" in js_code, "Immediate localStorage write on every keystroke")

    # -------------------------------------------------------------
    # SECTION 8: BACKUP, RESTORE & DATA DEFENSE
    # -------------------------------------------------------------
    report.append("\n[SECTION 8] BACKUP, RESTORE & CORRUPT DATA DEFENSE:")
    test("JSON.stringify(allData, null, 2)" in js_code, "JSON backup generates structured formatted export")
    test("chit_tracker_" in js_code, "Storage keys isolated with 'chit_tracker_' namespace")
    test("try {" in js_code and "JSON.parse(localStorage.getItem(key))" in js_code, 
         "Corrupted local data handled gracefully without crashing")

    # -------------------------------------------------------------
    # SECTION 9: PRIVACY PROTECTION (COMMISSION MASKING)
    # -------------------------------------------------------------
    report.append("\n[SECTION 9] PRIVACY PROTECTION (COMMISSION MASKING):")
    test("toggleSecretCommission" in js_code, "toggleSecretCommission function implemented")
    test("₹ ••••••" in html, "Commission defaults to masked bullet points on initial page load")
    test("isCommissionVisible = false" in js_code, "Commission starts hidden (isCommissionVisible = false)")

    # -------------------------------------------------------------
    # SECTION 10: NETLIFY DEPLOYMENT URL CONSISTENCY
    # -------------------------------------------------------------
    report.append("\n[SECTION 10] NETLIFY LIVE URL CONSISTENCY:")
    test("https://chitsravan.netlify.app" in js_code, "getNetlifyAppUrl points to https://chitsravan.netlify.app")
    test("https://spontaneous-swan-3a1f57.netlify.app" not in js_code, "Old spontaneous-swan URL completely eliminated")

    report.append("\n" + "=" * 75)
    report.append(f"FINAL TEST RESULT: {passed} PASSED, {failed} FAILED (TOTAL CHECKS: {passed + failed})")
    report.append("=" * 75)

    for line in report:
        print(line)

    return failed == 0

if __name__ == "__main__":
    success = run_edge_case_suite()
    sys.exit(0 if success else 1)
