import os
import subprocess
from PIL import Image

shiva_dir = r'd:\CHIT\02.SHIVA'
images_dir = os.path.join(shiva_dir, 'Monthly Images')
os.makedirs(images_dir, exist_ok=True)

edge_exe = r'C:\Program Files (x86)\Microsoft\Edge\Application\msedge.exe'

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
    display: flex;
    flex-direction: column;
    align-items: center;
    justify-content: flex-start;
  }
  .title-container {
    height: 110px;
    display: flex;
    align-items: center;
    justify-content: center;
    padding-top: 15px;
  }
  .title {
    font-size: 32px;
    font-weight: 800;
    color: #000000;
    letter-spacing: -0.5px;
    text-transform: uppercase;
  }
  .table-container {
    width: 934px;
  }
  table {
    width: 100%;
    border-collapse: collapse;
    border: 2px solid #000000;
  }
  th {
    background-color: #326ac7;
    color: #ffffff;
    font-size: 22px;
    font-weight: 700;
    height: 42px;
    border: 2px solid #000000;
    text-align: center;
    vertical-align: middle;
  }
  td {
    border: 2px solid #000000;
    height: 42px;
    font-size: 21px;
    font-weight: 700;
    vertical-align: middle;
  }
  .col-name {
    width: 340px;
    text-align: left;
    padding-left: 14px;
  }
  .col-amt {
    width: 594px;
    text-align: right;
    padding-right: 20px;
  }
  .taker {
    background-color: #f70305;
    color: #ffffff;
  }
  .nontaker {
    background-color: #9be278;
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
          <th class="col-name" style="text-align: center;">Person Name</th>
          <th class="col-amt" style="text-align: center;">Amount Need to Pay</th>
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

shiva_plan = [
    {'num': '01', 'month_full': 'March', 'year': '2026', 'person': 'Pavan', 'bid_amount': 9500},
    {'num': '02', 'month_full': 'April', 'year': '2026', 'person': 'veda', 'bid_amount': 9250},
    {'num': '03', 'month_full': 'May', 'year': '2026', 'person': 'Dharanya', 'bid_amount': 9000},
    {'num': '04', 'month_full': 'June', 'year': '2026', 'person': 'Rani', 'bid_amount': 8750},
    {'num': '05', 'month_full': 'July', 'year': '2026', 'person': 'Chaitu', 'bid_amount': 8500},
    {'num': '06', 'month_full': 'August', 'year': '2026', 'person': 'sukesh', 'bid_amount': 8250},
    {'num': '07', 'month_full': 'September', 'year': '2026', 'person': 'sampath', 'bid_amount': 8000},
    {'num': '08', 'month_full': 'October', 'year': '2026', 'person': 'vijay', 'bid_amount': 7750},
    {'num': '09', 'month_full': 'November', 'year': '2026', 'person': 'sreedhar', 'bid_amount': 7500},
    {'num': '10', 'month_full': 'December', 'year': '2026', 'person': 'Tharun', 'bid_amount': 7250},
    {'num': '11', 'month_full': 'January', 'year': '2027', 'person': 'chaturya', 'bid_amount': 7000},
    {'num': '12', 'month_full': 'February', 'year': '2027', 'person': 'mounika', 'bid_amount': 10000},
]

all_members = [item['person'] for item in shiva_plan]

takers_cum = []
for item in shiva_plan:
    takers_cum.append(item['person'])
    nontakers_cum = [p for p in all_members if p not in takers_cum]
    
    title = f"SHIVA CHIT – {item['month_full'].upper()} MONTH"
    file_name = f"{item['num']}. {item['month_full'].upper()} - {item['year']}.jpg"
    
    rows_html = []
    for name in takers_cum:
        rows_html.append(f"""
        <tr class="taker">
          <td class="col-name">{name}</td>
          <td class="col-amt">10,000</td>
        </tr>
        """)
        
    for name in nontakers_cum:
        rows_html.append(f"""
        <tr class="nontaker">
          <td class="col-name">{name}</td>
          <td class="col-amt">{item['bid_amount']:,}</td>
        </tr>
        """)
        
    html_content = html_template.replace('<!--TITLE-->', title).replace('<!--ROWS-->', "".join(rows_html))
    
    temp_html = os.path.join(r'd:\CHIT\WORKSPACE', f"temp_shiva_color_{item['num']}.html")
    with open(temp_html, 'w', encoding='utf-8') as f:
        f.write(html_content)
        
    temp_png = os.path.join(r'd:\CHIT\WORKSPACE', f"temp_shiva_color_{item['num']}.png")
    final_jpg = os.path.join(images_dir, file_name)
    
    cmd = [
        edge_exe,
        '--headless',
        '--disable-gpu',
        '--force-device-scale-factor=1',
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

print("All 12 Shiva Chit images regenerated with new colors successfully!")
