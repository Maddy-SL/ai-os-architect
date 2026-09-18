#!/usr/bin/env python3
"""
Interactive AI OS Onboarding Wizard (v2.0.0)
Guides a user through an adaptive interview, captures their profile and scope,
dynamically suggests a tailored folder architecture with clear rationale,
installs all Anthropic skills, and scaffolds their AI OS with strict cognitive sparring,
strategic simplicity, Pristine Root Zero, and visual craft rules.
"""

import sys
import os
from pathlib import Path

# Add parent scripts directory to import scaffold
script_dir = Path(__file__).resolve().parent
if str(script_dir) not in sys.path:
    sys.path.insert(0, str(script_dir))

from scaffold_ai_os import scaffold, ARCHETYPES

def print_banner():
    print("""
===================================================================
    ____  ___   ____  _____   ___             __    _ __           __ 
   /   | /   | / __ \/ ___/  /   |  _________/ /_  (_) /____  ____/ /_
  / /| |/ /| |/ / / /\__ \  / /| | / ___/ __/ __ \/ / __/ _ \/ __/ __/
 / ___ / ___ / /_/ /___/ / / ___ |/ /  / /_/ / / / / /_/  __/ /_/ /_  
/_/  |/_/  |_\____//____/ /_/  |_/_/   \__/_/ /_/_/\__/\___/\__/\__/  
                                                                      
           Autonomous Personal AI Operating System (v2.0.0)
      Pristine Root Zero | Cognitive Sparring | Layered Memory
===================================================================
""")

def prompt_with_default(question: str, default: str) -> str:
    res = input(f"{question} [{default}]: ").strip()
    return res if res else default

def main():
    print_banner()
    print("Welcome! Let's architect your persistent, compounding AI OS.\n")

    # Step 1: User Scope & Profile
    print("--- STEP 1: SCOPE & PROFILE ---")
    print("What is the primary focus of this AI OS?")
    print("  [1] Dual-Engine Hybrid OS (00_Inbox, 00_Outputs, 01_Personal, 02_Learning, 03_Projects, _System)")
    print("  [2] Numbered Workstations (Clean Level-1 Segmentation across all facets)")
    print("  [3] Work & Professional Only (00_Inbox, Projects, Engagements, Operations, Knowledge, Outputs)")
    print("  [4] Personal Life Only (00_Inbox, Life, Finance, Health, Learnings, Hobbies, Outputs)")
    scope_choice = prompt_with_default("Select mode (1/2/3/4)", "1")

    mode_map = {
        "1": "hybrid",
        "2": "numbered",
        "3": "work",
        "4": "personal"
    }
    selected_mode = mode_map.get(scope_choice, "hybrid")
    archetype = ARCHETYPES[selected_mode]

    user_name = prompt_with_default("Your name", "Explorer")
    title_domain = prompt_with_default(
        "Your profession / primary domain",
        "Digital Transformation & Technology Practitioner"
    )
    technical_stack = prompt_with_default(
        "Primary tools & software stack",
        "Python, Excel, SQL, Web Tools, Markdown"
    )
    north_star = prompt_with_default(
        "12-18 month 'North Star' milestone",
        "Achieve elite domain mastery and high-leverage professional autonomy"
    )
    workload = prompt_with_default(
        "Real weekly schedule / constraints",
        "45-50 hrs/week corporate workload; 10 hrs/week deep work available"
    )
    currency = prompt_with_default("Financial currency standard", "Indian Rupees (INR / ₹)")

    # Step 2: Dynamic Folder Recommendation based on User Input
    print("\n--- STEP 2: TAILORED FOLDER RECOMMENDATION ---")
    print(f"Based on your profile as a '{title_domain}' with focus on '{archetype['scope']}',")
    print(f"here is our recommended folder architecture:\n")
    
    for d in archetype["dirs"]:
        if "/" not in d and not d.startswith("."):
            print(f"  📁 {d}/")
    print("  📁 references/            (API schemas and tool SOPs)")
    print("  📁 _System/               (Connections registry, compounding templates, user context)")
    print("  📁 .agents/               (Skills hub, specialist agents, visual craft rules)")

    print("\nArchitecture Rationale:")
    if selected_mode in ["hybrid", "numbered"]:
        print("  • Pristine Root Zero: Root contains only AGENTS.md, MEMORY.md, pointer files, and .gitignore.")
        print("  • 00_Inbox: Zero-friction dropzone for voice notes and task captures; auto-routes out.")
        print("  • Dedicated _System Hub: Isolates system connections, 7 compounding templates, and user context.")
        print("  • Jeff Su Layered Memory: Root MEMORY.md is a living radar strictly capped under 200 lines.")
    elif selected_mode == "work":
        print("  • Enterprise Focus: Dedicated workstations for client engagements, builds, operations, and knowledge.")
        print("  • 00_Inbox: Intake gate for client briefs and technical RFCs before project creation.")
        print("  • Pristine Root Zero: Enforces clean directory discipline for enterprise repositories.")
    elif selected_mode == "personal":
        print("  • Self-Mastery: Dedicated hubs for personal finances, workouts, reading notes, and daily life ops.")
        print("  • 00_Inbox: Mobile capture dropzone for WhatsApp voice notes, receipts, and sparks.")

    confirm_foldering = prompt_with_default("\nProceed with this folder architecture? (y/n)", "y").lower()
    if confirm_foldering not in ["y", "yes"]:
        print("You can rerun this wizard or pass custom parameters using scripts/scaffold_ai_os.py.")
        sys.exit(0)

    # Step 3: Target Path & Skills
    print("\n--- STEP 3: ENVIRONMENT & CAPABILITIES ---")
    target_dir = prompt_with_default("Target directory to scaffold", ".")
    skip_clone_input = prompt_with_default(
        "Install all 16+ official Anthropic skills from GitHub? (y/n)",
        "y"
    ).lower()
    skip_clone = skip_clone_input not in ["y", "yes"]

    profile_data = {
        "user_name": user_name,
        "title_and_domain": title_domain,
        "primary_scope": archetype["scope"],
        "technical_stack": technical_stack,
        "north_star": north_star,
        "workload_constraints": workload,
        "currency_standard": currency,
        "financial_mechanism": "Spreadsheet & Database Ingestion",
        "financial_tool": "Excel / Supabase PostgreSQL",
        "cloud_db_name": "Supabase PostgreSQL",
        "cloud_db_endpoint": "ap-south-1"
    }

    print("\n[*] Scaffolding AI OS...")
    scaffold(
        target_path=target_dir,
        mode=selected_mode,
        profile_data=profile_data,
        skip_clone=skip_clone,
        overwrite=False
    )

    print("\n[✔] Setup Complete!")
    print("Next steps:")
    print("1. Open your workspace in Antigravity, Claude Code, or Cursor.")
    print("2. Ask your agent: 'Check my AI OS health' to run the Four-Cs baseline audit.")
    print("3. Ideas start in 00_Inbox/ before routing out to active project folders.")
    print("4. Your agent is configured as an Executive Chief of Staff and Cognitive Sparring Partner.")
    print("   Expect radical anti-sycophancy, strategic simplicity, and single physical next actions.\n")

if __name__ == "__main__":
    main()
