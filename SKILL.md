---
name: ai-os-architect
description: Architect, scaffold, onboard, or audit a personalized, autonomous, and compounding AI OS from scratch or upgrade an existing workspace. Use this skill whenever a user says "build an AI OS", "create an AI OS", "setup my AI OS", "how to make an AI OS", "onboard to AI OS", "upgrade my AI OS", "scaffold my AI OS", or wants to organize their personal assistant operating system with the 5 core life hubs (Brainstorm, Career, Learnings, Other Activities, Personal), Google Workspace MCP, the complete Anthropic skills catalog, and strict honesty non-negotiables.
---

# AI OS Architect: Autonomous Onboarding & Scaffolding Engine

This skill guides you in transforming any empty directory or partially organized folder into a persistent, compounding, and autonomous **Personal AI OS**.

It is grounded in the **Four-Cs Architecture** (Context, Connections, Capabilities, Cadence) and enforces radical simplicity through **5 Core Life Hubs**, the **Google Workspace MCP**, the full **Anthropic Skills Catalog**, and **Inviolable Honesty Non-Negotiables**.

---

## The 5 Core Life Hubs Architecture

Avoid over-complicated directory trees. The canonical AI OS standardizes on 5 primary hubs:

| Life Hub | Primary Directory | Core Purpose & Lifecycle |
| :--- | :--- | :--- |
| **Brainstorm** | `Brainstorm/` | Raw ideation, `/grill-me` drills, and the concept routing gate. **Auto-routes out.** |
| **Career** | `Career/` | Professional builds, consulting engagements, client deliverables, resume, career milestones. |
| **Learnings** | `Learnings/` | Academic research, study notes, technical deep-dives, book syntheses, topic syllabi. |
| **Other Activities** | `Other Activities/` | Sports (cricket, gym), hobbies, culinary exploration, creative pursuits, travel. |
| **Personal** | `Personal/` | Daily life ops, personal finances (`Finance/`), health, habits, and dropzone triage (`Inbox/`). |
| **Outputs** | `Outputs/` | Finished deliverables (decks, reports, models) and automated 15-day health audits (`Audits/`). |
| **References** | `references/` | Reusable API specifications, tool SOPs, and system cheat sheets. |
| **Agent Runtime** | `.agents/` | Skills hub (`.agents/skills/`) and declarative subagents (`.agents/agents/`). |

See [references/folder-structure-guide.md](references/folder-structure-guide.md) for full taxonomy details.

---

## Brainstorm Automatic Routing Logic

No project folder may be created in `Career/` or elsewhere without first passing through `Brainstorm/`:

```
[Incoming Spark / Idea]
          ↓
[Brainstorm/YYYY-MM-DD_Concept.md]
          ↓
[Interactive /grill-me Drill]
(Probe assumptions, weekly hours, technical feasibility, and risks)
          ↓
[Routing Decision Gate]
├── IF Career / Work initiative:       → Route to Career/Projects/ or Career/Engagements/
├── IF Study Topic / Skill to learn:   → Route to Learnings/[Topic_Name]/
├── IF Life Habit / Personal system:   → Route to Personal/[Category]/
├── IF Hobby / Sports / Recreation:    → Route to Other Activities/[Category]/
└── IF Flawed / High Opportunity Cost: → Archive to Brainstorm/_archive/
```

---

## End-to-End Onboarding Execution Workflow

When invoked, execute the following continuous 5-step sequence:

### Step 0: Pre-Flight Workspace Scan (Silent)
Before asking questions, inspect the target workspace using directory listing tools:
1. Detect existing directories (e.g. `src`, `docs`, `01_Personal`, custom names).
2. Check if `AGENTS.md`, `MEMORY.md`, `connections.md`, or `.mcp.json` exist.
3. Check if `.agents/skills` exists.

**Adaptive Opening**: Acknowledge detected items immediately:
> "I scanned your workspace and found [existing items]. We will preserve your existing work non-destructively and map it cleanly into the AI OS."

### Step 1: Adaptive Discovery Interview
Conduct an interactive interview using [references/discovery-interview-guide.md](references/discovery-interview-guide.md). Ask questions for clarity to deeply understand the person:
1. **Role & Daily Tools**: Title, core domain, daily software tools (Python, Excel, Figma, etc.).
2. **12–18 Month North Star**: Single most important career or venture milestone.
3. **Hard Constraints & Real Workload**: Actual weekly corporate load (e.g., 50 hrs) and realistic deep-work hours.
4. **Folder Alignment**: Confirm mapping of existing folders to the 5 Core Life Hubs.

### Step 2: Connections & Google Workspace MCP Spotlight
Explain that an AI OS must read AND write to real-world data:
1. Recommend the **Google Workspace MCP** (`uvx workspace-mcp`), which instantly connects 5 of the 7 universal data domains: Calendar, Contacts, Drive, Gmail, Tasks.
2. Identify remaining tools (GitHub, Supabase, Slack, Notion, WhatsApp).
Consult [references/mcp-connector-catalog.md](references/mcp-connector-catalog.md).

### Step 3: Install ALL Anthropic Skills by Default
Inform the user that all 16+ official skills from `https://github.com/anthropics/skills.git` are installed by default into `.agents/skills/`:
- `xlsx`, `docx`, `pptx`, `pdf` (Executive Document Suite)
- `frontend-design`, `webapp-testing`, `mcp-builder`, `web-artifacts-builder` (Dev Suite)
- `internal-comms`, `doc-coauthoring`, `brand-guidelines`, `skill-creator` (Ops & Comms)
- `theme-factory`, `canvas-design`, `algorithmic-art`, `slack-gif-creator` (Creative Suite)
Consult [references/anthropic-skills-catalog.md](references/anthropic-skills-catalog.md).

### Step 4: Scaffolding Execution
Execute the automated scaffolding script:
```bash
python scripts/scaffold_ai_os.py --target "<TARGET_DIRECTORY>"
```
This script:
1. Creates the 5 Core Life Hubs and support directories.
2. Clones all skills from `https://github.com/anthropics/skills.git` into `.agents/skills/`.
3. Renders canonical `AGENTS.md` (with honesty non-negotiables), `MEMORY.md` (<80 lines), `connections.md`, and pointer files (`CLAUDE.md`, `GEMINI.md`, `.agents/AGENTS.md`).
4. Generates `.mcp.json` with Google Workspace MCP configured.

### Step 5: Baseline Health Audit (Four-Cs Score)
Conclude by scoring the new setup out of 100 points using the Four-Cs standard (Context, Connections, Capabilities, Cadence) from [references/four-cs-framework.md](references/four-cs-framework.md) to celebrate progress and show the next highest-leverage improvements.

---

## Inviolable Operating Non-Negotiables

Every generated AI OS must embed these rules in its canonical `AGENTS.md`:

1. **Radical Intellectual Honesty**:
   - Disallow sycophancy (no flattery, no automatic agreement).
   - Disallow contrarian swinging (never oscillate between cheerleading and arguing).
   - Tell the user the truth plainly, with trade-offs and fatal flaws highlighted.
2. **Answer First with Balanced Triad**:
   - In the very first turn, present the substance, strengths, nuances, and fatal risks together.
   - Clarify only when two interpretations would produce materially different work.
3. **Grounding in Real Constraints**:
   - Plans, schedules, and timelines must factor in the user's actual weekly workload (e.g. 50-60 hr corporate job) and cognitive bandwidth.
4. **Memory Discipline (<80 Lines)**:
   - Root `MEMORY.md` is strictly an index (<80 lines).
   - Detailed project history stays in project folders; old milestones archive to `00_Resources/`.
5. **Brainstorm Decision Gate**:
   - Raw ideas cannot skip directly to active project folders. They must pass `/grill-me` in `Brainstorm/`.
6. **Backtracking & Self-Repair**:
   - When an agent encounters a broken link or routing miss, it must diagnose the failure and repair the routing index immediately.
7. **Single Source of Truth**:
   - Canonical rules live in `AGENTS.md` only. Pointer files contain zero rules.
