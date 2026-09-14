# MCP Connector Catalog & Systems Integration Guide

The **Connections** layer of an AI OS transforms the agent from a passive text generator into an active operating system capable of reading and writing across real-world tools.

---

## 1. Universal 7 Tier-1 Data Domains Mapping

| # | Universal Data Domain | Primary MCP Server / Tool | Alternative Protocol / Pipeline |
| :--- | :--- | :--- | :--- |
| **1** | **Revenue / Financials** | `supabase` MCP / Local SQLite / Excel | Bank statement ingestion script / CSV parser / Ledger DB |
| **2** | **Customer Interactions** | `google_workspace` (Contacts) / HubSpot MCP | Airtable MCP / Notion CRM DB |
| **3** | **Calendar & Scheduling** | `google_workspace` (Calendar) | Microsoft 365 Outlook Graph API script |
| **4** | **Communication (Email/Chat)**| `google_workspace` (Gmail) / Slack MCP | Microsoft Teams / Telegram Bot API / WhatsApp MCP |
| **5** | **Task & Project Tracking** | `google_workspace` (Tasks) / GitHub MCP | Linear MCP / Todoist API / Notion DB |
| **6** | **Meeting Intelligence** | Audio Dropzone (`Inbox/` + Whisper) | Granola / Otter / Fireflies export pipeline |
| **7** | **Knowledge & File Storage** | Local Filesystem + `google_workspace` (Drive) | Notion MCP / Obsidian Vault Sync / OneDrive |

---

## 2. Platform Backbones

### Backbone A: Google Workspace MCP (`workspace-mcp`)
For users in the Google ecosystem, `workspace-mcp` connects **5 of the 7 universal data domains** in a single installation:
*   **Calendar**: Focus blocks, event auditing, free/busy querying.
*   **Contacts**: Contact enrichment, email lookups, CRM tags.
*   **Gmail**: Unread triage, reply drafting, search client threads.
*   **Tasks**: Sync daily to-do items, track completion status.
*   **Drive / Docs / Sheets**: Search documents, read financial sheets, generate agendas.

```json
{
  "mcpServers": {
    "google_workspace": {
      "command": "uvx",
      "args": ["workspace-mcp"]
    }
  }
}
```

### Backbone B: Microsoft 365 Ecosystem (Corporate / Enterprise)
For corporate environments centered on Azure / Microsoft 365:
*   **Outlook**: Email search, draft creation, calendar availability via MS Graph MCP or custom script.
*   **OneDrive / SharePoint**: File reading and document synchronization.
*   **Teams**: Channel summaries, direct message drafting.

### Backbone C: Notion / Obsidian / Knowledge Backbones
*   **Notion MCP**: Read and write to Notion databases (roadmap, content calendars, client wikis).
*   **Obsidian Local Vault**: Direct local markdown reading and bidirectional linking via local filesystem tools.

### Backbone D: Developer & Cloud Infrastructure
*   **GitHub MCP** (`@modelcontextprotocol/server-github`): Manage issues, review PR diffs, trigger CI/CD workflows.
*   **PostgreSQL / Supabase MCP**: Inspect schemas, run read-only queries, verify database migrations.
*   **Puppeteer MCP**: Automated web scraping and browser validation.

### Backbone E: Mobile Dropzones & Fast Capture
*   **WhatsApp MCP** (`baileys` / local bridge): Capture voice notes, forwarded receipts, and mobile sparks directly into `Inbox/`.
*   **Local Dropzone (`Inbox/`)**: A folder staged for drag-and-drop receipts, PDFs, and scratch audio files. Orchestrated via `dropzone-triage`.

---

## 3. Connection Safety & Hygiene Non-Negotiables

1. **Zero Credential Exposure**: Never commit API keys, OAuth secrets, or connection strings into version control. Store credentials in `.env.local` or OS environment variables.
2. **Read-AND-Write Balance with Human Confirmation**: An AI OS must be able to act (write), not just read. However, irreversible external actions (sending emails, deleting files, running database migrations, canceling calendar events) must display a preview and await explicit human confirmation.
3. **Document in `connections.md`**: Every active integration must be logged in `connections.md` at the workspace root with endpoint, auth mechanism, and last tested date.
