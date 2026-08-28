#!/usr/bin/env python3
"""
Brand Identity System - Fixed vertical layout, 1600x1200px @300dpi
"""

import matplotlib.pyplot as plt
import matplotlib.patches as mpatches
from matplotlib import font_manager
from matplotlib.font_manager import FontProperties
from matplotlib.patches import FancyBboxPatch
import numpy as np

font_path = '/usr/share/fonts/opentype/noto/NotoSansCJK-Regular.ttc'
bold_font_path = '/usr/share/fonts/opentype/noto/NotoSansCJK-Bold.ttc'
font_manager.fontManager.addfont(font_path)
font_manager.fontManager.addfont(bold_font_path)

cn_font = FontProperties(fname=font_path)
cn_font_bold = FontProperties(fname=bold_font_path)

# Canvas: 160 x 120 units (maps to 1600x1200px at 300dpi with figsize)
fig, ax = plt.subplots(1, 1, figsize=(16, 12), dpi=300)
fig.patch.set_facecolor('#ffffff')
ax.set_facecolor('#ffffff')
ax.set_xlim(0, 160)
ax.set_ylim(0, 120)
ax.set_aspect('equal')
ax.axis('off')

def cn(x, y, text, size=10, bold=False, color='#333', ha='center', va='center',
       style='normal', alpha=1.0):
    fp = cn_font_bold if bold else cn_font
    return ax.text(x, y, text, fontsize=size, color=color, ha=ha, va=va,
                   fontproperties=fp, style=style, alpha=alpha)

def draw_dipper(cx, cy, scale=1.0, curve=False, ring=False):
    if ring:
        r = mpatches.Circle((cx, cy), 6*scale, facecolor='white', edgecolor='#2980b9', lw=1.5)
        ax.add_patch(r)
    ax.plot([cx, cx], [cy - 5*scale, cy + 5*scale], color='#2980b9',
            lw=2.5*scale, solid_capstyle='round')
    dots_y = np.linspace(-4.2, 4.2, 7)
    dots_s = [1.8, 1.2, 2.8, 1.8, 2.2, 1.4, 2.0]
    x_off = [0.8, 0.3, 0, -0.2, 0, 0.5, 1.0] if curve else [0]*7
    for i, (dy, ds, dxo) in enumerate(zip(dots_y, dots_s, x_off)):
        dc = 'white' if i == 2 else '#5dade2'
        dot = mpatches.Circle((cx + dxo*scale, cy + dy*scale), ds*0.38*scale,
                              facecolor=dc, edgecolor='#1a5276', lw=0.5)
        ax.add_patch(dot)

def card(cx, cy, w, h):
    c = FancyBboxPatch((cx - w/2, cy - h/2), w, h,
                       boxstyle="round,pad=1.5", facecolor='#f8f9fa',
                       edgecolor='#e0e6ed', lw=1)
    ax.add_patch(c)

# ============================================================
# SECTION 0: TITLE (y: 108-118)
# ============================================================
cn(80, 115, '品牌识别系统', size=22, bold=True, color='#1e3a5f')
cn(80, 111, 'Brand Identity System', size=12, color='#6b7c8d')
cn(80, 108, '百年京张AI创新带 · Diameter AI Innovation Belt', size=9, color='#8899aa')
ax.plot([15, 145], [106, 106], color='#e0e6ed', lw=1)

# ============================================================
# SECTION 1: LOGO SYSTEM (y: 84-104)
# ============================================================
cn(15, 103, '一、品牌标识体系', size=11, bold=True, color='#1e3a5f', ha='left')
cn(15, 100.5, 'Logo System · 对径几何 + 北斗七星光点序列', size=8, color='#8899aa', ha='left')

# Horizontal Logo (large, left)
hc_x, hc_y = 42, 92
card(hc_x, hc_y, 50, 14)
draw_dipper(hc_x - 17, hc_y, scale=1.0)
cn(hc_x - 4, hc_y + 2.5, '对径智轴', size=13, bold=True, color='#1e3a5f', ha='left')
cn(hc_x - 4, hc_y - 2.5, 'Diameter AI Innovation Belt', size=7, color='#2980b9',
   ha='left', style='italic')
cn(hc_x, hc_y - 11, '横版标识 · Horizontal Logo', size=8, bold=True, color='#34495e')

# Vertical Logo (middle)
vc_x, vc_y = 95, 92
card(vc_x, vc_y, 22, 20)
draw_dipper(vc_x, vc_y + 2, scale=0.7)
cn(vc_x, vc_y - 6, '对径智轴', size=9, bold=True, color='#1e3a5f')
cn(vc_x, vc_y - 9, 'AI 创新带', size=6.5, color='#2980b9')
cn(vc_x, vc_y + 12, '竖版标识', size=8, bold=True, color='#34495e', va='bottom')

# Icon Logo (right)
ic_x, ic_y = 128, 92
card(ic_x, ic_y, 20, 20)
draw_dipper(ic_x, ic_y, scale=0.6, curve=True, ring=True)
cn(ic_x, ic_y + 12, '图标标识', size=8, bold=True, color='#34495e', va='bottom')

ax.plot([15, 145], [82, 82], color='#e0e6ed', lw=0.5)

# ============================================================
# SECTION 2: COLOR PALETTE (y: 60-80)
# ============================================================
cn(15, 79, '二、色彩体系', size=11, bold=True, color='#1e3a5f', ha='left')
cn(15, 76.5, 'Color Palette · 科技蓝为核心，铁路红为传承，生态绿为底色', size=8,
   color='#8899aa', ha='left')

colors = [
    ('#2980b9', '科技蓝', 'Tech Blue'),
    ('#1a5276', '深空蓝', 'Deep Blue'),
    ('#c0392b', '铁路红', 'Railway Red'),
    ('#e74c3c', '活力红', 'Vibrant Red'),
    ('#27ae60', '生态绿', 'Eco Green'),
    ('#2ecc71', '新芽绿', 'Sprout Green'),
    ('#2c3e50', '深灰', 'Dark Gray'),
    ('#7f8c8d', '中灰', 'Mid Gray'),
    ('#bdc3c7', '浅灰', 'Light Gray'),
    ('#f8f9fa', '雾白', 'Fog White'),
]

cw = 10       # color swatch width
ch = 6        # color swatch total height (half is swatch, half is text area)
gap = 3       # gap between swatches
cx_start = 17
row_y = 74    # top of first row swatch

for i, (hex_c, name_cn, name_en) in enumerate(colors):
    col = i % 5
    row = i // 5
    x = cx_start + col * (cw + gap)
    yy = row_y - row * (ch + 3.5)  # row spacing: ch + 3.5
    
    # Swatch rectangle (top half of ch)
    swatch_h = ch * 0.45
    border = '#dee2e6' if hex_c == '#f8f9fa' else 'white'
    sw = FancyBboxPatch((x, yy - swatch_h), cw, swatch_h,
                        boxstyle="round,pad=0.3", facecolor=hex_c,
                        edgecolor=border, lw=1)
    ax.add_patch(sw)
    
    # Text below swatch (compact spacing)
    text_top = yy - swatch_h
    cn(x + cw/2, text_top - 0.8, name_cn, size=7.5, bold=True, color='#2c3e50', va='top')
    cn(x + cw/2, text_top - 2.8, name_en, size=6, color='#7f8c8d', va='top')
    cn(x + cw/2, text_top - 4.5, hex_c.upper(), size=5.5, color='#95a5a6', va='top', style='italic')

# Color category descriptions on the right
dcx = 105
dcy = 74

cn(dcx, dcy, '色彩分类说明', size=9.5, bold=True, color='#1e3a5f', ha='left', va='bottom')

cat_items = [
    ('主色 · Primary Colors', '#2980b9', '品牌核心识别色，用于 Logo、标题、重点强调'),
    ('辅色 · Accent Colors', '#c0392b', '京张铁路传承色，用于警示、强调、活动视觉'),
    ('点缀 · Green Accents', '#27ae60', '生态底色，用于环境、可持续相关视觉元素'),
    ('中性 · Neutral Grays', '#7f8c8d', '背景与文字层级，确保阅读舒适度'),
]

for i, (label, color, desc) in enumerate(cat_items):
    yy = dcy - 3 - i * 3.5
    dot = mpatches.Circle((dcx, yy), 0.9, facecolor=color, edgecolor='white', lw=0.6)
    ax.add_patch(dot)
    cn(dcx + 2.5, yy + 0.5, label, size=7.5, bold=True, color='#34495e', ha='left', va='center')
    cn(dcx + 2.5, yy - 1.5, desc, size=6, color='#8899aa', ha='left', va='top')

ax.plot([15, 145], [59, 59], color='#e0e6ed', lw=0.5)

# ============================================================
# SECTION 3: TYPOGRAPHY (y: 37-55)
# ============================================================
cn(15, 54, '三、字体系统', size=11, bold=True, color='#1e3a5f', ha='left')
cn(15, 51.5, 'Typography System · 中英文双语字体规范', size=8, color='#8899aa', ha='left')

# Chinese column
col_cn_x = 20
cn(col_cn_x, 48.5, '中文字体 · Noto Sans CJK SC', size=9.5, bold=True, color='#1e3a5f', ha='left', va='bottom')
cn(col_cn_x, 46, '中文标题样张', size=16, bold=True, color='#1e3a5f', ha='left', va='top')
cn(col_cn_x, 43, 'Chinese Title · Bold', size=7, color='#95a5a6', ha='left', va='top')
cn(col_cn_x, 40.5, '中文正文：创新是引领发展的第一动力。', size=8.5,
   color='#34495e', ha='left', va='top')
cn(col_cn_x, 38.5, 'Chinese Body · Regular', size=7, color='#95a5a6', ha='left', va='top')

# Divider
ax.plot([70, 70], [38, 49], color='#e0e6ed', lw=0.5)

# English column
col_en_x = 78
cn(col_en_x, 48.5, '英文字体 · Inter / Noto Sans', size=9.5, bold=True, color='#1e3a5f', ha='left', va='bottom')
cn(col_en_x, 46, 'Innovation Belt Design', size=15, bold=True, color='#1e3a5f', ha='left', va='top')
cn(col_en_x, 43, 'English Title · Bold', size=7, color='#95a5a6', ha='left', va='top')
cn(col_en_x, 40.5, 'The diameter axis transforms heritage.', size=8,
   color='#34495e', ha='left', va='top')
cn(col_en_x, 38.5, 'English Body · Regular', size=7, color='#95a5a6', ha='left', va='top')

# Font weights on right
fw_x = 125
cn(fw_x, 48.5, '字重层级', size=9.5, bold=True, color='#1e3a5f', ha='left', va='bottom')
cn(fw_x, 46, 'Font Weights', size=7, color='#95a5a6', ha='left', va='top')

weights = [
    ('Light 细体', '#7f8c8d', False),
    ('Regular 常规', '#34495e', False),
    ('Medium 中黑', '#2c3e50', False),
    ('Bold 粗体', '#1e3a5f', True),
]
for i, (name, color, is_bold) in enumerate(weights):
    yy = 43 - i * 2.5
    cn(fw_x, yy, name, size=8.5, color=color, ha='left', va='center', bold=is_bold)

ax.plot([15, 145], [36, 36], color='#e0e6ed', lw=0.5)

# ============================================================
# SECTION 4: BRAND HIERARCHY + SAFE SPACE (y: 6-34)
# ============================================================

# Left: Brand Hierarchy
cn(15, 33, '四、品牌层级', size=11, bold=True, color='#1e3a5f', ha='left')
cn(15, 30.5, 'Brand Hierarchy · 四级品牌架构', size=8, color='#8899aa', ha='left')

levels = [
    ('主标识', 'Master Brand', '对径智轴', '#2980b9', 45, 4),
    ('三核子品牌', 'Three Cores', '众智园 · AI原点 · 大钟寺', '#8e44ad', 39, 3.4),
    ('活动子品牌', 'Event Sub-brand', 'AI创新节 · 京张对话', '#e67e22', 33, 2.8),
    ('导视子品牌', 'Wayfinding', '园区导视 · 站点标识', '#27ae60', 27, 2.2),
]

lvl_cx = 30
bar_spacing = 1.5
start_y = 27  # top of first bar

for i, (cn_n, en_n, ex, color, w, h) in enumerate(levels):
    bar_top = start_y - sum(levels[j][5] + bar_spacing for j in range(i))
    bar_bottom = bar_top - h
    cy = (bar_top + bar_bottom) / 2
    
    bar = FancyBboxPatch((lvl_cx - w/2, bar_bottom), w, h,
                          boxstyle="round,pad=0.3", facecolor=color,
                          edgecolor='white', lw=0.8, alpha=0.92)
    ax.add_patch(bar)
    cn(lvl_cx - w/2 + 2, cy, cn_n, size=8, bold=True, color='white', ha='left', va='center')
    cn(lvl_cx + w/2 - 2, cy, en_n, size=6, color='white', ha='right', va='center', alpha=0.85)
    cn(lvl_cx, bar_bottom - 0.5, ex, size=5.5, color='#8899aa', va='top')
    
    if i < len(levels) - 1:
        next_top = bar_top - h - bar_spacing
        ax.plot([lvl_cx, lvl_cx], [bar_bottom + 0.3, next_top - 0.3],
                color='#bdc3c7', lw=1, ls='--')
        dot = mpatches.Circle((lvl_cx, (bar_bottom + next_top) / 2),
                               0.5, facecolor='#bdc3c7', edgecolor='none')
        ax.add_patch(dot)

# Vertical divider between row 4 sections
ax.plot([75, 75], [6, 33], color='#e0e6ed', lw=0.5)

# Right: Safe Space + Minimum Size
ss_title_x = 82
cn(ss_title_x, 33, '五、最小尺寸与安全空间', size=11, bold=True, color='#1e3a5f', ha='left')
cn(ss_title_x, 30.5, 'Minimum Size & Safe Space', size=8, color='#8899aa', ha='left')

# Safe space diagram (centered lower in the section)
ss_cx = 94
ss_cy = 18     # center y of safe space diagram
safe_w = 18    # safe box width
safe_h = 12    # safe box height

# Dashed safe box
safe_box = mpatches.Rectangle((ss_cx - safe_w/2, ss_cy - safe_h/2), safe_w, safe_h,
                               facecolor='none', edgecolor='#e74c3c', ls='--', lw=1)
ax.add_patch(safe_box)

# Mini logo inside (left side)
lg_x = ss_cx - safe_w/2 + 3
lg_scale = 0.55
ax.plot([lg_x, lg_x], [ss_cy - 3.5*lg_scale*2, ss_cy + 3.5*lg_scale*2],
        color='#2980b9', lw=1.8, solid_capstyle='round')
for i, dy in enumerate(np.linspace(-3, 3, 5)):
    dc = 'white' if i == 2 else '#5dade2'
    dot = mpatches.Circle((lg_x, ss_cy + dy), 0.45, facecolor=dc, edgecolor='#1a5276', lw=0.4)
    ax.add_patch(dot)

# Logo text (right of logo mark)
cn(lg_x + 2.5, ss_cy + 1, '对径', size=7.5, bold=True, color='#1e3a5f', ha='left')
cn(lg_x + 2.5, ss_cy - 1.5, 'Diameter', size=5, color='#2980b9', ha='left', style='italic')

# Dimension arrows - top (above safe box)
top_arrow_y = ss_cy + safe_h/2 + 1.5
ax.annotate('', xy=(ss_cx - safe_w/2, top_arrow_y), xytext=(ss_cx + safe_w/2, top_arrow_y),
            arrowprops=dict(arrowstyle='<->', color='#e74c3c', lw=0.7))
cn(ss_cx, top_arrow_y + 1.2, 'X = 安全空间', size=5.5, bold=True, color='#e74c3c', va='bottom')

# Dimension arrows - left
left_arrow_x = ss_cx - safe_w/2 - 2.5
ax.annotate('', xy=(left_arrow_x, ss_cy - safe_h/2), xytext=(left_arrow_x, ss_cy + safe_h/2),
            arrowprops=dict(arrowstyle='<->', color='#e74c3c', lw=0.7))
cn(left_arrow_x - 1, ss_cy, 'X', size=5.5, bold=True, color='#e74c3c', ha='right', va='center')

cn(ss_cx, ss_cy - safe_h/2 - 1, 'Safe Space = Logo Height', size=5, color='#95a5a6', va='top')

# Minimum size specs (right side)
ms_x = 123
ms_y = 26

cn(ms_x, ms_y, '最小使用规范', size=9, bold=True, color='#1e3a5f', ha='left', va='bottom')

specs = [
    ('印刷应用 Print', '标识高度 ≥ 15mm', '#2980b9'),
    ('屏幕应用 Screen', '标识高度 ≥ 20px', '#27ae60'),
    ('反白应用 Reverse', '深色背景使用反白标识', '#8e44ad'),
    ('禁用规范 Don\'t', '禁止拉伸、变形、更改颜色', '#c0392b'),
]

for i, (title, desc, color) in enumerate(specs):
    yy = ms_y - 3 - i * 3.5
    dot = mpatches.Circle((ms_x, yy), 0.8, facecolor=color, edgecolor='none')
    ax.add_patch(dot)
    cn(ms_x + 2, yy + 0.5, title, size=7.5, bold=True, color='#34495e', ha='left', va='center')
    cn(ms_x + 2, yy - 1.5, desc, size=6, color='#8899aa', ha='left', va='top')

# ============================================================
# FOOTER
# ============================================================
cn(80, 4, '© Diameter AI Innovation Belt · Brand Identity Guidelines v1.0 · 概念示意 Conceptual',
   size=6.5, color='#aab2bd')

# Save
output_path = '/Coze/Drive/城市设计思路/submission-diameter-ai-belt/submissions/PKU-FranklinWang/diameter-ai-innovation-belt/assets/figures/brand-identity-system.png'
plt.savefig(output_path, dpi=300, bbox_inches='tight', facecolor='white',
            edgecolor='none', pad_inches=0.2)
plt.close()
print(f"Saved: {output_path}")
print("Layout sections:")
print("  Title:       y 106-118")
print("  Logo System: y 82-104")
print("  Color:       y 59-80")
print("  Typography:  y 36-55")
print("  Hier+Safe:   y 6-34")
