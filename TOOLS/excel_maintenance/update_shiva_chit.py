import os
import shutil
import subprocess
import openpyxl
from openpyxl.styles import Font, PatternFill, Alignment, Border, Side
from PIL import Image

shiva_dir = r'd:\CHIT\02.SHIVA'
wb_path = os.path.join(shiva_dir, 'workbook shiva.xlsx')
backup_path = r'd:\CHIT\WORKSPACE\workbook_shiva_backup.xlsx'

# Create safe backup
shutil.copyfile(wb_path, backup_path)
print(f"Backup created at: {backup_path}")

edge_exe = r'C:\Program Files (x86)\Microsoft\Edge\Application\msedge.exe'
images_dir = os.path.join(shiva_dir, 'Monthly Images')
os.makedirs(images_dir, exist_ok=True)

# 12-month schedule for Shiva Chit from Shiva chit.jpg / Main chit shiva.xlsx
shiva_plan = [
    {
        'num': '01',
        'tab_name': 'MARCH',
        'month_full': 'March',
        'year': '2026',
        'person': 'Pavan',
        'bid_amount': 9500,
        'payout': 105000,
    },
    {
        'num': '02',
        'tab_name': 'APRIL',
        'month_full': 'April',
        'year': '2026',
        'person': 'veda',
        'bid_amount': 9250,
        'payout': 105000,
    },
    {
        'num': '03',
        'tab_name': 'MAY',
        'month_full': 'May',
        'year': '2026',
        'person': 'Dharanya',
        'bid_amount': 9000,
        'payout': 105000,
    },
    {
        'num': '04',
        'tab_name': 'JUNE',
        'month_full': 'June',
        'year': '2026',
        'person': 'Rani',
        'bid_amount': 8750,
        'payout': 105000,
    },
    {
        'num': '05',
        'tab_name': 'JULY',
        'month_full': 'July',
        'year': '2026',
        'person': 'Chaitu',
        'bid_amount': 8500,
        'payout': 106500,
    },
    {
        'num': '06',
        'tab_name': 'AUGUST',
        'month_full': 'August',
        'year': '2026',
        'person': 'sukesh',
        'bid_amount': 8250,
        'payout': 106500,
    },
    {
        'num': '07',
        'tab_name': 'SEP',
        'month_full': 'September',
        'year': '2026',
        'person': 'sampath',
        'bid_amount': 8000,
        'payout': 106500,
    },
    {
        'num': '08',
        'tab_name': 'OCT',
        'month_full': 'October',
        'year': '2026',
        'person': 'vijay',
        'bid_amount': 7750,
        'payout': 107500,
    },
    {
        'num': '09',
        'tab_name': 'NOV',
        'month_full': 'November',
        'year': '2026',
        'person': 'sreedhar',
        'bid_amount': 7500,
        'payout': 107500,
    },
    {
        'num': '10',
        'tab_name': 'DEC',
        'month_full': 'December',
        'year': '2026',
        'person': 'Tharun',
        'bid_amount': 7250,
        'payout': 109000,
    },
    {
        'num': '11',
        'tab_name': 'JAN',
        'month_full': 'January',
        'year': '2027',
        'person': 'chaturya',
        'bid_amount': 7000,
        'payout': 110000,
    },
    {
        'num': '12',
        'tab_name': 'FEB',
        'month_full': 'February',
        'year': '2027',
        'person': 'mounika',
        'bid_amount': 10000,
        'payout': 112500,
    }
]

all_members = [item['person'] for item in shiva_plan]

# ==========================================
# PART 1: UPDATE WORKBOOK SHIVA.XLSX
# ==========================================
wb = openpyxl.load_workbook(wb_path)

font_title = Font(name='Calibri', size=16, bold=True)
font_header = Font(name='Calibri', size=11, bold=True, color='FFFFFF')
fill_navy = PatternFill(start_color='2F5597', end_color='2F5597', fill_type='solid')

font_taker = Font(name='Calibri', size=11, bold=True, color='000000')
fill_taker = PatternFill(start_color='FFFF0000', end_color='FFFF0000', fill_type='solid')

font_nontaker = Font(name='Calibri', size=11, bold=False, color='000000')
fill_nontaker = PatternFill(start_color='C6EFCE', end_color='C6EFCE', fill_type='solid')

font_bold = Font(name='Calibri', size=11, bold=True)
font_regular = Font(name='Calibri', size=11)

align_center = Alignment(horizontal='center', vertical='center')
align_left = Alignment(horizontal='left', vertical='center')

table_border = Border(
    left=Side(style='thin', color='000000'),
    right=Side(style='thin', color='000000'),
    top=Side(style='thin', color='000000'),
    bottom=Side(style='thin', color='000000')
)
currency_fmt = '"₹"\\ #,##0;[Red]"₹"\\ \\-#,##0'

# Months to generate/populate (leaving APRIL, MAY, JIUNE, JULY untouched)
sheets_to_update = ['MARCH', 'AUGUST', 'SEP', 'OCT', 'NOV', 'DEC', 'JAN', 'FEB']

takers_cum = []
for idx, item in enumerate(shiva_plan):
    takers_cum.append(item['person'])
    tab = item['tab_name']
    
    # Only update sheets that are blank or new
    if tab in sheets_to_update:
        if tab in wb.sheetnames:
            ws = wb[tab]
            # Clear old empty cells if any
            for r in range(1, max(ws.max_row + 1, 30)):
                for c in range(1, max(ws.max_column + 1, 10)):
                    ws.cell(r, c).value = None
        else:
            ws = wb.create_sheet(title=tab)
            
        ws.column_dimensions['A'].width = 24.0
        ws.column_dimensions['B'].width = 28.0
        ws.column_dimensions['C'].width = 28.0
        
        # Title
        ws.merge_cells('A1:C1')
        ws['A1'] = f"                       Shiva chit – {item['month_full']} Month {item['year']}"
        ws['A1'].font = font_title
        ws['A1'].alignment = align_center
        ws.row_dimensions[1].height = 28.0
        
        # Headers
        headers = [('A3', 'NAMES'), ('B3', 'AMOUNT Need to PAY'), ('C3', 'paid status ')]
        for cell_ref, text in headers:
            cell = ws[cell_ref]
            cell.value = text
            cell.font = font_header
            cell.fill = fill_navy
            cell.alignment = align_center
            cell.border = table_border
        ws.row_dimensions[3].height = 24.0
        
        # Member rows
        row_idx = 4
        # Takers
        for name in takers_cum:
            c_name = ws.cell(row=row_idx, column=1, value=name)
            c_name.font = font_taker
            c_name.fill = fill_taker
            c_name.alignment = align_left
            c_name.border = table_border
            
            c_amt = ws.cell(row=row_idx, column=2, value='₹ 10,000')
            c_amt.font = font_taker
            c_amt.fill = fill_taker
            c_amt.alignment = align_center
            c_amt.number_format = currency_fmt
            c_amt.border = table_border
            
            c_status = ws.cell(row=row_idx, column=3, value=None)
            c_status.font = font_regular
            c_status.border = table_border
            
            ws.row_dimensions[row_idx].height = 20.0
            row_idx += 1
            
        # Non-Takers
        nontakers_now = [p for p in all_members if p not in takers_cum]
        for name in nontakers_now:
            c_name = ws.cell(row=row_idx, column=1, value=name)
            c_name.font = font_nontaker
            c_name.fill = fill_nontaker
            c_name.alignment = align_left
            c_name.border = table_border
            
            c_amt = ws.cell(row=row_idx, column=2, value=item['bid_amount'])
            c_amt.font = font_nontaker
            c_amt.fill = fill_nontaker
            c_amt.alignment = align_center
            c_amt.number_format = currency_fmt
            c_amt.border = table_border
            
            c_status = ws.cell(row=row_idx, column=3, value=None)
            c_status.font = font_regular
            c_status.border = table_border
            
            ws.row_dimensions[row_idx].height = 20.0
            row_idx += 1
            
        # Total Collection Row
        ws.cell(row=16, column=1, value="Total Collection").font = font_bold
        ws.cell(row=16, column=1).alignment = align_center
        ws.cell(row=16, column=1).border = table_border
        
        total_val = len(takers_cum) * 10000 + len(nontakers_now) * item['bid_amount']
        c_tot = ws.cell(row=16, column=2, value=f"₹ {total_val:,}")
        c_tot.font = font_bold
        c_tot.alignment = align_center
        c_tot.border = table_border
        
        ws.cell(row=16, column=3, value=None).border = table_border
        ws.row_dimensions[16].height = 22.0
        
        # Counting Section
        payout = item['payout']
        net_counting = payout - 10000
        
        ws.cell(row=19, column=2, value=f"Amount counting - {item['person'].upper()}").font = font_bold
        ws.cell(row=19, column=2).alignment = align_center
        
        counting_summary = f"Total - {item['tab_name']} {payout:,} REMOVE 10,000 (SELF PAID)   BALANCE {net_counting:,} COUNTING"
        ws.cell(row=20, column=1, value=counting_summary).font = font_bold
        
        ws.cell(row=22, column=1, value="ONLINE / UPI").font = font_regular
        ws.cell(row=23, column=1, value="CASH").font = font_regular
        ws.cell(row=24, column=1, value="PENDING").font = font_regular
        ws.cell(row=25, column=1, value="CHIT OWNER BALANCE").font = font_regular
        
        c_net = ws.cell(row=27, column=3, value=net_counting)
        c_net.font = font_bold
        c_net.number_format = currency_fmt

# Reorder sheets to chronological order:
desired_order = ['MARCH', 'APRIL', 'MAY', 'JIUNE', 'JULY', 'AUGUST', 'SEP', 'OCT', 'NOV', 'DEC', 'JAN', 'FEB']
# Only reorder existing sheets in workbook
wb._sheets = [wb[s] for s in desired_order if s in wb.sheetnames] + [wb[s] for s in wb.sheetnames if s not in desired_order]

wb.save(wb_path)
print(f"Shiva Chit Workbook updated successfully: {wb_path}")


# ==========================================
# PART 2: CREATE ALL 12 ANNOUNCEMENT IMAGES
# ==========================================
html_template = """<!DOCTYPE html>
<html lang="en">
<head>
<meta charset="UTF-8">
<style>
  * {
    margin: 0;
    padding: 0;
    box-sizing: border-box;
    font-family: Arial, "Helvetica Neue", Helvetica, sans-serif;
  }
  body {
    width: 1536px;
    height: 1024px;
    background-color: #ffffff;
    margin: 0;
    padding: 0;
    overflow: hidden;
  }
  .title-container {
    height: 106px;
    display: flex;
    align-items: center;
    justify-content: center;
    padding-top: 10px;
  }
  .title {
    font-size: 42px;
    font-weight: 700;
    color: #000000;
    letter-spacing: -0.5px;
  }
  .table-container {
    width: 1480px;
    margin: 0 auto;
  }
  table {
    width: 100%;
    border-collapse: collapse;
    border: 2px solid #000000;
  }
  th {
    background-color: #033773;
    color: #ffffff;
    font-size: 26px;
    font-weight: 700;
    height: 68px;
    border: 2px solid #000000;
    text-align: center;
    vertical-align: middle;
  }
  td {
    border: 2px solid #000000;
    height: 68px;
    font-size: 28px;
    font-weight: 700;
    vertical-align: middle;
  }
  .col-no {
    width: 134px;
    text-align: center;
  }
  .col-name {
    width: 652px;
    text-align: left;
    padding-left: 28px;
  }
  .col-amt {
    width: 694px;
    text-align: center;
  }
  .taker {
    background-color: #e00201;
    color: #ffffff;
  }
  .nontaker {
    background-color: #bfeab4;
    color: #000000;
  }
</style>
</head>
<body>
  <div class="title-container">
    <div class="title"><!--TITLE--></div>
  </div>
  <div class="table-container">
    <table>
      <thead>
        <tr>
          <th class="col-no">No.</th>
          <th class="col-name" style="text-align: center;">Name</th>
          <th class="col-amt">Amount Need to Pay</th>
        </tr>
      </thead>
      <tbody>
        <!--ROWS-->
      </tbody>
    </table>
  </div>
</body>
</html>
"""

takers_cum_img = []
for item in shiva_plan:
    takers_cum_img.append(item['person'])
    nontakers_cum_img = [p for p in all_members if p not in takers_cum_img]
    
    title = f"Shiva Chit – {item['month_full']} Month {item['year']}"
    file_name = f"{item['num']}. {item['month_full'].upper()} - {item['year']}.jpg"
    
    rows_html = []
    idx = 1
    for name in takers_cum_img:
        rows_html.append(f"""
        <tr class="taker">
          <td class="col-no">{idx}</td>
          <td class="col-name">{name}</td>
          <td class="col-amt">&#8377;10,000</td>
        </tr>
        """)
        idx += 1
        
    for name in nontakers_cum_img:
        rows_html.append(f"""
        <tr class="nontaker">
          <td class="col-no">{idx}</td>
          <td class="col-name">{name}</td>
          <td class="col-amt">&#8377;{item['bid_amount']:,}</td>
        </tr>
        """)
        idx += 1
        
    html_content = html_template.replace('<!--TITLE-->', title).replace('<!--ROWS-->', "".join(rows_html))
    
    temp_html = os.path.join(r'd:\CHIT\WORKSPACE', f"temp_shiva_{item['num']}.html")
    with open(temp_html, 'w', encoding='utf-8') as f:
        f.write(html_content)
        
    temp_png = os.path.join(r'd:\CHIT\WORKSPACE', f"temp_shiva_{item['num']}.png")
    final_jpg = os.path.join(images_dir, file_name)
    
    cmd = [
        edge_exe,
        '--headless',
        '--disable-gpu',
        '--force-device-scale-factor=1',
        f'--screenshot={temp_png}',
        '--window-size=1536,1024',
        f'file:///{temp_html.replace(os.sep, "/")}'
    ]
    subprocess.run(cmd, check=True)
    
    img = Image.open(temp_png)
    img.convert('RGB').save(final_jpg, 'JPEG', quality=95)
    print(f"Generated {file_name}")
    
    if os.path.exists(temp_html):
        os.remove(temp_html)
    if os.path.exists(temp_png):
        os.remove(temp_png)

print("All 12 Shiva Chit images generated successfully!")
