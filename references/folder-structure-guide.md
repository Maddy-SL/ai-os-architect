# AI OS Folder Structure & Routing Reference Guide

This guide establishes the folder taxonomies, recommendation logic, and agent routing conventions for personal and professional AI Operating Systems.

---

## 1. The Context-Driven Recommendation Engine

An effective AI OS does not force a generic directory structure onto every person. During the discovery interview, the agent determines the user's **primary scope** (Work, Personal, or Hybrid) and **role**, then generates a tailored recommendation with explicit rationale.

### Folder Taxonomy Decision Matrix

| User Focus / Scope | Recommended Archetype | Top-Level Foldering Layout | Key Strengths & Best Fit |
| :--- | :--- | :--- | :--- |
| **Hybrid (Dual-Engine)** | **Standard Named Hubs** | `Brainstorm/`<br>`Career/`<br>`Learnings/`<br>`Other Activities/`<br>`Personal/`<br>`Outputs/`<br>`references/`<br>`.agents/` | Balances corporate/work demands with personal life, health, hobbies, and finance. Natural semantic naming. |
| **Hybrid (Strictly Ordered)** | **Numbered Workstations** | `00_Outputs/`<br>`01_Personal/`<br>`02_Learning/`<br>`03_Projects/`<br>`04_Brainstorms/`<br>`references/`<br>`.agents/` | Deterministic alphabetical sorting in file explorers and CLI tools; distinct numerical separation between life ops and professional builds. |
| **Work / Enterprise Only** | **Professional Consulting / Executive** | `Brainstorm/`<br>`Engagements/` (or `Clients/`)<br>`Projects/`<br>`Operations/`<br>`Knowledge/`<br>`Outputs/`<br>`references/`<br>`.agents/` | Strictly professional. Isolates client workpapers, delivery documents, and firm operations from external noise. |
| **Work / Technical Only** | **Software Engineer / Technical Builder** | `Brainstorm/`<br>`Projects/`<br>`Architecture/`<br>`Docs/`<br>`DevOps/`<br>`Outputs/`<br>`references/`<br>`.agents/` | Optimized for repos, ADRs (Architectural Decision Records), API schemas, and deployment pipelines. |
| **Personal Life Only** | **Life Operations & Self-Mastery** | `Brainstorm/`<br>`Life/`<br>`Finance/`<br>`Health/`<br>`Learnings/`<br>`Hobbies/`<br>`Inbox/`<br>`Outputs/`<br>`references/`<br>`.agents/` | Tailored for individuals, students, or creators focusing on personal finances, habit tracking, fitness, and lifelong learning without corporate clutter. |

---

## 2. Directory Specifications & Lifecycle by Archetype

### Archetype 1: Dual-Engine Hybrid OS

#### A. Standard Named Hubs
*   `Brainstorm/`: Staging area for raw ideas. Mandatory `/grill-me` routing gate. Auto-routes out.
*   `Career/`: Professional projects, client engagements, career roadmap, resume, and milestones.
*   `Learnings/`: Level-2 topic folders for academic research, technical study notes, and book syntheses.
*   `Other Activities/`: Hobbies, sports (cricket, gym), culinary, creative pursuits, travel.
*   `Personal/`: Life ops, personal finances (`Finance/`), health logs, and dropzone triage (`Inbox/`).
*   `Outputs/`: Deliverables (decks, reports, models) and 15-day automated health audits (`Audits/`).
*   `references/`: System API specifications, tool SOPs, and cheat sheets.
*   `.agents/`: Runtime directory with `.agents/skills/` and `.agents/agents/`.

#### B. Numbered Workstations (`00_Outputs` to `04_Brainstorms`)
*   `00_Outputs/`: Final deliverables lifecycle (Draft -> Final -> Archive) and `Audits/`.
*   `01_Personal/`: Life ops, `Finance/`, `Health/`, and `Inbox/` (Dropzone).
*   `02_Learning/`: Standardized Level-2 subject folders (`01_Topic`, `02_Topic`) with syllabus and notes.
*   `03_Projects/`: Active software builds, client consulting engagements, and tools.
*   `04_Brainstorms/`: Raw sparks, concept evaluation, and council stress-testing.
*   `references/` & `.agents/`: Shared specifications, connectors, and agent skills.

---

### Archetype 2: Work & Professional OS (Enterprise / Tech)

*   `Brainstorm/`: Proposals, architectural concepts, business initiatives.
*   `Projects/` (or `Codebases/`): Active development projects, microservices, internal tools.
*   `Engagements/` (or `Clients/`): Client-specific folders containing discovery notes, BRDs, RCMs, and deliverables.
*   `Operations/`: Meeting agendas, quarterly OKRs, hiring rubrics, vendor reviews, team updates.
*   `Knowledge/` (or `Docs/`): Industry regulations, architectural blueprints, best-practice playbooks.
*   `Outputs/`: Customer decks, audit models, executive memos, release builds.
*   `references/`: Internal API docs, database credentials references, cloud environment configurations.

---

### Archetype 3: Personal Life OS (Life Ops & Growth)

*   `Brainstorm/`: Personal venture ideas, creative writing concepts, travel sparks.
*   `Life/`: Core values, annual reviews, home & apartment ops, vehicle maintenance, family commitments.
*   `Finance/`: Personal investment ledgers, net worth calculations, tax filings, budget sheets.
*   `Health/`: Workout tracking, medical reports, nutrition plans, biomarker history.
*   `Learnings/`: University/course syllabi, book reading summaries, skill practice logs.
*   `Hobbies/`: Sports logs, creative projects, cooking recipes, travel itineraries.
*   `Inbox/`: Staging ground for unprocessed WhatsApp voice notes, email dumps, and web bookmarks.
*   `Outputs/`: Published blog posts, creative artifacts, and 15-day personal life audits.

---

## 3. The Universal `Brainstorm/` Routing State Machine

Regardless of the archetype chosen, **no project or major folder may be created without first passing through `Brainstorm/`**:

```
[Incoming Spark / Idea]
          ↓
[Brainstorm/YYYY-MM-DD_Concept.md]
          ↓
[The /grill-me Drill]
- Clarify user assumptions & problem definition
- Evaluate real-world workload & time constraints
- Test technical feasibility & failure modes
          ↓
[Council 3-Lens Stress Test]
1. Skeptical Buyer / User Lens
2. Feasibility Engineer Lens
3. Opportunity Cost Analyst Lens
          ↓
[Routing Decision Gate]
├── IF Professional Project / Client Engagement:
│   └── Route to `Career/Projects/` or `Projects/` or `03_Projects/`
│
├── IF Study Topic / Skill acquisition:
│   └── Route to `Learnings/[Topic_Name]/` or `02_Learning/[Topic_Name]/`
│
├── IF Life Habit / Financial / Operational system:
│   └── Route to `Personal/` or `Finance/` or `Life/`
│
├── IF Hobby / Sports / Creative pursuit:
│   └── Route to `Other Activities/` or `Hobbies/`
│
└── IF Shelved / Flawed / High Opportunity Cost:
    └── Move to `Brainstorm/_archive/` with failure analysis documented
```

---

## 4. Adapting Existing User Setups (Non-Destructive Mapping)

When installing in a workspace that already contains existing files or directories:

1. **Perform Silent Pre-Flight Scan**: Detect existing folders (`src/`, `docs/`, `01_Personal/`, `Projects/`, etc.).
2. **Present Non-Destructive Mapping**: Propose keeping high-value folders intact while wrapping them with the AI OS navigation layer:

| Existing Folder Pattern | Archetype Mapping | Non-Destructive Action |
| :--- | :--- | :--- |
| Pre-existing numbered folders (`01_Personal`, `03_Projects`) | Map directly to Numbered Workstation Archetype | Preserve folder names; establish relative links in `MEMORY.md` and `AGENTS.md`. |
| Codebase directories (`src/`, `backend/`, `frontend/`) | Map to `Projects/[AppName]/` or Work Archetype | Group into project folder or document root as active project build. |
| Loose notes, PDFs, or spreadsheets at root | Map to `Brainstorm/`, `Learnings/`, or `Inbox/` | Offer to triage loose files cleanly into the designated hubs. |
| Existing `.mcp.json` or scripts | Preserve and integrate into `connections.md` | Audit active connections without overwriting credentials. |

*Golden Rule*: Never delete, rename, or forcefully move existing user folders without explicit user confirmation.
