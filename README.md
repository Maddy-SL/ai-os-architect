# 🧠 AI OS Architect

[![License: MIT](https://img.shields.io/badge/License-MIT-blue.svg)](LICENSE)
[![Architecture: Four-Cs](https://img.shields.io/badge/Architecture-Four--Cs-emerald.svg)](references/four-cs-framework.md)
[![Skills: Anthropic Catalog](https://img.shields.io/badge/Skills-Anthropic%20Official-purple.svg)](https://github.com/anthropics/skills.git)
[![Status: Production Ready](https://img.shields.io/badge/Status-Production%20Ready-success.svg)]()

> **Transform any blank directory or messy workspace into an autonomous, compounding personal AI Operating System across Work, Personal, or Hybrid contexts.**

`ai-os-architect` is a production-grade Agent Skill and CLI scaffolding engine designed for modern AI coding assistants (Claude Code, Antigravity, Cursor, Codex). It interviews the user, gathers their unique operational scope, **dynamically recommends a tailored folder architecture** with clear rationale, configures data connectors (Google Workspace, Microsoft 365, GitHub, Notion), installs all 16+ official **Anthropic Skills**, and scaffolds an intuitive workspace governed by **Strict Anti-Sycophancy & Intellectual Honesty Non-Negotiables**.

---

## 🌟 Why AI OS Architect?

Most AI assistant setups suffer from three fatal failure modes:
1. **Context Bloat & Drift**: Notes and logs accumulate in one massive prompt or file until the LLM degrades into hallucinations.
2. **The "Passive Chatbot" Trap**: The AI only answers when spoken to, with zero real-world connection to calendar, email, or tasks.
3. **Sycophancy & Flattery**: Without explicit behavioral constraints, AI assistants automatically agree with flawed ideas, flatter the user, and generate unrealistic fantasy schedules.

`ai-os-architect` solves this by codifying:
*   **Dynamic Folder Recommendation Engine**: Rather than imposing a rigid structure, it analyzes user scope (Work, Personal, Hybrid) and tools, then proposes the optimal foldering structure before writing.
*   **The Brainstorm Auto-Routing Gate**: Ideas enter `Brainstorm/`, endure `/grill-me` drills, and route out to projects or get killed.
*   **Strict Anti-Sycophancy Protocol**: Hardcoded bans on flattery, automatic agreement, and contrarian swinging. Plain truth and trade-offs presented immediately.
*   **Universal Data Connectors**: Google Workspace MCP (connects 5 universal data domains in one shot), Microsoft 365, GitHub, Supabase, and mobile dropzones.
*   **Complete Anthropic Skills Arsenal**: Pre-loaded with `xlsx`, `docx`, `pptx`, `pdf`, `frontend-design`, `webapp-testing`, etc.
*   **The Four-Cs Health Audit**: 100-point scoring system (Context, Connections, Capabilities, Cadence) with automated 15-day audits.

---

## 📂 The 3 Architectural Archetypes

### 1. Dual-Engine Hybrid OS (Work + Life)
Balances corporate projects with personal life ops, health, and finances.

*Named Hubs Layout:*
```
<AI_OS_ROOT>/
├── Brainstorm/                 # Raw Ideation & Council Gate (Auto-routes out)
├── Career/                     # Professional Builds, Consulting, Deliverables, Roadmap
├── Learnings/                  # Research, Study Logs, Technical Syllabi, Books
├── Other Activities/           # Hobbies, Sports (Cricket, Gym), Culinary, Travel
├── Personal/                   # Daily Life, Finances (Finance/), Health, Inbox
├── Outputs/                    # Final Deliverables & 15-day Audits (Audits/)
├── references/                 # API Specs, Tool SOPs, System Cheat Sheets
└── .agents/                    # Runtime: Skills Hub (.agents/skills/) & Subagents
```

*Numbered Workstations Layout (`--mode numbered`):*
```
<AI_OS_ROOT>/
├── 00_Outputs/                 # Deliverables & Audits
├── 01_Personal/                # Life Ops, Finance, Health, Dropzone Inbox
├── 02_Learning/                # Research & Study Curricula
├── 03_Projects/                # Professional Builds & Client Engagements
├── 04_Brainstorms/             # Raw Ideation & Routing Gate
├── references/                 # Tool & API Specifications
└── .agents/                    # Runtime Agents & Skills
```

### 2. Work & Professional OS (`--mode work`)
For corporate executives, consultants, engineers, or founders focused purely on professional output.
```
<AI_OS_ROOT>/
├── Brainstorm/                 # Feature specs, initiative proposals, pitch ideas
├── Projects/                   # Active builds, code repositories, internal tools
├── Engagements/                # Client discovery, BRDs, RCMs, deliverables
├── Operations/                 # Team workflows, meeting agendas, OKRs
├── Knowledge/                  # Architecture records (ADRs), regulatory playbooks
├── Outputs/                    # Client decks, audit reports, executive memos
├── references/                 # Internal API specs, database schemas
└── .agents/                    # Specialist subagents and skills
```

### 3. Personal Life OS (`--mode personal`)
For personal self-mastery, finances, workouts, reading, and habits without corporate noise.
```
<AI_OS_ROOT>/
├── Brainstorm/                 # Personal ideas, creative writing sparks, travel
├── Life/                       # Core values, routines, household ops, reviews
├── Finance/                    # Personal investments, budgets, taxes
├── Health/                     # Workouts, nutrition, sleep logs, biomarkers
├── Learnings/                  # Course syllabi, book notes, language study
├── Hobbies/                    # Sports, creative writing, music, travel
├── Inbox/                      # Dropzone for WhatsApp voice notes and mobile dumps
├── Outputs/                    # Personal essays, creative deliverables, audits
├── references/                 # Personal SOPs and tool cheat sheets
└── .agents/                    # Helper skills and agents
```

---

## 🚦 Dynamic Recommendation & Brainstorm Routing Logic

During onboarding, the agent conducts a discovery interview and recommends the exact folder structure:

```
[Gather User Scope & Role] ──> [Suggest Tailored Foldering with Rationale] ──> [User Confirms / Customizes]
                                                                                          │
                                                                                          ▼
                                                                              [Scaffold System & Rules]
```

Every project thereafter follows the **Brainstorm State Machine**:
```
[Incoming Spark / Idea]
          ↓
[Brainstorm/YYYY-MM-DD_Concept.md]
          ↓
[Interactive /grill-me Drill]
(Probe assumptions, weekly hours, technical feasibility, and risks)
          ↓
[Routing Decision Gate]
├── IF Professional Build / Client Work: → Route to Career/Projects/ or Engagements/
├── IF Study Topic / Skill Acquisition:  → Route to Learnings/[Topic_Name]/
├── IF Life Habit / Financial System:    → Route to Personal/ or Finance/
├── IF Hobby / Sports / Creative:       → Route to Other Activities/ or Hobbies/
└── IF Flawed / High Opportunity Cost:   → Archive to Brainstorm/_archive/
```

---

## 🚀 Quickstart Installation

### Method 1: Install as an Agent Skill (Recommended)

Clone this skill directly into your agent skills directory:

```bash
# For Antigravity / AI OS:
git clone https://github.com/Maddy-SL/ai-os-architect.git .agents/skills/ai-os-architect

# For Claude Code:
git clone https://github.com/Maddy-SL/ai-os-architect.git .claude/skills/ai-os-architect
```

Once installed, simply prompt your agent:
> *"Build an AI OS for me"*  
> or  
> *"Upgrade my existing workspace into an AI OS"*

The agent will audit your directory, conduct the discovery interview, dynamically suggest your tailored folder structure, install all Anthropic skills, configure connectors, and scaffold the system.

---

### Method 2: Run the Interactive Terminal Wizard (No Agent Needed)

Run the interactive setup wizard directly in your terminal:

```bash
# Launch the interactive wizard
python ai-os-architect/scripts/interactive_onboard.py
```

It interviews you, shows the recommended foldering with rationale, and sets up your entire workspace in under 60 seconds.

---

### Method 3: Headless CLI Scaffolding

For automated setups or scripted environments:

```bash
# Dual-Engine Hybrid (5 Core Life Hubs - default)
python ai-os-architect/scripts/scaffold_ai_os.py --target "." --mode hybrid

# Numbered Workstations (00_Outputs, 01_Personal, 02_Learning, 03_Projects, 04_Brainstorms)
python ai-os-architect/scripts/scaffold_ai_os.py --target "." --mode numbered

# Work & Professional Only (Enterprise)
python ai-os-architect/scripts/scaffold_ai_os.py --target "." --mode work

# Personal Life Only
python ai-os-architect/scripts/scaffold_ai_os.py --target "." --mode personal

# Fast offline mode (skip git cloning)
python ai-os-architect/scripts/scaffold_ai_os.py --target "." --skip-clone
```

---

## 🛡️ Inviolable Operating Non-Negotiables

Every AI OS scaffolded by this engine embeds these non-negotiables into `AGENTS.md`:

1. **Radical Intellectual Honesty & Anti-Sycophancy**:
   - Strict ban on flattery, automatic agreement, and contrarian swinging.
   - Tells the user the hard truth, trade-offs, and fatal flaws plainly.
2. **Answer First with Balanced Triad**:
   - Delivers the solution, execution nuances, and fatal risks together in the very first turn.
   - Clarifies only when two interpretations would produce materially different work.
3. **Grounding in Real Constraints**:
   - Factors in actual weekly corporate workload (e.g. 45-55 hr job) and deep-work bandwidth.
4. **Memory Discipline (<80 Lines)**:
   - Root `MEMORY.md` is strictly an index. Detailed history lives in project folders; old milestones archive to `00_Resources/`.
5. **Backtracking & Self-Repair**:
   - When an agent encounters a broken link or routing miss, it must diagnose why and repair documentation immediately.
6. **Verification Rigor**:
   - Calculations, regulatory citations, and code logic are verified twice before finalizing.
7. **Executive Density & Clean Output**:
   - High information density; clean email copy with zero markdown asterisks (`**`). Concludes with a Quick Summary.

---

## 📦 What's Included

*   `SKILL.md`: The progressive-disclosure skill prompt compatible with Claude Code, Antigravity, and Cursor.
*   `references/`: Deep architectural guides for folder taxonomy, Anthropic skills catalog, MCP connectors, discovery interview script, and the Four-Cs scoring rubric.
*   `templates/`: Production-ready templates for `AGENTS.md`, `MEMORY.md`, `connections.md`, `TEMPLATE_BRAINSTORM.md`, and pointer files.
*   `scripts/scaffold_ai_os.py`: Multi-mode cross-platform scaffolding engine.
*   `scripts/interactive_onboard.py`: Terminal interview wizard with tailored foldering recommendations.
*   `evals/evals.json`: Comprehensive test scenarios covering hybrid, work, personal, and existing workspace setups.

---

## 📄 License

MIT License. Free to use, modify, and distribute. Built by Madhur Lahoti.
