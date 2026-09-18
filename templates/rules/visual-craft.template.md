# Visual Craft: Anti-Slop & Zero-Bloat Standards

When generating UI/UX components, HTML/React widgets, slides, presentations, flowcharts, architecture diagrams, or data sheets, adhere strictly to these senior-craft standards. Never produce generic AI slop or verbose marketing filler.

---

## 1. Zero-Bloat Microcopy & Lexicon Banning
- **Banned AI Jargon**: Never use words like:
  - *seamless, empower, leverage, holistic, robust, comprehensive, paradigm, cutting-edge, synergize, delve, pave the way, elevate*.
- **Concrete Nouns & Metrics**: Replace vague descriptions with exact technical and business metrics (e.g., `42ms TTFB`, `PostgreSQL replica`, `$142k ARR`, `CARO 2020 Clause 3(i)`).
- **Word Ceilings**:
  - Flowchart / Diagram Nodes: Max 2–4 words (`[Verb + Noun]`).
  - Slide & Card Titles: Max 3–6 words.
  - Card Subtext / Bullets: Max 1 single line.
  - Slide Total Word Count: Under 50 words total across all cards.
- **Zero Preamble / Postscript**: Do not narrate or explain your design in conversational chatter. Deliver the artifact cleanly.

---

## 2. Flowcharts & Architecture (Mermaid)
- **Node Geometry**:
  - `([User Action])` for entry points.
  - `[Service / Worker]` for compute processes.
  - `[(Database)]` for persistent storage.
  - `[[External API]]` for third-party services.
  - `{"Condition?"}` for decision branches.
- **No Sentences in Nodes**: Max 2–4 words per node.
- **Curated Palette**: Always style nodes using clean `classDef` themes (slate/zinc with single accent); never leave diagrams default unstyled gray.

---

## 3. Presentations & Slides
- **16:9 Canvas**: Design for widescreen aspect ratio (`aspect-video`).
- **Stat-First Architecture**: Feature hero metrics (`text-4xl font-extrabold font-mono`) with trend indicators (`+28% YoY`), followed by a 4-word label.
- **2–3 Column Grids**: Never output a single vertical bulleted wall of text.
- **Density**: Under 50 words total per slide.

---

## 4. Spreadsheets & Tabular Data
- **Alignment**:
  - Text: Left-aligned.
  - Numbers, currencies, percentages, timestamps: Right-aligned with `font-mono tabular-nums`.
  - Status chips: Centered.
- **Polish**: Zebra striping (`even:bg-slate-50/50`), uppercase sticky headers, double-bordered bold totals rows, micro-pill status badges (`bg-emerald-50 text-emerald-700`). No editorial commentary columns.
