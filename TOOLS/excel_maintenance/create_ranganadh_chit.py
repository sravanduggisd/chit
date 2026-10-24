import os
import subprocess
import tempfile
import openpyxl
from openpyxl.styles import Font, PatternFill, Alignment, Border, Side
from PIL import Image

ranganadh_dir = r'd:\CHIT\04.Ranganadh Chit'
images_dir = os.path.join(ranganadh_dir, 'Monthly Images')
os.makedirs(images_dir, exist_ok=True)

edge_candidates = [
    r'C:\Program Files\Microsoft\Edge\Application\msedge.exe',
    r'C:\Program Files (x86)\Google\Chrome\Application\chrome.exe',
    r'C:\Program Files\Google\Chrome\Application\chrome.exe',
    r'C:\Program Files (x86)\Microsoft\Edge\Application\msedge.exe',
]
edge_exe = next((path for path in edge_candidates if os.path.isfile(path)), edge_candidates[0])

# 12 Months data structure from Ranganadh Chit.jpg
chit_plan = [
    {
        'num': '01',
        'month_short': 'AUG',
        'month_full': 'August',
        'year': '2026',
        'month_label': 'Aug-26',
        'person': 'Sarada',
        'bid_amount': 27780,
        'after_taken': 30000,
        'payout': 315000
    },
    {
        'num': '02',
        'month_short': 'SEP',
        'month_full': 'September',
        'year': '2026',
        'month_label': 'Sep-26',
        'person': 'Supraja',
        'bid_amount': 27000,
        'after_taken': 30000,
        'payout': 315000
    },
    {
        'num': '03',
        'month_short': 'OCT',
        'month_full': 'October',
        'year': '2026',
        'month_label': 'Oct-26',
        'person': 'Pavan',
        'bid_amount': 26280,
        'after_taken': 30000,
        'payout': 315000
    },
    {
        'num': '04',
        'month_short': 'NOV',
        'month_full': 'November',
        'year': '2026',
        'month_label': 'Nov-26',
        'person': 'Sravan',
        'bid_amount': 25500,
        'after_taken': 30000,
        'payout': 315000
    },
    {
        'num': '05',
        'month_short': 'DEC',
        'month_full': 'December',
        'year': '2026',
        'month_label': 'Dec-26',
        'person': 'Raki',
        'bid_amount': 24780,
        'after_taken': 30000,
        'payout': 319500
    },
    {
        'num': '06',
        'month_short': 'JAN',
        'month_full': 'January',
        'year': '2027',
        'month_label': 'Jan-27',
        'person': 'Dhana',
        'bid_amount': 24000,
        'after_taken': 30000,
        'payout': 319500
    },
    {
        'num': '07',
        'month_short': 'FEB',
        'month_full': 'February',
        'year': '2027',
        'month_label': 'Feb-27',
        'person': 'Satish',
        'bid_amount': 23280,
        'after_taken': 30000,
        'payout': 319500
    },
    {
        'num': '08',
        'month_short': 'MAR',
        'month_full': 'March',
        'year': '2027',
        'month_label': 'Mar-27',
        'person': 'Sudhamani',
        'bid_amount': 22500,
        'after_taken': 30000,
        'payout': 322500
    },
    {
        'num': '09',
        'month_short': 'APR',
        'month_full': 'April',
        'year': '2027',
        'month_label': 'Apr-27',
        'person': 'Harish',
        'bid_amount': 21780,
        'after_taken': 30000,
        'payout': 322500
    },
    {
        'num': '10',
        'month_short': 'MAY',
        'month_full': 'May',
        'year': '2027',
        'month_label': 'May-27',
        'person': 'Hari',
        'bid_amount': 21000,
        'after_taken': 30000,
        'payout': 327000
    },
    {
        'num': '11',
        'month_short': 'JUN',
        'month_full': 'June',
        'year': '2027',
        'month_label': 'Jun-27',
        'person': 'Mounika',
        'bid_amount': 20280,
        'after_taken': 30000,
        'payout': 330000
    },
    {
        'num': '12',
        'month_short': 'JUL',
        'month_full': 'July',
        'year': '2027',
        'month_label': 'Jul-27',
        'person': 'Swetha',
        'bid_amount': 30000,
        'after_taken': 30000,
        'payout': 337500
    }
]

all_members = [
    'Sarada', 'Supraja', 'Pavan', 'Sravan', 'Raki', 'Dhana',
    'Satish', 'Sudhamani', 'Harish', 'Hari', 'Mounika', 'Swetha'
]

# ==========================================
# PART 1: CREATE EXCEL WORKBOOK
# ==========================================
wb = openpyxl.Workbook()
ws_master = wb.active
ws_master.title = "Master Chit Tracker"

# Styles
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
currency_fmt = '"â‚¹"\\ #,##0;[Red]"â‚¹"\\ \\-#,##0'

# Master Sheet Content
ws_master.merge_cells('A1:F1')
ws_master['A1'] = "â‚¹3.6 Lakhs Ranganadh Chit Plan â€“ 12 Months"
ws_master['A1'].font = Font(name='Calibri', size=18, bold=True, color='002060')
ws_master['A1'].alignment = align_center

ws_master.merge_cells('A2:F2')
ws_master['A2'] = "Standard amount after taking chit: â‚¹30,000/month"
ws_master['A2'].font = Font(name='Calibri', size=12, bold=True, color='595959')
ws_master['A2'].alignment = align_center

master_headers = ['S.No', 'Month', 'Person', 'BID Amount', 'After Chit Taken', 'Fixed Amount Will Receive']
for col_idx, h_text in enumerate(master_headers, 1):
    cell = ws_master.cell(row=4, column=col_idx, value=h_text)
    cell.font = font_header
    cell.fill = fill_navy
    cell.alignment = align_center
    cell.border = table_border

for idx, item in enumerate(chit_plan, 1):
    r = 4 + idx
    ws_master.cell(row=r, column=1, value=idx).alignment = align_center
    ws_master.cell(row=r, column=2, value=item['month_label']).alignment = align_center
    ws_master.cell(row=r, column=3, value=item['person']).alignment = align_left
    
    c_bid = ws_master.cell(row=r, column=4, value=item['bid_amount'])
    c_bid.number_format = currency_fmt
    c_bid.alignment = align_center
    
    c_taken = ws_master.cell(row=r, column=5, value=item['after_taken'])
    c_taken.number_format = currency_fmt
    c_taken.alignment = align_center
    
    c_pay = ws_master.cell(row=r, column=6, value=item['payout'])
    c_pay.number_format = currency_fmt
    c_pay.alignment = align_center
    
    for c in range(1, 7):
        ws_master.cell(row=r, column=c).border = table_border
        ws_master.cell(row=r, column=c).font = font_bold if c in [1, 2, 3] else font_regular

for c, w in [('A', 10), ('B', 15), ('C', 22), ('D', 20), ('E', 20), ('F', 28)]:
    ws_master.column_dimensions[c].width = w

# 12 Individual Month Sheets
takers_so_far = []
for month_idx, item in enumerate(chit_plan):
    takers_so_far.append(all_members[month_idx])
    nontakers_now = [p for p in all_members if p not in takers_so_far]
    
    ws = wb.create_sheet(title=item['month_short'])
    
    ws.column_dimensions['A'].width = 22.0
    ws.column_dimensions['B'].width = 32.0
    ws.column_dimensions['C'].width = 28.0
    
    # Title
    ws.merge_cells('A1:C1')
    ws['A1'] = f"                       Ranganadh Chit - {item['month_full'].upper()} MONTH {item['year']}"
    ws['A1'].font = font_title
    ws['A1'].alignment = align_center
    ws.row_dimensions[1].height = 28.0
    
    # Headers
    headers = [('A3', 'Name'), ('B3', 'Amount Need to Pay'), ('C3', 'paid status ')]
    for cell_ref, text in headers:
        cell = ws[cell_ref]
        cell.value = text
        cell.font = font_header
        cell.fill = fill_navy
        cell.alignment = align_center
        cell.border = table_border
    ws.row_dimensions[3].height = 24.0
    
    # Rows 4 to 15
    row_idx = 4
    # Takers (Red fill, 30,000)
    for name in takers_so_far:
        c_name = ws.cell(row=row_idx, column=1, value=name)
        c_name.font = font_taker
        c_name.fill = fill_taker
        c_name.alignment = align_left
        c_name.border = table_border
        
        c_amt = ws.cell(row=row_idx, column=2, value='â‚¹ 30,000')
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
        
    # Non-Takers (Light green fill, bid_amount)
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
    
    total_val = len(takers_so_far) * 30000 + len(nontakers_now) * item['bid_amount']
    c_tot = ws.cell(row=16, column=2, value=f"â‚¹ {total_val:,}")
    c_tot.font = font_bold
    c_tot.alignment = align_center
    c_tot.border = table_border
    
    ws.cell(row=16, column=3, value=None).border = table_border
    ws.row_dimensions[16].height = 22.0
    
    # Amount Counting Section
    payout = item['payout']
    net_counting = payout - 30000
    
    ws.cell(row=19, column=2, value=f"Amount counting - {all_members[month_idx].upper()}").font = font_bold
    ws.cell(row=19, column=2).alignment = align_center
    
    counting_summary = f"Total - {item['month_short']} {payout:,} REMOVE 30,000 (SELF PAID)   BALANCE {net_counting:,} COUNTING"
    ws.cell(row=20, column=1, value=counting_summary).font = font_bold
    
    ws.cell(row=22, column=1, value="ONLINE / UPI").font = font_regular
    ws.cell(row=23, column=1, value="CASH").font = font_regular
    ws.cell(row=24, column=1, value="PENDING").font = font_regular
    ws.cell(row=25, column=1, value="CHIT OWNER BALANCE").font = font_regular
    
    c_net = ws.cell(row=27, column=3, value=net_counting)
    c_net.font = font_bold
    c_net.number_format = currency_fmt

wb_path = os.path.join(ranganadh_dir, 'Ranganadh_Chit_WORKBOOK.xlsx')
wb.save(wb_path)
print(f"Ranganadh Chit Workbook created successfully at: {wb_path}")


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
    width: 1024px;
    height: 731px;
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
    font-size: 34px;
    font-weight: 700;
    color: #000000;
    letter-spacing: -0.5px;
  }
  .table-container {
    width: 988px;
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
    font-size: 16px;
    font-weight: 700;
    height: 46px;
    border: 2px solid #000000;
    text-align: center;
    vertical-align: middle;
  }
  td {
    border: 2px solid #000000;
    height: 46px;
    font-size: 20px;
    font-weight: 700;
    vertical-align: middle;
  }
  .col-no {
    width: 90px;
    text-align: center;
  }
  .col-name {
    width: 415px;
    text-align: left;
    padding-left: 28px;
  }
  .col-amt {
    width: 483px;
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

takers_cum = []
for item in chit_plan:
    month_idx = len(takers_cum)
    takers_cum.append(all_members[month_idx])
    nontakers_cum = [p for p in all_members if p not in takers_cum]
    
    title = f"RANGANADH CHIT - {item['month_full'].upper()} MONTH"
    file_name = f"{item['num']}. {item['month_full'].upper()} - {item['year']}.jpg"
    
    rows_html = []
    idx = 1
    for name in takers_cum:
        rows_html.append(f"""
        <tr class="taker">
          <td class="col-no">{idx}</td>
          <td class="col-name">{name}</td>
          <td class="col-amt">&#8377;30,000</td>
        </tr>
        """)
        idx += 1
        
    for name in nontakers_cum:
        rows_html.append(f"""
        <tr class="nontaker">
          <td class="col-no">{idx}</td>
          <td class="col-name">{name}</td>
          <td class="col-amt">&#8377;{item['bid_amount']:,}</td>
        </tr>
        """)
        idx += 1
        
    html_content = html_template.replace('<!--TITLE-->', title).replace('<!--ROWS-->', "".join(rows_html))
    
    temp_dir = tempfile.gettempdir()
    temp_html = os.path.join(temp_dir, f"temp_ranganadh_{item['num']}.html")
    with open(temp_html, 'w', encoding='utf-8') as f:
        f.write(html_content)
        
    temp_png = os.path.join(temp_dir, f"temp_ranganadh_{item['num']}.png")
    final_jpg = os.path.join(images_dir, file_name)
    
    cmd = [
        edge_exe,
        '--headless',
        '--no-sandbox',
        '--disable-gpu',
        '--disable-crash-reporter',
        '--disable-software-rasterizer=false',
        '--user-data-dir=' + os.path.join(tempfile.gettempdir(), 'chit_chrome_profile_' + item['num']),
        '--force-device-scale-factor=1',
        '--hide-scrollbars',
        f'--screenshot={temp_png}',
        '--window-size=1024,731',
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

print("All 12 Ranganadh Chit images generated successfully!")
