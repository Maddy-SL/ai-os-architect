# AI OS: Master Memory Index (`MEMORY.md`)

This file stores your profile, active operating state, workstation links, and durable decisions. It serves as my persistent brain across sessions. Keep under 80 lines.

---

## Current Operating State

**Last operational review:** {{TODAY_DATE}}
**Agent rules:** root [AGENTS.md](file:///{{AI_OS_ROOT}}/AGENTS.md) is canonical. Pointers contain no standalone rules.

| Area | Current Focus | Source of Truth |
| :--- | :--- | :--- |
| **North Star** | {{NORTH_STAR_GOAL}} | This file - User Profile |
{{OPERATING_STATE_ROWS}}
| **Audits** | 15-day cadence health scoring | `Outputs/Audits/` |

---

## 👤 User Profile
*   **Name / Role**: {{USER_NAME}} | {{USER_TITLE_AND_DOMAIN}}
*   **Primary Scope**: {{PRIMARY_SCOPE}}
*   **Technical Stack & Daily Tools**: {{TECHNICAL_STACK}}
*   **12–18 Month North Star**: {{NORTH_STAR_GOAL}}
*   **Weekly Workload & Real Constraints**: {{WORKLOAD_CONSTRAINTS}}
*   **Core Operating Preferences**:
    *   Values strict intellectual honesty, directness, and anti-sycophancy (no cheerleading, no fence-sitting, no contrarian pendulum).
    *   Prefers answer-first responses presenting strengths, execution nuances, and fatal risks together in the first turn.
    *   Requires definite recommendations (Pick a Horse) with explicit boundary conditions instead of unranked pros/cons.
    *   Requires the "So What?" drilldown connecting data, specs, and compliance to cash flow, balance sheet, or audit impact.
    *   Mandatory pre-mortem analysis identifying top failure modes and Day-1 mitigations.
    *   Zero throat-clearing: ban conversational filler, prompt recaps, and AI buzzwords (*"seamless"*, *"robust"*, *"delve"*); open with substance.
    *   Requires grounding in real constraints & Pareto triage (Day-1 80/20 wins alongside enterprise target states).
    *   Prefers structured tables, bullet points, and quick summaries.

---

## 📂 Active Workstations
{{WORKSTATIONS_LIST}}

---

## 🧠 Learned Context & Decisions
*(Keep high-level milestones here. Archive detailed history to `00_Resources/` or workstation logs.)*

- **{{TODAY_DATE}}**: **Initialized AI OS Workspace**: Established {{ARCHETYPE_NAME}} architecture, configured connections, installed Anthropic skills catalog, and codified inviolable anti-sycophancy operating rules.
