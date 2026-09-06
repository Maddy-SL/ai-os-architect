# 🧠 AI OS Architect

[![License: MIT](https://img.shields.io/badge/License-MIT-blue.svg)](LICENSE)
[![Architecture: Four-Cs](https://img.shields.io/badge/Architecture-Four--Cs-emerald.svg)](references/four-cs-framework.md)
[![Skills: Anthropic Catalog](https://img.shields.io/badge/Skills-Anthropic%20Official-purple.svg)](https://github.com/anthropics/skills.git)
[![Status: Production Ready](https://img.shields.io/badge/Status-Production%20Ready-success.svg)]()

> **Transform any blank directory or messy workspace into an autonomous, compounding personal AI Operating System.**

`ai-os-architect` is a production-grade Agent Skill and CLI scaffolding engine designed for AI coding assistants (Claude Code, Antigravity, Cursor, Codex). It guides any user through an interactive discovery interview, maps their personal 7 Tier-1 data domains, configures the **Google Workspace MCP**, installs all 16+ official **Anthropic Skills**, and scaffolds an intuitive workspace based on **5 Core Life Hubs** and **Inviolable Honesty Non-Negotiables**.

---

## 🌟 Why AI OS Architect?

Most AI assistant setups suffer from three fatal failure modes:
1. **Context Bloat & Drift**: Notes and logs accumulate in one massive prompt or file until the LLM degrades into hallucinations.
2. **The "Passive Chatbot" Trap**: The AI only answers when spoken to, with zero real-world connection to calendar, email, or tasks.
3. **Sycophancy & Cheerleading**: Without explicit behavioral constraints, AI assistants automatically agree with bad ideas and flatter the user.

`ai-os-architect` solves this by codifying:
*   **The 5 Core Life Hubs**: Radical organizational simplicity without nested clutter.
*   **The Brainstorm Auto-Routing Gate**: Ideas enter `Brainstorm/`, endure `/grill-me` drills, and route out to projects or get killed.
*   **Google Workspace MCP Priority**: Connects 5 of the 7 Universal Data Domains in a single configuration.
*   **Complete Anthropic Skills Arsenal**: Pre-loaded with `xlsx`, `docx`, `pptx`, `pdf`, `frontend-design`, `webapp-testing`, etc.
*   **Inviolable Non-Negotiables**: Hardcoded honesty, answer-first triad, and memory discipline (<80 lines).
*   **The Four-Cs Health Audit**: 100-point scoring system (Context, Connections, Capabilities, Cadence) with automated 15-day audits.

---

## 📂 The 5 Core Life Hubs Architecture

```
<AI_OS_ROOT>/
├── AGENTS.md                   # CANONICAL Operating Playbook (Single source of truth, <200 lines)
├── CLAUDE.md                   # Pointer to AGENTS.md
├── GEMINI.md                   # Pointer to AGENTS.md
├── MEMORY.md                   # Root Memory Index (<80 lines: Profile, State, High-Level Decisions)
├── connections.md              # Master Connections Registry (7 Universal Data Domains + Cloud DBs + Cron)
│
├── Brainstorm/                 # Raw Ideation & Council Gate (Auto-routes to appropriate hub)
│   ├── _archive/               # Shelved, parked, or rejected brainstorms
│   ├── TEMPLATE_BRAINSTORM.md  # Template with /grill-me + Decision Gate
│   └── README.md               # Brainstorm routing logic & instructions
│
├── Career/                     # Professional Builds, Consulting, Deliverables, Career Goals
│   ├── Projects/               # Active work projects & codebases
│   ├── Engagements/            # Client consulting / employer deliverables
│   ├── Roadmap/                # Career milestone planning & resume
│   └── README.md               # Master registry of active career initiatives
│
├── Learnings/                  # Research, Study Logs, Technical Notes, Book Summaries
│   ├── [Subject_Folders]/      # Topic-specific folders (notes, cheat sheets, references)
│   └── README.md               # Master learning syllabus & index
│
├── Personal/                   # Daily Life, Finances, Health, Routines
│   ├── Finance/                # Personal investments, budgets, taxes
│   ├── Health/                 # Fitness logs, medical records, nutrition
│   ├── Life/                   # Long-term personal goals, habits, ops
│   ├── Inbox/                  # Dropzone triage staging (WhatsApp dumps, voice memos, raw drops)
│   └── README.md
│
├── Other Activities/           # Hobbies, Sports, Creative Pursuits, Side Explorations
│   ├── Sports/                 # Cricket, fitness activities, matches
│   ├── Hobbies/                # Food/culinary exploration, casual writing, travel
│   └── README.md
│
├── Outputs/                    # Final Deliverables (Reports, Decks, Models) & Audits
│   ├── Audits/                 # Automated 15-day workspace health audit reports
│   └── README.md
│
├── references/                 # Knowledge Hub: Reusable API Specs & SOPs
│   ├── google-workspace-api.md # Endpoints, auth, and common queries for Google MCP
│   └── README.md
│
└── .agents/                    # Agent Runtime & Customizations
    ├── AGENTS.md               # Pointer to root AGENTS.md
    ├── agents/                 # Declarative Specialist Subagents (*.md)
    └── skills/                 # Agent Skills Hub (ALL Anthropic skills + Custom skills)
```

---

## 🚦 Automatic Routing Logic for `Brainstorm/`

No project folder can be created without passing through the `Brainstorm/` decision gate:

```
[Raw Spark / Incoming Idea]
            ↓
    [Brainstorm Folder]
  (YYYY-MM-DD_Concept.md)
            ↓
[Interactive /grill-me Drill]
(Uncover assumptions, bottlenecks, feasibility, and real-world friction)
            ↓
    [The Decision Gate]
┌───────────┬─────────────┬──────────────┬──────────────────┬─────────────┐
│ If Career │ If Learning │ If Personal  │ If Hobby/Side    │ If Shelved  │
│ / Business│ / Knowledge │ / Life Ops   │ / Creative       │ / Fatal Flaw│
└─────┬─────┴──────┬──────┴──────┬───────┴────────┬─────────┴──────┬──────┘
      ↓            ↓             ↓                ↓                ↓
  `Career/`   `Learnings/`  `Personal/` `Other Activities/` `Brainstorm/_archive/`
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
> *"Build an AI OS from scratch for me"*  
> or  
> *"Upgrade my existing workspace into an AI OS"*

The agent will automatically conduct the pre-flight scan, run the discovery interview, scaffold the 5 hubs, install all Anthropic skills, and configure Google Workspace MCP.

---

### Method 2: Run the Interactive Terminal Wizard (No Agent Needed)

You can run the interactive setup wizard directly in your terminal. It asks you 5 simple questions, maps your directory, installs all Anthropic skills, and sets up your entire system in under 60 seconds:

```bash
# Clone the repository
git clone https://github.com/Maddy-SL/ai-os-architect.git

# Launch the interactive wizard
python ai-os-architect/scripts/interactive_onboard.py
```

---

### Method 3: Headless CLI Scaffolding

For automated setups or CI pipelines, run the headless CLI script:

```bash
# Run on current directory (with automatic Anthropic skills clone)
python ai-os-architect/scripts/scaffold_ai_os.py --target "."

# Run with a custom user profile JSON
python ai-os-architect/scripts/scaffold_ai_os.py --target "/path/to/workspace" --profile-json profile.json

# Offline / fast mode (skip git cloning)
python ai-os-architect/scripts/scaffold_ai_os.py --target "." --skip-clone
```

---

## 🛡️ Inviolable Operating Non-Negotiables

Every AI OS scaffolded by this engine embeds these non-negotiables into `AGENTS.md`:

1. **Radical Intellectual Honesty**:
   - Strict ban on flattery, sycophancy, and contrarian swinging.
   - Tells the user the hard truth, trade-offs, and fatal flaws plainly.
2. **Answer First with Balanced Triad**:
   - Delivers the solution, execution nuances, and fatal risks in the very first turn.
   - Clarifies only when two interpretations would produce materially different work.
3. **Grounding in Real Constraints**:
   - Factors in actual weekly corporate workload (e.g. 50-60 hr job) and deep-work bandwidth.
4. **Memory Discipline (<80 Lines)**:
   - Root `MEMORY.md` is strictly an index. Detailed project history lives in project folders; old milestones archive to `00_Resources/`.
5. **Backtracking & Self-Repair**:
   - When an agent encounters a broken link or routing miss, it must diagnose why and repair the documentation immediately.

---

## 📦 What's Included

*   `SKILL.md`: The progressive-disclosure skill prompt (<500 lines) compatible with Claude Code and Antigravity.
*   `references/`: Deep architectural guides for folder taxonomy, Anthropic skills catalog, MCP connectors, discovery interview script, and the Four-Cs scoring rubric.
*   `templates/`: Production-ready templates for `AGENTS.md`, `MEMORY.md`, `connections.md`, `TEMPLATE_BRAINSTORM.md`, and pointer files.
*   `scripts/scaffold_ai_os.py`: Cross-platform, zero-dependency Python CLI scaffolding tool.
*   `evals/evals.json`: Automated test cases for validating skill performance.

---

## 📄 License

MIT License. Free to use, modify, and distribute. Built by Madhur Lahoti.
