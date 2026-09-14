#!/usr/bin/env python3
"""
AI OS Scaffolding Engine
Cross-platform, zero-dependency tool to scaffold or upgrade an AI OS.
Supports multiple architectural archetypes based on user context:
  - hybrid: Dual-Engine 5 Core Life Hubs (Brainstorm, Career, Learnings, Other Activities, Personal)
  - numbered: Numbered Workstations (00_Outputs, 01_Personal, 02_Learning, 03_Projects, 04_Brainstorms)
  - work: Professional / Enterprise Only (Brainstorm, Projects, Engagements, Operations, Knowledge, Outputs)
  - personal: Personal Life Only (Brainstorm, Life, Finance, Health, Learnings, Hobbies, Inbox, Outputs)
Installs all Anthropic skills from https://github.com/anthropics/skills.git.
Enforces Inviolable Operating Non-Negotiables (Anti-Sycophancy, Answer-First, Verification).
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
    "workload_constraints": "40-50 hours/week professional commitments; 8-10 hours deep work available",
    "currency_standard": "Indian Rupees (INR / ₹)",
    "financial_mechanism": "Spreadsheet / DB Ingestion",
    "financial_tool": "MS Excel / Supabase",
    "cloud_db_name": "Supabase PostgreSQL",
    "cloud_db_endpoint": "ap-south-1"
}

ARCHETYPES = {
    "hybrid": {
        "name": "Dual-Engine Hybrid (5 Core Life Hubs)",
        "scope": "Dual-Engine Hybrid (Work + Life)",
        "dirs": [
            "Brainstorm", "Brainstorm/_archive",
            "Career", "Career/Projects", "Career/Engagements", "Career/Roadmap",
            "Learnings",
            "Other Activities", "Other Activities/Sports", "Other Activities/Hobbies",
            "Personal", "Personal/Finance", "Personal/Health", "Personal/Life", "Personal/Inbox",
            "Outputs", "Outputs/Audits",
            "references", "00_Resources", ".agents", ".agents/skills", ".agents/agents"
        ],
        "routing_table": """| Workstation | Path | Purpose & Focus |
| :--- | :--- | :--- |
| **Brainstorm** | `[Brainstorm](file:///{{AI_OS_ROOT}}/Brainstorm)` | Raw ideation, `/grill-me` drills, and concept routing gate. Auto-routes out. |
| **Career** | `[Career](file:///{{AI_OS_ROOT}}/Career)` | Professional builds, consulting engagements, client deliverables, resume, career milestones. |
| **Learnings** | `[Learnings](file:///{{AI_OS_ROOT}}/Learnings)` | Academic research, study notes, technical deep-dives, book syntheses, topic syllabi. |
| **Other Activities** | `[Other Activities](file:///{{AI_OS_ROOT}}/Other%20Activities)` | Sports, fitness, culinary exploration, creative pursuits, travel. |
| **Personal** | `[Personal](file:///{{AI_OS_ROOT}}/Personal)` | Daily life operations, personal finances (`Finance/`), health, habits, and dropzone triage (`Inbox/`). |
| **Outputs** | `[Outputs](file:///{{AI_OS_ROOT}}/Outputs)` | Finished deliverables (decks, reports, models) and automated 15-day health audits (`Audits/`). |
| **References** | `[references](file:///{{AI_OS_ROOT}}/references)` | Reusable API specifications, tool SOPs, and system cheat sheets. |""",
        "brainstorm_routing": """*   **Career Initiative**: Propose creating a project folder in `Career/Projects/` and register in `Career/README.md`.
*   **Study Topic**: Propose creating a learning folder in `Learnings/[Topic_Name]/` with topic `README.md`.
*   **Habit / Financial System**: Update `Personal/MEMORY.md`.
*   **Hobby / Sports Project**: Stage into `Other Activities/`.
*   **Shelved / Flawed**: Move to `Brainstorm/_archive/` with failure analysis documented.""",
        "operating_rows": """| **Active Builds** | {{ACTIVE_PROJECTS_SUMMARY}} | `Career/README.md` |
| **Learnings** | {{CURRENT_STUDY_FOCUS}} | `Learnings/README.md` |""",
        "workstations_list": """*   **[Brainstorm](file:///{{AI_OS_ROOT}}/Brainstorm)**: Active ideation & `/grill-me` drills. Master guide in `Brainstorm/README.md`.
*   **[Career](file:///{{AI_OS_ROOT}}/Career)**: Professional projects, consulting, and roadmap. Registry in `Career/README.md`.
*   **[Learnings](file:///{{AI_OS_ROOT}}/Learnings)**: Research notes and study syllabi. Master index in `Learnings/README.md`.
*   **[Other Activities](file:///{{AI_OS_ROOT}}/Other%20Activities)**: Sports, fitness, culinary exploration, and hobbies.
*   **[Personal](file:///{{AI_OS_ROOT}}/Personal)**: Daily life ops, finances (`Finance/`), and inbox triage (`Inbox/`).
*   **[Outputs](file:///{{AI_OS_ROOT}}/Outputs)**: Final deliverable decks, reports, and [Audits](file:///{{AI_OS_ROOT}}/Outputs/Audits).""",
        "readme_files": [
            ("Brainstorm/README.md", "# Brainstorming Hub\n\nAll raw ideas enter here using `TEMPLATE_BRAINSTORM.md` before auto-routing to Career, Learnings, Personal, Other Activities, or Archive.\n"),
            ("Career/README.md", "# Career Projects & Engagements Registry\n\nSingle source of truth for active career initiatives, client deliverables, and roadmap milestones.\n"),
            ("Career/MEMORY.md", "# Career Memory Log\n\nMilestones, promotion notes, client feedback, and technical achievements.\n"),
            ("Learnings/README.md", "# Learnings Curriculum & Master Syllabus\n\nOrganized topic by topic in dedicated Level-2 subject folders.\n"),
            ("Learnings/MEMORY.md", "# Learnings Memory Log\n\nKey cognitive models, book summaries, and study takeaways.\n"),
            ("Other Activities/README.md", "# Other Activities & Recreation\n\nSports, fitness, culinary exploration, and creative hobbies.\n"),
            ("Personal/README.md", "# Personal Operations\n\nFinance, Health, Life planning, and Dropzone Inbox.\n"),
            ("Personal/MEMORY.md", "# Personal Memory Log\n\nLife ops milestones, personal routines, and financial goals.\n"),
            ("Outputs/README.md", "# Deliverables & Outputs\n\nDraft -> Final -> Archive lifecycle hub for finished reports, decks, and audits.\n"),
            ("references/README.md", "# References & API Specs Hub\n\nStore reusable API endpoint docs, tool SOPs, and system cheat sheets here so agents never re-research tools.\n"),
            ("references/google-workspace-api.md", "# Google Workspace MCP API Reference\n\nConnects Calendar, Contacts, Drive, Gmail, Docs, Sheets, and Tasks via `uvx workspace-mcp`.\n")
        ]
    },
    "numbered": {
        "name": "Numbered Workstations (Level-1 Segmentation)",
        "scope": "Dual-Engine Hybrid (Numbered Workstations)",
        "dirs": [
            "00_Outputs", "00_Outputs/Audits",
            "01_Personal", "01_Personal/Finance", "01_Personal/Health", "01_Personal/Life", "01_Personal/Inbox",
            "02_Learning",
            "03_Projects",
            "04_Brainstorms", "04_Brainstorms/_archive",
            "references", "00_Resources", ".agents", ".agents/skills", ".agents/agents"
        ],
        "routing_table": """| Workstation | Path | Purpose & Focus |
| :--- | :--- | :--- |
| **Outputs** | `[00_Outputs](file:///{{AI_OS_ROOT}}/00_Outputs)` | Finished deliverables (decks, reports, models) and automated 15-day health audits (`Audits/`). |
| **Personal** | `[01_Personal](file:///{{AI_OS_ROOT}}/01_Personal)` | Daily life operations, personal finances (`Finance/`), health, habits, and dropzone triage (`Inbox/`). |
| **Learning** | `[02_Learning](file:///{{AI_OS_ROOT}}/02_Learning)` | Academic research, study notes, technical deep-dives, book syntheses, topic syllabi. |
| **Projects** | `[03_Projects](file:///{{AI_OS_ROOT}}/03_Projects)` | Professional builds, consulting engagements, client deliverables, codebases. |
| **Brainstorms**| `[04_Brainstorms](file:///{{AI_OS_ROOT}}/04_Brainstorms)` | Raw ideation, `/grill-me` drills, and concept routing gate. Auto-routes out. |
| **References** | `[references](file:///{{AI_OS_ROOT}}/references)` | Reusable API specifications, tool SOPs, and system cheat sheets. |""",
        "brainstorm_routing": """*   **Professional Project**: Route to `03_Projects/[Project_Name]/` and register in `03_Projects/PROJECT_REGISTRY.md`.
*   **Study Topic**: Route to `02_Learning/[Topic_Name]/` with topic syllabus and notes.
*   **Personal Life Habit / Finance**: Route to `01_Personal/` and update `01_Personal/MEMORY.md`.
*   **Shelved / Flawed**: Move to `04_Brainstorms/_archive/` with failure analysis documented.""",
        "operating_rows": """| **Active Builds** | {{ACTIVE_PROJECTS_SUMMARY}} | `03_Projects/PROJECT_REGISTRY.md` |
| **Learnings** | {{CURRENT_STUDY_FOCUS}} | `02_Learning/README.md` |""",
        "workstations_list": """*   **[00_Outputs](file:///{{AI_OS_ROOT}}/00_Outputs)**: Finished deliverable decks, reports, and [Audits](file:///{{AI_OS_ROOT}}/00_Outputs/Audits).
*   **[01_Personal](file:///{{AI_OS_ROOT}}/01_Personal)**: Daily life ops, finances (`Finance/`), and inbox triage (`Inbox/`).
*   **[02_Learning](file:///{{AI_OS_ROOT}}/02_Learning)**: Research notes and study syllabi. Master index in `02_Learning/README.md`.
*   **[03_Projects](file:///{{AI_OS_ROOT}}/03_Projects)**: Professional projects, consulting, and builds. Registry in `03_Projects/PROJECT_REGISTRY.md`.
*   **[04_Brainstorms](file:///{{AI_OS_ROOT}}/04_Brainstorms)**: Active ideation & `/grill-me` drills. Master guide in `04_Brainstorms/README.md`.""",
        "readme_files": [
            ("04_Brainstorms/README.md", "# Brainstorms Hub\n\nAll raw ideas enter here before auto-routing to Projects, Learning, Personal, or Archive.\n"),
            ("03_Projects/README.md", "# Projects & Engagements Registry\n\nSingle source of truth for active professional initiatives and client builds.\n"),
            ("03_Projects/MEMORY.md", "# Projects Memory Log\n\nMilestones, technical decisions, and client work.\n"),
            ("02_Learning/README.md", "# Learning Curriculum & Master Syllabus\n\nOrganized by Level-2 subject folders.\n"),
            ("02_Learning/MEMORY.md", "# Learning Memory Log\n\nKey mental models, study notes, and summaries.\n"),
            ("01_Personal/README.md", "# Personal Operations\n\nFinance, Health, Life, and Dropzone Inbox.\n"),
            ("01_Personal/MEMORY.md", "# Personal Memory Log\n\nLife ops milestones and personal routines.\n"),
            ("00_Outputs/README.md", "# Deliverables & Outputs\n\nDraft -> Final -> Archive lifecycle hub for finished deliverables and audits.\n"),
            ("references/README.md", "# References & API Specs Hub\n\nAPI endpoint documentation and system SOPs.\n"),
            ("references/google-workspace-api.md", "# Google Workspace MCP API Reference\n\nConnects Calendar, Contacts, Drive, Gmail, Docs, Sheets, and Tasks via `uvx workspace-mcp`.\n")
        ]
    },
    "work": {
        "name": "Work & Professional OS",
        "scope": "Professional & Corporate Only",
        "dirs": [
            "Brainstorm", "Brainstorm/_archive",
            "Projects",
            "Engagements",
            "Operations",
            "Knowledge",
            "Outputs", "Outputs/Audits",
            "references", "00_Resources", ".agents", ".agents/skills", ".agents/agents"
        ],
        "routing_table": """| Workstation | Path | Purpose & Focus |
| :--- | :--- | :--- |
| **Brainstorm** | `[Brainstorm](file:///{{AI_OS_ROOT}}/Brainstorm)` | Raw proposals, initiative sparks, and `/grill-me` drills. Auto-routes out. |
| **Projects** | `[Projects](file:///{{AI_OS_ROOT}}/Projects)` | Active development builds, code repositories, internal tooling. |
| **Engagements**| `[Engagements](file:///{{AI_OS_ROOT}}/Engagements)` | Client discovery notes, BRDs, RCMs, client-specific workpapers. |
| **Operations** | `[Operations](file:///{{AI_OS_ROOT}}/Operations)` | Team workflows, meeting agendas, OKRs, hiring, performance reviews. |
| **Knowledge** | `[Knowledge](file:///{{AI_OS_ROOT}}/Knowledge)` | Architectural decision records (ADRs), domain research, industry playbooks. |
| **Outputs** | `[Outputs](file:///{{AI_OS_ROOT}}/Outputs)` | Executive decks, reports, release builds, and health audits (`Audits/`). |
| **References** | `[references](file:///{{AI_OS_ROOT}}/references)` | Reusable API specifications, tool SOPs, and system cheat sheets. |""",
        "brainstorm_routing": """*   **Internal Build / Tool**: Route to `Projects/[Project_Name]/` and register in `Projects/README.md`.
*   **Client Deliverable / Engagement**: Route to `Engagements/[Client_Name]/`.
*   **Operational Process / Standard**: Route to `Operations/`.
*   **Architectural / Domain Knowledge**: Route to `Knowledge/[Domain_Name]/`.
*   **Shelved / Flawed**: Move to `Brainstorm/_archive/` with failure analysis documented.""",
        "operating_rows": """| **Active Builds** | {{ACTIVE_PROJECTS_SUMMARY}} | `Projects/README.md` |
| **Engagements** | Client deliverables & advisory | `Engagements/README.md` |
| **Knowledge** | Architectural standards & playbooks | `Knowledge/README.md` |""",
        "workstations_list": """*   **[Brainstorm](file:///{{AI_OS_ROOT}}/Brainstorm)**: Active proposals & `/grill-me` drills. Master guide in `Brainstorm/README.md`.
*   **[Projects](file:///{{AI_OS_ROOT}}/Projects)**: Active development builds and tools. Registry in `Projects/README.md`.
*   **[Engagements](file:///{{AI_OS_ROOT}}/Engagements)**: Client advisory notes, BRDs, and workpapers.
*   **[Operations](file:///{{AI_OS_ROOT}}/Operations)**: Team workflows, meeting agendas, and operational OKRs.
*   **[Knowledge](file:///{{AI_OS_ROOT}}/Knowledge)**: Architecture records and industry playbooks.
*   **[Outputs](file:///{{AI_OS_ROOT}}/Outputs)**: Executive reports, presentation decks, and audits.""",
        "readme_files": [
            ("Brainstorm/README.md", "# Brainstorming Hub\n\nAll initiative sparks, technical RFCs, and feature ideas enter here using `TEMPLATE_BRAINSTORM.md` before auto-routing.\n"),
            ("Projects/README.md", "# Projects Registry\n\nMaster catalog of active technical builds, repositories, and tools.\n"),
            ("Projects/MEMORY.md", "# Projects Memory Log\n\nTechnical architecture milestones, decisions, and system logs.\n"),
            ("Engagements/README.md", "# Client Engagements & Advisory\n\nClient discovery, BRDs, RCMs, and engagement deliverables.\n"),
            ("Operations/README.md", "# Operations & Team Cadence\n\nMeeting agendas, operational OKRs, reviews, and workflows.\n"),
            ("Knowledge/README.md", "# Knowledge & Architectural Standards\n\nADRs, regulatory guidelines, best-practice playbooks, and research.\n"),
            ("Outputs/README.md", "# Executive Outputs & Audits\n\nFinal deliverables, client decks, and automated 15-day system health audits.\n"),
            ("references/README.md", "# References & API Specs Hub\n\nProduction API specs, database schemas, and service connection docs.\n")
        ]
    },
    "personal": {
        "name": "Personal Life OS",
        "scope": "Personal Life & Self-Mastery Only",
        "dirs": [
            "Brainstorm", "Brainstorm/_archive",
            "Life",
            "Finance",
            "Health",
            "Learnings",
            "Hobbies",
            "Inbox",
            "Outputs", "Outputs/Audits",
            "references", "00_Resources", ".agents", ".agents/skills", ".agents/agents"
        ],
        "routing_table": """| Workstation | Path | Purpose & Focus |
| :--- | :--- | :--- |
| **Brainstorm** | `[Brainstorm](file:///{{AI_OS_ROOT}}/Brainstorm)` | Personal venture sparks, creative ideas, and `/grill-me` drills. Auto-routes out. |
| **Life** | `[Life](file:///{{AI_OS_ROOT}}/Life)` | Core values, vision, routine checklists, family reminders, home ops. |
| **Finance** | `[Finance](file:///{{AI_OS_ROOT}}/Finance)` | Personal budgets, net-worth trackers, tax filings, investments. |
| **Health** | `[Health](file:///{{AI_OS_ROOT}}/Health)` | Workout tracking, nutrition, biomarkers, medical records. |
| **Learnings** | `[Learnings](file:///{{AI_OS_ROOT}}/Learnings)` | Academic courses, study notes, book syntheses, skill acquisition. |
| **Hobbies** | `[Hobbies](file:///{{AI_OS_ROOT}}/Hobbies)` | Sports, creative writing, music, travel itineraries. |
| **Inbox** | `[Inbox](file:///{{AI_OS_ROOT}}/Inbox)` | Dropzone for WhatsApp voice notes, mobile dumps, and quick bookmarks. |
| **Outputs** | `[Outputs](file:///{{AI_OS_ROOT}}/Outputs)` | Creative deliverables, essays, and 15-day personal health audits (`Audits/`). |
| **References** | `[references](file:///{{AI_OS_ROOT}}/references)` | Personal SOPs, checklists, and tool cheat sheets. |""",
        "brainstorm_routing": """*   **Study Topic / Course**: Route to `Learnings/[Topic_Name]/` with topic notes.
*   **Financial / Investment Idea**: Route to `Finance/`.
*   **Health / Fitness Goal**: Route to `Health/`.
*   **Creative Project / Hobby**: Route to `Hobbies/`.
*   **Life Habit / Routine**: Route to `Life/`.
*   **Shelved / Flawed**: Move to `Brainstorm/_archive/` with failure analysis documented.""",
        "operating_rows": """| **Learnings** | {{CURRENT_STUDY_FOCUS}} | `Learnings/README.md` |
| **Finance & Health**| Personal life metrics & budgets | `Finance/` & `Health/` |""",
        "workstations_list": """*   **[Brainstorm](file:///{{AI_OS_ROOT}}/Brainstorm)**: Active ideation & `/grill-me` drills. Master guide in `Brainstorm/README.md`.
*   **[Life](file:///{{AI_OS_ROOT}}/Life)**: Core values, annual reviews, routines, and life ops.
*   **[Finance](file:///{{AI_OS_ROOT}}/Finance)**: Personal net worth, investment ledgers, and budget sheets.
*   **[Health](file:///{{AI_OS_ROOT}}/Health)**: Fitness tracking, medical history, and nutrition logs.
*   **[Learnings](file:///{{AI_OS_ROOT}}/Learnings)**: Study syllabi and book summaries.
*   **[Hobbies](file:///{{AI_OS_ROOT}}/Hobbies)**: Sports, creative pursuits, and travel planning.
*   **[Inbox](file:///{{AI_OS_ROOT}}/Inbox)**: Raw dropzone for quick mobile notes and captures.
*   **[Outputs](file:///{{AI_OS_ROOT}}/Outputs)**: Personal deliverables and 15-day audits.""",
        "readme_files": [
            ("Brainstorm/README.md", "# Brainstorming Hub\n\nAll personal sparks, creative ideas, and habits enter here using `TEMPLATE_BRAINSTORM.md` before auto-routing.\n"),
            ("Life/README.md", "# Life Operations & Vision\n\nCore values, annual reviews, routine checklists, and family ops.\n"),
            ("Life/MEMORY.md", "# Life Operations Memory Log\n\nKey milestones, family reminders, and habit progress.\n"),
            ("Finance/README.md", "# Personal Finance Hub\n\nNet worth tracking, budgets, investments, and tax records.\n"),
            ("Health/README.md", "# Health & Fitness\n\nWorkouts, nutrition, medical history, and sleep data.\n"),
            ("Learnings/README.md", "# Learning & Knowledge\n\nBook summaries, courses, and intellectual deep-dives.\n"),
            ("Hobbies/README.md", "# Hobbies & Recreation\n\nSports, culinary exploration, creative writing, and travel.\n"),
            ("Inbox/README.md", "# Dropzone Inbox\n\nStaging ground for unprocessed voice notes, receipts, and mobile bookmarks.\n"),
            ("Outputs/README.md", "# Outputs & Audits\n\nCreative writing, summaries, and 15-day life audits.\n"),
            ("references/README.md", "# References & SOPs\n\nPersonal SOPs, tool instructions, and cheat sheets.\n")
        ]
    }
}

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

    # 2. Write core config files
    brainstorm_folder = "04_Brainstorms" if mode == "numbered" else "Brainstorm"
    files_to_render = [
        ("AGENTS.template.md", "AGENTS.md"),
        ("MEMORY.template.md", "MEMORY.md"),
        ("connections.template.md", "connections.md"),
        ("TEMPLATE_BRAINSTORM.template.md", f"{brainstorm_folder}/TEMPLATE_BRAINSTORM.md"),
        ("POINTER.template.md", "CLAUDE.md"),
        ("POINTER.template.md", "GEMINI.md"),
        ("POINTER.template.md", ".agents/AGENTS.md")
    ]
    
    print("[*] Populating core playbook, memory, and routing templates...")
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

    # 3. Create starter READMEs and MEMORY files for archetype workstations
    for rel_path, default_content in archetype["readme_files"]:
        p = target / rel_path
        if not p.exists() or overwrite:
            p.parent.mkdir(parents=True, exist_ok=True)
            p.write_text(default_content, encoding="utf-8")
            print(f"    [CREATED] {rel_path}")

    # 4. Generate .mcp.json with Google Workspace MCP configured
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

    # 5. Clone ALL Anthropic skills from github.com/anthropics/skills.git
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
    print(" AI OS Scaffolding Complete!")
    print(f" Selected Archetype: {archetype['name']}")
    print(f" Canonical Playbook: {target}/AGENTS.md")
    print(f" Root Memory Index: {target}/MEMORY.md")
    print(" Inviolable Rules Embedded: Anti-Sycophancy, Answer-First, Real Constraints")
    print("========================================================")

def main():
    parser = argparse.ArgumentParser(description="Scaffold or upgrade an AI OS workspace across Work, Personal, or Hybrid contexts.")
    parser.add_argument("--target", default=".", help="Target directory to scaffold")
    parser.add_argument("--mode", choices=["hybrid", "numbered", "work", "personal"], default="hybrid",
                        help="Architectural archetype: hybrid (5 hubs), numbered (00-04), work (enterprise), or personal (life)")
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
