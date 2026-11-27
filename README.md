# ⚛ 量子计算学习站

面向**零基础转岗者**（尤其前端工程师）的量子计算学习包，静态站点，可直接部署到 GitHub Pages。

## 内容清单

| 类型 | 文件 | 说明 |
|---|---|---|
| 🏠 主页 | `index.html` | 学习路径 + 动画课程 + 资料导航 |
| 🎬 动画 ×4 | `assets/videos/` | 量子态转化五步（42s）、量子门与态演化、Grover 振幅放大、QPE 相位估计 |
| 📖 13 章资料 | `docs/bootcamp-live.html` | 五公设 / 数学 / 门完全手册 / 算法推导 / Qiskit，内嵌动画 |
| 🎯 面试题 | `docs/interview-qa.html` | 32 题带答案要点 + 考前自查清单 |
| 🌲 集成学习 | `docs/ensemble*.html` | 面试版 + 小学生版 |
| 🤖 监督学习 | `docs/supervised*.html` | 面试版 + 小学生版 |
| 📽️ 课件 | `assets/ppt/` | 面试串讲 PPT（动画版 16 页 / 纯净版 15 页） |
| ☁️ 量子云平台 | `docs/quantum-clouds.html` | 国内 8+ 平台功能调研、对比矩阵、官网截图（2026-11 调研） |
| 📄 Markdown 原文 | `docs/*.md` | 全部资料的源文件，可下载 |

## 本地预览

直接双击 `index.html` 即可（全部资源相对路径、无外链依赖）。

## 部署到 GitHub Pages

方式一（网页上传，最简单）：

1. 在 GitHub 新建仓库，如 `quantum-learning`；
2. 把本目录（`量子计算学习站/`）下的**全部内容**上传到仓库根目录（Add file → Upload files，注意保持文件夹结构）；
3. 仓库 → Settings → Pages → Source 选 `main` 分支 `/ (root)` → Save；
4. 等一两分钟，访问 `https://<你的用户名>.github.io/quantum-learning/`。

方式二（命令行）：

```bash
cd 量子计算学习站
git init
git add .
git commit -m "量子计算学习站"
git branch -M main
git remote add origin https://github.com/<你的用户名>/quantum-learning.git
git push -u origin main
# 然后在仓库 Settings → Pages 中启用 Pages（main / root）
```

> 仓库根目录已包含 `.nojekyll`，跳过 Jekyll 处理，中文文件名可直接访问。

## 目录结构

```
量子计算学习站/
├── index.html            # 主页
├── .nojekyll             # 跳过 GitHub Pages 的 Jekyll
├── build_docs.py         # Markdown → 文档页渲染脚本（python + markdown 库）
├── assets/
│   ├── videos/           # 4 支 Remotion 动画
│   ├── ppt/              # 2 份课件 PPT
│   ├── poster.png        # 主动画封面帧
│   └── screenshots/      # 4 张量子云平台官网实拍截图
└── docs/                 # 渲染好的文档页 + Markdown 原文
    └── quantum-clouds.html  # 国内量子云平台专题页
```

## 重新构建文档页

修改 Markdown 后重跑：

```bash
python build_docs.py
```
