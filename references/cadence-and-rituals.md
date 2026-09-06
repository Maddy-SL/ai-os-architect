# AI OS Cadence & Autonomous Compounding Rituals

In the **Four-Cs Architecture**, **Cadence** is the engine of compounding. Without recurring rituals, an AI OS quickly degenerates into a passive chatbot that you only talk to when you are stuck.

With automated cadences, the AI OS actively organizes your life, keeps tasks aligned, flags inactive project drift, and audits its own operational health.

---

## 1. The Three Core Operating Rituals

```
┌─────────────────────────────────────────────────────────────┐
│ 1. DAILY MORNING KICKOFF (5 Minutes)                        │
│    Calendar collision check, Google Tasks Top 3,            │
│    Dropzone voice note triage                               │
├─────────────────────────────────────────────────────────────┤
│ 2. EVENING / SESSION RETROSPECTIVE (3 Minutes)              │
│    Accomplishments logged, project memory updated,          │
│    backtracking repair of broken links                      │
├─────────────────────────────────────────────────────────────┤
│ 3. 15-DAY AUTONOMOUS HEALTH AUDIT (Automated)               │
│    Four-Cs 100-point scoreboard, memory index pruning,      │
│    top-3 leverage-weighted gap resolution                   │
└─────────────────────────────────────────────────────────────┘
```

---

## 2. Detailed Ritual Execution Guide

### A. Morning Kickoff (Daily at 08:00 Local Time)
*   **Prompt to Agent**: *"Run morning briefing"* or automated via background cron.
*   **Actions Performed**:
    1. **Calendar Sanity Check**: Connects to Google Calendar via `google_workspace` MCP. Identifies meeting density, conflicts, and deep-work blocks.
    2. **Top 3 Needle-Movers**: Pulls pending items from Google Tasks (`google-tasks-sync`). Ranks the top 3 highest-leverage tasks for the day.
    3. **Dropzone Ingestion**: Checks `Personal/Inbox/` for unprocessed voice memos, WhatsApp notes, or forwarded emails. Runs `dropzone-triage` to route them into Google Tasks or relevant workstations.
*   **Output Format**:
    ```markdown
    ### 🌅 Morning Kickoff — [YYYY-MM-DD]
    *   **Focus Blocks**: 09:00 - 11:30 (Deep Work), 14:00 - 16:00 (Client Review)
    *   **Top 3 Priorities Today**:
        1. [ ] Finalize Q3 ERP Transformation BRD
        2. [ ] 25-min Systems Thinking Reading Ritual
        3. [ ] Review Cloud Supabase Migration
    *   **Dropzone Notes Processed**: 2 items routed to Career/Projects
    ```

---

### B. Session / Evening Wrap-Up (End of Deep Work)
*   **Prompt to Agent**: *"Wrap up session"* or *"Record session milestones"*.
*   **Actions Performed**:
    1. **Memory Index Sync**: Appends high-level milestones to root `MEMORY.md`. Ensures root file stays under 80 lines (prunes older history to `00_Resources/MEMORY_ARCHIVE_*.md`).
    2. **Workstation Memory Update**: Records technical architecture decisions into `Career/MEMORY.md` or `Learnings/MEMORY.md`.
    3. **Backtracking Repair Check**: If any file search missed or took redundant turns during the session, the agent inspects the relevant folder's `README.md` and updates the index.

---

### C. 15-Day Autonomous Four-Cs Health Audit
*   **Execution**: Scheduled autonomously every 15 days (e.g. 1st and 16th of each month) via Antigravity scheduler, Windows Task Scheduler, or cPanel cron.
*   **Scoring Engine**: Evaluates the workspace out of 100 points:
    *   **Context (25 pts)**: `AGENTS.md` substantive, `MEMORY.md` <80 lines, references populated.
    *   **Connections (25 pts)**: 7 Universal Data Domains reached, `connections.md` updated, read-and-write balance.
    *   **Capabilities (25 pts)**: All Anthropic skills installed, domain skills built, specialist subagents defined.
    *   **Cadence (25 pts)**: Scheduled cron triggers active, recent activity within 30 days, templates intact.
*   **Deliverable**: Automatically writes audit report to `Outputs/Audits/YYYY-MM-DD_OS_Audit.md` with top 3 leverage gaps.

---

## 3. The Compounding Flywheel

```
[Work Happens]
      ↓
[Mistake or New Need Discovered]
      ↓
[Backtracking Protocol] → Fixes index / Creates new reference in references/
      ↓
[New Capability Needed]  → Built as modular Skill via skill-creator
      ↓
[15-Day Audit]          → Verifies system integrity & scores compounding progress
```

By enforcing this loop, your AI OS gets demonstrably faster, more accurate, and more autonomous every single week.
