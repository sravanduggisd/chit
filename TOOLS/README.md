# Project tools and checks

## Validation scripts

Run these from `D:\CHIT`:

```powershell
python TOOLS/test_chit_suite.py
python TOOLS/test_edge_cases_comprehensive.py
python TOOLS/test_math_and_logic_simulation.py
```

The structural suite checks required files, image presence/resolution, embedded app data, UI/source markers, and server endpoint strings. The edge-case suite checks source patterns and also makes an anonymous Firebase request; the configured database currently returns HTTP 401, so that live ping fails until database access is configured. The math suite contains calculations and source checks. Passing these scripts is useful but does not replace browser testing or a signed-in sync test.

The scripts currently use absolute `D:\CHIT` paths. Run the project from that location for their file checks to work.

## Maintenance and utilities

- `excel_maintenance/`: scripts that generate/update workbooks and associated monthly cards. `create_ranganadh_chit.py` rebuilds the Ranganadh workbook and all 12 cards, so review its schedule before running it.
- `dev_utilities/`: workbook inspections, previews, screenshots, and layout diagnostics. Some utilities write output to the older `D:\CHIT\WORKSPACE` location; check the script's paths before running one.
- Other scripts at the top of `TOOLS/` are historical app patchers, Firebase/sync configuration helpers, and diagnostics. Review a script before running it because some rewrite `MAIN/index.html`.

Python requirements for the workbook/image validation and maintenance scripts include `openpyxl` and `Pillow`. Image generation also requires a supported local Chromium-based browser.
