# MCP Connector Catalog & Google Workspace Priority Guide

The **Connections** layer of an AI OS transforms the agent from a passive text generator into an active operating system capable of reading and writing across real-world tools.

---

## 1. The Priority Backbone: Google Workspace MCP

For personal productivity, executive operations, and knowledge work, the **Google Workspace MCP** (`workspace-mcp`) provides the highest return on connection effort. A single integration connects **5 of the 7 Tier-1 Universal Data Domains**:

| Universal Data Domain | Google Workspace Capability | Agent Read / Write Action |
| :--- | :--- | :--- |
| **Calendar** | Google Calendar | Schedule focus blocks, audit meeting load, check free/busy. |
| **Customer / Contacts** | Google Contacts | Lookup email addresses, enrich contact details, CRM tags. |
| **Communication** | Gmail | Triage unread emails, draft replies, search client threads. |
| **Project & Tasks** | Google Tasks | Sync daily to-do items (`google-tasks-sync`), track milestones. |
| **Knowledge & Files** | Google Drive / Docs / Sheets | Search docs, read spreadsheets, write meeting agendas. |

### Configuration Example (`.mcp.json` or Claude Desktop Config)

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

*Safety Rule*: External emails (`send_gmail_message`) and calendar event mutations (`manage_event`) require explicit user confirmation before execution.

---

## 2. Universal 7 Tier-1 Data Domains Mapping

| # | Data Domain | Recommended MCP Server / Tool | Alternative Script / Pipeline |
| :--- | :--- | :--- | :--- |
| **1** | **Revenue / Financials** | `supabase` MCP / Local SQLite / Excel | Bank statement ingestion script / CSV parser |
| **2** | **Customer Interactions** | `google_workspace` (Contacts/Gmail) | HubSpot API / Airtable MCP |
| **3** | **Calendar** | `google_workspace` (Calendar) | Outlook Graph API script |
| **4** | **Communication** | `google_workspace` (Gmail) + `whatsapp-mcp` | Slack MCP / Telegram Bot API |
| **5** | **Task Tracking** | `google_workspace` (Google Tasks) | Linear MCP / Todoist API / Notion DB |
| **6** | **Meeting Intelligence**| Audio Dropzone (`01_Personal/Inbox/`) | Whisper API script + Granola/Otter export |
| **7** | **Knowledge & Files** | Local Filesystem + `google_workspace` (Drive) | Notion MCP / Obsidian Vault sync |

---

## 3. Specialized Role-Based MCP Recommendations

Depending on the user's domain, recommend these targeted connectors:

### For Software Engineers & DevOps
*   **GitHub MCP** (`@modelcontextprotocol/server-github`): Manage issues, review PR diffs, trigger GitHub Actions workflows.
*   **PostgreSQL / Supabase MCP**: Inspect live schemas, execute non-destructive queries, verify migrations.
*   **Puppeteer MCP**: Headless web automation and dynamic SPA scraping.

### For Consultants, CAs & Business Advisors
*   **Google Workspace MCP**: Master productivity hub.
*   **Postgres / SQLite MCP**: Financial ledger querying and comparative reporting.
*   **Slack MCP**: Corporate updates and channel summaries.

### For Solo Founders & Creators
*   **Google Workspace MCP**: Essential back-office operations.
*   **Notion MCP**: Editorial calendar and content pipelines.
*   **WhatsApp MCP** (`baileys`): Mobile dropzone for on-the-go voice notes and quick captures.

---

## 4. Connection Safety & Hygiene Rules

1. **Zero Credential Exposure**: Never commit API keys, client secrets, or OAuth tokens to Git. Store secrets in `.env.local` or environment variables.
2. **Read-AND-Write Balance**: An AI OS must be able to act (write), not just query (read). However, irreversible write actions (sending emails, modifying production DBs, deleting files) must show a preview and await confirmation.
3. **Registry Documentation**: Every active connection must be documented in [connections.md](file:///h:/AI%20OS/connections.md) with endpoint, auth mechanism, and last tested date.
