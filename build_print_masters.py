import os
import subprocess
from PIL import Image

# Output directory
out_dir = r"assets/badges/print-master"
os.makedirs(out_dir, exist_ok=True)

# 4 Standard Bambu AMS Solid Colors
C_GOLD  = "#E5A823"  # Bambu PLA Basic Gold/Yellow (Outer frame & accents)
C_BLUE  = "#3B82C8"  # Bambu PLA Matte Sky Blue (Background field)
C_GREEN = "#2E7D47"  # Bambu PLA Basic Green (Bottom ribbon & ground)
C_BROWN = "#7A3E20"  # Bambu PLA Matte Brown/Terracotta (Main subject body)

# Shared Outer Shield Frame & Green Ribbon Geometry
# Canvas: 450 x 450 (10 units = 1.0 mm physical scale -> 45mm total size)
# Outer shield path (symmetrical classical ornate heraldic crest)
SHIELD_OUTER = """
M 225,25
C 255,42 278,48 308,62
C 332,74 345,95 356,120
C 382,140 398,170 395,208
C 392,232 380,250 375,272
C 385,302 372,342 346,368
C 312,392 268,414 225,435
C 182,414 138,392 104,368
C 78,342 65,302 75,272
C 70,250 58,232 55,208
C 52,170 68,140 94,120
C 105,95 118,74 142,62
C 172,48 195,42 225,25 Z
"""

# Inner cavity (Inner edge of the gold frame)
SHIELD_INNER = """
M 225,50
C 248,65 266,70 290,82
C 310,92 320,108 328,128
C 350,145 362,170 360,202
C 358,220 348,235 344,252
C 352,278 340,310 320,332
C 292,352 258,370 225,388
C 192,370 158,352 130,332
C 110,310 98,278 106,252
C 102,235 92,220 90,202
C 88,170 100,145 122,128
C 130,108 140,92 160,82
C 184,70 202,65 225,50 Z
"""

# Bottom Folded Ribbon Banner (Green #2E7D47 with Brown #7A3E20 fold tucks)
RIBBON_SVG = f"""
  <!-- Ribbon Left Fold Wing -->
  <polygon points="125,335 80,335 98,365 72,395 125,375" fill="{C_GREEN}"/>
  <polygon points="125,355 125,375 140,355" fill="{C_BROWN}"/>

  <!-- Ribbon Right Fold Wing -->
  <polygon points="325,335 370,335 352,365 378,395 325,375" fill="{C_GREEN}"/>
  <polygon points="325,355 325,375 310,355" fill="{C_BROWN}"/>

  <!-- Ribbon Main Center Banner -->
  <path d="M 120,330 Q 225,342 330,330 L 330,375 Q 225,392 120,375 Z" fill="{C_GREEN}"/>
"""

def make_badge_svg(inner_art_svg):
    return f"""<svg xmlns="http://www.w3.org/2000/svg" viewBox="0 0 450 450" width="450" height="450">
  <!-- Layer 1: Solid Gold Outer Shield (Beveled Rim Base) -->
  <path d="{SHIELD_OUTER.strip()}" fill="{C_GOLD}"/>

  <!-- Layer 2: Sky Blue Inner Field Plate -->
  <path d="{SHIELD_INNER.strip()}" fill="{C_BLUE}"/>

  <!-- Layer 3: Central Subject Vector Art -->
{inner_art_svg}

  <!-- Layer 4: Bottom Folded Ribbon Banner -->
{RIBBON_SVG}
</svg>"""

# ==============================================================================
# BADGE 01: Great Wall Sentinel (长城守卫者)
# Watchtower, crenellations, stone wall ramparts, green hill base
# ==============================================================================
art_01 = f"""
  <!-- Green Hill Base -->
  <path d="M 90,260 Q 225,290 360,255 L 360,340 L 90,340 Z" fill="{C_GREEN}"/>

  <!-- Left Wall Rampart -->
  <polygon points="90,240 180,205 180,285 90,305" fill="{C_BROWN}"/>
  <polygon points="95,225 115,220 115,240 95,245" fill="{C_GOLD}"/>
  <polygon points="125,215 145,210 145,232 125,238" fill="{C_GOLD}"/>
  <polygon points="155,205 175,200 175,222 155,228" fill="{C_GOLD}"/>

  <!-- Right Wall Rampart -->
  <polygon points="270,205 360,235 360,300 270,285" fill="{C_BROWN}"/>
  <polygon points="275,200 295,205 295,228 275,222" fill="{C_GOLD}"/>
  <polygon points="305,210 325,216 325,238 305,232" fill="{C_GOLD}"/>
  <polygon points="335,220 355,226 355,248 335,242" fill="{C_GOLD}"/>

  <!-- Central Great Wall Watchtower Fortress -->
  <polygon points="175,145 275,145 285,285 165,285" fill="{C_BROWN}"/>

  <!-- Crenellations / Battlements on Top (>=1.2mm teeth) -->
  <rect x="172" y="125" width="22" height="22" rx="2" fill="{C_GOLD}"/>
  <rect x="201" y="125" width="22" height="22" rx="2" fill="{C_GOLD}"/>
  <rect x="229" y="125" width="22" height="22" rx="2" fill="{C_GOLD}"/>
  <rect x="257" y="125" width="22" height="22" rx="2" fill="{C_GOLD}"/>

  <!-- Watchtower Windows (Arch apertures) -->
  <path d="M 195,175 A 10,10 0 0,1 215,175 L 215,195 L 195,195 Z" fill="{C_BLUE}"/>
  <path d="M 235,175 A 10,10 0 0,1 255,175 L 255,195 L 235,195 Z" fill="{C_BLUE}"/>

  <!-- Central Gateway Archway -->
  <path d="M 205,235 A 20,20 0 0,1 245,235 L 245,285 L 205,285 Z" fill="{C_GOLD}"/>
"""

# ==============================================================================
# BADGE 02: National Treasure Explorer (国宝探索者)
# Chinese Bronze Ding ritual vessel + explorer magnifying glass + discovery stars
# ==============================================================================
art_02 = f"""
  <!-- Ancient Bronze Ding Ritual Cauldron Vessel -->
  <!-- 3 Sturdy Cauldron Legs -->
  <polygon points="160,240 180,240 172,305 152,305" fill="{C_BROWN}"/>
  <polygon points="215,240 235,240 232,310 218,310" fill="{C_BROWN}"/>
  <polygon points="270,240 290,240 298,305 278,305" fill="{C_BROWN}"/>

  <!-- Ding Main Body Bowl -->
  <path d="M 145,150 L 305,150 C 315,210 295,250 225,255 C 155,250 135,210 145,150 Z" fill="{C_BROWN}"/>

  <!-- Ding Top Loop Handles -->
  <path d="M 152,150 L 152,120 L 172,120 L 172,150 Z" fill="{C_GOLD}"/>
  <path d="M 278,150 L 278,120 L 298,120 L 298,150 Z" fill="{C_GOLD}"/>

  <!-- Ding Ornamental Gold Inlay Band -->
  <rect x="150" y="165" width="150" height="20" rx="3" fill="{C_GOLD}"/>
  <circle cx="180" cy="175" r="5" fill="{C_BROWN}"/>
  <circle cx="225" cy="175" r="5" fill="{C_BROWN}"/>
  <circle cx="270" cy="175" r="5" fill="{C_BROWN}"/>

  <!-- Explorer Magnifying Glass (Right Side) -->
  <!-- Handle -->
  <polygon points="295,245 340,290 328,302 283,257" fill="{C_BROWN}"/>
  <!-- Gold Rim -->
  <circle cx="275" cy="225" r="32" fill="{C_GOLD}"/>
  <!-- Inner Glass Lens -->
  <circle cx="275" cy="225" r="20" fill="{C_BLUE}"/>

  <!-- 4-Pointed Discovery Stars (>=1.5mm) -->
  <path d="M 130,105 Q 135,115 145,115 Q 135,115 130,125 Q 125,115 115,115 Q 125,115 130,105 Z" fill="{C_GOLD}"/>
  <path d="M 320,120 Q 324,128 332,128 Q 324,128 320,136 Q 316,128 308,128 Q 316,128 320,120 Z" fill="{C_GOLD}"/>
"""

# ==============================================================================
# BADGE 03: Forbidden City Codebreaker (紫禁城解密者)
# Palace pavilion gate, layered golden eaves, keyhole, compass motif
# ==============================================================================
art_03 = f"""
  <!-- Palace Gatehouse Main Red/Brown Wall -->
  <polygon points="120,200 330,200 335,325 115,325" fill="{C_BROWN}"/>

  <!-- Double Layered Imperial Golden Eaves -->
  <!-- Upper Eave -->
  <path d="M 170,140 Q 225,120 280,140 L 270,160 L 180,160 Z" fill="{C_GOLD}"/>
  <!-- Lower Wide Eave -->
  <path d="M 105,190 Q 225,160 345,190 L 330,210 Q 225,185 120,210 Z" fill="{C_GOLD}"/>

  <!-- Central Palace Arched Doorway -->
  <path d="M 195,240 A 30,30 0 0,1 255,240 L 255,325 L 195,325 Z" fill="{C_GOLD}"/>
  <path d="M 205,250 A 20,20 0 0,1 245,250 L 245,325 L 205,325 Z" fill="{C_BLUE}"/>

  <!-- Antique Keyhole on the Right Wall (Width 16, Height 26) -->
  <circle cx="295" cy="255" r="8" fill="{C_GOLD}"/>
  <polygon points="290,255 300,255 303,275 287,275" fill="{C_GOLD}"/>

  <!-- Decryption Pocket Compass (Upper-Left Sky) -->
  <circle cx="155" cy="120" r="24" fill="{C_GOLD}"/>
  <circle cx="155" cy="120" r="16" fill="{C_BLUE}"/>
  <!-- 4-point compass star -->
  <polygon points="155,108 159,118 167,120 159,122 155,132 151,122 143,120 151,118" fill="{C_BROWN}"/>
"""

# ==============================================================================
# BADGE 04: Cine-World Challenger (电影世界挑战者)
# Clapperboard, angled clapping stick, curved film strip, adventure star
# ==============================================================================
art_04 = f"""
  <!-- Sweeping Film Strip Behind Clapperboard -->
  <path d="M 100,160 C 150,90 300,80 340,150 C 370,200 340,280 290,290" 
        fill="none" stroke="{C_BROWN}" stroke-width="26" stroke-linecap="round"/>
  <!-- Film Sprocket Holes (Cutout Blue, each >= 1.2mm) -->
  <circle cx="120" cy="140" r="5" fill="{C_BLUE}"/>
  <circle cx="150" cy="115" r="5" fill="{C_BLUE}"/>
  <circle cx="185" cy="102" r="5" fill="{C_BLUE}"/>
  <circle cx="225" cy="100" r="5" fill="{C_BLUE}"/>
  <circle cx="265" cy="105" r="5" fill="{C_BLUE}"/>
  <circle cx="305" cy="122" r="5" fill="{C_BLUE}"/>
  <circle cx="335" cy="155" r="5" fill="{C_BLUE}"/>
  <circle cx="345" cy="195" r="5" fill="{C_BLUE}"/>
  <circle cx="335" cy="235" r="5" fill="{C_BLUE}"/>

  <!-- Main Clapperboard Body (Solid Warm Brown) -->
  <rect x="155" y="195" width="140" height="90" rx="6" fill="{C_BROWN}"/>

  <!-- Clapperboard Top Plate (Diagonal stripes) -->
  <rect x="155" y="195" width="140" height="24" rx="2" fill="{C_GOLD}"/>
  <polygon points="175,195 190,195 170,219 155,219" fill="{C_BROWN}"/>
  <polygon points="215,195 230,195 210,219 195,219" fill="{C_BROWN}"/>
  <polygon points="255,195 270,195 250,219 235,219" fill="{C_BROWN}"/>

  <!-- Clapperboard Open Top Stick (Angled ~22 deg) -->
  <g transform="rotate(-22 155 195)">
    <rect x="155" y="171" width="140" height="24" rx="2" fill="{C_GOLD}"/>
    <polygon points="175,171 190,171 170,195 155,195" fill="{C_BROWN}"/>
    <polygon points="215,171 230,171 210,195 195,195" fill="{C_BROWN}"/>
    <polygon points="255,171 270,171 250,195 235,195" fill="{C_BROWN}"/>
  </g>

  <!-- Big Bold Adventure Star (Left) -->
  <polygon points="125,210 132,228 150,228 136,240 141,258 125,246 109,258 114,240 100,228 118,228" fill="{C_GOLD}"/>
"""

# ==============================================================================
# BADGE 05: Memory Collector (记忆收藏家)
# Retro explorer travel camera + 2 floating Polaroid photo cards
# ==============================================================================
art_05 = f"""
  <!-- Left Polaroid Photo Card (Tilted -18 deg) -->
  <g transform="rotate(-18 170 160)">
    <rect x="135" y="95" width="65" height="80" rx="4" fill="{C_GOLD}"/>
    <rect x="142" y="102" width="51" height="52" fill="{C_BROWN}"/>
    <!-- Inner mountain sketch -->
    <polygon points="145,150 168,122 190,150" fill="{C_BLUE}"/>
  </g>

  <!-- Right Polaroid Photo Card (Tilted +18 deg) -->
  <g transform="rotate(18 280 160)">
    <rect x="250" y="95" width="65" height="80" rx="4" fill="{C_GOLD}"/>
    <rect x="257" y="102" width="51" height="52" fill="{C_BROWN}"/>
    <!-- Inner sun sketch -->
    <circle cx="282" cy="128" r="14" fill="{C_BLUE}"/>
  </g>

  <!-- Explorer Retro Camera Body -->
  <rect x="145" y="195" width="160" height="95" rx="10" fill="{C_BROWN}"/>

  <!-- Camera Top Metal Plate & Dials -->
  <rect x="155" y="180" width="140" height="18" rx="3" fill="{C_GOLD}"/>
  <rect x="175" y="170" width="20" height="12" rx="2" fill="{C_GOLD}"/>
  <rect x="255" y="172" width="25" height="10" rx="2" fill="{C_GOLD}"/>

  <!-- Viewfinder Window -->
  <rect x="255" y="202" width="24" height="16" rx="2" fill="{C_BLUE}"/>

  <!-- Large Centered Camera Lens Ring -->
  <circle cx="215" cy="245" r="36" fill="{C_GOLD}"/>
  <circle cx="215" cy="245" r="26" fill="{C_BROWN}"/>
  <circle cx="215" cy="245" r="15" fill="{C_BLUE}"/>
"""

# ==============================================================================
# BADGE 06: Beijing Grand Explorer (北京大探险家 · 终极荣誉章)
# 8-Pointed Starburst Compass Rose Medallion + Laurel Wreath Branches
# ==============================================================================
art_06 = f"""
  <!-- Flanking Laurel Wreath Branches (Left & Right Green Leaves) -->
  <!-- Left Laurel Branch -->
  <g fill="{C_GREEN}">
    <path d="M 140,285 Q 120,230 140,165 Q 125,230 140,285" fill="{C_GREEN}"/>
    <ellipse cx="128" cy="180" rx="12" ry="7" transform="rotate(-35 128 180)"/>
    <ellipse cx="120" cy="210" rx="13" ry="8" transform="rotate(-15 120 210)"/>
    <ellipse cx="122" cy="240" rx="13" ry="8" transform="rotate(10 122 240)"/>
    <ellipse cx="132" cy="270" rx="12" ry="7" transform="rotate(30 132 270)"/>
  </g>

  <!-- Right Laurel Branch -->
  <g fill="{C_GREEN}">
    <path d="M 310,285 Q 330,230 310,165 Q 325,230 310,285" fill="{C_GREEN}"/>
    <ellipse cx="322" cy="180" rx="12" ry="7" transform="rotate(35 322 180)"/>
    <ellipse cx="330" cy="210" rx="13" ry="8" transform="rotate(15 330 210)"/>
    <ellipse cx="328" cy="240" rx="13" ry="8" transform="rotate(-10 328 240)"/>
    <ellipse cx="318" cy="270" rx="12" ry="7" transform="rotate(-30 318 270)"/>
  </g>

  <!-- Compass Rose Outer Dial Ring -->
  <circle cx="225" cy="215" r="75" fill="none" stroke="{C_BROWN}" stroke-width="12"/>

  <!-- 8-Pointed Faceted Starburst Compass Rose (Gold & Brown bevels) -->
  <!-- North Point -->
  <polygon points="225,120 225,215 210,215" fill="{C_GOLD}"/>
  <polygon points="225,120 225,215 240,215" fill="{C_BROWN}"/>

  <!-- South Point -->
  <polygon points="225,310 225,215 240,215" fill="{C_GOLD}"/>
  <polygon points="225,310 225,215 210,215" fill="{C_BROWN}"/>

  <!-- East Point -->
  <polygon points="320,215 225,215 225,200" fill="{C_GOLD}"/>
  <polygon points="320,215 225,215 225,230" fill="{C_BROWN}"/>

  <!-- West Point -->
  <polygon points="130,215 225,215 225,230" fill="{C_GOLD}"/>
  <polygon points="130,215 225,215 225,200" fill="{C_BROWN}"/>

  <!-- 4 Minor Diagonal Points (NE, NW, SE, SW) -->
  <polygon points="280,160 225,215 233,207" fill="{C_GOLD}"/>
  <polygon points="280,160 225,215 225,215" fill="{C_BROWN}"/>
  <polygon points="170,160 225,215 217,207" fill="{C_BROWN}"/>
  <polygon points="170,160 225,215 225,215" fill="{C_GOLD}"/>
  <polygon points="280,270 225,215 233,223" fill="{C_BROWN}"/>
  <polygon points="280,270 225,215 225,215" fill="{C_GOLD}"/>
  <polygon points="170,270 225,215 217,223" fill="{C_GOLD}"/>
  <polygon points="170,270 225,215 225,215" fill="{C_BROWN}"/>

  <!-- Central Hub Medallion -->
  <circle cx="225" cy="215" r="18" fill="{C_GOLD}"/>
  <circle cx="225" cy="215" r="10" fill="{C_BROWN}"/>

  <!-- North Crowning Star -->
  <polygon points="225,92 229,102 240,102 231,108 234,118 225,112 216,118 219,108 210,102 221,102" fill="{C_GOLD}"/>
"""

badges = [
    ("badge_01", "长城守卫者", art_01),
    ("badge_02", "国宝探索者", art_02),
    ("badge_03", "紫禁城解密者", art_03),
    ("badge_04", "电影世界挑战者", art_04),
    ("badge_05", "记忆收藏家", art_05),
    ("badge_06", "北京大探险家", art_06),
]

edge_exe = r"C:\Program Files (x86)\Microsoft\Edge\Application\msedge.exe"

for badge_id, name, art in badges:
    svg_content = make_badge_svg(art)
    svg_path = os.path.join(out_dir, f"{badge_id}.svg")
    with open(svg_path, "w", encoding="utf-8") as f:
        f.write(svg_content)
    print(f"Saved: {svg_path}")

    # Create HTML wrapper for high-res transparent screenshot rendering
    html_content = f"""<!DOCTYPE html>
<html>
<head>
<meta charset="utf-8">
<style>
* {{ margin: 0; padding: 0; box-sizing: border-box; }}
body {{ background: transparent; overflow: hidden; width: 900px; height: 900px; }}
svg {{ width: 900px; height: 900px; display: block; }}
</style>
</head>
<body>
{svg_content}
</body>
</html>"""
    temp_html = f"temp_{badge_id}.html"
    with open(temp_html, "w", encoding="utf-8") as f:
        f.write(html_content)

    png_path = os.path.abspath(os.path.join(out_dir, f"{badge_id}.png"))
    cmd = [
        edge_exe,
        "--headless=new",
        "--default-background-color=00000000",
        f"--screenshot={png_path}",
        "--window-size=900,900",
        "file:///" + os.path.abspath(temp_html).replace("\\", "/")
    ]
    subprocess.run(cmd, capture_output=True)

    # Also generate clean white background preview JPG
    if os.path.exists(png_path):
        with Image.open(png_path) as im:
            # im is 900x900 RGBA
            bg = Image.new("RGB", im.size, (255, 255, 255))
            bg.paste(im, mask=im.split()[3])
            jpg_path = os.path.join(out_dir, f"{badge_id}_preview.jpg")
            bg.save(jpg_path, quality=95)
            print(f"Rendered: {png_path} & {jpg_path}")

    if os.path.exists(temp_html):
        os.remove(temp_html)

print("All 6 badges generated and rendered successfully!")
