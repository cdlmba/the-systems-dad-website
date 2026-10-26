---
name: CIO Infrastructure Management
description: Governance and technical standards for the Christopher Lynn Systems Edge Infrastructure and Agentic Orchestration Layer.
---

# 🛡️ SystemCIO Infrastructure Skill

This skill codifies the high-authority technical standards for the "Christopher Lynn Systems" ecosystem. It ensures that all modifications adhere to a secure, serverless-first architecture on Cloudflare, augmented by a local agentic orchestration layer.

## 🏗️ Core Architecture Standards

### 1. Serverless Edge First
All functional logic (payments, membership, routing) must reside in the **Cloudflare Worker** ([index.js](file:///c:/Users/Test/OneDrive/Documents/1%20Projects/104%20Christopher%20Lynn%20Systems%20Website/src/index.js)) or a serverless function. No legacy persistent backends should be added without CEO approval.

### 2. Multi-Brand Isolation & Parity
The infrastructure handles three distinct brands. All routing and manifestation must respect the "Brand Barrier" while maintaining technical parity:
*   **Christopher Lynn Systems (CLS)**: The primary B2B professional brand. Served from the root or `/vault_cls`.
*   **The Systems Dad (TSD)**: The B2C fatherhood brand. Served from `/tsd` or `/vault_tsd`.
*   **MarginReset (MR)**: The B2C conversion brand. Served from `/mr` or `/vault_mr`.
*   **Parity Standard**: All brands must share the same CSS core and global configuration object (`window.siteConfig`) to ensure consistent behavior.

### 3. Stripe Direct Serverless
Fulfillment must be handled directly at the Edge. No legacy Flask/Python backends.
*   **Success Logic**: Use the `/api/stripe-verify` endpoint to convert `session_id` into a long-lived access token.
*   **Fulfillment Ledger**: Store purchase records in **Cloudflare KV**. 
    *   Key format: `access_<token>` -> `{email, productId, timestamp}`.
    *   Secondary index: `user_<email>` -> `token` (for recovery).

### 4. Asset Integrity & High-Authority Manifestation
All static and premium assets must be processed through the build pipeline.
*   **Minification**: CSS and JS must be minified via `build_dist.py`.
*   **PDF Generation**: High-authority whitepapers and lead magnets must be generated as branded PDFs using `build_pdf.py` (fpdf2 engine).
    *   **Standard**: Use Montserrat typography and the warm cream/sage green color palette.
    *   **Deployment**: PDFs must be mirrored to the `/images/` directory for direct web access.
*   **Premium Asset Gating**: Transition from physical gated downloads to **Stealth HTML Assets**. Premium content must reside in underscored directories (`/_tsd/`, `/_cls/`) or use non-sequential slugs to prevent enumeration, served via the Edge Routing Layer.

## 🌐 Edge Worker & Discord Bot Architecture

### 1. Request Body Stream Constraints (The Single-Read Rule)
In Cloudflare Workers, a Request's body is a readable stream. Standard cloning or reading multiple times (such as calling `request.clone().text()` followed by `request.json()`) can lock the stream and throw a `TypeError: Body already consumed` exception.
*   **Standard**: Read the request body exactly once as raw text at the entry point of the route handler:
    ```javascript
    const bodyText = await request.text();
    ```
*   Pass `bodyText` directly to all signature verification functions, and then parse it using `JSON.parse(bodyText)` to retrieve the payload.

### 2. Interactive Handshake Resolution & The Deferred Lifecycle
Discord requires a response to all slash command interactions within **3 seconds**. If a command triggers a high-latency execution (e.g. calling Gemini, scraping Reddit, or executing Trello operations), standard synchronous execution will cause Discord to return a "Transaction Failed" error.
*   **Standard**: Immediately return an HTTP Deferred Channel Message response (Type `5`):
    ```javascript
    return new Response(JSON.stringify({ type: 5 }), {
      headers: { 'Content-Type': 'application/json' }
    });
    ```
*   Use Cloudflare's `event.waitUntil(promise)` or pass `ctx.waitUntil(promise)` to allow the worker to run the high-latency AI or API task asynchronously in the background.
*   Upon task completion, push a Discord Followup request (POST `/webhooks/{application_id}/{interaction_token}`) to manifest the rich embed.

### 3. Serverless Cron Constraints
The Cloudflare Workers Free Tier enforces a maximum of **5 active Cron Triggers** per deployed worker script. 
*   **Standard**: Do not exceed 5 cron schedules. Multiple overlapping scheduled tasks (e.g. Morning Briefs, Pulse Logs, Check-ins) must be bundled under a single, unified cron schedule (e.g., `0 11 * * *`) rather than spawning separate cron rules.

### 4. Zero-Dependency Script Portability & Automated Registration
*   **Wrangler Commands**: Prepend all `wrangler` commands in `package.json` with `npx ` (e.g., `npx wrangler deploy`) to ensure execution on Windows terminals without global package installation.
*   **Shell Output Encoding**: PowerShell scripts (like `upload-secrets.ps1`) must be written in pure ASCII. Emojis and specialized ANSI symbols must be omitted to prevent parsing exceptions and statement block crashes in default Windows PowerShell environments.
*   **Global Command Registration**: Batch register all 27 global slash commands using `node register-commands.js` to ensure the Discord Application API is updated systematically without hitting rate limits.

### 5. Antigravity Direct KV Trigger Bridge
The `/ag` slash commands provide a direct, low-friction integration for developer agent commands from Discord to local AI environments.
*   **Command `/ag [instruction]`**: Writes a JSON payload to Cloudflare KV with the prefix `ag_instruction_[timestamp]`.
*   **Ingestion Logic**: The local agent (Antigravity) scans KV during execution cycles to read and ingest queued instruction keys, executing codebase operations autonomously.
*   **Plan Validation**: The `/ag-plan [instruction]` command leverages Gemini to draft interactive, multi-phase execution plans directly in Discord before launching full execution.

## 🤖 Agentic Orchestration Layer

### 1. Local-Cloud Sync
The infrastructure is augmented by a local Python-based agentic layer that performs high-latency or non-edge tasks:
*   **Lead Extraction**: `tsd_lead_engine.py` scrapes external signals (Reddit/X) and performs AI intent scoring (Gemini).
*   **Task Governance**: `sync_agent_tasks.py` pulls active assignments from GitHub Issues labeled `agent-task`.

### 2. Narrative Orchestration
*   **Source of Truth**: 
    *   **Standard Pages**: The `.copy/` directory contains the Markdown-based narrative. Use `python sync_copy.py` to bridge edits to HTML.
    *   **High-Authority Assets (Dad Mode Kit)**: Direct HTML Manifestation is the preferred standard. Edit HTML directly to preserve complex layouts, interactive logic, and print-optimization.
*   **Protocol**: For standard pages, narrative changes MUST be made in the Markdown manifest first. For Dad Mode Kit tools, HTML is the final authority.
*   **Markers**: HTML anchors (e.g., `<!-- copy-block: id -->`) are optional for HTML-first assets but mandatory for all synchronized sections. 
## 🖋️ Prose Governance (The Orwell Protocol)

These govern prose: docs, PR text, messages. Never touch code or technical terms; swap in everyday words only where precision survives.

1. Never use a metaphor, simile or other figure of speech which you are used to seeing in print.
2. Never use a long word where a short one will do.
3. If it is possible to cut a word out, always cut it out.
4. Never use the passive where you can use the active.
5. Never use a foreign phrase, a scientific word or a jargon word if you can think of an everyday English equivalent.
6. Break any of these rules sooner than say anything outright barbarous.

Review every prose output against these rules before delivering.

### 4. Global Configuration Injection
To maintain architectural parity, all build processes MUST inject site-wide 'globals' from `site-config.json` into the browser's `window.siteConfig` object via the `<head>`. This ensures interactive scripts have immediate, server-side validated access to commerce URLs and routing metadata.

### 5. Recursive Component Replacement
The build system supports up to 3 levels of recursive tag replacement (e.g., `{{{{tag}}}}`). High-authority interactive components (like `eggshell_audit`) should be managed as standalone files and injected into content components to maintain modularity and prevent logic duplication.

### 3. Persistence Layers (External)
*   **Google Sheets**: Used as a centralized lead ledger. Access is managed via a Service Account.
*   **GitHub Issues**: Used as the primary task ingestion protocol for the AI Agent.

## 🔒 Security Protocol (The CIO Guard)

### 1. Header Enforcement
Every response MUST be injected with the following security headers via the Worker:
*   **CSP (Content Security Policy)**: Only whitelisted third-parties (Stripe, Whop, Clarity, GA, Gemini) are allowed.
*   **HSTS**: Forced HTTPS with preload status.
*   **X-Frame-Options**: Set to `SAMEORIGIN` to prevent clickjacking.

### 2. Secret Management
**NEVER** commit API keys or secret tokens to the repository. 
*   **Edge Secrets**: Managed via `wrangler secret put`.
*   **Local Secrets**: Managed via a local `.env` file (ensure it is in `.gitignore`).
*   **Service Accounts**: Stored in isolated JSON files within the `DiscordBot` or `.agents` directories.

## 🚀 Deployment Operations (The Namecheap/FTP Protocol)
Before every deployment, the SystemCIO must verify:
1.  **Build Success**: `python build_site.py --brand all` completes without errors.
2.  **Asset Collection**: `python build_dist.py` successfully mirrors the brand assets into the `public/` directory for Edge multiplexing.
3.  **Deployment Engine**: The `Deploy to Namecheap` GitHub Action is the primary deployment path. Pushing to `main` triggers an FTP sync of the root directory to the server's `public_html/`.
4.  **Audit**: Run `/cio-audit` (or manual inspection) to confirm header compliance and artifact parity.

**System Status: Hardened 💎**
