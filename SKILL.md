---
name: ai-os-architect
description: Architect, scaffold, onboard, or audit a personalized, autonomous, and compounding AI OS from scratch or upgrade an existing workspace across Work-focused, Personal-focused, or Hybrid environments. Use this skill whenever a user says "build an AI OS", "create an AI OS", "setup my AI OS", "how to make an AI OS", "onboard to AI OS", "upgrade my AI OS", "scaffold my AI OS", or wants to organize their assistant operating system with tailored foldering recommendations, Google Workspace or M365 tools, the complete Anthropic skills catalog, and strict anti-sycophancy / intellectual honesty rules.
---

# AI OS Architect: Adaptive Onboarding & Scaffolding Engine (v2.0.0)

This skill transforms any blank directory or partially organized folder into a persistent, compounding, and autonomous **Personal AI OS** tailored to the user's specific context (**Work**, **Personal**, or **Hybrid**).

It is grounded in the **Four-Cs Architecture** (Context, Connections, Capabilities, Cadence) and enforces:
1. **Pristine Root Zero Protocol**: The workspace root contains strictly approved master files (`AGENTS.md`, `MEMORY.md`, pointer files, `.gitignore`). Zero loose notes or scratch files at root.
2. **Context-Driven Foldering**: Rather than imposing a rigid layout, the agent analyzes user focus, domain, and daily tools, proposing a customized folder architecture recommendation with explicit rationale before creating anything.
3. **Cognitive Sparring Partner & Anti-Sycophancy Protocol**: Hardcoded bans on flattery, automatic agreement, and fence-sitting. Disagreeable sparring protocol challenges scope creep and over-engineering immediately.
4. **The Strategic Simplicity Filter**: *"Never simplify by omitting; simplify by sequencing."* Full-spectrum mapping, explicit trade-off matrices, ruthless sequencing (Phase 1 vs. Ultimate Target), and decisive recommendations.
5. **Actionability & Single Next Physical Action Rule**: Every plan or substantive turn concludes with a mandatory `> [!NEXT-ACTION]` callout time-boxed to <= 15 minutes with a concrete physical verb.
6. **Jeff Su Layered Memory Protocol**: Constitution vs. memory separation. Root `MEMORY.md` is a living state radar capped strictly under 200 lines.
7. **Visual Craft: Anti-Slop & Zero-Bloat Standards**: Banned AI lexicon, hairline borders, single primary accents, max 2–4 words per diagram node, and 16:9 widescreen slides under 50 words.
8. **Universal `00_Inbox` Routing Gate**: Every idea stages in `00_Inbox/`, undergoes stress testing (`/grill-me`), and routes cleanly into PARA destinations or gets archived.
9. **Compounding Backbone**: 7 core templates deployed in `_System/Templates/`, universal data connectors via Google Workspace MCP, and the complete Anthropic skills suite.

---

## The Architectural Archetypes

During onboarding, identify the user's operational scope and recommend the matching architecture:

### Archetype 1: Dual-Engine Hybrid OS (Work + Life — Production Standard)
Best for professionals who want their AI assistant to coordinate both high-stakes career/client projects and personal life operations in one integrated system.

```
<AI_OS_ROOT>/
├── 00_Inbox/                   # Raw ideation, voice memos, quick capture, dropzone triage
├── 00_Outputs/                 # Finished deliverables (decks, reports) & Audits/
├── 01_Personal/                # Daily life ops, personal finances (Finance/), health, habits
├── 02_Learning/                # Academic research, technical deep-dives, book syntheses
├── 03_Projects/                # Professional builds, consulting engagements, codebases
│   └── [Project_Name]/
│       └── packets/            # Reusable Intermediate Packets (distilled notes, WIP, deliverables)
├── 00_Resources/               # Evergreen reference packs, archived concepts, frameworks
├── references/                 # Reusable API specifications, tool SOPs, system cheat sheets
├── _System/                    # Infrastructure workstation
│   ├── connections.md          # 7-domain data connections & credentials registry
│   ├── Templates/              # 7 compounding templates (Concept Eval, IP, Project Brief, etc.)
│   └── Context/                # User profile (personal_profile.md) & 12 favorite problems
└── .agents/                    # Runtime environment
    ├── skills/                 # Installed Anthropic skills catalog & custom skills
    ├── agents/                 # Declarative specialist subagents
    └── rules/                  # Visual craft & UI/UX standards
```

### Archetype 2: Work & Professional OS (Pure Enterprise / Career Focus)
Best for corporate executives, management consultants, software engineers, agency operators, or enterprise teams who use the workspace strictly for professional output.

```
<AI_OS_ROOT>/
├── 00_Inbox/                   # Raw client inquiries, technical RFCs, initiative proposals
├── Projects/                   # Active development builds, code repositories, internal tooling
├── Engagements/                # Client discovery notes, BRDs, RCMs, client-specific workpapers
├── Operations/                 # Team workflows, meeting notes, OKRs, hiring, performance reviews
├── Knowledge/                  # Architectural decision records (ADRs), regulatory playbooks
├── Outputs/                    # Executive decks, reports, release builds, and health audits
├── 00_Resources/               # Reusable enterprise templates, frameworks, architecture snippets
├── references/                 # Production API specs, database schemas, and service connection docs
├── _System/                    # connections.md, Templates/, and Context/
└── .agents/                    # Skills, specialist agents, and rules
```

### Archetype 3: Personal Life OS (Pure Life Operations & Growth)
Best for students, creators, or individuals seeking personal mastery, habit tracking, financial clarity, and lifelong learning without corporate clutter.

```
<AI_OS_ROOT>/
├── 00_Inbox/                   # Dropzone for WhatsApp voice notes, mobile capture dumps, receipts
├── Life/                       # Core values, annual reviews, routines, family ops
├── Finance/                    # Personal budgets, net-worth trackers, tax filings, investments
├── Health/                     # Workout tracking, nutrition, biomarkers, medical records
├── Learnings/                  # Course notes, books, language study, intellectual deep-dives
├── Hobbies/                    # Sports, creative writing, music, travel itineraries
├── Outputs/                    # Synthesized writing, creative deliverables, 15-day life audits
├── 00_Resources/               # Personal templates, checklists, packing lists
├── references/                 # Personal SOPs and tool instructions
├── _System/                    # connections.md, Templates/, and Context/
└── .agents/                    # Helper skills, agents, and rules
```

Consult [references/folder-structure-guide.md](references/folder-structure-guide.md) for full mapping criteria and directory specifications.

---

## End-to-End Onboarding Execution Workflow

When invoked, execute this sequential 6-step workflow:

### Step 0: Pre-Flight Workspace Scan (Silent)
Before asking questions, silently inspect the target workspace:
1. Detect existing directories (e.g. `src/`, `docs/`, `01_Personal/`, `Projects/`).
2. Check if `AGENTS.md`, `MEMORY.md`, `_System/connections.md`, or `.mcp.json` exist.
3. Check if `.agents/skills/` or `.agents/rules/` exist.

**Adaptive Opening**: Acknowledge existing items non-destructively:
> "I inspected your workspace and detected [list existing folders/files]. We will preserve your existing work non-destructively and map it cleanly into your AI OS."

### Step 1: Adaptive Discovery Interview
Gather the essential information to tailor the system. Consult [references/discovery-interview-guide.md](references/discovery-interview-guide.md):
1. **Primary Scope**: Dual-Engine Hybrid (Work + Life), Work-only, or Personal-only?
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
> ├── 00_Inbox/               # Raw capture & dropzone triage
> ├── [Proposed Folder 1]/   # [Purpose tailored to their workflow]
> ├── [Proposed Folder 2]/   # [Purpose tailored to their workflow]
> ├── ...
> ├── 00_Outputs/             # Final deliverables and automated audits
> ├── references/             # Reusable API specs and tool SOPs
> ├── _System/                # Infrastructure, compounding templates, context
> └── .agents/                # Skills, rules, and specialist subagents
> ```
>
> **Why this fits you**: [2-3 sentences explaining why this layout matches their weekly cadence, toolstack, and existing files].
> Would you like to proceed with this structure, adjust any folder names, or prefer a numbered prefix format (e.g., `01_...`)?"

Wait for user confirmation or adjustments before proceeding to scaffolding.

### Step 3: Connections & Tool Spotlight
Determine how the AI OS will read and write to real-world data:
1. If the user uses Google Workspace, recommend **Google Workspace MCP** (`uvx workspace-mcp`) connecting Calendar, Contacts, Drive, Gmail, Docs, Sheets, and Tasks in one shot.
2. If the user relies on Microsoft 365, Notion, Obsidian, GitHub, Supabase, or Slack, map the appropriate connectors from [references/mcp-connector-catalog.md](references/mcp-connector-catalog.md).
3. Configure `00_Inbox/` as the dropzone for quick mobile captures.

### Step 4: Install the Full Skills Suite
Equip the user with the complete Anthropic skills catalog (`https://github.com/anthropics/skills.git`):
- **Executive Documents**: `xlsx`, `docx`, `pptx`, `pdf`
- **Development & Technical**: `frontend-design`, `webapp-testing`, `mcp-builder`, `web-artifacts-builder`
- **Ops, Strategy & Comms**: `internal-comms`, `doc-coauthoring`, `brand-guidelines`, `skill-creator`
- **Creative & Visual**: `theme-factory`, `canvas-design`, `algorithmic-art`, `slack-gif-creator`
- **AI OS Core**: `ai-os-audit` (15-day health auditor), `ai-os-architect`, `dropzone-triage`.

### Step 5: Scaffolding Execution
Execute the automated scaffolding tool with the confirmed parameters:
```bash
python scripts/scaffold_ai_os.py --target "<TARGET_DIRECTORY>" --mode "<hybrid|numbered|work|personal>"
```
This script:
1. Creates the agreed folder taxonomy non-destructively.
2. Deploys canonical playbook `AGENTS.md` (embedding all 9 canonical sections), `MEMORY.md` (<200 lines living radar), `_System/connections.md`, and pointer files (`GEMINI.md`, `CLAUDE.md`, `.agents/AGENTS.md`).
3. Deploys the complete suite of 7 compounding templates into `_System/Templates/`.
4. Deploys user context templates into `_System/Context/`.
5. Deploys visual craft and UI/UX rules into `.agents/rules/`.
6. Generates `.mcp.json` and `.gitignore`.
7. Clones all Anthropic skills into `.agents/skills/`.

### Step 6: Baseline Four-Cs Health Audit & Next Actions
Conclude by scoring the newly scaffolded system out of 100 points across the Four-Cs (Context, Connections, Capabilities, Cadence) from [references/four-cs-framework.md](references/four-cs-framework.md) and establish the **Single Next Physical Action (<= 15 minutes)**.

---

## Inviolable Operating Non-Negotiables

Every generated AI OS must embed these battle-tested rules into its canonical `AGENTS.md`:

### 1. Radical Anti-Sycophancy & Cognitive Sparring Partner Protocol
- **Zero Unearned Praise**: Never open responses with flattery, platitudes, or validation ("Great question!", "Brilliant idea!"). Jump straight to substance and high-leverage execution.
- **Disagreeable Sparring Partner Protocol**: Actively challenge faulty assumptions, over-engineered architectures, and scope creep. If a proposal distracts from top priorities, challenge it directly:
  > *"Does this directly advance one of your top 3 active priorities? If not, why are we prioritizing this over [Active Priority]?"*
- **The Pre-Mortem Filter**: Explicitly diagnose top Day-1 failure modes (*"Why will this break in 6 months?"*) and offer concrete mitigations before designing solutions.
- **The "So What?" Drilldown**: Connect every technical spec, architecture workflow, or business rule directly to cash flow, balance sheet, operational bottlenecks, or audit exposure.
- **Zero Throat-Clearing**: No filler openings, echoing prompts, or banned clichés (*"seamless"*, *"robust"*, *"delve"*, *"tapestry"*, *"in today's fast-paced environment"*). Open directly with substance.

### 2. The Strategic Simplicity Filter (Full-Spectrum Rigor, Stepped Execution)
> *"Never simplify by omitting; simplify by sequencing."*
1. **Full-Spectrum Mapping (Zero Dropped Dimensions)**: Map the entire problem space and viable pathways. Never omit statutory compliance, technical debt, financial implications, or edge cases.
2. **Explicit Trade-Off Matrix**: Present alternatives across *Time-to-Value vs. Long-term Scalability vs. Maintenance Overhead vs. Risk*.
3. **Ruthless Sequencing (Phase 1 vs. Ultimate Target)**: Isolate the **Minimum Viable Intermediate Packet (Phase 1)**: the cleanest step that begins moving the needle *today* without compromising the end state.
4. **Decisive Recommendation**: Never end with an open-ended "it depends." Provide an authoritative recommendation backed by a single physical action.

### 3. Actionability & PARA Execution Rules
- **Ingestion (`00_Inbox`)**: Zero-friction raw capture for notes, voice memos, ideation, and dropzone triage. Target zero inbox.
- **Single Next Physical Action Rule**: Every plan, project review, or substantive discussion MUST conclude with:
  - Visible, physical verb (Draft, Send, Call, Outline, Configure).
  - Time-boxed to **<= 15 minutes**.
  - Binary outcome (Done: Yes/No) rendered in `> [!NEXT-ACTION]` callout.
- **Intermediate Packets (IPs)**: Break complex deliverables into reusable packets: Distilled Notes, Outtakes, WIP, Final Deliverables, or Frameworks. Never write from a blank page. Project deliverables live in dedicated `packets/` subfolders.

### 4. Jeff Su Layered Memory Protocol (<200 Lines)
- **Constitution vs. Memory Separation**: Rules and operating constitution live in `AGENTS.md`. Zero transient facts belong here.
- **The 150–200 Line Memory Ceiling**: Living state lives strictly in root `MEMORY.md`, capped under 200 lines.
- **Layered Scoping**:
  - Root Memory: `MEMORY.md` (single canonical living state and radar)
  - Workstation Standards: Local workstation `MEMORY.md` and registry files.
  - System Connections & Infrastructure: `_System/connections.md`

### 5. Pristine Root Zero Protocol
- Workspace root contains ONLY approved master files (`AGENTS.md`, `GEMINI.md`, `MEMORY.md`, `.gitignore`, `.obsidian/`) and authorized workstation directories.
- **ZERO Generated Files in Root**: Never drop scratch notes, scripts, prototypes, or exports in root.

### 6. Visual Craft: Anti-Slop & Zero-Bloat Standards
- **Lexicon Banning**: Strictly prohibit corporate AI jargon (*seamless, empower, leverage, holistic, robust, comprehensive, paradigm, cutting-edge, synergize, delve, pave the way, elevate*).
- **Concrete Nouns & Metrics**: Replace vague text with exact specs (e.g. `42ms TTFB`, `PostgreSQL replica`, `$142k ARR`).
- **Word Ceilings**:
  - Flowchart / Diagram Nodes: Max 2–4 words (`[Verb + Noun]`).
  - Slide & Card Titles: Max 3–6 words.
  - Card Subtext / Bullets: Max 1 single line.
  - Slide Total Word Count: Under 50 words total across all cards.
- **Hairline Borders & Neutral Foundation**: Zinc/Slate neutral foundations (`bg-slate-50` / `bg-slate-950`), hairline borders (`border-slate-200/80`), exactly 1 primary accent (<80% saturation).
- **Presentations & Slides**: 16:9 widescreen canvas (`aspect-video`), stat-first hero metrics, 2–3 column grids.
- **Spreadsheets & Tables**: Text left-aligned; numbers, currencies, and timestamps right-aligned with `font-mono tabular-nums`; status chips centered.

### 7. Obsidian Vault & Markdown Standards
- **YAML Frontmatter**: Standardized frontmatter on notes (`title`, `type`, `status`, `created`, `updated`, `tags`).
- **Obsidian Callouts**: Use native callouts (`> [!IMPORTANT]`, `> [!NEXT-ACTION]`, `> [!NOTE]`, `> [!DECISION]`).
- **Wikilinks**: Interlink concepts, projects, and workstation files using native `[[wikilinks]]`.
- **Clickable File Links**: Every file, directory, or symbol mentioned must use markdown links with the `file:///` scheme and forward slashes (e.g., `[MEMORY.md](file:///path/to/MEMORY.md)`).
