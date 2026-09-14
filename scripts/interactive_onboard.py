#!/usr/bin/env python3
"""
Interactive AI OS Onboarding Wizard
Guides a user through an adaptive interview, captures their profile and scope,
dynamically suggests a tailored folder architecture with clear rationale,
installs all Anthropic skills, and scaffolds their AI OS with strict anti-sycophancy and elite reasoning rules.
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
                                                                      
           Autonomous Personal AI Operating System Scaffolder
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
    print("  [1] Dual-Engine Hybrid (5 Core Life Hubs: Brainstorm, Career, Learnings, Other, Personal)")
    print("  [2] Numbered Workstations (00_Outputs, 01_Personal, 02_Learning, 03_Projects, 04_Brainstorms)")
    print("  [3] Work & Professional Only (Enterprise, Projects, Engagements, Operations, Knowledge)")
    print("  [4] Personal Life Only (Life, Finance, Health, Learnings, Hobbies, Inbox)")
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
    print("  📁 .agents/               (Skills hub and declarative subagents)")

    print("\nRationale:")
    if selected_mode == "hybrid":
        print("  • Balances professional career execution with personal life ops, health, and finances.")
        print("  • Raw sparks stage in Brainstorm/ before routing out, preventing premature project bloat.")
    elif selected_mode == "numbered":
        print("  • Enforces clean, deterministic alphabetical sorting across file managers and terminal tools.")
        print("  • Distinct numerical boundaries separate personal life (01) from technical projects (03).")
    elif selected_mode == "work":
        print("  • Eliminates personal noise: dedicated workspaces for client engagements, builds, and ops.")
        print("  • Isolates architectural decision records and firm knowledge from active sprints.")
    elif selected_mode == "personal":
        print("  • Clean separation for personal finances, workouts, reading notes, and daily routines.")
        print("  • Includes a dedicated Inbox dropzone for mobile audio dumps and quick captures.")

    confirm_foldering = prompt_with_default("\nProceed with this folder architecture? (y/n)", "y").lower()
    if confirm_foldering not in ["y", "yes"]:
        print("You can rerun this wizard or pass custom directories using scripts/scaffold_ai_os.py.")
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
    print("3. Ideas start in Brainstorm/ before routing out to active folders.")
    print("4. Your agent is hardcoded for radical honesty, zero sycophancy, and definite recommendations. Enjoy your external brain!\n")

if __name__ == "__main__":
    main()
