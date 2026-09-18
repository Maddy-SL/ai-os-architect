# AI OS Folder Structure & Routing Reference Guide (v2.0.0)

This guide establishes the folder taxonomies, recommendation logic, and agent routing conventions for personal and professional AI Operating Systems under the **Pristine Root Zero Protocol**.

---

## 1. The Pristine Root Zero Protocol

A core architectural principle of AI OS v2.0.0 is **Root Zero Discipline**:
- The workspace root directory (`/`) contains **ONLY** approved master files and authorized first-level directories.
- **Strictly Approved Root Files**:
  - `AGENTS.md` (Canonical operating constitution & single source of truth)
  - `MEMORY.md` (Living state radar, capped under 200 lines)
  - `GEMINI.md`, `CLAUDE.md`, `.agents/AGENTS.md` (Pointer files to `AGENTS.md`)
  - `.gitignore` (Environment and cache rules)
  - Optional `.obsidian/` configuration folder
- **ZERO Generated Files at Root**:
  - No scratch notes, draft scripts, experiment files, or exports may ever be dropped into the root directory.
  - Scratch scripts live in dedicated subdirectories or IDE scratch spaces.
  - Deliverables route to `00_Outputs/` or project `packets/`.

---

## 2. The Context-Driven Recommendation Engine

During onboarding, the agent analyzes the user's primary focus (Work, Personal, or Hybrid) and proposes the optimal layout:

### Archetype Taxonomy Matrix

| User Focus / Scope | Recommended Archetype | Top-Level Foldering Layout | Key Strengths & Best Fit |
| :--- | :--- | :--- | :--- |
| **Hybrid (Dual-Engine)** | **Numbered Workstations** | `00_Inbox/`<br>`00_Outputs/`<br>`01_Personal/`<br>`02_Learning/`<br>`03_Projects/`<br>`00_Resources/`<br>`_System/`<br>`references/`<br>`.agents/` | Complete balance between corporate/client builds and personal life ops, health, and finance. Strict alphabetical ordering and deterministic routing. |
| **Work / Enterprise Only** | **Professional Consulting & Enterprise** | `00_Inbox/`<br>`Projects/`<br>`Engagements/`<br>`Operations/`<br>`Knowledge/`<br>`Outputs/`<br>`00_Resources/`<br>`_System/`<br>`references/`<br>`.agents/` | Strictly professional. Isolates client workpapers, delivery documents, and firm operations from external noise. |
| **Personal Life Only** | **Life Operations & Self-Mastery** | `00_Inbox/`<br>`Life/`<br>`Finance/`<br>`Health/`<br>`Learnings/`<br>`Hobbies/`<br>`Outputs/`<br>`00_Resources/`<br>`_System/`<br>`references/`<br>`.agents/` | Tailored for individuals, students, or creators focusing on personal finances, habit tracking, fitness, and lifelong learning without corporate clutter. |

---

## 3. Directory Specifications & Lifecycle

### Dual-Engine Hybrid OS (Production Standard)

*   `00_Inbox/`: Raw ideation, voice memo transcripts, quick capture dumps, and dropzone triage. Target is **Inbox Zero**. Auto-routes out into PARA workstations.
*   `00_Outputs/`: Finished deliverables lifecycle (Draft -> Final -> Archive) and automated 15-day health audits (`Audits/`).
*   `01_Personal/`: Life ops, `Finance/`, `Health/`, and daily personal routines. Local state tracked in `01_Personal/MEMORY.md`.
*   `02_Learning/`: Standardized Level-2 subject folders (`01_Subject`, `02_Subject`) with syllabus, reading notes, and syntheses.
*   `03_Projects/`: Active professional builds, client consulting engagements, and codebases. Master registry in `03_Projects/PROJECT_REGISTRY.md`. Intermediate Packets live in `03_Projects/[Project]/packets/`.
*   `00_Resources/`: Evergreen reference packs, archived concepts, and reusable cheat sheets.
*   `_System/`: System infrastructure hub:
    *   `_System/connections.md`: Universal data domain connections and credentials state.
    *   `_System/Templates/`: Compounding template library (Concept Evaluation, Intermediate Packet, Project Brief, Weekly Review, etc.).
    *   `_System/Context/`: User profile context (`personal_profile.md`) and cognitive filter (`twelve_problems.md`).
*   `references/`: API endpoint schemas and tool SOPs.
*   `.agents/`: Runtime directory with `.agents/skills/`, `.agents/agents/`, and `.agents/rules/`.

---

## 4. The Universal `00_Inbox/` Routing State Machine

Every new idea, capture, or proposal stages in `00_Inbox/` before entering active directories:

```
[Incoming Spark / Note / Voice Memo]
                 ↓
[00_Inbox/YYYY-MM-DD_Concept.md]
                 ↓
[The /grill-me Drill]
- Clarify assumptions & problem definition
- Evaluate real-world workload & time constraints
- Test technical feasibility & Day-1 failure modes (Pre-Mortem)
                 ↓
[Council 3-Lens Stress Test]
1. Skeptical Buyer / Stakeholder Lens
2. Feasibility Engineer Lens
3. Opportunity Cost Analyst Lens
                 ↓
[Routing Decision Gate]
├── IF Professional Build / Client Engagement:
│   └── Route to `03_Projects/[Project_Name]/` + Register in `PROJECT_REGISTRY.md`
│
├── IF Study Topic / Skill Acquisition:
│   └── Route to `02_Learning/[Topic_Name]/`
│
├── IF Life Habit / Personal Financial System:
│   └── Route to `01_Personal/` + Update `01_Personal/MEMORY.md`
│
├── IF Evergreen Resource / Reusable Framework:
│   └── Route to `00_Resources/` or `_System/Templates/`
│
└── IF Shelved / Flawed / High Opportunity Cost:
    └── Move to `00_Inbox/_archive/` with failure analysis documented
```

---

## 5. Intermediate Packets (IPs) Architecture

Complex deliverables must never be attempted in a single massive session. They are broken into reusable **Intermediate Packets** stored in `03_Projects/[Project]/packets/`:
- **IP-01: Distilled Notes**: Key research takeaways and summarized source material.
- **IP-02: Outtakes**: High-quality sections cut from earlier versions, preserved for reuse.
- **IP-03: Work-in-Process**: Working outlines, diagrams, and draft wireframes.
- **IP-04: Final Deliverables**: Shipped assets, decks, models, or pull requests.
- **IP-05: Reusable Frameworks**: Checklists, templates, and SOPs extracted from the completed work.
