#!/usr/bin/env python3
"""
AI OS Scaffolding Engine
Cross-platform, zero-dependency tool to scaffold or upgrade an AI OS.
Standardizes on the 5 Core Life Hubs:
  - Brainstorm (with auto-routing)
  - Career
  - Learnings
  - Other Activities
  - Personal
Plus Outputs, references, and .agents runtime.
Installs all Anthropic skills from https://github.com/anthropics/skills.git.
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
    "technical_stack": "Python, Markdown, Web Tools, Spreadsheets",
    "north_star": "Achieve high-leverage autonomy and executive domain mastery in 12-18 months",
    "workload_constraints": "40-50 hours/week professional commitments; 8-10 hours deep work available",
    "financial_mechanism": "Spreadsheet / DB Ingestion",
    "financial_tool": "MS Excel / Supabase",
    "cloud_db_name": "Supabase PostgreSQL",
    "cloud_db_endpoint": "ap-south-1"
}

CORE_HUBS = [
    "Brainstorm",
    "Brainstorm/_archive",
    "Career",
    "Career/Projects",
    "Career/Engagements",
    "Career/Roadmap",
    "Learnings",
    "Other Activities",
    "Other Activities/Sports",
    "Other Activities/Hobbies",
    "Personal",
    "Personal/Finance",
    "Personal/Health",
    "Personal/Life",
    "Personal/Inbox",
    "Outputs",
    "Outputs/Audits",
    "references",
    "00_Resources",
    ".agents",
    ".agents/skills",
    ".agents/agents"
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

def scaffold(target_path: str, profile_data: dict = None, skip_clone: bool = False, overwrite: bool = False):
    target = Path(target_path).resolve()
    target.mkdir(parents=True, exist_ok=True)
    
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
        
    # 1. Create Core Life Hubs
    print("[*] Ensuring the 5 Core Life Hubs exist...")
    for hub in CORE_HUBS:
        p = target / hub
        p.mkdir(parents=True, exist_ok=True)
        
    # Normalized AI_OS_ROOT with forward slashes for markdown links
    ai_os_root = target.as_posix()
    today_str = datetime.now().strftime("%Y-%m-%d")
    
    replacements = {
        "AI_OS_ROOT": ai_os_root,
        "TODAY_DATE": today_str,
        "DATE": today_str,
        "USER_NAME": profile["user_name"],
        "USER_TITLE_AND_DOMAIN": profile["title_and_domain"],
        "TECHNICAL_STACK": profile["technical_stack"],
        "NORTH_STAR_GOAL": profile["north_star"],
        "WORKLOAD_CONSTRAINTS": profile["workload_constraints"],
        "ACTIVE_PROJECTS_SUMMARY": "Foundation initialization",
        "CURRENT_STUDY_FOCUS": "Workspace architecture & AI agent orchestration",
        "FINANCIAL_MECHANISM": profile["financial_mechanism"],
        "FINANCIAL_TOOL": profile["financial_tool"],
        "CLOUD_DB_NAME": profile["cloud_db_name"],
        "CLOUD_DB_ENDPOINT": profile["cloud_db_endpoint"],
        "CONCEPT_NAME": "Starter_Concept"
    }

    # 2. Write core config files
    files_to_render = [
        ("AGENTS.template.md", "AGENTS.md"),
        ("MEMORY.template.md", "MEMORY.md"),
        ("connections.template.md", "connections.md"),
        ("TEMPLATE_BRAINSTORM.template.md", "Brainstorm/TEMPLATE_BRAINSTORM.md"),
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

    # 3. Create starter READMEs and MEMORY files for workstations
    hub_files = [
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
    
    for rel_path, default_content in hub_files:
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
    print(" Core Life Hubs: Brainstorm, Career, Learnings, Other Activities, Personal")
    print(f" Canonical Playbook: {target}/AGENTS.md")
    print(f" Root Memory Index: {target}/MEMORY.md")
    print("========================================================")

def main():
    parser = argparse.ArgumentParser(description="Scaffold or upgrade an AI OS workspace.")
    parser.add_argument("--target", default=".", help="Target directory to scaffold")
    parser.add_argument("--profile-json", help="Path to profile JSON with custom identity fields")
    parser.add_argument("--skip-clone", action="store_true", help="Skip cloning Anthropic skills repo")
    parser.add_argument("--overwrite", action="store_true", help="Overwrite existing files")
    
    args = parser.parse_args()
    
    profile_data = None
    if args.profile_json and Path(args.profile_json).exists():
        with open(args.profile_json, "r", encoding="utf-8") as f:
            profile_data = json.load(f)
            
    scaffold(args.target, profile_data=profile_data, skip_clone=args.skip_clone, overwrite=args.overwrite)

if __name__ == "__main__":
    main()
