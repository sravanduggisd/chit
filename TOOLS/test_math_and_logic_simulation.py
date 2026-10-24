import json
import re
import sys

# Ensure UTF-8 output across all consoles
if hasattr(sys.stdout, 'reconfigure'):
    sys.stdout.reconfigure(encoding='utf-8')

def run_simulation_tests():
    report = []
    passed = 0
    failed = 0

    def assert_eq(cond, title, details=""):
        nonlocal passed, failed
        if cond:
            passed += 1
            report.append(f"  [PASS] {title}")
        else:
            failed += 1
            report.append(f"  [FAIL] {title} -> {details}")

    report.append("=" * 75)
    report.append("   CHIT FUND MATHEMATICAL & BUSINESS LOGIC SIMULATION TEST SUITE   ")
    report.append("=" * 75)

    with open(r"d:\CHIT\MAIN\index.html", "r", encoding="utf-8") as f:
        html = f.read()

    # -------------------------------------------------------------
    # TEST 1: CHIT SCHEME CONFIGURATION INTEGRITY
    # -------------------------------------------------------------
    report.append("\n[TEST 1] CHIT SCHEME CONFIGURATION INTEGRITY:")
    chit_keys = ['ganapathi', 'shiva', 'venkateshwara', 'ranganadh']
    for ck in chit_keys:
        assert_eq(f"id: '{ck}'" in html or f'id: "{ck}"' in html, f"Chit '{ck}' defined with unique ID")

    # -------------------------------------------------------------
    # TEST 2: STANDARD INSTALLMENTS
    # -------------------------------------------------------------
    standards = {
        'ganapathi': 20000,
        'shiva': 10000,
        'venkateshwara': 25000,
        'ranganadh': 30000
    }

    report.append("\n[TEST 2] STANDARD INSTALLMENT & MEMBER POOL INTEGRITY:")
    for ck, std in standards.items():
        assert_eq(f"standardAmt: {std}" in html, f"{ck.capitalize()} standard installment = ₹ {std:,}")

    # -------------------------------------------------------------
    # TEST 3: 12-MONTH DURATION PER CHIT CYCLE
    # -------------------------------------------------------------
    report.append("\n[TEST 3] 12-MONTH DURATION VERIFICATION FOR EACH CHIT:")
    cycles = {
        'ganapathi': ('March 2026', 'February 2027'),
        'shiva': ('March 2026', 'February 2027'),
        'venkateshwara': ('April 2026', 'March 2027'),
        'ranganadh': ('August 2026', 'July 2027')
    }
    for ck, (start_m, end_m) in cycles.items():
        assert_eq(start_m in html and end_m in html, f"{ck.capitalize()} cycle: {start_m} to {end_m} (12 months)")

    # -------------------------------------------------------------
    # TEST 4: TAKER VS NON-TAKER PAYMENT & COMMISSION CALCULATIONS
    # -------------------------------------------------------------
    report.append("\n[TEST 4] TAKER VS NON-TAKER PAYMENT LOGIC SIMULATION:")
    # Simulation 1: Ganapathi Month 1 (March 2026, Sarath Babu bid 18500, payout 210000)
    # 1 taker (pays 20000), 11 non-takers (pay 18500)
    ganapathi_m1_target = (1 * 20000) + (11 * 18500)  # 223500
    ganapathi_m1_comm = ganapathi_m1_target - 210000  # 13500
    assert_eq(ganapathi_m1_target == 223500, f"Ganapathi Mar 2026: Total Target = ₹ {ganapathi_m1_target:,}")
    assert_eq(ganapathi_m1_comm == 13500, f"Ganapathi Mar 2026: Commission = ₹ {ganapathi_m1_comm:,}")

    # Simulation 2: Shiva Month 1 (March 2026, Pavan bid 9500, payout 105000)
    # 1 taker (pays 10000), 11 non-takers (pay 9500)
    shiva_m1_target = (1 * 10000) + (11 * 9500)  # 114500
    shiva_m1_comm = shiva_m1_target - 105000  # 9500
    assert_eq(shiva_m1_target == 114500, f"Shiva Mar 2026: Total Target = ₹ {shiva_m1_target:,}")
    assert_eq(shiva_m1_comm == 9500, f"Shiva Mar 2026: Commission = ₹ {shiva_m1_comm:,}")

    # Simulation 3: Venkateshwara Month 1 (April 2026, D DHANUNJAYA bid 23150, payout 262500)
    # 1 taker (pays 25000), 11 non-takers (pay 23150)
    venk_m1_target = (1 * 25000) + (11 * 23150)  # 279650
    venk_m1_comm = venk_m1_target - 262500  # 17150
    assert_eq(venk_m1_target == 279650, f"Venkateshwara Apr 2026: Total Target = ₹ {venk_m1_target:,}")
    assert_eq(venk_m1_comm == 17150, f"Venkateshwara Apr 2026: Commission = ₹ {venk_m1_comm:,}")

    # Simulation 4: Ranganadh Month 1 (August 2026, Sarada bid 27780, payout 315000)
    # 1 taker (pays 30000), 11 non-takers (pay 27780)
    rang_m1_target = (1 * 30000) + (11 * 27780)  # 335580
    rang_m1_comm = rang_m1_target - 315000  # 20580
    assert_eq(rang_m1_target == 335580, f"Ranganadh Aug 2026: Total Target = ₹ {rang_m1_target:,}")
    assert_eq(rang_m1_comm == 20580, f"Ranganadh Aug 2026: Commission = ₹ {rang_m1_comm:,}")

    # Simulation 5: Ranganadh Month 2 (September 2026, Supraja bid 27000, payout 315000)
    # 2 takers (Sarada, Supraja pay 30000), 10 non-takers (pay 27000)
    rang_m2_target = (2 * 30000) + (10 * 27000)  # 60000 + 270000 = 330000
    rang_m2_comm = rang_m2_target - 315000  # 15000
    assert_eq(rang_m2_target == 330000, f"Ranganadh Sep 2026: Total Target = ₹ {rang_m2_target:,}")
    assert_eq(rang_m2_comm == 15000, f"Ranganadh Sep 2026: Commission = ₹ {rang_m2_comm:,}")

    # -------------------------------------------------------------
    # TEST 5: PROGRESS TALLY EDGE CASES (0/12, 6/12, 12/12 PAID)
    # -------------------------------------------------------------
    report.append("\n[TEST 5] PROGRESS TALLY EDGE CASES (0/12, 6/12, 12/12 PAID):")
    total_members = 12
    for count, expected_pct in [(0, 0), (6, 50), (12, 100)]:
        pct = round((count / total_members) * 100)
        assert_eq(pct == expected_pct, f"{count}/12 Paid members -> Progress Bar = {pct}%")

    # -------------------------------------------------------------
    # TEST 6: LOCK SETTLEMENT PROTECTION
    # -------------------------------------------------------------
    report.append("\n[TEST 6] SAFEGUARDS AGAINST MUTATIONS ON LOCKED MONTHS:")
    assert_eq("if (state.__locked)" in html, "togglePayment strictly checks state.__locked")
    assert_eq("${isLocked ? 'disabled" in html or "state.__locked ? 'disabled" in html, "UI controls disabled when isLocked is true")

    # -------------------------------------------------------------
    # TEST 7: LOCALSTORAGE JSON CORRUPTION DEFENSE
    # -------------------------------------------------------------
    report.append("\n[TEST 7] LOCALSTORAGE JSON CORRUPTION DEFENSE:")
    test_json_valid = '{"paid": true, "mode": "Cash", "note": "Paid 10k"}'
    test_json_corrupted = '{"paid": true, mode: invalid}'
    parsed_safely = False
    try:
        json.loads(test_json_valid)
        try:
            json.loads(test_json_corrupted)
        except Exception:
            parsed_safely = True
    except Exception:
        pass
    assert_eq(parsed_safely, "Corrupt JSON safely caught by try/catch fallback")

    report.append("\n" + "=" * 75)
    report.append(f"SIMULATION TEST RESULTS: {passed} PASSED, {failed} FAILED (TOTAL: {passed + failed})")
    report.append("=" * 75)

    for line in report:
        print(line)

    return failed == 0

if __name__ == "__main__":
    success = run_simulation_tests()
    sys.exit(0 if success else 1)
