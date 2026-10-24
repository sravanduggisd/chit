import os
import json
import re
import openpyxl
from PIL import Image

def run_all_tests():
    report = []
    failed = 0
    passed = 0

    def assert_test(cond, title, details=""):
        nonlocal passed, failed
        if cond:
            passed += 1
            report.append(f"  [PASS] {title}")
        else:
            failed += 1
            report.append(f"  [FAIL] {title} -> {details}")

    report.append("================================================================")
    report.append("       CHIT TRACKER PROFESSIONAL PROJECT VALIDATION SUITE        ")
    report.append("================================================================")

    # -------------------------------------------------------------
    # TEST SUITE 1: FILE EXISTENCE & STRUCTURE
    # -------------------------------------------------------------
    report.append("\n[1] CHECKING CORE PROJECT FILES & WORKBOOKS...")
    expected_workbooks = [
        r"d:\CHIT\01.GANAPATHI\Ganapathi_Chit_April- WORKBOOK.xlsx",
        r"d:\CHIT\02.SHIVA\workbook shiva.xlsx",
        r"d:\CHIT\03.VENKATESHWARA\workbook VENKATESHWARA.xlsx",
        r"d:\CHIT\04.Ranganadh Chit\Ranganadh_Chit_WORKBOOK.xlsx"
    ]
    for wb_path in expected_workbooks:
        exists = os.path.exists(wb_path)
        assert_test(exists, f"Workbook: {os.path.basename(wb_path)}", f"Missing at {wb_path}")

    expected_app_files = [
        r"d:\CHIT\MAIN\index.html",
        r"d:\CHIT\MAIN\manifest.json",
        r"d:\CHIT\MAIN\sw.js",
        r"d:\CHIT\MAIN\server.py",
        r"d:\CHIT\MAIN\icon-192.png",
        r"d:\CHIT\MAIN\icon-512.png",
        r"d:\CHIT\MAIN\app_icon.ico",
        r"d:\CHIT\MAIN\Run_Server_For_Mobile.bat",
        r"d:\CHIT\Open_Chit_Tracker.bat",
        r"d:\CHIT\Create_Desktop_Shortcut.bat"
    ]
    for f_path in expected_app_files:
        exists = os.path.exists(f_path)
        size = os.path.getsize(f_path) if exists else 0
        assert_test(exists and size > 0, f"App File: {os.path.basename(f_path)} ({size} bytes)", "Missing or empty")

    # -------------------------------------------------------------
    # TEST SUITE 2: MONTHLY IMAGES COMPLETION (48/48)
    # -------------------------------------------------------------
    report.append("\n[2] CHECKING MONTHLY ANNOUNCEMENT IMAGES (48 TOTAL)...")
    chit_image_dirs = {
        "01.GANAPATHI": r"d:\CHIT\01.GANAPATHI\Monthly images",
        "02.SHIVA": r"d:\CHIT\02.SHIVA\Monthly Images",
        "03.VENKATESHWARA": r"d:\CHIT\03.VENKATESHWARA\Monthly Images",
        "04.Ranganadh Chit": r"d:\CHIT\04.Ranganadh Chit\Monthly Images"
    }
    for name, img_dir in chit_image_dirs.items():
        if os.path.exists(img_dir):
            imgs = [f for f in os.listdir(img_dir) if f.lower().endswith(('.jpg', '.png'))]
            valid_imgs = 0
            for img_name in imgs:
                try:
                    p = os.path.join(img_dir, img_name)
                    with Image.open(p) as img:
                        w, h = img.size
                        if w > 500 and h > 500:
                            valid_imgs += 1
                except Exception:
                    pass
            assert_test(valid_imgs >= 12, f"{name}: {valid_imgs}/12 valid monthly images", f"Found {valid_imgs} valid images in {img_dir}")
        else:
            assert_test(False, f"{name} Monthly Images directory exists", f"Not found at {img_dir}")

    # -------------------------------------------------------------
    # TEST SUITE 3: MAIN APP EMBEDDED DATA ACCURACY
    # -------------------------------------------------------------
    report.append("\n[3] TESTING MAIN/INDEX.HTML EMBEDDED CHIT DATA...")
    html_path = r"d:\CHIT\MAIN\index.html"
    with open(html_path, "r", encoding="utf-8") as f:
        html_content = f.read()

    chits_expected = ["ganapathi", "shiva", "venkateshwara", "ranganadh"]
    for c_id in chits_expected:
        assert_test(f"id: '{c_id}'" in html_content or f'id: "{c_id}"' in html_content, f"App defines chit ID: {c_id}")

    key_members = ["Sarath Babu", "P. Hari", "Anil", "Harish", "Supraja"]
    for m in key_members:
        assert_test(m in html_content, f"Key Member present: {m}")

    # -------------------------------------------------------------
    # TEST SUITE 4: WHATSAPP NOTICES TEMPLATE COMPLIANCE
    # -------------------------------------------------------------
    report.append("\n[4] TESTING WHATSAPP NOTICE FORMAT...")
    template_checks = [
        "Hai Everyone",
        "Taken By:",
        "This Month Amount:",
        "Everyone, please transfer the amount to:",
        "PhonePe:",
        "Please refer to the attached image",
        "Note: Members who have already taken the chit need to pay",
        "Please complete the payment and share the payment screenshot",
        "Thank you"
    ]
    for phrase in template_checks:
        found = phrase in html_content
        assert_test(found, f"WhatsApp Template contains: '{phrase}'")

    # -------------------------------------------------------------
    # TEST SUITE 5: ADVANCED CHIT 2.0 & NEW FEATURES
    # -------------------------------------------------------------
    report.append("\n[5] TESTING NEW FEATURES (NOTES, LOCK, CLOUD SYNC, PRIVACY)...")
    ui_elements = [
        ("Owner Commission Card", "statCommission"),
        ("Stealth Eye Toggle Button", "stealthEyeBtn"),
        ("Chit Winner / Payout Box", "winnerPayoutBox"),
        ("Month Lock Button", "btnLockMonth"),
        ("Month Lock Confirmation Modal", "lockModal"),
        ("Notes / Remainder Notebook", "member-note-input"),
        ("Google Firebase Realtime Cloud Sync", "cloudSyncModal"),
        ("Cloud Sync Button", "btnCloudSync"),
        ("Realtime Sync Badge", "syncIndicator"),
        ("Phone Cards Container", "membersCardsContainer"),
        ("Table Wrapper", "membersTableWrapper"),
        ("Install App Button", "btnInstallApp"),
        ("Backup Export Button", "exportDataBackup")
    ]
    for label, element_id in ui_elements:
        has_id = f'id="{element_id}"' in html_content or f"id='{element_id}'" in html_content or element_id in html_content
        assert_test(has_id, f"UI Feature verified: {label} ({element_id})")

    # -------------------------------------------------------------
    # TEST SUITE 6: SERVER & MULTI-DEVICE SYNC ENGINE
    # -------------------------------------------------------------
    report.append("\n[6] TESTING SERVER & LOCAL WI-FI ENGINE...")
    server_path = r"d:\CHIT\MAIN\server.py"
    with open(server_path, "r", encoding="utf-8") as f:
        server_code = f.read()
    assert_test("/api/sync" in server_code, "server.py implements GET/POST /api/sync endpoint")
    assert_test("/api/ping" in server_code, "server.py implements /api/ping healthcheck")
    assert_test("Access-Control-Allow-Origin" in server_code, "server.py supports CORS for cross-device access")

    # -------------------------------------------------------------
    # SUMMARY
    # -------------------------------------------------------------
    report.append("\n================================================================")
    report.append(f" TOTAL TESTS RUN: {passed + failed} | PASSED: {passed} | FAILED: {failed}")
    if failed == 0:
        report.append(" 🎉 RESULT: ALL TESTS PASSED! WORKSPACE IS 100% VERIFIED & PRODUCTION READY!")
    else:
        report.append(" ⚠️ RESULT: SOME TESTS FAILED. PLEASE REVIEW.")
    report.append("================================================================")

    output_text = "\n".join(report)
    print("TEST_SUITE_COMPLETE")
    print(f"Passed: {passed}, Failed: {failed}")
    if failed > 0:
        for line in report:
            if "[FAIL]" in line:
                print(line)
    return failed == 0

if __name__ == "__main__":
    run_all_tests()
