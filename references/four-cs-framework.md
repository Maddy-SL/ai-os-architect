# The Four-Cs Architecture Framework (v2.0.0)

Popularized by AI systems architect Nate Herk and refined for production environments, the **Four-Cs Architecture** evaluates whether an AI OS is built for autonomous, long-term compounding.

---

## 1. The Four Layers

```
┌─────────────────────────────────────────────────────────────┐
│ 1. CONTEXT (Knows the Person & Business)                   │
│    Operating manual (AGENTS.md), Living Memory (<200 lines),│
│    _System/Context/, Pristine Root Zero, cognitive sparring │
├─────────────────────────────────────────────────────────────┤
│ 2. CONNECTIONS (Reaches the Real World)                    │
│    7 Universal Data Domains, Google Workspace MCP priority, │
│    cloud databases, _System/connections.md, read/write      │
├─────────────────────────────────────────────────────────────┤
│ 3. CAPABILITIES (Knows How to Execute Work)                 │
│    Anthropic skills catalog, custom domain skills,          │
│    visual craft rules (.agents/rules/), specialist agents   │
├─────────────────────────────────────────────────────────────┤
│ 4. CADENCE (Runs Without Being Asked)                       │
│    Daily morning briefing, weekly review ritual,            │
│    15-day health audit, _System/Templates/ compounding      │
└─────────────────────────────────────────────────────────────┘
```

---

## 2. The 100-Point Scoring System

Each "C" is scored out of 25 points, totaling 100:

### A. Context (25 Pts)
*   **Operating Manual (5 pts)**: Canonical `AGENTS.md` exists and is substantive (>200 words, single source of truth).
*   **Pristine Root Zero Protocol (5 pts)**: Workspace root contains strictly approved files; zero unorganized scratch notes.
*   **Living Memory Discipline (5 pts)**: Root `MEMORY.md` index exists and is maintained under 200 lines as an active radar.
*   **Context & Principles Filter (5 pts)**: `_System/Context/personal_profile.md` and `twelve_problems.md` populated.
*   **Durable Decisions Log (5 pts)**: Dated decision entries logging major architectural and operational milestones.

### B. Connections (25 Pts)
*   **Universal Domain Reach (10 pts)**: Coverage of the 7 Tier-1 domains (1.4 pts per domain reachable, capped at 10). Google Workspace MCP immediately covers 5 domains (7 pts).
*   **Reference Guides for Tools (5 pts)**: Every connected tool has an accompanying guide in `references/`.
*   **Connection Freshness (5 pts)**: All credentials/tokens active, tested within 30 days.
*   **Documentation in `_System/connections.md` (3 pts)**: Single registry listing tools, auth state, and data domains.
*   **Read-AND-Write Balance (2 pts)**: The OS can take real-world action (send drafts, modify tasks, update records), not just read.

### C. Capabilities (25 Pts)
*   **Installed Skills Suite (10 pts)**: Anthropic skills catalog installed in `.agents/skills/`.
*   **Visual Craft & UI/UX Directives (5 pts)**: Rules installed in `.agents/rules/` (`visual-craft.md`, `ui_ux_standards.md`).
*   **Custom Domain Skills (5 pts)**: Specialist skills built for specific user workflows (e.g. `deploy-agent`, `ai-os-architect`).
*   **Specialist Subagents (5 pts)**: Declarative expert agent personas defined in `.agents/agents/*.md` or runtime subagents.

### D. Cadence (25 Pts)
*   **Automated Scheduled Triggers (10 pts)**: At least one recurring cron or background job (daily briefing, 15-day audit).
*   **Compounding Templates Suite (5 pts)**: Complete suite of 7 compounding templates present in `_System/Templates/`.
*   **Weekly Review Ritual (5 pts)**: Regular inbox clearance to Inbox Zero and project radar maintenance.
*   **Recent Activity / Usage Signal (5 pts)**: Files modified within 30 days, recent decision entries.

---

## 3. Maturity Stages

| Total Score | Maturity Stage | System Characteristics |
| :--- | :--- | :--- |
| **0 – 39** | **Stage 0: Foundation** | Disorganized root, no canonical playbook, passive chat assistant. |
| **40 – 69** | **Stage 1: Built** | Structured folders, basic memory, initial skills installed. |
| **70 – 89** | **Stage 2: Compounding** | Deep context, Google Workspace connected, skills running, memory pruned. |
| **90 – 100** | **Stage 3: Autonomous** | Full 7-domain reach, automated recurring cron cadences, 15-day self-auditing. |

---

## 4. Leverage Multipliers

When identifying gaps during an audit, rank them using leverage multipliers:
*   **0 Tier-1 domains reachable**: **4x** multiplier (AI OS is blind to reality).
*   **Operating manual missing or bloated**: **3x** multiplier (shaky foundation).
*   **0 skills installed**: **2x** multiplier (no capabilities).
*   **No recurring cadence or review ritual**: **2x** multiplier (no autonomy; relies entirely on human prompts).
*   **Root Zero violation / clutter**: **1.5x** multiplier (cognitive friction and context degradation).
