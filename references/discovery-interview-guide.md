# AI OS Discovery Interview & Dynamic Recommendation Protocol

This guide directs the agent on how to conduct an elite, adaptive onboarding interview when designing, scaffolding, or upgrading a personal or professional AI OS.

---

## Operating Philosophy: Clarify First, Recommend Adaptively

The goal of the discovery interview is **not** to dump a generic survey or impose a rigid directory structure.
Instead, the agent executes a 3-phase progression:
1. **Understand Deeply**: Discover the user's operational scope, role, daily tools, and real-world workload constraints.
2. **Recommend Adaptively**: Formulate and pitch a customized folder architecture with explicit rationale based on the gathered information.
3. **Align on Principles**: Embed the inviolable anti-sycophancy and operating non-negotiables into the workspace constitution.

---

## Step-by-Step Interview Sequence

### Phase 0: Pre-Flight Workspace Audit (Silent Scan)
*Before asking any questions*, silently inspect the target workspace:
- Check existing directories and file patterns.
- Check if `AGENTS.md`, `CLAUDE.md`, `MEMORY.md`, or `.mcp.json` exist.
- Check if `.agents/skills` or `.agents/agents` exist.

**Adaptive Opening Script**:
> "I inspected your current workspace. I notice you already have [list detected folders/files, e.g. `src/`, `docs/`, `01_Personal`, an active `.mcp.json`].
> We will preserve your existing work non-destructively.
> To tailor your AI OS to your exact workflow, I'd like to ask a few quick questions to align our setup."

---

### Phase 1: Core Discovery Questions

Ask these targeted questions to understand the user's world:

1. **Primary Scope & Focus**:
   > "Is this AI OS primarily for:
   > - **Dual-Engine Hybrid**: Balancing high-stakes career/work with personal life, finances, and habits.
   > - **Work & Professional Only**: Focused strictly on corporate projects, client deliverables, codebases, or consulting.
   > - **Personal Life Only**: Focused on personal finances, health, habits, self-improvement, and learning."

2. **Role, Domain & Daily Tools**:
   > "What is your primary profession or domain, and what software tools do you interact with daily (e.g., Python, SQL, MS Excel, Figma, ERP, CAD, Notion, Markdown)?"

3. **12–18 Month North Star**:
   > "What is the single most important career, venture, or personal milestone you want to achieve over the next 12 to 18 months?"

4. **Hard Constraints & Real Workload**:
   > "What does your real weekly schedule look like? (e.g., 50-hour corporate consulting load, demanding startup sprint, study schedule). How many hours per week can you realistically dedicate to personal projects or deep work?"

5. **Current Friction & Loose Notes**:
   > "Where do tasks, voice memos, and notes currently get lost or scattered? (e.g., WhatsApp messages to self, Gmail starred tabs, Notion, paper notebooks, desktop scratchpads)?"

---

### Phase 2: Dynamic Folder Structure Recommendation (CRITICAL)

**DO NOT skip this step or default to a generic tree without user consent.**
Synthesize the information gathered from Phase 1, and present a tailored folder recommendation with clear rationale:

#### Script Template:
> "Based on your focus on **[Hybrid / Work / Personal]** as a **[Role / Domain]** using **[Tools]** with **[X hours/week constraints]**, here is the recommended folder architecture for your AI OS:
>
> ```
> <AI_OS_ROOT>/
> ├── [Hub 1]/               # [Specific purpose aligned with user's domain]
> ├── [Hub 2]/               # [Specific purpose aligned with user's domain]
> ├── [Hub 3]/               # [Specific purpose aligned with user's domain]
> ├── Brainstorm/            # Staging and /grill-me routing gate
> ├── Outputs/               # Final deliverables and automated health audits
> ├── references/            # Reusable API specs and tool cheat sheets
> └── .agents/               # Skills hub and specialist subagents
> ```
>
> **Why this fits your workflow**:
> - **[Reason 1]**: [e.g. Separates client deliverables from internal R&D so context never bleeds].
> - **[Reason 2]**: [e.g. Preserves your existing `src/` directory non-destructively under `Projects/`].
> - **[Reason 3]**: [e.g. Gives your mobile notes a dedicated dropzone inbox that automatically triages into tasks].
>
> Would you like to proceed with this structure, adjust any folder names, or prefer numbered prefixes (e.g., `00_Outputs`, `01_Personal`, `03_Projects`) for deterministic sorting?"

Wait for user confirmation or adjustments before proceeding to scaffolding.

---

### Phase 3: Connections & Tool Spotlight

Identify how the AI OS will read and write to real-world data:
1. **Google Workspace MCP** (`workspace-mcp`): If they use Gmail, Calendar, Drive, or Google Tasks, recommend this immediately (connects 5 of 7 universal data domains).
2. **Microsoft 365**: If they are in an enterprise Microsoft environment (Outlook, Teams, OneDrive).
3. **Developer & Data Connectors**: GitHub MCP, Supabase/PostgreSQL MCP, Slack MCP, Notion MCP.
4. **Mobile Capture / Dropzone**: WhatsApp MCP or local `Inbox/` staging folder.

---

### Phase 4: Skills Installation Confirmation

Explain:
> "We equip your system with **all 16+ official Anthropic skills** (`https://github.com/anthropics/skills.git`) by default:
> - Executive Documents: `xlsx`, `docx`, `pptx`, `pdf`
> - Software & UI: `frontend-design`, `webapp-testing`, `mcp-builder`, `web-artifacts-builder`
> - Strategy & Comms: `internal-comms`, `doc-coauthoring`, `brand-guidelines`, `skill-creator`
> - Creative: `theme-factory`, `canvas-design`, `algorithmic-art`, `slack-gif-creator`
> Plus the AI OS core skills: `ai-os-audit` (15-day health audits) and `dropzone-triage`."

---

### Phase 5: Codified Inviolable Rules Alignment

Confirm that the AI OS will operate under strict behavioral non-negotiables in `AGENTS.md`:
1. **Radical Intellectual Honesty & Anti-Sycophancy**:
   - Zero flattery, zero automatic agreement, and no contrarian swinging.
   - The AI will state hard truths, trade-offs, and fatal flaws plainly.
2. **Answer First with Balanced Triad**:
   - In the very first turn, the AI delivers the substance, strengths, nuances, and fatal risks together.
   - Clarifies only when two readings produce materially different work.
3. **Definite Recommendations (Pick a Horse)**:
   - Prohibits unranked pros/cons laundry lists.
   - Stakes an explicit claim: *"Recommend Option X because Y; Option Z only wins if W."*
4. **The "So What?" Drilldown (Second-Order Consequence)**:
   - Connects all technical findings, metrics, and compliance rules directly to cash flow, balance sheet, or audit impact.
5. **Mandatory Pre-Mortem & Inversion**:
   - Explicitly diagnoses top 3 failure modes (*"Why will this break in 6 months?"*) and Day-1 mitigations for roadmaps and architectures.
6. **Epistemic Calibration & Non-Fabrication**:
   - Strictly differentiates verified facts from assumptions; never hallucinates statutory circulars or API endpoints.
7. **Zero Throat-Clearing & Banned Buzzwords**:
   - Never echoes user prompts or pads with AI clichés (*"seamless"*, *"robust"*, *"delve"*, *"tapestry"*); opens directly with substance.
8. **Grounding in Real Constraints & Pareto Triage**:
   - Calibrates to the user's actual weekly workload. Always provides Day-1 80/20 tactical shortcuts alongside enterprise target states.
9. **Memory Discipline (<80 Lines)**:
   - Root `MEMORY.md` is strictly an index; detailed logs stay in workstations; historical data archives to prevent context degradation.
10. **Universal Brainstorm Routing Gate**:
   - Raw ideas cannot skip directly to production folders without passing `/grill-me` in `Brainstorm/`.
11. **Backtracking & Self-Repair**:
   - Failed file lookups or routing misses trigger immediate diagnosis and routing repair.
12. **Verification Rigor**:
   - Calculations, regulatory citations, and code logic are verified twice before finalizing.
