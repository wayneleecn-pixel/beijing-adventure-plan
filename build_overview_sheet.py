import os
from PIL import Image, ImageDraw, ImageFont

out_dir = r"assets/badges/print-master"

# Load the 6 preview images (900x900)
badges_meta = [
    ("badge_01", "01. 长城守卫者", "Great Wall Sentinel"),
    ("badge_02", "02. 国宝探索者", "National Treasure Explorer"),
    ("badge_03", "03. 紫禁城解密者", "Forbidden City Codebreaker"),
    ("badge_04", "04. 电影世界挑战者", "Cine-World Challenger"),
    ("badge_05", "05. 记忆收藏家", "Memory Collector"),
    ("badge_06", "06. 北京大探险家", "Beijing Grand Explorer"),
]

# Grid configuration: 3 columns x 2 rows
# Thumbnail size: 500 x 500
thumb_size = 460
card_w = 520
card_h = 600
padding_top = 220
padding_bottom = 120
padding_x = 60

canvas_w = padding_x * 2 + card_w * 3
canvas_h = padding_top + card_h * 2 + padding_bottom

# Background color: warm clean off-white / light slate
sheet = Image.new("RGB", (canvas_w, canvas_h), (248, 246, 242))
draw = ImageDraw.Draw(sheet)

# Try font loading, fallback to default if not found
try:
    font_title = ImageFont.truetype("msyh.ttc", 38)
    font_sub = ImageFont.truetype("msyh.ttc", 20)
    font_name = ImageFont.truetype("msyhbd.ttc", 24)
    font_en = ImageFont.truetype("msyh.ttc", 16)
    font_spec = ImageFont.truetype("msyh.ttc", 18)
except:
    try:
        font_title = ImageFont.truetype("simhei.ttf", 38)
        font_sub = ImageFont.truetype("simhei.ttf", 20)
        font_name = ImageFont.truetype("simhei.ttf", 24)
        font_en = ImageFont.truetype("simhei.ttf", 16)
        font_spec = ImageFont.truetype("simhei.ttf", 18)
    except:
        font_title = ImageFont.load_default()
        font_sub = font_title
        font_name = font_title
        font_en = font_title
        font_spec = font_title

# Header
title_text = "北京亲子旅行冒险计划 · 6枚儿童冒险徽章 3D打印制造母稿"
sub_text = "40–45mm FDM 规范 | Bambu Lab AMS 4色方案 | 0.4mm喷嘴优化 | 纯色平面矢量拓扑"
draw.text((canvas_w // 2, 70), title_text, fill=(35, 30, 25), font=font_title, anchor="mt")
draw.text((canvas_w // 2, 125), sub_text, fill=(120, 110, 100), font=font_sub, anchor="mt")

# Color Swatches in Header
colors = [
    ("#E5A823", "金色 (Frame/Star)"),
    ("#3B82C8", "天蓝 (Sky/Background)"),
    ("#2E7D47", "森林绿 (Ribbon/Ground)"),
    ("#7A3E20", "暖棕 (Subject/Structure)"),
]

swatch_start_x = canvas_w // 2 - 380
swatch_y = 165
for i, (hex_c, label) in enumerate(colors):
    sx = swatch_start_x + i * 200
    # draw circle
    draw.ellipse([sx, swatch_y, sx + 22, swatch_y + 22], fill=hex_c, outline=(200, 195, 185), width=1)
    draw.text((sx + 30, swatch_y + 11), f"{hex_c} {label}", fill=(80, 75, 70), font=font_en, anchor="lm")

# Place Badges
for idx, (b_id, name, en) in enumerate(badges_meta):
    r = idx // 3
    c = idx % 3
    
    x = padding_x + c * card_w
    y = padding_top + r * card_h
    
    # Card background
    card_margin = 15
    draw.rounded_rectangle(
        [x + card_margin, y, x + card_w - card_margin, y + card_h - 20],
        radius=16,
        fill=(255, 255, 255),
        outline=(230, 225, 218),
        width=1
    )
    
    # Load and resize preview image
    img_path = os.path.join(out_dir, f"{b_id}_preview.jpg")
    if os.path.exists(img_path):
        with Image.open(img_path) as im:
            thumb = im.resize((thumb_size, thumb_size), Image.Resampling.LANCZOS)
            # Center inside card
            img_x = x + (card_w - thumb_size) // 2
            img_y = y + 20
            sheet.paste(thumb, (img_x, img_y))
            
    # Labels
    text_y = y + 20 + thumb_size + 15
    draw.text((x + card_w // 2, text_y), name, fill=(35, 30, 25), font=font_name, anchor="mt")
    draw.text((x + card_w // 2, text_y + 30), en, fill=(140, 130, 120), font=font_en, anchor="mt")

# Bottom Specs Footer
footer_text = "注：所有闭合色块最小特征尺寸均 >= 0.8–1.0mm (在45mm成品下)，杜绝微碎碎片，保证 AMS 换料路径干净顺畅。"
draw.text((canvas_w // 2, canvas_h - 55), footer_text, fill=(150, 140, 130), font=font_spec, anchor="mt")

output_sheet_jpg = os.path.join(out_dir, "print_master_all_6.jpg")
sheet.save(output_sheet_jpg, quality=95)
print(f"Overview sheet saved: {output_sheet_jpg}")
