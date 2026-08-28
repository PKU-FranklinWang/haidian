#!/usr/bin/env python3
"""
Generate Regional Synergy Map for Diameter AI Innovation Belt
京张AI创新带区域协同关系图
"""

import matplotlib.pyplot as plt
import matplotlib.patches as mpatches
from matplotlib import font_manager
from matplotlib.font_manager import FontProperties
import numpy as np

# Register Chinese font
font_path = '/usr/share/fonts/opentype/noto/NotoSansCJK-Regular.ttc'
font_manager.fontManager.addfont(font_path)
bold_font_path = '/usr/share/fonts/opentype/noto/NotoSansCJK-Bold.ttc'
font_manager.fontManager.addfont(bold_font_path)

# Create font properties
cn_font = FontProperties(fname=font_path)
cn_font_bold = FontProperties(fname=bold_font_path)

# Create figure
fig, ax = plt.subplots(1, 1, figsize=(16, 12), dpi=300)
fig.patch.set_facecolor('#f8f9fa')
ax.set_facecolor('#f8f9fa')

# Set axis limits
ax.set_xlim(0, 160)
ax.set_ylim(0, 120)
ax.set_aspect('equal')
ax.axis('off')

def cn_text(x, y, text, fontsize=10, fontweight='normal', color='#333333',
            ha='center', va='center', style='normal', zorder=5):
    """Helper to draw Chinese text with proper font"""
    fp = cn_font_bold if fontweight == 'bold' else cn_font
    return ax.text(x, y, text, fontsize=fontsize, color=color,
                   ha=ha, va=va, fontproperties=fp, style=style, zorder=zorder)

# ============================================================
# Title
# ============================================================
cn_text(80, 115, '区域协同关系图', fontsize=20, fontweight='bold', color='#1e3a5f')
cn_text(80, 110, 'Regional Synergy Relationship Map', fontsize=12, color='#6b7c8d')
cn_text(80, 106, '百年京张AI创新带 · 五大区域节点协同体系', fontsize=10, color='#8899aa')

# ============================================================
# Outer ring - 京津冀区域辐射
# ============================================================
outer_circle = mpatches.Circle((80, 60), 45, fill=False, edgecolor='#c9d3dd',
                                linestyle='--', linewidth=1.5, zorder=1)
ax.add_patch(outer_circle)

inner_circle = mpatches.Circle((80, 60), 35, facecolor='#e8eef3', edgecolor='#c9d3dd',
                                linewidth=1, alpha=0.6, zorder=1)
ax.add_patch(inner_circle)

cn_text(80, 14, '京津冀区域辐射圈', fontsize=11, fontweight='bold', color='#5a6b7c')
cn_text(80, 10.5, 'Jing-Jin-Ji Regional Radiation', fontsize=8, color='#8899aa')

# ============================================================
# Center - 百年京张AI创新带（对径智轴）
# ============================================================
ax.plot([80, 80], [40, 80], color='#2980b9', linewidth=8, solid_capstyle='round', zorder=5)

center_circle = mpatches.Circle((80, 60), 8, facecolor='#2980b9', edgecolor='#1a5276',
                                 linewidth=2, zorder=6)
ax.add_patch(center_circle)

cn_text(80, 63, '百年京张', fontsize=11, fontweight='bold', color='white', zorder=7)
cn_text(80, 57, 'AI创新带', fontsize=10, fontweight='bold', color='white', zorder=7)

# Small light dots along the diameter (Big Dipper style)
diameter_dots_y = np.linspace(45, 75, 7)
for i, y in enumerate(diameter_dots_y):
    if i == 3:
        continue  # center already drawn
    dot_size = 2.5 if i in [0, 6] else 1.8
    dot = mpatches.Circle((80, y), dot_size * 0.7, facecolor='white',
                           edgecolor='#1a5276', linewidth=0.8, zorder=7)
    ax.add_patch(dot)

cn_text(80, 48, '对径智轴', fontsize=9, color='#1a5276', fontweight='bold')

# ============================================================
# Regional nodes
# ============================================================
nodes = [
    # North - 怀柔科学城
    (80, 95, 'Huairou Science City', '怀柔科学城', '基础科研协同',
     '#27ae60', '#d5f5e3'),
    # Northeast - 未来科学城
    (107, 85, 'Future Science City', '未来科学城', '未来产业协同',
     '#9b59b6', '#ebdef0'),
    # East - 亦庄经开区
    (117, 60, 'Yizhuang ETDZ', '亦庄经开区', '成果转化协同',
     '#e67e22', '#fdebd0'),
    # Northwest - 北纬社区
    (53, 80, 'Beiwei Community', '北纬社区', '创新生活协同',
     '#16a085', '#d1f2eb'),
]

node_positions = {}

for (x, y, name_en, name_cn, subtitle_cn, color, light_color) in nodes:
    node_positions[name_cn] = (x, y)
    
    glow = mpatches.Circle((x, y), 9, facecolor=light_color, edgecolor='none', alpha=0.7, zorder=3)
    ax.add_patch(glow)
    
    node_circle = mpatches.Circle((x, y), 6.5, facecolor=color, edgecolor='white',
                                   linewidth=2, zorder=4)
    ax.add_patch(node_circle)
    
    # Label position
    label_dx = 0
    label_dy = 12
    ha = 'center'
    
    if x > 90:
        label_dx = 10
        label_dy = 0
        ha = 'left'
    elif x < 70:
        label_dx = -10
        label_dy = 0
        ha = 'right'
    
    cn_text(x + label_dx, y + label_dy, name_cn, fontsize=11, fontweight='bold',
            color=color, ha=ha)
    cn_text(x + label_dx, y + label_dy - 3.5, name_en, fontsize=7.5,
            color='#6b7c8d', ha=ha)
    cn_text(x + label_dx, y + label_dy - 7, subtitle_cn, fontsize=8,
            color='#8899aa', ha=ha, style='italic')

# ============================================================
# Synergy connection lines
# ============================================================
cx, cy = 80, 60

synergy_styles = {
    'knowledge': {'color': '#2980b9', 'linestyle': '-', 'linewidth': 2, 'label': '知识溢出 Knowledge Spillover'},
    'talent': {'color': '#8e44ad', 'linestyle': '--', 'linewidth': 2, 'label': '人才流动 Talent Flow'},
    'computing': {'color': '#16a085', 'linestyle': '-.', 'linewidth': 2, 'label': '算力调度 Computing Dispatch'},
    'testing': {'color': '#e67e22', 'linestyle': ':', 'linewidth': 2.5, 'label': '测试验证 Testing & Validation'},
    'commercial': {'color': '#27ae60', 'linestyle': '-', 'linewidth': 1.2, 'label': '成果转化 Commercialization'},
}

def draw_synergy_line(ax, x1, y1, x2, y2, style, offset_perp=0):
    dx = x2 - x1
    dy = y2 - y1
    length = np.sqrt(dx**2 + dy**2)
    
    px = -dy / length
    py = dx / length
    
    ox1 = x1 + px * offset_perp
    oy1 = y1 + py * offset_perp
    ox2 = x2 + px * offset_perp
    oy2 = y2 + py * offset_perp
    
    ax.plot([ox1, ox2], [oy1, oy2], color=style['color'],
            linestyle=style['linestyle'], linewidth=style['linewidth'],
            alpha=0.7, zorder=2)
    
    arrow_size = 1.5
    ang = np.arctan2(oy2 - oy1, ox2 - ox1)
    ax.annotate('', xy=(ox2 - 5 * np.cos(ang), oy2 - 5 * np.sin(ang)),
                xytext=(ox2 - 8 * np.cos(ang), oy2 - 8 * np.sin(ang)),
                arrowprops=dict(arrowstyle='->', color=style['color'], lw=style['linewidth'], alpha=0.8))

# 怀柔科学城 (North) - 知识溢出 + 人才流动
hx, hy = node_positions['怀柔科学城']
draw_synergy_line(ax, cx, cy, hx, hy, synergy_styles['knowledge'], offset_perp=-1.5)
draw_synergy_line(ax, cx, cy, hx, hy, synergy_styles['talent'], offset_perp=1.5)

# 未来科学城 (Northeast) - 知识溢出 + 算力调度
fx, fy = node_positions['未来科学城']
draw_synergy_line(ax, cx, cy, fx, fy, synergy_styles['knowledge'], offset_perp=-1.5)
draw_synergy_line(ax, cx, cy, fx, fy, synergy_styles['computing'], offset_perp=1.5)

# 亦庄经开区 (East) - 成果转化 + 测试验证
yx, yy = node_positions['亦庄经开区']
draw_synergy_line(ax, cx, cy, yx, yy, synergy_styles['commercial'], offset_perp=-1.5)
draw_synergy_line(ax, cx, cy, yx, yy, synergy_styles['testing'], offset_perp=1.5)

# 北纬社区 (Northwest) - 人才流动 + 算力调度
bx, by = node_positions['北纬社区']
draw_synergy_line(ax, cx, cy, bx, by, synergy_styles['talent'], offset_perp=-1.5)
draw_synergy_line(ax, cx, cy, bx, by, synergy_styles['computing'], offset_perp=1.5)

# Cross-node synergies
draw_synergy_line(ax, hx, hy, fx, fy, synergy_styles['knowledge'], offset_perp=0)
draw_synergy_line(ax, fx, fy, yx, yy, synergy_styles['commercial'], offset_perp=0)
draw_synergy_line(ax, bx, by, hx, hy, synergy_styles['talent'], offset_perp=0)

# ============================================================
# North arrow
# ============================================================
north_x, north_y = 148, 100
ax.annotate('', xy=(north_x, north_y + 8), xytext=(north_x, north_y - 4),
            arrowprops=dict(arrowstyle='->', color='#2c3e50', lw=2))
ax.plot([north_x - 3, north_x + 3], [north_y - 2, north_y - 2], color='#2c3e50', linewidth=1.5)
cn_text(north_x, north_y + 10, 'N', fontsize=12, fontweight='bold', color='#2c3e50')
cn_text(north_x, north_y - 7, '指北针', fontsize=7, color='#8899aa')

# ============================================================
# Legend
# ============================================================
legend_x = 15
legend_y_start = 45
legend_spacing = 5

cn_text(legend_x, legend_y_start + 2, '协同关系图例', fontsize=11, fontweight='bold',
        color='#1e3a5f', ha='left', va='bottom')
cn_text(legend_x, legend_y_start - 1, 'Synergy Types Legend', fontsize=8,
        color='#8899aa', ha='left', va='top')

for i, (key, style) in enumerate(synergy_styles.items()):
    y = legend_y_start - 6 - i * legend_spacing
    ax.plot([legend_x, legend_x + 12], [y, y], color=style['color'],
            linestyle=style['linestyle'], linewidth=style['linewidth'])
    cn_text(legend_x + 14, y, style['label'], fontsize=8.5, color='#34495e',
            ha='left', va='center')

# Node type legend
node_legend_y = legend_y_start - 6 - len(synergy_styles) * legend_spacing - 6
cn_text(legend_x, node_legend_y + 2, '区域节点', fontsize=10, fontweight='bold',
        color='#1e3a5f', ha='left', va='bottom')

node_legend_items = [
    ('#2980b9', '创新带核心 Core Belt'),
    ('#e8eef3', '北京市域 Beijing City'),
    ('#c9d3dd', '京津冀辐射 Jing-Jin-Ji'),
]

for i, (color, label) in enumerate(node_legend_items):
    y = node_legend_y - 3 - i * 4.5
    patch = mpatches.Circle((legend_x + 2, y), 2, facecolor=color, edgecolor='#95a5a6', linewidth=0.8)
    ax.add_patch(patch)
    cn_text(legend_x + 7, y, label, fontsize=8, color='#34495e',
            ha='left', va='center')

# ============================================================
# Scale bar
# ============================================================
scale_x = 125
scale_y = 14
scale_length = 20

ax.plot([scale_x, scale_x + scale_length], [scale_y, scale_y],
        color='#2c3e50', linewidth=2)
ax.plot([scale_x, scale_x], [scale_y - 1, scale_y + 1], color='#2c3e50', linewidth=2)
ax.plot([scale_x + scale_length, scale_x + scale_length], [scale_y - 1, scale_y + 1],
        color='#2c3e50', linewidth=2)
cn_text(scale_x + scale_length / 2, scale_y + 2.5, '10 km', fontsize=8,
        color='#2c3e50', ha='center', va='bottom')
cn_text(scale_x + scale_length / 2, scale_y - 3, '比例尺 · Scale', fontsize=7,
        color='#8899aa', ha='center', va='top')

# ============================================================
# Bottom notes
# ============================================================
cn_text(10, 5, '概念示意 · Conceptual Diagram', fontsize=7, color='#aab2bd',
        ha='left', va='bottom')
cn_text(150, 5, 'Diameter AI Innovation Belt © 2024', fontsize=7, color='#aab2bd',
        ha='right', va='bottom')

# Save
output_path = '/Coze/Drive/城市设计思路/submission-diameter-ai-belt/submissions/PKU-FranklinWang/diameter-ai-innovation-belt/assets/figures/regional-synergy-map.png'
plt.savefig(output_path, dpi=300, bbox_inches='tight', facecolor='#f8f9fa',
            edgecolor='none', pad_inches=0.2)
plt.close()

print(f"Regional synergy map saved to: {output_path}")
