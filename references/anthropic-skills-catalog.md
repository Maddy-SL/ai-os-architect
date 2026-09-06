# Anthropic Skills Catalog Reference Guide

**Official Repository**: [https://github.com/anthropics/skills.git](https://github.com/anthropics/skills.git)

In the AI OS architecture, **all skills from the official Anthropic repository are installed by default** into `<AI_OS_ROOT>/.agents/skills/`. This provides an immediate, battle-tested operational foundation across document creation, software engineering, visual design, and internal communications.

---

## Complete Catalog of Shipped Skills

| Skill Directory | Focus Area | Description & Core Triggers | Primary Dependencies |
| :--- | :--- | :--- | :--- |
| **`xlsx`** | Data & Finance | Create, format, formula-bind, and manipulate `.xlsx` workbooks. Enforces strict financial models, zero gridlines, and Comic Sans MS/Calibri typography. | `openpyxl`, Python 3 |
| **`docx`** | Professional Docs | Generate and format executive Word documents (`.docx`), proposals, BRDs, and templates with tables of contents, clean headers, and callouts. | `python-docx`, Python 3 |
| **`pptx`** | Presentations | Create, edit, split, and style PowerPoint presentations (`.pptx`). Layout control, speaker notes, and brand-aligned slide design. | `python-pptx`, Node.js |
| **`pdf`** | Document Pipeline | Extract text/tables, split, merge, encrypt, fill forms, and OCR scanned PDFs. Convert docs/pptx to PDF headlessly. | `pypdf`, `pdfplumber` |
| **`frontend-design`** | UI/UX & Web | Design distinctive, production-grade frontend interfaces in React, Tailwind CSS, or HTML/JS. Prevents generic cookie-cutter styling. | Node.js, Tailwind CSS |
| **`webapp-testing`** | QA Automation | Automated browser testing, screenshot capture, and UI verification using Playwright. Headless or visual UI assertion suites. | Playwright, Chromium |
| **`internal-comms`** | Executive Writing | Draft internal status reports, leadership updates, 3P memos, newsletters, incident reports, and company FAQs following proven corporate comms formulas. | Markdown |
| **`doc-coauthoring`** | Collaborative Specs| Structured workflows for drafting technical documentation, RFCs, proposals, and decision docs collaboratively with iterative refinement. | Markdown |
| **`mcp-builder`** | MCP Engineering | Step-by-step guide and template scaffolding for building custom Model Context Protocol (MCP) servers in Python (FastMCP) or TypeScript. | Python / Node.js |
| **`skill-creator`** | Meta-Skill Engine | Create, refine, benchmark, and optimize agent skills using evals, assertions, progressive disclosure, and test suites. | Python 3 |
| **`theme-factory`** | Visual Theming | 10 pre-set design themes (typography, color palettes, spacing tokens) applicable across HTML landing pages, slide decks, and reports. | CSS / Tailwind |
| **`web-artifacts-builder`** | Complex Web Apps | Build elaborate, stateful, multi-component React/Tailwind/shadcn web artifacts and interactive dashboards. | React, Vite, Tailwind |
| **`brand-guidelines`** | Brand Identity | Brand voice enforcement, messaging frameworks, visual consistency, logo positioning, and corporate identity compliance. | Markdown |
| **`algorithmic-art`** | Generative Art | Programmatic SVG/Canvas art creation, geometric patterns, generative math visualizations, and custom abstract graphics. | JavaScript / Python |
| **`canvas-design`** | Canvas Layouts | Visual design, poster layouts, hero banners, and high-impact social graphics on 2D canvas interfaces. | HTML5 Canvas / CSS |
| **`slack-gif-creator`** | Visual Messaging | Automated animated GIF generator and meme designer optimized for Slack reactions, internal celebrations, and team culture. | Python (`imageio`, `Pillow`) |

---

## Automated Installation & Synchronization

The scaffolding engine clones the repository into a temporary cache and copies all skill folders into `.agents/skills/`:

```bash
# Automated by scripts/scaffold_ai_os.py:
git clone --depth 1 https://github.com/anthropics/skills.git temp_skills
# Moves all folders directly into .agents/skills/
```

### Updating Anthropic Skills
To refresh installed Anthropic skills to the latest upstream version:
```bash
python scripts/scaffold_ai_os.py --update-skills
```
