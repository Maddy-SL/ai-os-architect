#!/usr/bin/env python3
"""
AI OS Scaffolding Engine (v2.0.0)
Cross-platform, zero-dependency tool to scaffold or upgrade an AI OS.
Supports multiple architectural archetypes based on user context:
  - hybrid: Dual-Engine Hybrid (00_Inbox, 00_Outputs, 01_Personal, 02_Learning, 03_Projects, _System)
  - numbered: Numbered Workstations (00_Inbox, 00_Outputs, 01_Personal, 02_Learning, 03_Projects, _System)
  - work: Professional / Enterprise Only (00_Inbox, Projects, Engagements, Operations, Knowledge, Outputs, _System)
  - personal: Personal Life Only (00_Inbox, Life, Finance, Health, Learnings, Hobbies, Outputs, _System)
Installs all Anthropic skills from https://github.com/anthropics/skills.git.
Enforces Inviolable Operating Non-Negotiables:
  - Cognitive Sparring Partner Protocol (Zero Unearned Praise, Pre-Mortem Filter, "So What?" Drilldown)
  - Strategic Simplicity Filter ("Never simplify by omitting; simplify by sequencing")
  - Single Next Physical Action Rule (<= 15 minutes, binary outcome)
  - Pristine Root Zero Protocol
  - Jeff Su Layered Memory Protocol (150-200 lines ceiling)
  - Visual Craft: Anti-Slop & Zero-Bloat Standards
"""

import os
import sys
import json
import shutil
import argparse
import subprocess
from pathlib import Path
from datetime import datetime

ANTHROPIC_SKILLS_REPO = "https://github.com/anthropics/skills.git"

DEFAULT_PROFILE = {
    "user_name": "Explorer",
    "title_and_domain": "Knowledge Worker / Practitioner",
    "primary_scope": "Dual-Engine Hybrid (Work + Life)",
    "technical_stack": "Python, Markdown, Web Tools, Spreadsheets",
    "north_star": "Achieve high-leverage autonomy and executive domain mastery in 12-18 months",
    "workload_constraints": "45-50 hours/week professional commitments; 8-10 hours deep work available",
    "currency_standard": "Indian Rupees (INR / ₹)",
    "financial_mechanism": "Spreadsheet / DB Ingestion",
    "financial_tool": "MS Excel / Supabase",
    "cloud_db_name": "Supabase PostgreSQL",
    "cloud_db_endpoint": "ap-south-1"
}

ARCHETYPES = {
    "hybrid": {
        "name": "Dual-Engine Hybrid OS (Work + Life)",
        "scope": "Dual-Engine Hybrid (Work + Life)",
        "dirs": [
            "00_Inbox", "00_Inbox/_archive",
            "00_Outputs", "00_Outputs/Audits",
            "01_Personal", "01_Personal/Finance", "01_Personal/Health", "01_Personal/Life",
            "02_Learning",
            "03_Projects",
            "00_Resources",
            "references",
            "_System", "_System/Templates", "_System/Context",
            ".agents", ".agents/skills", ".agents/agents", ".agents/rules"
        ],
        "routing_table": """| Workstation | Path | Purpose & Focus |
| :--- | :--- | :--- |
| **Inbox** | `[00_Inbox](file:///{{AI_OS_ROOT}}/00_Inbox)` | Raw ideation, voice memos, quick capture, and dropzone triage. Auto-routes out. |
| **Outputs** | `[00_Outputs](file:///{{AI_OS_ROOT}}/00_Outputs)` | Finished deliverables (decks, reports, models) and automated audits (`Audits/`). |
| **Personal** | `[01_Personal](file:///{{AI_OS_ROOT}}/01_Personal)` | Daily life operations, personal finances (`Finance/`), health, habits. |
| **Learning** | `[02_Learning](file:///{{AI_OS_ROOT}}/02_Learning)` | Academic research, study notes, technical deep-dives, book syntheses, topic syllabi. |
| **Projects** | `[03_Projects](file:///{{AI_OS_ROOT}}/03_Projects)` | Professional builds, consulting engagements, client deliverables, codebases. |
| **Resources**| `[00_Resources](file:///{{AI_OS_ROOT}}/00_Resources)` | Evergreen frameworks, reusable reference packs, and archived concepts. |
| **System** | `[_System](file:///{{AI_OS_ROOT}}/_System)` | System connections (`connections.md`), compounding templates, and user context. |
| **References** | `[references](file:///{{AI_OS_ROOT}}/references)` | Reusable API specifications, tool SOPs, and system cheat sheets. |""",
        "brainstorm_routing": """*   **Professional Project**: Route to `03_Projects/[Project_Name]/` and register in `03_Projects/PROJECT_REGISTRY.md`.
*   **Study Topic**: Route to `02_Learning/[Topic_Name]/` with topic syllabus and notes.
*   **Personal Life Habit / Finance**: Route to `01_Personal/` and update `01_Personal/MEMORY.md`.
*   **Evergreen Resource / Framework**: Route to `00_Resources/` or `_System/Templates/`.
*   **Shelved / Flawed**: Move to `00_Inbox/_archive/` with failure analysis documented.""",
        "operating_rows": """| **Active Builds** | {{ACTIVE_PROJECTS_SUMMARY}} | `03_Projects/PROJECT_REGISTRY.md` |
| **Learnings** | {{CURRENT_STUDY_FOCUS}} | `02_Learning/README.md` |""",
        "workstations_list": """*   **[00_Inbox](file:///{{AI_OS_ROOT}}/00_Inbox)**: Raw ideation & dropzone capture. Master guide in `00_Inbox/README.md`.
*   **[00_Outputs](file:///{{AI_OS_ROOT}}/00_Outputs)**: Finished deliverable decks, reports, and [Audits](file:///{{AI_OS_ROOT}}/00_Outputs/Audits).
*   **[01_Personal](file:///{{AI_OS_ROOT}}/01_Personal)**: Daily life ops, finances (`Finance/`), health. Master log in `01_Personal/MEMORY.md`.
*   **[02_Learning](file:///{{AI_OS_ROOT}}/02_Learning)**: Research notes and study syllabi. Master index in `02_Learning/README.md`.
*   **[03_Projects](file:///{{AI_OS_ROOT}}/03_Projects)**: Professional projects, consulting, and builds. Registry in `03_Projects/PROJECT_REGISTRY.md`.
*   **[00_Resources](file:///{{AI_OS_ROOT}}/00_Resources)**: Evergreen references and archived packets.
*   **[_System](file:///{{AI_OS_ROOT}}/_System)**: Connections registry in `_System/connections.md` and templates in `_System/Templates/`.""",
        "readme_files": [
            ("00_Inbox/README.md", "# 00_Inbox Hub\n\nAll raw ideas, voice memos, and task dumps enter here before auto-routing to Projects, Learning, Personal, or Resources. Target Inbox Zero.\n"),
            ("03_Projects/README.md", "# Projects & Engagements Hub\n\nSingle source of truth for active professional initiatives and client builds.\n"),
            ("03_Projects/PROJECT_REGISTRY.md", "# Project Registry & Master Radar\n\n| Project | Status | Workstation | Next Physical Action | Definition of Done |\n| :--- | :--- | :--- | :--- | :--- |\n| Foundation | `ACTIVE` | `03_Projects` | Configure core tools | System onboarded |\n"),
            ("02_Learning/README.md", "# Learning Curriculum & Master Syllabus\n\nOrganized by Level-2 subject folders.\n"),
            ("02_Learning/MEMORY.md", "# Learning Memory Log\n\nKey mental models, study notes, and summaries.\n"),
            ("01_Personal/README.md", "# Personal Operations\n\nFinance, Health, and Life routines.\n"),
            ("01_Personal/MEMORY.md", "# Personal Memory Log\n\nLife ops milestones, personal routines, and financial goals.\n"),
            ("00_Outputs/README.md", "# Deliverables & Outputs\n\nDraft -> Final -> Archive lifecycle hub for finished deliverables and audits.\n"),
            ("00_Outputs/Audits/README.md", "# Autonomous Health Audits\n\n15-day automated Four-Cs audits scored out of 100 points.\n"),
            ("00_Resources/README.md", "# Evergreen Resources\n\nReusable frameworks, templates, and archived packets.\n"),
            ("references/README.md", "# References & API Specs Hub\n\nAPI endpoint documentation and system SOPs.\n"),
            ("references/google-workspace-api.md", "# Google Workspace MCP API Reference\n\nConnects Calendar, Contacts, Drive, Gmail, Docs, Sheets, and Tasks via `uvx workspace-mcp`.\n")
        ]
    },
    "numbered": {
        "name": "Numbered Workstations (Level-1 Segmentation)",
        "scope": "Dual-Engine Hybrid (Numbered Workstations)",
        "dirs": [
            "00_Inbox", "00_Inbox/_archive",
            "00_Outputs", "00_Outputs/Audits",
            "01_Personal", "01_Personal/Finance", "01_Personal/Health", "01_Personal/Life",
            "02_Learning",
            "03_Projects",
            "00_Resources",
            "references",
            "_System", "_System/Templates", "_System/Context",
            ".agents", ".agents/skills", ".agents/agents", ".agents/rules"
        ],
        "routing_table": """| Workstation | Path | Purpose & Focus |
| :--- | :--- | :--- |
| **Inbox** | `[00_Inbox](file:///{{AI_OS_ROOT}}/00_Inbox)` | Raw ideation, voice memos, quick capture, and dropzone triage. Auto-routes out. |
| **Outputs** | `[00_Outputs](file:///{{AI_OS_ROOT}}/00_Outputs)` | Finished deliverables (decks, reports, models) and automated audits (`Audits/`). |
| **Personal** | `[01_Personal](file:///{{AI_OS_ROOT}}/01_Personal)` | Daily life operations, personal finances (`Finance/`), health, habits. |
| **Learning** | `[02_Learning](file:///{{AI_OS_ROOT}}/02_Learning)` | Academic research, study notes, technical deep-dives, book syntheses, topic syllabi. |
| **Projects** | `[03_Projects](file:///{{AI_OS_ROOT}}/03_Projects)` | Professional builds, consulting engagements, client deliverables, codebases. |
| **Resources**| `[00_Resources](file:///{{AI_OS_ROOT}}/00_Resources)` | Evergreen frameworks, reusable reference packs, and archived concepts. |
| **System** | `[_System](file:///{{AI_OS_ROOT}}/_System)` | System connections (`connections.md`), compounding templates, and user context. |
| **References** | `[references](file:///{{AI_OS_ROOT}}/references)` | Reusable API specifications, tool SOPs, and system cheat sheets. |""",
        "brainstorm_routing": """*   **Professional Project**: Route to `03_Projects/[Project_Name]/` and register in `03_Projects/PROJECT_REGISTRY.md`.
*   **Study Topic**: Route to `02_Learning/[Topic_Name]/` with topic syllabus and notes.
*   **Personal Life Habit / Finance**: Route to `01_Personal/` and update `01_Personal/MEMORY.md`.
*   **Evergreen Resource / Framework**: Route to `00_Resources/` or `_System/Templates/`.
*   **Shelved / Flawed**: Move to `00_Inbox/_archive/` with failure analysis documented.""",
        "operating_rows": """| **Active Builds** | {{ACTIVE_PROJECTS_SUMMARY}} | `03_Projects/PROJECT_REGISTRY.md` |
| **Learnings** | {{CURRENT_STUDY_FOCUS}} | `02_Learning/README.md` |""",
        "workstations_list": """*   **[00_Inbox](file:///{{AI_OS_ROOT}}/00_Inbox)**: Raw ideation & dropzone capture. Master guide in `00_Inbox/README.md`.
*   **[00_Outputs](file:///{{AI_OS_ROOT}}/00_Outputs)**: Finished deliverable decks, reports, and [Audits](file:///{{AI_OS_ROOT}}/00_Outputs/Audits).
*   **[01_Personal](file:///{{AI_OS_ROOT}}/01_Personal)**: Daily life ops, finances (`Finance/`), health.
*   **[02_Learning](file:///{{AI_OS_ROOT}}/02_Learning)**: Research notes and study syllabi. Master index in `02_Learning/README.md`.
*   **[03_Projects](file:///{{AI_OS_ROOT}}/03_Projects)**: Professional projects, consulting, and builds. Registry in `03_Projects/PROJECT_REGISTRY.md`.
*   **[00_Resources](file:///{{AI_OS_ROOT}}/00_Resources)**: Evergreen references and archived packets.
*   **[_System](file:///{{AI_OS_ROOT}}/_System)**: Connections registry in `_System/connections.md` and templates in `_System/Templates/`.""",
        "readme_files": [
            ("00_Inbox/README.md", "# 00_Inbox Hub\n\nAll raw ideas, voice memos, and task dumps enter here before auto-routing to Projects, Learning, Personal, or Resources.\n"),
            ("03_Projects/README.md", "# Projects & Engagements Registry\n\nSingle source of truth for active professional initiatives and client builds.\n"),
            ("03_Projects/PROJECT_REGISTRY.md", "# Project Registry & Master Radar\n\n| Project | Status | Workstation | Next Physical Action | Definition of Done |\n| :--- | :--- | :--- | :--- | :--- |\n| Foundation | `ACTIVE` | `03_Projects` | Configure core tools | System onboarded |\n"),
            ("02_Learning/README.md", "# Learning Curriculum & Master Syllabus\n\nOrganized by Level-2 subject folders.\n"),
            ("02_Learning/MEMORY.md", "# Learning Memory Log\n\nKey mental models, study notes, and summaries.\n"),
            ("01_Personal/README.md", "# Personal Operations\n\nFinance, Health, and Life.\n"),
            ("01_Personal/MEMORY.md", "# Personal Memory Log\n\nLife ops milestones and personal routines.\n"),
            ("00_Outputs/README.md", "# Deliverables & Outputs\n\nDraft -> Final -> Archive lifecycle hub for finished deliverables and audits.\n"),
            ("00_Outputs/Audits/README.md", "# Autonomous Health Audits\n\n15-day automated Four-Cs audits scored out of 100 points.\n"),
            ("00_Resources/README.md", "# Evergreen Resources\n\nReusable frameworks, templates, and archived packets.\n"),
            ("references/README.md", "# References & API Specs Hub\n\nAPI endpoint documentation and system SOPs.\n"),
            ("references/google-workspace-api.md", "# Google Workspace MCP API Reference\n\nConnects Calendar, Contacts, Drive, Gmail, Docs, Sheets, and Tasks via `uvx workspace-mcp`.\n")
        ]
    },
    "work": {
        "name": "Work & Professional OS (Enterprise)",
        "scope": "Professional & Corporate Only",
        "dirs": [
            "00_Inbox", "00_Inbox/_archive",
            "Projects",
            "Engagements",
            "Operations",
            "Knowledge",
            "Outputs", "Outputs/Audits",
            "00_Resources",
            "references",
            "_System", "_System/Templates", "_System/Context",
            ".agents", ".agents/skills", ".agents/agents", ".agents/rules"
        ],
        "routing_table": """| Workstation | Path | Purpose & Focus |
| :--- | :--- | :--- |
| **Inbox** | `[00_Inbox](file:///{{AI_OS_ROOT}}/00_Inbox)` | Raw initiative proposals, client requests, and quick captures. Auto-routes out. |
| **Projects** | `[Projects](file:///{{AI_OS_ROOT}}/Projects)` | Active development builds, code repositories, internal tooling. |
| **Engagements**| `[Engagements](file:///{{AI_OS_ROOT}}/Engagements)` | Client discovery notes, BRDs, RCMs, client-specific workpapers. |
| **Operations** | `[Operations](file:///{{AI_OS_ROOT}}/Operations)` | Team workflows, meeting agendas, OKRs, hiring, performance reviews. |
| **Knowledge** | `[Knowledge](file:///{{AI_OS_ROOT}}/Knowledge)` | Architectural decision records (ADRs), domain research, industry playbooks. |
| **Outputs** | `[Outputs](file:///{{AI_OS_ROOT}}/Outputs)` | Executive decks, reports, release builds, and health audits (`Audits/`). |
| **System** | `[_System](file:///{{AI_OS_ROOT}}/_System)` | System connections (`connections.md`), compounding templates, and user context. |
| **References** | `[references](file:///{{AI_OS_ROOT}}/references)` | Reusable API specifications, tool SOPs, and system cheat sheets. |""",
        "brainstorm_routing": """*   **Internal Build / Tool**: Route to `Projects/[Project_Name]/` and register in `Projects/PROJECT_REGISTRY.md`.
*   **Client Deliverable / Engagement**: Route to `Engagements/[Client_Name]/`.
*   **Operational Process / Standard**: Route to `Operations/`.
*   **Architectural / Domain Knowledge**: Route to `Knowledge/[Domain_Name]/`.
*   **Evergreen Resource / Framework**: Route to `00_Resources/` or `_System/Templates/`.
*   **Shelved / Flawed**: Move to `00_Inbox/_archive/` with failure analysis documented.""",
        "operating_rows": """| **Active Builds** | {{ACTIVE_PROJECTS_SUMMARY}} | `Projects/PROJECT_REGISTRY.md` |
| **Engagements** | Client deliverables & advisory | `Engagements/README.md` |
| **Knowledge** | Architectural standards & playbooks | `Knowledge/README.md` |""",
        "workstations_list": """*   **[00_Inbox](file:///{{AI_OS_ROOT}}/00_Inbox)**: Raw intake and triage gate. Master guide in `00_Inbox/README.md`.
*   **[Projects](file:///{{AI_OS_ROOT}}/Projects)**: Active development builds and tools. Registry in `Projects/PROJECT_REGISTRY.md`.
*   **[Engagements](file:///{{AI_OS_ROOT}}/Engagements)**: Client advisory notes, BRDs, and workpapers.
*   **[Operations](file:///{{AI_OS_ROOT}}/Operations)**: Team workflows, meeting agendas, and operational OKRs.
*   **[Knowledge](file:///{{AI_OS_ROOT}}/Knowledge)**: Architecture records and industry playbooks.
*   **[Outputs](file:///{{AI_OS_ROOT}}/Outputs)**: Executive reports, presentation decks, and audits.
*   **[_System](file:///{{AI_OS_ROOT}}/_System)**: Connections registry in `_System/connections.md` and templates in `_System/Templates/`.""",
        "readme_files": [
            ("00_Inbox/README.md", "# 00_Inbox Hub\n\nAll initiative sparks, technical RFCs, and incoming client requests enter here before auto-routing.\n"),
            ("Projects/README.md", "# Projects Registry\n\nMaster catalog of active technical builds, repositories, and tools.\n"),
            ("Projects/PROJECT_REGISTRY.md", "# Project Registry & Master Radar\n\n| Project | Status | Next Physical Action | Definition of Done |\n| :--- | :--- | :--- | :--- |\n| Foundation | `ACTIVE` | Configure core tools | System onboarded |\n"),
            ("Engagements/README.md", "# Client Engagements & Advisory\n\nClient discovery, BRDs, RCMs, and engagement deliverables.\n"),
            ("Operations/README.md", "# Operations & Team Cadence\n\nMeeting agendas, operational OKRs, reviews, and workflows.\n"),
            ("Knowledge/README.md", "# Knowledge & Architectural Standards\n\nADRs, regulatory guidelines, best-practice playbooks, and research.\n"),
            ("Outputs/README.md", "# Executive Outputs & Audits\n\nFinal deliverables, client decks, and automated 15-day system health audits.\n"),
            ("00_Resources/README.md", "# Evergreen Resources\n\nReusable enterprise templates, frameworks, and architecture snippets.\n"),
            ("references/README.md", "# References & API Specs Hub\n\nProduction API specs, database schemas, and service connection docs.\n")
        ]
    },
    "personal": {
        "name": "Personal Life OS (Self-Mastery)",
        "scope": "Personal Life & Self-Mastery Only",
        "dirs": [
            "00_Inbox", "00_Inbox/_archive",
            "Life",
            "Finance",
            "Health",
            "Learnings",
            "Hobbies",
            "Outputs", "Outputs/Audits",
            "00_Resources",
            "references",
            "_System", "_System/Templates", "_System/Context",
            ".agents", ".agents/skills", ".agents/agents", ".agents/rules"
        ],
        "routing_table": """| Workstation | Path | Purpose & Focus |
| :--- | :--- | :--- |
| **Inbox** | `[00_Inbox](file:///{{AI_OS_ROOT}}/00_Inbox)` | Dropzone for WhatsApp voice notes, mobile dumps, and quick bookmarks. Auto-routes out. |
| **Life** | `[Life](file:///{{AI_OS_ROOT}}/Life)` | Core values, vision, routine checklists, family commitments, home ops. |
| **Finance** | `[Finance](file:///{{AI_OS_ROOT}}/Finance)` | Personal budgets, net-worth trackers, tax filings, investments. |
| **Health** | `[Health](file:///{{AI_OS_ROOT}}/Health)` | Workout tracking, nutrition, biomarkers, medical records. |
| **Learnings** | `[Learnings](file:///{{AI_OS_ROOT}}/Learnings)` | Academic courses, study notes, book syntheses, skill acquisition. |
| **Hobbies** | `[Hobbies](file:///{{AI_OS_ROOT}}/Hobbies)` | Sports, creative writing, music, travel itineraries. |
| **Outputs** | `[Outputs](file:///{{AI_OS_ROOT}}/Outputs)` | Creative deliverables, essays, and 15-day personal health audits (`Audits/`). |
| **System** | `[_System](file:///{{AI_OS_ROOT}}/_System)` | System connections (`connections.md`), compounding templates, and user context. |
| **References** | `[references](file:///{{AI_OS_ROOT}}/references)` | Personal SOPs, checklists, and tool cheat sheets. |""",
        "brainstorm_routing": """*   **Study Topic / Course**: Route to `Learnings/[Topic_Name]/` with topic notes.
*   **Financial / Investment Idea**: Route to `Finance/`.
*   **Health / Fitness Goal**: Route to `Health/`.
*   **Creative Project / Hobby**: Route to `Hobbies/`.
*   **Life Habit / Routine**: Route to `Life/`.
*   **Evergreen Resource / Framework**: Route to `00_Resources/` or `_System/Templates/`.
*   **Shelved / Flawed**: Move to `00_Inbox/_archive/` with failure analysis documented.""",
        "operating_rows": """| **Learnings** | {{CURRENT_STUDY_FOCUS}} | `Learnings/README.md` |
| **Finance & Health**| Personal life metrics & budgets | `Finance/` & `Health/` |""",
        "workstations_list": """*   **[00_Inbox](file:///{{AI_OS_ROOT}}/00_Inbox)**: Raw dropzone for quick mobile notes and captures. Master guide in `00_Inbox/README.md`.
*   **[Life](file:///{{AI_OS_ROOT}}/Life)**: Core values, annual reviews, routines, and life ops.
*   **[Finance](file:///{{AI_OS_ROOT}}/Finance)**: Personal net worth, investment ledgers, and budget sheets.
*   **[Health](file:///{{AI_OS_ROOT}}/Health)**: Fitness tracking, medical history, and nutrition logs.
*   **[Learnings](file:///{{AI_OS_ROOT}}/Learnings)**: Study syllabi and book summaries.
*   **[Hobbies](file:///{{AI_OS_ROOT}}/Hobbies)**: Sports, creative pursuits, and travel planning.
*   **[Outputs](file:///{{AI_OS_ROOT}}/Outputs)**: Personal deliverables and 15-day audits.
*   **[_System](file:///{{AI_OS_ROOT}}/_System)**: Connections registry in `_System/connections.md` and templates in `_System/Templates/`.""",
        "readme_files": [
            ("00_Inbox/README.md", "# 00_Inbox Hub\n\nStaging ground for unprocessed voice notes, receipts, and mobile bookmarks. Target Inbox Zero.\n"),
            ("Life/README.md", "# Life Operations & Vision\n\nCore values, annual reviews, routine checklists, and family ops.\n"),
            ("Life/MEMORY.md", "# Life Operations Memory Log\n\nKey milestones, family reminders, and habit progress.\n"),
            ("Finance/README.md", "# Personal Finance Hub\n\nNet worth tracking, budgets, investments, and tax records.\n"),
            ("Health/README.md", "# Health & Fitness\n\nWorkouts, nutrition, medical history, and sleep data.\n"),
            ("Learnings/README.md", "# Learning & Knowledge\n\nBook summaries, courses, and intellectual deep-dives.\n"),
            ("Hobbies/README.md", "# Hobbies & Recreation\n\nSports, culinary exploration, creative writing, and travel.\n"),
            ("Outputs/README.md", "# Outputs & Audits\n\nCreative writing, summaries, and 15-day life audits.\n"),
            ("00_Resources/README.md", "# Evergreen Resources\n\nPersonal life templates, travel packing lists, and workout frameworks.\n"),
            ("references/README.md", "# References & SOPs\n\nPersonal SOPs, tool instructions, and cheat sheets.\n")
        ]
    }
}

COMPOUNDING_TEMPLATES = [
    "Template - Concept Evaluation.md",
    "Template - Intermediate Packet.md",
    "Template - Progressive Distillation.md",
    "Template - Project Brief.md",
    "Template - Weekly Review Ritual.md",
    "Template - Wiki Concept Page.md",
    "Template - Workstation Standard.md"
]

RULE_TEMPLATES = [
    ("visual-craft.template.md", "visual-craft.md"),
    ("ui_ux_standards.template.md", "ui_ux_standards.md")
]

CONTEXT_TEMPLATES = [
    ("personal_profile.template.md", "personal_profile.md"),
    ("twelve_problems.template.md", "twelve_problems.md")
]

def run_command(cmd, cwd=None):
    """Run a shell command safely."""
    try:
        res = subprocess.run(cmd, cwd=cwd, check=True, stdout=subprocess.PIPE, stderr=subprocess.PIPE, text=True)
        return True, res.stdout
    except Exception as e:
        return False, str(e)

def scan_existing(target_dir: Path):
    """Detect existing folders and files in target directory."""
    existing = {
        "dirs": [],
        "files": [],
        "has_agents_md": (target_dir / "AGENTS.md").exists(),
        "has_memory_md": (target_dir / "MEMORY.md").exists(),
        "has_mcp_json": (target_dir / ".mcp.json").exists(),
        "has_skills": (target_dir / ".agents" / "skills").exists()
    }
    if target_dir.exists():
        for item in target_dir.iterdir():
            if item.is_dir() and not item.name.startswith("."):
                existing["dirs"].append(item.name)
            elif item.is_file():
                existing["files"].append(item.name)
    return existing

def render_template(template_path: Path, replacements: dict) -> str:
    """Read template file and apply placeholder replacements."""
    content = template_path.read_text(encoding="utf-8")
    for k, v in replacements.items():
        content = content.replace(f"{{{{{k}}}}}", str(v))
    return content

def scaffold(target_path: str, mode: str = "hybrid", profile_data: dict = None, skip_clone: bool = False, overwrite: bool = False):
    target = Path(target_path).resolve()
    target.mkdir(parents=True, exist_ok=True)
    
    if mode not in ARCHETYPES:
        print(f"[!] Unknown mode '{mode}', defaulting to 'hybrid'")
        mode = "hybrid"
        
    archetype = ARCHETYPES[mode]
    profile = DEFAULT_PROFILE.copy()
    if profile_data:
        profile.update(profile_data)
        
    script_dir = Path(__file__).resolve().parent
    templates_dir = script_dir.parent / "templates"
    
    print(f"[*] Auditing target workspace: {target}")
    audit = scan_existing(target)
    if audit["dirs"]:
        print(f"    Detected existing directories: {', '.join(audit['dirs'])}")
    if audit["files"]:
        print(f"    Detected existing root files: {', '.join(audit['files'])}")
        
    print(f"[*] Applying Archetype: {archetype['name']}")
    
    # 1. Create Core Directories for Selected Archetype
    print(f"[*] Scaffolding directories for {archetype['name']}...")
    for rel_dir in archetype["dirs"]:
        p = target / rel_dir
        p.mkdir(parents=True, exist_ok=True)
        
    ai_os_root = target.as_posix()
    today_str = datetime.now().strftime("%Y-%m-%d")
    
    # Format replacement map
    replacements = {
        "AI_OS_ROOT": ai_os_root,
        "TODAY_DATE": today_str,
        "DATE": today_str,
        "ARCHETYPE_NAME": archetype["name"],
        "PRIMARY_SCOPE": profile.get("primary_scope", archetype["scope"]),
        "USER_NAME": profile["user_name"],
        "USER_TITLE_AND_DOMAIN": profile["title_and_domain"],
        "TECHNICAL_STACK": profile["technical_stack"],
        "NORTH_STAR_GOAL": profile["north_star"],
        "WORKLOAD_CONSTRAINTS": profile["workload_constraints"],
        "CURRENCY_STANDARD": profile.get("currency_standard", "Indian Rupees (INR / ₹)"),
        "ACTIVE_PROJECTS_SUMMARY": "Foundation initialization",
        "CURRENT_STUDY_FOCUS": "Workspace architecture & autonomous agent workflows",
        "FINANCIAL_MECHANISM": profile["financial_mechanism"],
        "FINANCIAL_TOOL": profile["financial_tool"],
        "CLOUD_DB_NAME": profile["cloud_db_name"],
        "CLOUD_DB_ENDPOINT": profile["cloud_db_endpoint"],
        "CONCEPT_NAME": "Starter_Concept",
        "WORKSTATION_ROUTING_TABLE": archetype["routing_table"].replace("{{AI_OS_ROOT}}", ai_os_root),
        "BRAINSTORM_ROUTING_LOGIC": archetype["brainstorm_routing"],
        "OPERATING_STATE_ROWS": archetype["operating_rows"].replace("{{ACTIVE_PROJECTS_SUMMARY}}", "Foundation initialization").replace("{{CURRENT_STUDY_FOCUS}}", "Workspace architecture"),
        "WORKSTATIONS_LIST": archetype["workstations_list"].replace("{{AI_OS_ROOT}}", ai_os_root)
    }

    # 2. Write Core Canonical Files (Root Zero Protocol)
    files_to_render = [
        ("AGENTS.template.md", "AGENTS.md"),
        ("MEMORY.template.md", "MEMORY.md"),
        ("connections.template.md", "_System/connections.md"),
        ("POINTER.template.md", "GEMINI.md"),
        ("POINTER.template.md", "CLAUDE.md"),
        ("POINTER.template.md", ".agents/AGENTS.md")
    ]
    
    print("[*] Populating canonical playbook, living memory radar, and root pointers...")
    for src_name, dest_rel in files_to_render:
        dest_path = target / dest_rel
        if dest_path.exists() and not overwrite:
            print(f"    [SKIP] {dest_rel} exists (use --overwrite to replace)")
            continue
        template_file = templates_dir / src_name
        if template_file.exists():
            rendered = render_template(template_file, replacements)
            dest_path.parent.mkdir(parents=True, exist_ok=True)
            dest_path.write_text(rendered, encoding="utf-8")
            print(f"    [CREATED] {dest_rel}")
        else:
            print(f"    [WARN] Missing template: {src_name}")

    # 3. Create Compounding Templates in _System/Templates/
    print("[*] Deploying Compounding Templates into _System/Templates/...")
    tpl_source_dir = templates_dir / "_System" / "Templates"
    tpl_target_dir = target / "_System" / "Templates"
    tpl_target_dir.mkdir(parents=True, exist_ok=True)

    for tpl_name in COMPOUNDING_TEMPLATES:
        dest_tpl = tpl_target_dir / tpl_name
        if not dest_tpl.exists() or overwrite:
            src_tpl = tpl_source_dir / tpl_name
            if src_tpl.exists():
                rendered = render_template(src_tpl, replacements)
                dest_tpl.write_text(rendered, encoding="utf-8")
                print(f"    [CREATED] _System/Templates/{tpl_name}")

    # 4. Deploy User Context Templates in _System/Context/
    print("[*] Deploying User Context into _System/Context/...")
    ctx_source_dir = templates_dir / "_System" / "Context"
    ctx_target_dir = target / "_System" / "Context"
    ctx_target_dir.mkdir(parents=True, exist_ok=True)

    for src_name, dest_name in CONTEXT_TEMPLATES:
        dest_ctx = ctx_target_dir / dest_name
        if not dest_ctx.exists() or overwrite:
            src_ctx = ctx_source_dir / src_name
            if src_ctx.exists():
                rendered = render_template(src_ctx, replacements)
                dest_ctx.write_text(rendered, encoding="utf-8")
                print(f"    [CREATED] _System/Context/{dest_name}")

    # 5. Deploy Rules into .agents/rules/
    print("[*] Deploying Visual Craft & UI/UX Rules into .agents/rules/...")
    rules_source_dir = templates_dir / "rules"
    rules_target_dir = target / ".agents" / "rules"
    rules_target_dir.mkdir(parents=True, exist_ok=True)

    for src_name, dest_name in RULE_TEMPLATES:
        dest_rule = rules_target_dir / dest_name
        if not dest_rule.exists() or overwrite:
            src_rule = rules_source_dir / src_name
            if src_rule.exists():
                dest_rule.write_text(src_rule.read_text(encoding="utf-8"), encoding="utf-8")
                print(f"    [CREATED] .agents/rules/{dest_name}")

    # 6. Create starter READMEs and logs for archetype workstations
    print("[*] Populating workstation READMEs and radar logs...")
    for rel_path, default_content in archetype["readme_files"]:
        p = target / rel_path
        if not p.exists() or overwrite:
            p.parent.mkdir(parents=True, exist_ok=True)
            p.write_text(default_content, encoding="utf-8")
            print(f"    [CREATED] {rel_path}")

    # 7. Generate .gitignore if missing
    gitignore_path = target / ".gitignore"
    if not gitignore_path.exists():
        gitignore_content = """# Environments & Secrets
.env
.env.local
*.env

# Python
__pycache__/
*.py[cod]

# Temporary files
.temp*
.cache/

# Obsidian workspace cache
.obsidian/workspace*
"""
        gitignore_path.write_text(gitignore_content, encoding="utf-8")
        print("    [CREATED] .gitignore")

    # 8. Generate .mcp.json with Google Workspace MCP configured
    mcp_json_path = target / ".mcp.json"
    if not mcp_json_path.exists() or overwrite:
        mcp_config = {
            "mcpServers": {
                "google_workspace": {
                    "command": "uvx",
                    "args": ["workspace-mcp"]
                }
            }
        }
        mcp_json_path.write_text(json.dumps(mcp_config, indent=2), encoding="utf-8")
        print("    [CREATED] .mcp.json (Configured with google_workspace MCP)")

    # 9. Clone ALL Anthropic skills from github.com/anthropics/skills.git
    skills_dir = target / ".agents" / "skills"
    if not skip_clone:
        print(f"[*] Installing ALL skills from {ANTHROPIC_SKILLS_REPO}...")
        temp_clone_dir = target / ".temp_anthropic_skills"
        if temp_clone_dir.exists():
            shutil.rmtree(temp_clone_dir, ignore_errors=True)
            
        success, out = run_command(["git", "clone", "--depth", "1", ANTHROPIC_SKILLS_REPO, str(temp_clone_dir)])
        if success:
            cloned_count = 0
            for item in temp_clone_dir.iterdir():
                if item.is_dir() and not item.name.startswith("."):
                    dest_skill = skills_dir / item.name
                    if not dest_skill.exists() or overwrite:
                        if dest_skill.exists():
                            shutil.rmtree(dest_skill, ignore_errors=True)
                        shutil.copytree(item, dest_skill)
                        cloned_count += 1
            shutil.rmtree(temp_clone_dir, ignore_errors=True)
            print(f"    [SUCCESS] Installed {cloned_count} Anthropic skills into .agents/skills/")
        else:
            print(f"    [WARN] Git clone failed: {out}. Check internet or clone manually.")
    else:
        print("    [SKIP] Skill cloning skipped via --skip-clone flag.")

    print("\n========================================================")
    print(" AI OS Scaffolding Complete (v2.0.0)!")
    print(f" Selected Archetype: {archetype['name']}")
    print(f" Canonical Playbook: {target}/AGENTS.md")
    print(f" Living Radar Index: {target}/MEMORY.md (<200 lines)")
    print(f" System Directory:   {target}/_System/ (Connections, Templates, Context)")
    print(f" Rules Directory:    {target}/.agents/rules/ (Visual Craft & UI/UX)")
    print(" Root Zero Protocol: Enforced (Strictly approved files at root)")
    print(" Inviolable Rules:   Cognitive Sparring, Strategic Simplicity, Next-Action")
    print("========================================================")

def main():
    parser = argparse.ArgumentParser(description="Scaffold or upgrade an AI OS workspace across Work, Personal, or Hybrid contexts.")
    parser.add_argument("--target", default=".", help="Target directory to scaffold")
    parser.add_argument("--mode", choices=["hybrid", "numbered", "work", "personal"], default="hybrid",
                        help="Architectural archetype: hybrid (00-03 + _System), numbered, work (enterprise), or personal (life)")
    parser.add_argument("--profile-json", help="Path to profile JSON with custom identity fields")
    parser.add_argument("--skip-clone", action="store_true", help="Skip cloning Anthropic skills repo")
    parser.add_argument("--overwrite", action="store_true", help="Overwrite existing files")
    
    args = parser.parse_args()
    
    profile_data = None
    if args.profile_json and Path(args.profile_json).exists():
        with open(args.profile_json, "r", encoding="utf-8") as f:
            profile_data = json.load(f)
            
    scaffold(args.target, mode=args.mode, profile_data=profile_data, skip_clone=args.skip_clone, overwrite=args.overwrite)

if __name__ == "__main__":
    main()
