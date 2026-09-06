# AI OS Discovery Interview & Clarification Protocol

This guide directs the agent on how to conduct an elite onboarding interview when designing or upgrading a personal AI OS.

---

## Operating Philosophy: Clarify First, Understand Deeply

The goal of the discovery interview is **not** to dump a 30-question survey. It is an interactive, adaptive conversation designed to uncover:
1. **Who the user is** (professional identity, technical stack, core strengths).
2. **Where they are heading** (their 12-18 month "North Star" goal).
3. **Their actual constraints** (work hours, corporate friction, cognitive limits).
4. **Their active tools** (what systems contain their data).
5. **What they already have set up** (existing folders, memory, or scripts).

---

## Step-by-Step Interview Sequence

### Step 0: Pre-Flight Workspace Audit (Silent Scan)
*Before asking any question*, the agent must inspect the target directory:
- Run `ls` / `Get-ChildItem` to see existing folders.
- Check if `AGENTS.md`, `CLAUDE.md`, `MEMORY.md`, or `.mcp.json` exist.
- Check if `.agents/skills` or `.agents/agents` exist.

**Adaptive Opening Script**:
> "I scanned your current workspace. I notice you already have [list detected folders/files, e.g., `01_Personal`, `03_Projects`, an active `.mcp.json`].
> We will preserve your existing work and build cleanly on top of it.
> To tailor this AI OS to your exact workflow, I have a few quick questions to align our setup."

---

### Step 1: Identity, Domain & North Star

**Questions to Ask**:
1. **Role & Domain**: "What is your primary profession or domain, and what are the main technical or business tools you use daily (e.g., Python, Excel, Figma, ERP, CAD)?"
2. **12–18 Month North Star**: "What is the single most important career, academic, or venture milestone you want to achieve over the next 12 to 18 months?"
3. **Hard Constraints & Real Workload**: "What does your real weekly schedule look like? (e.g., 50-hour consulting load, intense startup sprint, deep-work weekends). How many hours per week can you realistically dedicate to personal projects and study?"
4. **Interaction Style**: "How do you want me to interact? Our non-negotiable default is **radical intellectual honesty** (no sycophancy, no cheerleading, grounded direct feedback). Do you have any specific communication preferences (e.g., concise executive bullet points, deep analytical dives, visual UI widgets)?"

---

### Step 2: The 5 Core Life Hubs Confirmation

Present the clean 5-hub folder structure:
- **`Brainstorm`**: Raw ideation and `/grill-me` drills (auto-routes out to Career, Learnings, Personal, or Other Activities).
- **`Career`**: Professional builds, consulting, career roadmap, resume, client deliverables.
- **`Learnings`**: Research notes, courses, technical deep dives, book summaries.
- **`Other Activities`**: Sports (e.g. cricket, gym), hobbies, creative writing, travel.
- **`Personal`**: Daily life, personal finances, health, family, routines, inbox dropzone.

*Adaptive clarification*: If the user already has existing folders (like `03_Projects` or `docs`), explain how they map to these 5 hubs and ask if they prefer to keep existing names or adopt the standardized hub taxonomy.

---

### Step 3: Connections & Google Workspace MCP

**Questions to Ask**:
1. "Do you use Google Workspace (Gmail, Google Calendar, Google Drive, Google Tasks)?
   *(If yes)* We prioritize the **Google Workspace MCP** because it connects 5 of the 7 universal data domains in one shot."
2. "What other tools hold your daily work? (e.g., GitHub, Supabase/PostgreSQL, Slack, Notion, WhatsApp voice notes)?"

---

### Step 4: Skills Installation Confirmation

Explain:
> "We install **all 16+ official skills from Anthropic** (`https://github.com/anthropics/skills.git`) by default (`xlsx`, `docx`, `pptx`, `pdf`, `frontend-design`, `webapp-testing`, `internal-comms`, `skill-creator`, etc.) so you have a complete operational toolkit from day one.
> In addition, we install custom AI OS core skills:
> 1. `ai-os-audit`: 15-day autonomous health auditor.
> 2. `ai-os-architect`: This scaffolding and onboarding engine.
> 3. `dropzone-triage`: For triaging incoming voice notes and mobile messages."

---

### Step 5: Codified Non-Negotiables Agreement

Confirm the core behavioral DNA:
1. **Radical Intellectual Honesty**: AI will never flatter, cheerlead, or swing contrarian. It will state risks, trade-offs, and flaws plainly.
2. **Answer First with Balanced Triad**: In every turn, AI presents substance, strengths, nuances, and fatal risks together in the very first turn.
3. **Constraint-Aware Planning**: Plans must reflect actual work hours and bandwidth.
4. **Memory Hygiene**: Root `MEMORY.md` stays under 80 lines as a high-level index. Deep logs live in workstation folders.
5. **Brainstorm Decision Gate**: New ideas never bypass `Brainstorm/`.
