import os
from PIL import Image, ImageDraw, ImageFont

app_dir = r'd:\CHIT\APP'

# Create app icon (192x192 and 512x512)
for size in [192, 512]:
    img = Image.new('RGBA', (size, size), color=(0, 0, 0, 0))
    draw = ImageDraw.Draw(img)
    
    # Rounded gradient background
    margin = int(size * 0.05)
    radius = int(size * 0.22)
    # Draw dark blue-indigo rounded rectangle
    draw.rounded_rectangle(
        [(margin, margin), (size - margin, size - margin)],
        radius=radius,
        fill=(30, 58, 138, 255),
        outline=(59, 130, 246, 255),
        width=int(size * 0.03)
    )
    
    # Inner gold circle
    center = size // 2
    circle_r = int(size * 0.32)
    draw.ellipse(
        [(center - circle_r, center - circle_r), (center + circle_r, center + circle_r)],
        fill=(245, 158, 11, 255)
    )
    
    # Draw Indian Rupee Symbol or "₹"
    # Using Arial or Calibri font
    font_size = int(size * 0.38)
    try:
        font = ImageFont.truetype(r'C:\Windows\Fonts\arial.ttf', font_size)
    except:
        font = ImageFont.load_default()
        
    text = "₹"
    bbox = draw.textbbox((0, 0), text, font=font)
    text_w = bbox[2] - bbox[0]
    text_h = bbox[3] - bbox[1]
    text_x = center - text_w // 2
    text_y = center - text_h // 2 - int(size * 0.04)
    draw.text((text_x, text_y), text, font=font, fill=(255, 255, 255, 255))
    
    icon_path = os.path.join(app_dir, f'icon-{size}.png')
    img.save(icon_path, 'PNG')
    print(f"Saved {icon_path}")

print("App icons created successfully!")
