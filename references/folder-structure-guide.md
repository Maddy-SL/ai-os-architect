# AI OS Folder Structure & Routing Reference Guide

This guide establishes the canonical directory taxonomy for personal AI Operating Systems. It balances radical simplicity with structured agent navigation.

---

## 1. The 5 Core Life Hubs

Rather than fracturing life into dozens of confusing sub-directories, every personal AI OS should center on **5 foundational hubs**:

```
<AI_OS_ROOT>/
├── Brainstorm/         # Raw ideation, /grill-me drills, and concept routing gate
├── Career/             # Professional builds, consulting, career roadmap, resume, client work
├── Learnings/          # Research, study notes, book syntheses, technical deep dives
├── Other Activities/   # Sports, fitness, culinary exploration, creative hobbies, side quests
├── Personal/           # Daily life ops, personal finances, health, family, inbox dropzone
│
├── Outputs/            # Final deliverables (decks, reports, models) & automated audits
├── references/         # API specs, tool SOPs, and system cheat sheets
└── .agents/            # Runtime directory: skills hub + declarative subagents
```

---

## 2. Directory Specifications & Lifecycle

### A. `Brainstorm/` (The Staging & Routing Gate)
*   **Purpose**: The mandatory entry point for all unvetted ideas, side-project sparks, new venture thoughts, and automation experiments.
*   **Operating Rule**: **No new project folder may be created in `Career/` or elsewhere without first passing through `Brainstorm/`.**
*   **Subdirectories**:
    *   `_archive/`: Shelved, parked, or rejected concepts (with post-mortem notes).
*   **Files**:
    *   `TEMPLATE_BRAINSTORM.md`: Structured template containing the spark, `/grill-me` interview questions, and Council stress-test.
    *   `YYYY-MM-DD_Concept_Name.md`: Active brainstorm documents.

### B. `Career/` (Professional Growth & Deliverables)
*   **Purpose**: Professional execution, active career roadmaps, resume/CV assets, client engagements, and production software builds.
*   **Recommended Subdirectories**:
    *   `Projects/`: Active coding projects or standalone tools.
    *   `Engagements/`: Client consulting deliverables, discovery notes, BRDs, RCMs.
    *   `Roadmap/`: 12-18 month career goals, promotion trackers, resume versions, executive articulation notes.
*   **Key Files**:
    *   `README.md`: Central registry of all career projects and current status.
    *   `MEMORY.md`: Domain-specific career memory (promotions, feedback, milestones).

### C. `Learnings/` (Knowledge & Intellectual Capital)
*   **Purpose**: Study notes, academic courses, technical concept mastery, and book summaries.
*   **Recommended Subdirectories**:
    *   `01_Topic_Name/`, `02_Topic_Name/`: Standardized Level 2 topic folders (e.g. `01_Cognitive_Thinking`, `02_Cloud_Architecture`).
    *   Each topic folder should contain:
        *   `README.md`: Topic syllabus and study milestones.
        *   `notes/`: Synthesized Markdown notes.
        *   `assets/`: Visual diagrams, cheat sheets, reference PDFs.
*   **Key Files**:
    *   `README.md`: Master curriculum index.

### D. `Other Activities/` (Recreation, Hobbies & Sports)
*   **Purpose**: Protects and organizes personal fulfillment outside corporate and academic work.
*   **Recommended Subdirectories**:
    *   `Sports/`: Sports logs, cricket match analysis, workout tracking, event schedules.
    *   `Hobbies/`: Culinary exploration, travel itineraries, creative writing, music.
*   **Key Files**:
    *   `README.md`: Overview of active hobbies and recreational goals.

### E. `Personal/` (Life Operations, Finances & Dropzone)
*   **Purpose**: Daily routines, household ops, personal financial balance sheets, and raw inbox triage.
*   **Recommended Subdirectories**:
    *   `Finance/`: Personal investments, budget sheets, tax filings, net worth tracking.
    *   `Health/`: Medical history, routine checkups, nutrition plans.
    *   `Life/`: Core values, yearly reviews, family reminders, housing/apartment ops.
    *   `Inbox/`: The triage staging ground for incoming WhatsApp voice notes, email forward dumps, and quick mobile captures.
*   **Key Files**:
    *   `MEMORY.md`: Personal life milestones and durable preferences.

### F. Support Hubs
*   **`Outputs/`**:
    *   Holds finalized deliverable files (PDFs, PPTX decks, executive spreadsheets).
    *   Contains `Audits/` subdirectory for 15-day automated health audit reports.
*   **`references/`**:
    *   API documentation, schemas, and SOPs (e.g. `google-workspace-api.md`).
    *   *Rule*: Agents must check `references/` before researching external APIs.
*   **`.agents/`**:
    *   Runtime hub for `.agents/skills/` (tools & workflows) and `.agents/agents/` (specialist personas).

---

## 3. The `Brainstorm/` Automatic Routing State Machine

Every concept in `Brainstorm/` must resolve into an unambiguous routing destination:

```
[Incoming Spark / Idea]
          ↓
[Brainstorm/YYYY-MM-DD_Concept.md]
          ↓
[The /grill-me Drill]
- Clarify user assumptions
- Evaluate real-world workload & time constraints
- Test technical feasibility & failure modes
          ↓
[Council 3-Lens Stress Test]
1. Skeptical Buyer / User Lens
2. Feasibility Engineer Lens
3. Opportunity Cost Analyst Lens
          ↓
[Routing Decision Gate]
├── IF Career / Venture / Work initiative:
│   └── Route to `Career/Projects/[Project_Name]/` (Create folder + register in README)
│
├── IF Study Topic / Skill acquisition:
│   └── Route to `Learnings/[Topic_Name]/` (Create syllabus + notes folder)
│
├── IF Habit / Routine / Financial system:
│   └── Route to `Personal/[Category]/` (Update Personal/MEMORY.md)
│
├── IF Hobby / Sports / Creative pursuit:
│   └── Route to `Other Activities/[Category]/`
│
└── IF Shelved / Flawed / High Opportunity Cost:
    └── Move to `Brainstorm/_archive/` with fatal flaw documented
```

---

## 4. Adapting Existing User Setups (Pre-Flight Mapping)

When an AI OS is installed in a workspace that already contains folders, execute non-destructive mapping:

| Existing Folder Pattern | Recommended Mapping to 5-Hub Architecture | Action |
| :--- | :--- | :--- |
| Numbered folders (`01_Personal`, `03_Projects`) | Direct 1:1 match to `Personal/` and `Career/` | Keep existing folder name; create relative routing links. |
| Mixed codebases at root (`src/`, `backend/`, `app/`) | Group into `Career/Projects/[AppName]/` | Propose clean grouping to prevent root clutter. |
| Scattered study notes / PDFs at root | Group into `Learnings/[Topic_Name]/` | Move to relevant subject syllabus. |
| Disorganized markdown notes / scratchpads | Stage into `Brainstorm/` or `Personal/Inbox/` | Triage via `dropzone-triage`. |

*Rule*: Never delete or forcefully move existing user folders without explicit approval.
