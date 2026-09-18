# AI OS Cadence & Autonomous Compounding Rituals (v2.0.0)

In the **Four-Cs Architecture**, **Cadence** is the engine of compounding. Without recurring rituals, an AI OS quickly degenerates into a passive chatbot that you only talk to when you are stuck.

With automated cadences, the AI OS actively organizes your life, keeps tasks aligned, flags inactive project drift, and audits its own operational health.

---

## 1. The Core Operating Rituals

```
┌─────────────────────────────────────────────────────────────┐
│ 1. DAILY MORNING KICKOFF (5 Minutes)                        │
│    Calendar collision check, Google Tasks Top 3,            │
│    00_Inbox voice note triage                               │
├─────────────────────────────────────────────────────────────┤
│ 2. WEEKLY REVIEW RITUAL (20–30 Minutes)                     │
│    Clear 00_Inbox to Inbox Zero, audit active projects      │
│    radar (<= 5 active), set single next physical actions    │
├─────────────────────────────────────────────────────────────┤
│ 3. EVENING / SESSION RETROSPECTIVE (3 Minutes)              │
│    Milestones logged, project memory updated,               │
│    backtracking repair of broken links                      │
├─────────────────────────────────────────────────────────────┤
│ 4. 15-DAY AUTONOMOUS HEALTH AUDIT (Automated)               │
│    Four-Cs 100-point scoreboard, memory index pruning       │
│    (<200 lines), Root Zero hygiene audit                    │
└─────────────────────────────────────────────────────────────┘
```

---

## 2. Detailed Ritual Execution Guide

### A. Morning Kickoff (Daily at 08:00 Local Time)
*   **Prompt to Agent**: *"Run morning briefing"* or automated via background cron.
*   **Actions Performed**:
    1. **Calendar Sanity Check**: Connects to Google Calendar via `google_workspace` MCP. Identifies meeting density, conflicts, and deep-work blocks.
    2. **Top 3 Needle-Movers**: Pulls pending items from Google Tasks. Ranks the top 3 highest-leverage tasks for the day.
    3. **Dropzone Ingestion**: Checks `00_Inbox/` for unprocessed voice memos, WhatsApp notes, or forwarded emails. Runs `dropzone-triage` to route them into Google Tasks or relevant workstations.
*   **Output Format**:
    ```markdown
    ### 🌅 Morning Kickoff — [YYYY-MM-DD]
    *   **Focus Blocks**: 09:00 - 11:30 (Deep Work), 14:00 - 16:00 (Client Review)
    *   **Top 3 Priorities Today**:
        1. [ ] Finalize Q3 ERP Transformation BRD
        2. [ ] 25-min Systems Thinking Reading Ritual
        3. [ ] Review Cloud Supabase Migration
    *   **00_Inbox Notes Processed**: 2 items routed to 03_Projects/
    ```

---

### B. Weekly Review Ritual (Sundays or Mondays, 20–30 Mins)
*   **Template**: `_System/Templates/Template - Weekly Review Ritual.md`
*   **Phase 1: Emergency Triage**:
    - Triage email and digital desktop.
    - Process every note in `00_Inbox/` into PARA destinations or archive; achieve **Inbox Zero**.
*   **Phase 2: Preventative Maintenance**:
    - Calendar lookahead for next 14 days.
    - Project radar audit: Ensure active projects count is strictly <= 5. Archive stalled or completed projects to `99_Archive/`.
*   **Phase 3: Planning for Action**:
    - Select top 3 project priorities for the upcoming week.
    - Ensure every active project has a verified **Single Next Physical Action (<= 15 mins)** with a concrete physical verb.
    - Update living state in root `MEMORY.md`.

---

### C. Session / Evening Wrap-Up (End of Deep Work)
*   **Prompt to Agent**: *"Wrap up session"* or *"Record session milestones"*.
*   **Actions Performed**:
    1. **Memory Radar Sync**: Appends high-level milestones to root `MEMORY.md`. Ensures root file stays strictly under 200 lines.
    2. **Workstation Memory Update**: Records technical architecture decisions into project logs.
    3. **Backtracking Repair Check**: If any file search missed or took redundant turns during the session, the agent inspects the relevant folder's `README.md` and updates the index immediately.

---

### D. 15-Day Autonomous Four-Cs Health Audit
*   **Execution**: Scheduled autonomously every 15 days (e.g. 1st and 16th of each month).
*   **Scoring Engine**: Evaluates the workspace out of 100 points:
    *   **Context (25 pts)**: Canonical `AGENTS.md` substantive, living `MEMORY.md` <200 lines, `_System/Context/` populated, Pristine Root Zero maintained.
    *   **Connections (25 pts)**: 7 Universal Data Domains reached, `_System/connections.md` updated, read-and-write balance.
    *   **Capabilities (25 pts)**: All Anthropic skills installed, domain skills built, visual craft rules present in `.agents/rules/`.
    *   **Cadence (25 pts)**: Scheduled cron triggers active, recent activity within 30 days, compounding templates intact.
*   **Deliverable**: Automatically writes audit report to `00_Outputs/Audits/YYYY-MM-DD_OS_Audit.md` with top 3 leverage gaps.
