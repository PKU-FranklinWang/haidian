#!/usr/bin/env python3
"""Generate offline HTML from proposal.md - single file, no external dependencies"""
import markdown
import os
import re

BASE = "/Coze/Drive/城市设计思路/submission-diameter-ai-belt/submissions/PKU-FranklinWang/diameter-ai-innovation-belt"

def generate_html(md_path, out_path, lang="zh", title=""):
    with open(md_path, 'r', encoding='utf-8') as f:
        content = f.read()
    
    # Extract frontmatter
    fm = {}
    if content.startswith('---'):
        parts = content.split('---', 2)
        if len(parts) >= 3:
            fm_text = parts[1]
            content = parts[2]
            for line in fm_text.strip().split('\n'):
                if ':' in line:
                    k, v = line.split(':', 1)
                    fm[k.strip()] = v.strip().strip('"')
    
    # Convert markdown to HTML
    html_content = markdown.markdown(
        content,
        extensions=['tables', 'fenced_code', 'toc', 'sane_lists']
    )
    
    # Generate TOC from headings
    headings = re.findall(r'<h([23])[^>]*id="([^"]*)"[^>]*>(.*?)</h\1>', html_content)
    toc_html = '<nav class="toc"><h3>目录 / Table of Contents</h3><ul>'
    current_level = 2
    for level, hid, htext in headings:
        lvl = int(level)
        if lvl == 3 and current_level == 2:
            toc_html += '<ul>'
            current_level = 3
        elif lvl == 2 and current_level == 3:
            toc_html += '</ul></li>'
            current_level = 2
        # strip HTML tags from heading text
        clean_text = re.sub(r'<[^>]+>', '', htext)
        toc_html += f'<li><a href="#{hid}">{clean_text}</a>'
        if lvl == 2:
            toc_html += '</li>'
    while current_level > 2:
        toc_html += '</ul>'
        current_level -= 1
    toc_html += '</ul></nav>'
    
    page_title = title or fm.get('title', 'Proposal')
    
    css = """
    * { margin: 0; padding: 0; box-sizing: border-box; }
    body {
        font-family: -apple-system, BlinkMacSystemFont, "Segoe UI", "PingFang SC",
                     "Microsoft YaHei", "Helvetica Neue", Arial, sans-serif;
        background: #f5f6f8;
        color: #1a1a2e;
        line-height: 1.8;
        font-size: 16px;
    }
    .container {
        max-width: 960px;
        margin: 0 auto;
        padding: 40px 30px;
        background: #fff;
        min-height: 100vh;
        box-shadow: 0 0 40px rgba(0,0,0,0.06);
    }
    .header {
        border-bottom: 3px solid #1e3a5f;
        padding-bottom: 24px;
        margin-bottom: 32px;
    }
    .header h1 {
        font-size: 2rem;
        color: #1e3a5f;
        margin-bottom: 8px;
    }
    .header .subtitle {
        color: #5a6c7d;
        font-size: 1.1rem;
    }
    .meta {
        display: flex;
        flex-wrap: wrap;
        gap: 16px;
        margin-top: 16px;
        font-size: 0.9rem;
        color: #6b7c8d;
    }
    .meta span {
        background: #eef2f7;
        padding: 4px 12px;
        border-radius: 4px;
    }
    .toc {
        background: #f0f4f8;
        border-left: 4px solid #2e86de;
        padding: 20px 24px;
        margin: 24px 0 32px;
        border-radius: 0 8px 8px 0;
    }
    .toc h3 {
        color: #1e3a5f;
        margin-bottom: 12px;
        font-size: 1.1rem;
    }
    .toc ul { list-style: none; padding-left: 0; }
    .toc ul ul { padding-left: 20px; margin-top: 4px; }
    .toc li {
        margin: 6px 0;
    }
    .toc a {
        color: #2e86de;
        text-decoration: none;
        font-size: 0.95rem;
    }
    .toc a:hover { text-decoration: underline; }
    h1, h2, h3, h4, h5, h6 {
        color: #1e3a5f;
        margin-top: 1.6em;
        margin-bottom: 0.8em;
        line-height: 1.4;
    }
    h2 {
        font-size: 1.5rem;
        border-bottom: 2px solid #dce4ec;
        padding-bottom: 8px;
        margin-top: 2em;
    }
    h3 { font-size: 1.2rem; color: #2c5282; }
    h4 { font-size: 1.05rem; color: #2d3748; }
    p { margin: 0.8em 0; }
    ul, ol { margin: 0.8em 0; padding-left: 2em; }
    li { margin: 0.4em 0; }
    blockquote {
        border-left: 4px solid #48bb78;
        background: #f0fff4;
        padding: 12px 20px;
        margin: 16px 0;
        color: #2d3748;
        border-radius: 0 6px 6px 0;
    }
    table {
        width: 100%;
        border-collapse: collapse;
        margin: 16px 0;
        font-size: 0.92rem;
    }
    th, td {
        border: 1px solid #cbd5e0;
        padding: 10px 12px;
        text-align: left;
    }
    th {
        background: #edf2f7;
        font-weight: 600;
        color: #2d3748;
    }
    tr:nth-child(even) { background: #f7fafc; }
    code {
        background: #edf2f7;
        padding: 2px 6px;
        border-radius: 3px;
        font-size: 0.9em;
        font-family: "SF Mono", Consolas, Monaco, monospace;
    }
    pre {
        background: #2d3748;
        color: #e2e8f0;
        padding: 16px;
        border-radius: 6px;
        overflow-x: auto;
        margin: 16px 0;
    }
    pre code {
        background: none;
        color: inherit;
        padding: 0;
    }
    hr {
        border: none;
        border-top: 1px solid #cbd5e0;
        margin: 32px 0;
    }
    img {
        max-width: 100%;
        height: auto;
        border-radius: 6px;
        margin: 16px 0;
        box-shadow: 0 2px 12px rgba(0,0,0,0.08);
    }
    a { color: #2b6cb0; }
    .footer {
        margin-top: 48px;
        padding-top: 24px;
        border-top: 1px solid #e2e8f0;
        color: #718096;
        font-size: 0.85rem;
        text-align: center;
    }
    @media print {
        body { background: #fff; }
        .container { box-shadow: none; max-width: 100%; padding: 20px; }
        .toc { page-break-after: always; }
        h2 { page-break-after: avoid; }
    }
    """
    
    html = f"""<!DOCTYPE html>
<html lang="{lang}">
<head>
<meta charset="UTF-8">
<meta name="viewport" content="width=device-width, initial-scale=1.0">
<title>{page_title}</title>
<style>{css}</style>
</head>
<body>
<div class="container">
<div class="header">
<h1>{page_title}</h1>
<div class="subtitle">{fm.get('summary', '')}</div>
<div class="meta">
<span>作者: {fm.get('author_github', '')}</span>
<span>版本: {fm.get('iteration', '')}</span>
<span>许可: {fm.get('license', '')}</span>
</div>
</div>
{toc_html}
<article>
{html_content}
</article>
<div class="footer">
Diameter AI Innovation Belt — Urban Design Proposal | Generated from proposal.md
</div>
</div>
</body>
</html>"""
    
    with open(out_path, 'w', encoding='utf-8') as f:
        f.write(html)
    print(f"Generated: {out_path} ({len(html)} bytes)")

# Generate Chinese version
generate_html(
    os.path.join(BASE, "proposal.md"),
    os.path.join(BASE, "report", "proposal.html"),
    lang="zh-CN",
    title="对径式AI创新带 — 百年京张AI创新带城市设计方案"
)
