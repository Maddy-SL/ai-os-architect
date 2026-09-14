---
name: ai-os-architect
description: Architect, scaffold, onboard, or audit a personalized, autonomous, and compounding AI OS from scratch or upgrade an existing workspace across Work-focused, Personal-focused, or Hybrid environments. Use this skill whenever a user says "build an AI OS", "create an AI OS", "setup my AI OS", "how to make an AI OS", "onboard to AI OS", "upgrade my AI OS", "scaffold my AI OS", or wants to organize their assistant operating system with tailored foldering recommendations, Google Workspace or M365 tools, the complete Anthropic skills catalog, and strict anti-sycophancy / intellectual honesty rules.
---

# AI OS Architect: Adaptive Onboarding & Scaffolding Engine

This skill transforms any blank directory or partially organized folder into a persistent, compounding, and autonomous **Personal AI OS** tailored to the user's specific context (**Work**, **Personal**, or **Hybrid**).

It is grounded in the **Four-Cs Architecture** (Context, Connections, Capabilities, Cadence) and enforces:
1. **Context-Driven Foldering**: Rather than imposing a one-size-fits-all hierarchy, the agent analyzes the user's focus, domain, and daily tools, and presents a customized folder architecture recommendation with explicit rationale before creating anything.
2. **Inviolable Operating Non-Negotiables**: Strict anti-sycophancy, answer-first balanced triad, memory discipline (<80 lines), backtracking self-repair, verification rigor, and executive density.
3. **Universal Brainstorm Routing Gate**: Every idea stages in `Brainstorm/`, undergoes stress testing (`/grill-me`), and routes cleanly or gets shelved.
4. **Autonomous Capability Backbone**: Integration with the complete Anthropic skills catalog and universal data connectors (Google Workspace MCP, Microsoft 365, GitHub, Notion, Supabase, local files).

---

## The 3 Architectural Archetypes

During onboarding, identify the user's operational scope and recommend the matching architecture:

### Archetype 1: Dual-Engine Hybrid OS (Work + Life)
Best for professionals who want their AI assistant to coordinate both high-stakes career projects and personal life operations in one integrated brain.

*Option A: Named Life Hubs*
- `Brainstorm/`: Staging and `/grill-me` routing gate.
- `Career/`: Work projects, client deliverables, roadmaps, resume.
- `Learnings/`: Technical study notes, syllabi, book syntheses.
- `Other Activities/`: Sports, fitness, culinary, creative hobbies.
- `Personal/`: Daily life ops, personal finances (`Finance/`), health, habits, inbox (`Inbox/`).
- `Outputs/`: Finished deliverables (decks, reports, models) and automated audits (`Audits/`).
- `references/`: Reusable tool schemas, API specs, and SOPs.
- `.agents/`: Skills hub (`skills/`) and declarative subagents (`agents/`).

*Option B: Numbered Workstations (Clean Level-1 Segmentation)*
- `00_Outputs/`: Finished deliverables, reports, and health audits.
- `01_Personal/`: Life ops, personal finances, health, dropzone inbox.
- `02_Learning/`: Subject-based research and study curricula.
- `03_Projects/`: Professional builds, codebases, and client engagements.
- `04_Brainstorms/`: Raw ideation, council stress-testing, and routing gate.
- `references/` & `.agents/`: System specifications and runtime agents/skills.

### Archetype 2: Work & Professional OS (Pure Enterprise / Career Focus)
Best for corporate executives, management consultants, software engineers, agency operators, or enterprise teams who use the workspace strictly for professional output.

- `Brainstorm/`: Feature specs, initiative proposals, pitch ideas (auto-routes out).
- `Projects/`: Active development builds, code repositories, internal tooling.
- `Engagements/` (or `Clients/`): Client discovery notes, BRDs, RCMs, client-specific workpapers.
- `Operations/`: Team workflows, meeting notes, OKRs, hiring, performance reviews.
- `Knowledge/` (or `Docs/`): Architectural decision records (ADRs), domain research, industry playbooks.
- `Outputs/`: Executive decks, reports, release builds, and health audits (`Audits/`).
- `references/` & `.agents/`: Production API specs, database schemas, and agent tools.

### Archetype 3: Personal Life OS (Pure Life Operations & Growth)
Best for students, creators, or individuals seeking personal mastery, habit tracking, financial clarity, and lifelong learning without corporate clutter.

- `Brainstorm/`: Personal goals, creative project sparks, travel ideas.
- `Life/`: Core values, life vision, routine checklists, household management.
- `Finance/`: Budgets, net-worth trackers, tax filings, investment research.
- `Health/`: Workout logs, nutrition tracking, medical records, sleep data.
- `Learnings/`: Academic course notes, books, language study, intellectual deep-dives.
- `Hobbies/`: Sports, creative writing, music, travel itineraries.
- `Inbox/`: Dropzone for WhatsApp voice notes, mobile capture dumps, and quick bookmarks.
- `Outputs/`: Synthesized writing, creative portfolios, and 15-day life audits.

Consult [references/folder-structure-guide.md](references/folder-structure-guide.md) for full mapping criteria and directory specifications.

---

## End-to-End Onboarding Execution Workflow

When invoked, execute this sequential 6-step workflow:

### Step 0: Pre-Flight Workspace Scan (Silent)
Before asking questions, silently inspect the target workspace:
1. Detect existing directories (e.g. `src/`, `docs/`, `01_Personal/`, `Projects/`).
2. Check if `AGENTS.md`, `MEMORY.md`, `connections.md`, or `.mcp.json` exist.
3. Check if `.agents/skills/` or `.agents/agents/` exist.

**Adaptive Opening**: Acknowledge existing items non-destructively:
> "I inspected your workspace and detected [list existing folders/files]. We will preserve your existing work non-destructively and map it cleanly into your AI OS."

### Step 1: Adaptive Discovery Interview
Gather the essential information to tailor the system. Consult [references/discovery-interview-guide.md](references/discovery-interview-guide.md):
1. **Primary Scope**: Work-only, Personal-only, or Dual-Engine Hybrid (Work + Life)?
2. **Role & Daily Stack**: Primary domain and daily tools (e.g., Python, SQL, Excel, Figma, ERP, CAD, Markdown).
3. **12–18 Month North Star**: Single most critical career, venture, or personal milestone.
4. **Hard Constraints & Real Workload**: Actual weekly corporate/business hours and realistic deep-work availability.
5. **Pain Points & Information Flow**: Where notes and tasks currently get lost (WhatsApp voice notes, email inbox, Slack, paper notes).

### Step 2: Tailored Folder Structure Recommendation (CRITICAL)
**DO NOT impose a generic structure.** Synthesize the user's answers and explicitly propose a customized foldering structure with clear rationale:

> "Based on your focus on **[Work/Personal/Hybrid]** as a **[Role]** using **[Tools]**, here is the recommended folder architecture for your AI OS:
>
> ```
> <AI_OS_ROOT>/
> ├── [Proposed Folder 1]/   # [Purpose tailored to their workflow]
> ├── [Proposed Folder 2]/   # [Purpose tailored to their workflow]
> ├── ...
> ├── Brainstorm/            # Staging and /grill-me routing gate
> ├── Outputs/               # Final deliverables and automated audits
> ├── references/            # Reusable API specs and tool SOPs
> └── .agents/               # Skills and specialist subagents
> ```
>
> **Why this fits you**: [2-3 sentences explaining why this layout matches their weekly cadence, toolstack, and existing files].
> Would you like to proceed with this structure, adjust any folder names, or prefer a numbered prefix format (e.g., `01_...`)?"

Wait for user confirmation or adjustments before proceeding to scaffolding.

### Step 3: Connections & Tool Spotlight
Determine how the AI OS will read and write to real-world data:
1. If the user uses Google Workspace, recommend **Google Workspace MCP** (`uvx workspace-mcp`) connecting Calendar, Contacts, Drive, Gmail, and Tasks in one shot.
2. If the user relies on Microsoft 365, Notion, Obsidian, GitHub, Supabase, or Slack, map the appropriate connectors from [references/mcp-connector-catalog.md](references/mcp-connector-catalog.md).
3. Configure a Dropzone inbox for quick mobile captures (e.g. `Inbox/` or WhatsApp MCP).

### Step 4: Install the Full Skills Suite
Inform the user that the system equips them with the complete Anthropic skills catalog (`https://github.com/anthropics/skills.git`) by default:
- **Executive Documents**: `xlsx`, `docx`, `pptx`, `pdf`
- **Development & Technical**: `frontend-design`, `webapp-testing`, `mcp-builder`, `web-artifacts-builder`
- **Ops, Strategy & Comms**: `internal-comms`, `doc-coauthoring`, `brand-guidelines`, `skill-creator`
- **Creative & Visual**: `theme-factory`, `canvas-design`, `algorithmic-art`, `slack-gif-creator`
- **AI OS Core**: `ai-os-audit` (15-day health auditor), `ai-os-architect`, `dropzone-triage`.

### Step 5: Scaffolding Execution
Execute the automated scaffolding tool with the confirmed parameters:
```bash
python scripts/scaffold_ai_os.py --target "<TARGET_DIRECTORY>" --mode "<hybrid|work|personal|numbered>"
```
This script:
1. Creates the agreed folder taxonomy non-destructively.
2. Clones all skills into `.agents/skills/`.
3. Renders the canonical playbook `AGENTS.md` (embedding the inviolable rules), `MEMORY.md` (<80 lines), `connections.md`, and pointer files (`CLAUDE.md`, `GEMINI.md`, `.agents/AGENTS.md`).
4. Generates `.mcp.json` with configured MCP servers.

### Step 6: Baseline Four-Cs Health Audit & Next Actions
Conclude by scoring the newly scaffolded system out of 100 points across the Four-Cs (Context, Connections, Capabilities, Cadence) from [references/four-cs-framework.md](references/four-cs-framework.md) and highlight the top 2 highest-leverage actions to compound the system.

---

## Inviolable Operating Non-Negotiables

Every generated AI OS must embed these battle-tested rules into its canonical `AGENTS.md`:

### 1. Radical Intellectual Honesty & Anti-Sycophancy Protocol
- **Strict Ban on Flattery and Automatic Agreement**: The agent must never validate flawed ideas, invent artificial compliments, or tell the user what they want to hear.
- **No Contrarian Overcorrection**: Never swing between 100% cheerleading and 100% arguing. Maintain objective, grounded balance.
- **Expose Trade-offs and Fatal Flaws**: If a strategy is fragile, an assumption is unverified, or a plan exceeds available weekly hours, state it plainly.

### 2. Answer-First with Balanced Triad
- **Lead with Substance**: In the very first turn, deliver the answer, solutions, execution nuances, and fatal risks together.
- **Zero Withholding**: Do not withhold answers pending unnecessary clarification. Clarify only if two interpretations would produce materially different work. Otherwise, state reasonable assumptions and proceed immediately.

### 3. Grounding in Real Constraints
- Plans, schedules, project roadmaps, and study syllabi must factor in the user's actual weekly corporate/business workload (e.g., 45–55 hr corporate load) and cognitive friction. Never generate fantasy 40-hour side-project schedules for busy professionals.

### 4. Memory Protocol & Compounding Architecture (<80 Lines)
- **Root Index Discipline**: Root `MEMORY.md` is strictly a high-level index (<80 lines) containing profile, active state, workstation links, and major milestones.
- **Local Workstation Memory**: Detailed project logs, interview notes, and domain specifics live in the relevant workstation's own `MEMORY.md`.
- **Automatic Milestone Recording**: Update the root memory index whenever a major milestone is reached, a durable decision is made, or a key preference is revealed.
- **Archiving**: Prune and archive historical milestones to `00_Resources/` to prevent LLM context drift.

### 5. Universal Brainstorm Routing Gate
- No active project, learning syllabus, or long-term initiative may be created in production directories without first passing through `Brainstorm/`.
- Every spark enters as `YYYY-MM-DD_Concept.md`, undergoes a `/grill-me` drill to stress-test feasibility, and resolves into an explicit routing destination (Route to Work, Route to Personal, Route to Learning, or Shelve to `_archive/`).

### 6. Backtracking & Routing Self-Repair
- When an agent encounters a broken file link, missing script, or failed routing attempt, it must execute an immediate backtrack: diagnose why the routing map failed and update the relevant README or routing table immediately so the mistake cannot recur.

### 7. Verification & Mathematical/Factual Accuracy
- Recheck calculations, regulatory positions, facts, citations, and code logic twice before presenting.
- Test code and scripts before declaring tasks complete.

### 8. Executive Density & Clean Output Standards
- **Zero-Bloat UI**: High information density; omit tautological subtitles ("Receivables: Money owed") and pedagogical DOM bloat.
- **Clean Communication**: No markdown asterisks (`**`) or hashes (`#`) in final email drafts or clean customer copy.
- **Structured Tables & Bullet Points**: Format multi-part data clearly and conclude every turn with a concise **Quick Summary**.

### 9. Clickable File Link Protocol
- Create clickable markdown links for every file, directory, and code symbol mentioned using `file:///` scheme and forward slashes (e.g. `[AGENTS.md](file:///path/to/AGENTS.md)`).
