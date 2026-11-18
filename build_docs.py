# -*- coding: utf-8 -*-
"""把学习资料 Markdown 渲染成站点页面（与主页同一套样式）"""
import io, os, markdown, re

BASE = os.path.dirname(os.path.abspath(__file__))
DOCS = os.path.join(BASE, 'docs')

CSS = '''
:root{--ink:#0f172a;--body:#334155;--muted:#64748b;--line:#e2e8f0;--bg:#f8fafc;
--brand:#1e3a8a;--accent:#0d9488;--card:#ffffff;--code-bg:#f1f5f9;}
*{box-sizing:border-box}
body{margin:0;font-family:"Segoe UI","Microsoft YaHei",system-ui,sans-serif;
color:var(--body);background:var(--bg);line-height:1.75;font-size:16px}
.topbar{position:sticky;top:0;z-index:9;background:rgba(255,255,255,.92);backdrop-filter:blur(8px);
border-bottom:1px solid var(--line);padding:12px 24px;display:flex;gap:16px;align-items:center}
.topbar a.home{font-weight:700;color:var(--brand);text-decoration:none}
.topbar a.back{color:var(--accent);text-decoration:none;font-size:14px}
.wrap{max-width:960px;margin:0 auto;padding:40px 24px 80px}
h1{font-size:32px;color:var(--ink);border-bottom:3px solid var(--accent);padding-bottom:12px}
h2{font-size:24px;color:var(--brand);margin-top:44px;border-left:5px solid var(--accent);padding-left:12px}
h3{font-size:19px;color:var(--ink);margin-top:28px}
blockquote{margin:16px 0;padding:12px 18px;background:#eff6ff;border-left:4px solid var(--brand);
border-radius:0 8px 8px 0;color:#1e40af}
table{border-collapse:collapse;width:100%;margin:18px 0;background:var(--card);font-size:14.5px}
th{background:#1e3a8a;color:#fff;padding:9px 12px;text-align:left}
td{border:1px solid var(--line);padding:8px 12px;vertical-align:top}
tr:nth-child(even) td{background:#f8fafc}
code{background:var(--code-bg);padding:2px 6px;border-radius:4px;font-size:.92em;
font-family:Consolas,Menlo,monospace;color:#0f172a}
pre{background:#0f172a;color:#e2e8f0;padding:18px;border-radius:10px;overflow-x:auto}
pre code{background:none;color:inherit;padding:0}
hr{border:none;border-top:1px solid var(--line);margin:40px 0}
details{background:var(--card);border:1px solid var(--line);border-radius:8px;padding:12px 16px;margin:12px 0}
summary{cursor:pointer;font-weight:600;color:var(--brand)}
ul li,ol li{margin:4px 0}
strong{color:var(--ink)}
.dmath{background:var(--card);border:1px solid var(--line);border-left:4px solid var(--accent);
border-radius:8px;padding:14px 20px;margin:14px 0;font-family:Georgia,'Times New Roman',serif;
font-size:17px;color:var(--ink);overflow-x:auto;white-space:pre-wrap}
'''

def render(md_path, title, out_name):
    src = io.open(md_path, encoding='utf8').read()
    # 展示公式 $$...$$ 包成公式框
    src = re.sub(r'\$\$([^$]+)\$\$', lambda m: '<div class="dmath">' + m.group(1).strip() + '</div>', src, flags=re.S)
    # 行内公式 $...$ 保留原样（markdown 会当普通文本，去除美元符号更干净）
    src = re.sub(r'(?<!\w)\$([^$\n]+)\$(?!\w)', r' \1 ', src)
    html_body = markdown.markdown(src, extensions=['tables', 'fenced_code', 'toc'])
    page = f'''<!DOCTYPE html>
<html lang="zh-CN"><head><meta charset="utf-8">
<meta name="viewport" content="width=device-width,initial-scale=1">
<title>{title} | 量子计算学习站</title>
<style>{CSS}</style></head>
<body>
<nav class="topbar">
  <a class="home" href="../index.html">⚛ 量子计算学习站</a>
  <a class="back" href="../index.html">← 返回首页</a>
</nav>
<div class="wrap">{html_body}</div>
</body></html>'''
    out = os.path.join(DOCS, out_name)
    io.open(out, 'w', encoding='utf8').write(page)
    print('built', out_name, len(page))

JOBS = [
    ('../量子计算面试题及参考答案.md', '量子计算面试题及参考答案（32 题带答案）', 'interview-qa.html'),
    ('../量子计算转岗面试/量子计算转岗面试资料.md', '前端转量子计算：系统学习资料（13 章）', 'bootcamp.html'),
    ('../集成学习算法介绍.md', '集成学习算法（面试版）', 'ensemble.html'),
    ('../集成学习-小学生版.md', '集成学习：好多小树一起想办法（小学生版）', 'ensemble-kids.html'),
    ('../监督学习算法-面试版.md', '监督学习常见算法（面试版）', 'supervised.html'),
    ('../监督学习-小学生版.md', '监督学习：跟着答案学本领（小学生版）', 'supervised-kids.html'),
]
for path, title, out in JOBS:
    render(os.path.join(BASE, path), title, out)

# 转岗资料 HTML 版（内嵌视频的那份）替换视频路径
p = os.path.join(BASE, '../量子计算转岗面试/量子计算转岗面试资料.html')
s = io.open(p, encoding='utf8').read()
s = s.replace('动画/', '../assets/videos/')
io.open(os.path.join(DOCS, 'bootcamp-live.html'), 'w', encoding='utf8').write(s)
print('built bootcamp-live.html')
