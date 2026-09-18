# 🧠 AI OS Architect (v2.0.0)

[![License: MIT](https://img.shields.io/badge/License-MIT-blue.svg)](LICENSE)
[![Version: v2.0.0](https://img.shields.io/badge/Release-v2.0.0-emerald.svg)](https://github.com/Maddy-SL/ai-os-architect/releases/tag/v2.0.0)
[![Architecture: Root--Zero & Layered--Memory](https://img.shields.io/badge/Architecture-Root--Zero%20%26%20Layered--Memory-success.svg)](references/folder-structure-guide.md)
[![Skills: Anthropic Official](https://img.shields.io/badge/Skills-Anthropic%20Official-purple.svg)](https://github.com/anthropics/skills.git)
[![Visual Craft: Anti--Slop Standards](https://img.shields.io/badge/Visual%20Craft-Anti--Slop%20Standards-indigo.svg)](templates/rules/visual-craft.template.md)

> **Transform any blank directory or messy workspace into an autonomous, compounding personal AI Operating System across Work, Personal, or Hybrid contexts.**

`ai-os-architect` is an enterprise-grade Agent Skill and CLI scaffolding engine designed for modern AI coding assistants (Antigravity, Claude Code, Cursor, Codex). It audits the user's workspace, conducts an adaptive discovery interview, **dynamically recommends a tailored folder architecture** with clear rationale, configures data connectors (Google Workspace MCP, Microsoft 365, GitHub, Supabase), installs all 16+ official **Anthropic Skills**, and scaffolds an autonomous workspace governed by the **Cognitive Sparring Partner Protocol**, **Pristine Root Zero**, and **Visual Craft Standards**.

---

## 🌟 What's New in v2.0.0

*   **Pristine Root Zero Protocol**: The workspace root contains strictly approved master files (`AGENTS.md`, `MEMORY.md`, pointer files, `.gitignore`). Eliminates untracked scratch notes and clutter at root.
*   **00_Inbox Intake Gate**: Replaces legacy brainstorm directories with `00_Inbox/`—a zero-friction dropzone for voice memos, raw thoughts, and task captures designed for daily triage to Inbox Zero.
*   **Cognitive Sparring Partner Protocol**: Hardcoded bans on flattery, cheerleading, and automatic agreement. Actively challenges over-engineering and scope creep (*"Does this directly advance one of your top 3 active priorities?"*).
*   **The Strategic Simplicity Filter**: *"Never simplify by omitting; simplify by sequencing."* Full-spectrum mapping, explicit trade-off matrices, ruthless sequencing (Phase 1 vs. Ultimate Target), and decisive recommendations.
*   **Single Next Physical Action Rule**: Every plan or substantive response concludes with a mandatory `> [!NEXT-ACTION]` callout time-boxed to **<= 15 minutes** with a concrete physical verb and binary completion criteria.
*   **Jeff Su Layered Memory Protocol**: Clean separation between constitution (`AGENTS.md`) and living state memory (`MEMORY.md`), with root memory strictly capped under **200 lines**.
*   **Visual Craft: Anti-Slop & Zero-Bloat Standards**: Banned AI lexicon (*seamless, empower, leverage, holistic, robust, comprehensive, paradigm, cutting-edge, synergize, delve, pave the way, elevate*), hairline borders (`border-slate-200/80`), max 2–4 words per flowchart node, and 16:9 widescreen slides under 50 words.
*   **Compounding Templates Hub**: Deploys 7 production-grade templates into `_System/Templates/` (Concept Evaluation, Intermediate Packet, Progressive Distillation, Project Brief, Weekly Review Ritual, Wiki Concept Page, Workstation Standard).
*   **User Context & Problem Filter**: Deploys `_System/Context/personal_profile.md` and `_System/Context/twelve_problems.md` (Feynman / Tiago Forte 12 favorite problems filter).

---

## 📂 The 3 Architectural Archetypes

### 1. Dual-Engine Hybrid OS (Work + Life — Production Standard)
Balances corporate and client projects with personal life ops, health, and finances.

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

### 2. Work & Professional OS (`--mode work`)
For corporate executives, consultants, engineers, or founders focused purely on professional output.

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

### 3. Personal Life OS (`--mode personal`)
For personal self-mastery, finances, workouts, reading, and habits without corporate noise.

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

---

## 🚦 The Universal `00_Inbox/` Routing State Machine

Every incoming idea, voice memo, or capture enters `00_Inbox/` and passes the evaluation gate:

```
[Incoming Spark / Idea / Voice Memo]
                 ↓
[00_Inbox/YYYY-MM-DD_Concept.md]
                 ↓
[The /grill-me Drill]
(Probe assumptions, weekly hours, technical feasibility, and Pre-Mortem risks)
                 ↓
[Council 3-Lens Stress Test]
1. Skeptical Buyer / Stakeholder Lens
2. Feasibility Engineer Lens
3. Opportunity Cost Analyst Lens
                 ↓
[Routing Decision Gate]
├── IF Professional Build / Client Work: → Route to 03_Projects/ or Projects/
├── IF Study Topic / Skill Acquisition:  → Route to 02_Learning/ or Learnings/
├── IF Life Habit / Financial System:    → Route to 01_Personal/ or Finance/
├── IF Evergreen Resource / Framework:   → Route to 00_Resources/ or _System/Templates/
└── IF Flawed / High Opportunity Cost:   → Archive to 00_Inbox/_archive/
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

Once installed, prompt your agent:
> *"Build an AI OS for me"*  
> or  
> *"Upgrade my existing workspace into an AI OS"*

The agent will audit your directory, conduct the discovery interview, dynamically suggest your tailored folder structure, install all Anthropic skills, configure connectors, and scaffold the system.

---

### Method 2: Run the Interactive Terminal Wizard (No Agent Needed)

Run the interactive setup wizard directly in your terminal:

```bash
# Launch the interactive wizard
python .agents/skills/ai-os-architect/scripts/interactive_onboard.py
```

It interviews you, shows the recommended foldering with rationale, and sets up your entire workspace in under 60 seconds.

---

### Method 3: Headless CLI Scaffolding

For automated setups or scripted environments:

```bash
# Dual-Engine Hybrid (Production default)
python .agents/skills/ai-os-architect/scripts/scaffold_ai_os.py --target "." --mode hybrid

# Numbered Workstations
python .agents/skills/ai-os-architect/scripts/scaffold_ai_os.py --target "." --mode numbered

# Work & Professional Only (Enterprise)
python .agents/skills/ai-os-architect/scripts/scaffold_ai_os.py --target "." --mode work

# Personal Life Only (Self-Mastery)
python .agents/skills/ai-os-architect/scripts/scaffold_ai_os.py --target "." --mode personal

# Fast offline mode (skip git cloning)
python .agents/skills/ai-os-architect/scripts/scaffold_ai_os.py --target "." --skip-clone
```

---

## 🛡️ Inviolable Operating Non-Negotiables

Every AI OS scaffolded by this engine embeds these non-negotiables into `AGENTS.md`:

1. **Cognitive Sparring Partner & Anti-Sycophancy**: Strict ban on flattery, cheerleading, and automatic agreement. Actively challenges over-engineering and distraction from active priorities.
2. **The Strategic Simplicity Filter**: Never simplify by omitting; simplify by sequencing. Full-spectrum mapping, explicit trade-off matrices, ruthless sequencing (Phase 1 vs. Ultimate Target), and decisive recommendations.
3. **Single Next Physical Action Rule**: Every plan or substantive turn concludes with a mandatory `> [!NEXT-ACTION]` callout time-boxed to <= 15 minutes with a physical verb and binary outcome.
4. **The Pre-Mortem Filter**: Explicitly diagnoses top 3 failure modes (*"Why will this break in 6 months?"*) and Day-1 mitigations before starting execution.
5. **The "So What?" Drilldown**: Connects all technical findings, architecture specs, and compliance rules directly to cash flow, balance sheet, or operational bottlenecks.
6. **Jeff Su Layered Memory Protocol (<200 Lines)**: Root `MEMORY.md` is strictly a living state radar. Detailed history lives in project folders; old milestones archive to `00_Resources/`.
7. **Pristine Root Zero Protocol**: Root contains only approved master files. Zero loose scratch notes or temporary exports at root.
8. **Visual Craft & Lexicon Banning**: Strictly bans AI corporate clichés (*seamless, empower, leverage, holistic, robust, comprehensive, paradigm, cutting-edge, synergize, delve, pave the way, elevate*), enforces hairline borders, 16:9 slides under 50 words, and tabular numbers.
9. **Universal `00_Inbox` Routing Gate**: Raw ideas cannot skip directly to production folders without passing `/grill-me` in `00_Inbox/`.
10. **Backtracking & Self-Repair**: When an agent encounters a broken link or routing miss, it must diagnose why and repair documentation immediately.

---

## 📦 What's Included

*   `SKILL.md`: The progressive-disclosure skill prompt compatible with Antigravity, Claude Code, Cursor, and Codex.
*   `references/`: Deep architectural guides for folder taxonomy, Anthropic skills catalog, MCP connectors, discovery interview script, cadence rituals, and the Four-Cs scoring rubric.
*   `templates/`: Production-ready templates:
    *   `AGENTS.template.md` (9 canonical sections)
    *   `MEMORY.template.md` (<200 lines living radar)
    *   `connections.template.md` (_System/connections.md)
    *   `POINTER.template.md` (GEMINI.md, CLAUDE.md, .agents/AGENTS.md)
    *   `_System/Templates/` (7 core compounding templates)
    *   `_System/Context/` (personal_profile.md, twelve_problems.md)
    *   `rules/` (visual-craft.template.md, ui_ux_standards.template.md)
*   `scripts/scaffold_ai_os.py`: Multi-mode cross-platform scaffolding engine.
*   `scripts/interactive_onboard.py`: Terminal interview wizard with tailored foldering recommendations.
*   `evals/evals.json`: Comprehensive test scenarios covering hybrid, work, personal, and existing workspace setups.

---

## 📄 License

MIT License. Free to use, modify, and distribute. Built by Madhur Lahoti.
