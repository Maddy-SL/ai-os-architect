# AI OS Master Connections Registry (`connections.md`)

**Last Consolidated**: {{TODAY_DATE}}  
**System**: Personal AI OS (Autonomous & Compounding)  
**User**: {{USER_NAME}} | {{USER_TITLE_AND_DOMAIN}}

---

## 1. Universal Data Domain Coverage (7 Tier-1 Domains)

| # | Domain | Connected Mechanism | Tool / Service | Read / Write | Auth / Pipeline State | Reference Guide |
| :--- | :--- | :--- | :--- | :--- | :--- | :--- |
| **1** | **Revenue / Financials** | {{FINANCIAL_MECHANISM}} | {{FINANCIAL_TOOL}} | Read & Write | Active | `references/financial-api.md` |
| **2** | **Customer Interactions** | Google Workspace MCP | Google Contacts / Gmail CRM | Read & Write | Active & Authenticated | `references/google-workspace-api.md` |
| **3** | **Calendar** | Google Workspace MCP | Google Calendar | Read & Write | Active & Authenticated | `references/google-workspace-api.md` |
| **4** | **Communication** | Google Workspace MCP | Gmail | Read & Write | Active & Authenticated | `references/google-workspace-api.md` |
| **5** | **Task & Project Tracking** | Google Workspace MCP | Google Tasks | Read & Write | Active & Authenticated | `references/google-workspace-api.md` |
| **6** | **Meeting Intelligence** | Ingestion Pipeline | Audio & Voice dropzone (`Personal/Inbox/`) | Read Only | Active via `dropzone-triage` | `references/dropzone-pipeline.md` |
| **7** | **Knowledge / Files** | MCP & Local Filesystem | Local Hard Drive + Google Drive | Read & Write | Active & Synced | `references/google-workspace-api.md` |

---

## 2. Cloud Infrastructure & Databases

| Infrastructure Service | Resource / Project | Endpoint / Identifier | Management Tool | Reference Guide |
| :--- | :--- | :--- | :--- | :--- |
| **Google Workspace MCP** | Primary productivity hub | `uvx workspace-mcp` | Local MCP Server | `references/google-workspace-api.md` |
| **Cloud Database** | {{CLOUD_DB_NAME}} | {{CLOUD_DB_ENDPOINT}} | SQL / MCP | `references/db-api.md` |

---

## 3. Recurring Automation Cadence & Cron Registry

1.  **Morning Briefing & Task Alignment**: Reviews calendar, unread high-priority emails, and daily tasks.
2.  **Weekly Retrospective**: Reviews progress across `Career/` and `Learnings/`.
3.  **15-Day Workspace Health Audit**: Executes `ai-os-audit` to score Context, Connections, Capabilities, and Cadence into `Outputs/Audits/`.
4.  **Dropzone Triage Routine**: Ingests incoming voice notes and mobile messages from `Personal/Inbox/`.

---

## 4. Operational Safety Protocols

*   **Irreversible Writes Guardrail**: Outbound emails, calendar deletions, or production database mutations require explicit user preview and approval.
*   **Zero Credential Exposure**: No API secrets or passwords may ever be saved in plaintext or committed to Git. All tokens reside in `.env.local` or environment variables.
