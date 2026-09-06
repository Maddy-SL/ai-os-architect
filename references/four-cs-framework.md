# The Four-Cs Architecture Framework

Popularized by AI systems architect Nate Herk and refined for production environments, the **Four-Cs Architecture** evaluates whether an AI OS is built for autonomous, long-term compounding.

---

## 1. The Four Layers

```
┌─────────────────────────────────────────────────────────────┐
│ 1. CONTEXT (Knows the Person & Business)                   │
│    Operating manual (AGENTS.md), Root Memory index,         │
│    references hub, decision logs, voice principles          │
├─────────────────────────────────────────────────────────────┤
│ 2. CONNECTIONS (Reaches the Real World)                    │
│    7 Universal Data Domains, Google Workspace MCP priority, │
│    cloud databases, read-AND-write capabilities             │
├─────────────────────────────────────────────────────────────┤
│ 3. CAPABILITIES (Knows How to Execute Work)                 │
│    Anthropic skills catalog, custom domain skills,          │
│    declarative specialist subagents (.agents/agents/)       │
├─────────────────────────────────────────────────────────────┤
│ 4. CADENCE (Runs Without Being Asked)                       │
│    Recurring cron jobs, morning briefings, weekly digests,  │
│    15-day automated health audits, decision gates           │
└─────────────────────────────────────────────────────────────┘
```

---

## 2. The 100-Point Scoring System

Each "C" is scored out of 25 points, totaling 100:

### A. Context (25 Pts)
*   **Operating Manual (5 pts)**: Canonical `AGENTS.md` exists and is substantive (>200 words, single source of truth).
*   **Identity & Constraints (5 pts)**: User profile, role, 18-month North Star, and real-world friction clearly captured.
*   **Memory Discipline (5 pts)**: Root `MEMORY.md` index exists, is maintained under 80 lines, and links to archives.
*   **Reference Hub (5 pts)**: `references/` directory populated with API specs and tool SOPs.
*   **Decision Records (5 pts)**: Dated decision log tracking major architectural and operational pivots.

### B. Connections (25 Pts)
*   **Universal Domain Reach (10 pts)**: Coverage of the 7 Tier-1 domains (1.4 pts per domain reachable, capped at 10). Recommending `google_workspace` immediately covers 5 domains (7 pts).
*   **Reference Guides for Tools (5 pts)**: Every connected tool has an accompanying guide in `references/`.
*   **Connection Freshness (5 pts)**: All credentials/tokens active, tested within 30 days.
*   **Documentation in `connections.md` (3 pts)**: Single registry listing tools, auth state, and data domains.
*   **Read-AND-Write Balance (2 pts)**: The OS can take real-world action (send drafts, modify tasks, update records), not just read.

### C. Capabilities (25 Pts)
*   **Installed Skills (10 pts)**: Multiple modular skills installed (e.g. Anthropic skills suite).
*   **Custom / Domain-Specific Skills (10 pts)**: At least one custom skill built for the user's specific domain (e.g. `ai-os-audit`, `dropzone-triage`).
*   **Specialist Subagents (5 pts)**: Declarative expert agent personas defined in `.agents/agents/*.md`.

### D. Cadence (25 Pts)
*   **Automated Scheduled Triggers (10 pts)**: At least one recurring cron or background job (daily briefing, 15-day audit).
*   **Activity / Usage Signal (10 pts)**: Files modified within 30 days, recent decision entries.
*   **Standardized Templates (5 pts)**: Reusable templates (`TEMPLATE_BRAINSTORM.md`, document templates).

---

## 3. Maturity Stages

| Total Score | Maturity Stage | System Characteristics |
| :--- | :--- | :--- |
| **0 – 39** | **Stage 0: Foundation** | Disorganized files, no canonical playbook, passive chat assistant. |
| **40 – 69** | **Stage 1: Built** | Structured folders, basic memory, initial skills installed. |
| **70 – 89** | **Stage 2: Compounding** | Deep context, Google Workspace connected, skills running, memory pruned. |
| **90 – 100** | **Stage 3: Autonomous** | Full 7-domain reach, automated recurring cron cadences, 15-day self-auditing. |

---

## 4. Leverage Multipliers

When identifying gaps during an audit, rank them using leverage multipliers:
*   **0 Tier-1 domains reachable**: **4x** multiplier (AI OS is blind to reality).
*   **Operating manual missing or bloated**: **3x** multiplier (shaky foundation).
*   **0 skills installed**: **2x** multiplier (no capabilities).
*   **No recurring cadence**: **2x** multiplier (no autonomy; relies entirely on human prompts).
*   **Missing reference guides**: **1.5x** multiplier (agents repeatedly re-research APIs).
