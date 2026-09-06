#!/usr/bin/env python3
"""
Interactive AI OS Onboarding Wizard
Guides a new user through a step-by-step interview in the terminal,
captures their profile, maps their workspace, installs all Anthropic skills,
and scaffolds their 5 Core Life Hubs.
"""

import sys
import os
from pathlib import Path

# Add parent scripts directory to import scaffold
script_dir = Path(__file__).resolve().parent
if str(script_dir) not in sys.path:
    sys.path.insert(0, str(script_dir))

from scaffold_ai_os import scaffold

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
    print("Welcome! Let's configure your persistent, compounding AI OS.")
    print("This wizard will capture your profile, set up your 5 Core Life Hubs,")
    print("and install all Anthropic skills.\n")

    # Step 1: User Profile
    user_name = prompt_with_default("1. What is your full name?", "Explorer")
    title_domain = prompt_with_default(
        "2. What is your profession / primary domain?",
        "Digital Transformation & Technology Consultant"
    )
    technical_stack = prompt_with_default(
        "3. What are your primary technical tools / stack?",
        "Python, Excel, SQL, Web Tools, Markdown"
    )
    north_star = prompt_with_default(
        "4. What is your 12-18 month 'North Star' goal?",
        "Achieve elite domain mastery and high-leverage professional autonomy"
    )
    workload = prompt_with_default(
        "5. What does your real weekly corporate load look like?",
        "45-50 hrs/week corporate workload; 10 hrs/week deep work available"
    )

    # Step 2: Target Path
    target_dir = prompt_with_default("6. Target directory to scaffold?", ".")
    
    # Step 3: Options
    skip_clone_input = prompt_with_default(
        "7. Install all 16+ official Anthropic skills from GitHub? (y/n)",
        "y"
    ).lower()
    skip_clone = skip_clone_input not in ["y", "yes"]

    profile_data = {
        "user_name": user_name,
        "title_and_domain": title_domain,
        "technical_stack": technical_stack,
        "north_star": north_star,
        "workload_constraints": workload,
        "financial_mechanism": "Spreadsheet & Database Ingestion",
        "financial_tool": "Excel / Supabase PostgreSQL",
        "cloud_db_name": "Supabase PostgreSQL",
        "cloud_db_endpoint": "ap-south-1"
    }

    print("\n[*] Starting AI OS Scaffolding...\n")
    scaffold(
        target_path=target_dir,
        profile_data=profile_data,
        skip_clone=skip_clone,
        overwrite=False
    )

    print("\n[✔] Setup Complete!")
    print("Next steps:")
    print("1. Open your workspace in Claude Code, Antigravity, or Cursor.")
    print("2. Ask your agent: 'Run morning briefing' or 'Check my AI OS health'.")
    print("3. Ideas start in Brainstorm/ before routing to Career, Learnings, or Personal.")
    print("Enjoy your new autonomous external brain!\n")

if __name__ == "__main__":
    main()
