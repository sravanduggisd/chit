import json

with open(r'd:\CHIT\WORKSPACE\ganapathi_sheet_analysis.json', 'r', encoding='utf-8') as f:
    data = json.load(f)

with open(r'd:\CHIT\WORKSPACE\readable_summary.txt', 'w', encoding='utf-8') as out:
    for sheet, content in data.items():
        out.write(f"=== SHEET: {sheet} ===\n")
        out.write(f"Merged cells: {content['merged_cells']}\n")
        for r in content['rows']:
            items = []
            for c in r['cells']:
                if c['val'] is not None:
                    items.append(f"C{c['col']}: {c['val']}")
            out.write(f"R{r['row']:2d}: " + " | ".join(items) + "\n")
        out.write("\n")

print("readable_summary.txt written")
