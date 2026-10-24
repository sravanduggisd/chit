import os
import subprocess
from PIL import Image

output_dir = r'd:\CHIT\01.GANAPATHI\New folder'
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

earlier_months = [
    {
        'file_name': 'MARCH.jpg',
        'title': 'Ganapathi Chit – March Month 2026',
        'bid_amount': 18500,
        'takers': ['Sarath Babu'],
        'nontakers': ['Anil', 'Jyothi', 'Girl', 'Sumanth', 'Ramanaiah', 'Harish', 'Pallavi', 'P. Hari', 'Anjineyulu', 'Vamsi Madhu', 'Uma Suri']
    },
    {
        'file_name': 'APRIL.jpg',
        'title': 'Ganapathi Chit – April Month 2026',
        'bid_amount': 18000,
        'takers': ['Sarath Babu', 'Anil'],
        'nontakers': ['Jyothi', 'Girl', 'Sumanth', 'Ramanaiah', 'Harish', 'Pallavi', 'P. Hari', 'Anjineyulu', 'Vamsi Madhu', 'Uma Suri']
    },
    {
        'file_name': 'MAY.jpg',
        'title': 'Ganapathi Chit – May Month 2026',
        'bid_amount': 17500,
        'takers': ['Sarath Babu', 'Anil', 'Jyothi'],
        'nontakers': ['Girl', 'Sumanth', 'Ramanaiah', 'Harish', 'Pallavi', 'P. Hari', 'Anjineyulu', 'Vamsi Madhu', 'Uma Suri']
    },
    {
        'file_name': 'JUNE.jpg',
        'title': 'Ganapathi Chit – June Month 2026',
        'bid_amount': 17000,
        'takers': ['Sarath Babu', 'Anil', 'Jyothi', 'Girl'],
        'nontakers': ['Sumanth', 'Ramanaiah', 'Harish', 'Pallavi', 'P. Hari', 'Anjineyulu', 'Vamsi Madhu', 'Uma Suri']
    },
    {
        'file_name': 'JULY.jpg',
        'title': 'Ganapathi Chit – July Month 2026',
        'bid_amount': 16500,
        'takers': ['Sarath Babu', 'Anil', 'Jyothi', 'Girl', 'Anjineyulu'],
        'nontakers': ['Ramanaiah', 'Harish', 'Pallavi', 'P. Hari', 'Sumanth', 'Vamsi Madhu', 'Uma Suri']
    }
]

for m in earlier_months:
    rows_html = []
    idx = 1
    for name in m['takers']:
        rows_html.append(f"""
        <tr class="taker">
          <td class="col-no">{idx}</td>
          <td class="col-name">{name}</td>
          <td class="col-amt">&#8377;20,000</td>
        </tr>
        """)
        idx += 1
        
    for name in m['nontakers']:
        rows_html.append(f"""
        <tr class="nontaker">
          <td class="col-no">{idx}</td>
          <td class="col-name">{name}</td>
          <td class="col-amt">&#8377;{m['bid_amount']:,}</td>
        </tr>
        """)
        idx += 1
        
    html_content = html_template.replace('<!--TITLE-->', m['title']).replace('<!--ROWS-->', "".join(rows_html))
    
    temp_html = os.path.join(r'd:\CHIT\WORKSPACE', f"temp_{m['file_name']}.html")
    with open(temp_html, 'w', encoding='utf-8') as f:
        f.write(html_content)
        
    temp_png = os.path.join(r'd:\CHIT\WORKSPACE', f"temp_{m['file_name']}.png")
    final_jpg = os.path.join(output_dir, m['file_name'])
    
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
    print(f"Generated {m['file_name']} successfully at {final_jpg}")
    
    # Clean temp files
    if os.path.exists(temp_html):
        os.remove(temp_html)
    if os.path.exists(temp_png):
        os.remove(temp_png)

print("All remaining earlier month images generated successfully!")
