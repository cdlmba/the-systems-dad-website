---
name: Embedded CTO
description: Code architecture, technical debt management, and refactoring protocols.
---

# 🏛️ Embedded CTO Agent Skill

This skill codifies the high-authority technical oversight for Christopher Lynn Systems (CLS) and The Systems Dad (TSD). It ensures that the codebase remains modular, maintainable, and aligned with industry best practices for edge computing.

## 🏗️ Architectural Guarding

### 1. The Modularity & Parity Mandate
*   **Decoupling**: Business logic must be separated from request/response handling.
*   **Encapsulation**: Brand-specific logic (TSD vs CLS vs MR) must reside in isolated modules to prevent cross-contamination.
*   **Technical Parity**: Maintain a shared CSS core and global configuration object (`window.siteConfig`) across all brands to ensure consistent manifestation and behavior.
*   **Dry Principle**: Identify and refactor repetitive logic into utility functions.

### 2. Serverless Edge Bot Modularity & Async Design
When porting complex integrations (like Discord bots) from persistent environments (Python/cogs) to V8 Isolates (Workers):
*   **Module Porting**: Decompose monolithic cogs into modular ES modules placed in `/commands`. Dispatch incoming requests from the main entry point by loading these sub-modules dynamically based on the command name.
*   **Deferred Response Pattern**: Decouple the initial HTTP acknowledgment (`type: 5`) from command processing. Business logic handlers must accept the `env` and `ctx` arguments, using `ctx.waitUntil()` to resolve async work in the background.
*   **Native Rest Clients**: Do not import massive npm wrapper libraries (e.g. for Trello or Google Sheets). Write clean, standard HTTP requests using the browser-native `fetch` API. This drastically reduces the worker bundle size and prevents runtime dependency crashes.
*   **Shared Global Context**: Inject site-wide configs (such as `BRAND_CONTEXT` for GenAI or Google Sheet IDs) into global JS variables or environment bindings (`env`) to avoid repeating brand voice rules across handlers.

### 3. Error Governance
*   **Fail-Safe Defaults**: Every handler must have a clear `try/catch` block with appropriate user-facing responses vs internal error logging.
*   **Validation**: Input validation is mandatory for all POST/PUT routes.

---

## 🔧 Refactoring Protocols

### 1. The Monolith Decomposer
When refactoring a "God-file":
1.  **Map Dependencies**: Identify all external imports and internal variables used by the function.
2.  **Extract**: Move the function to a dedicated file in `/src/modules/` or `/src/api/`.
3.  **Inject**: Pass necessary environment variables (`env`) and context (`ctx`) into the module from the main entry point.
4.  **Test**: Verify that the functionality remains identical using local wrangler simulation.

### 2. Tech Debt Linter
Flag code for refactoring IF:
*   Nested conditionals exceed 3 levels.
*   A function body exceeds 50 lines.
*   Hardcoded configuration strings are used instead of `env` variables.
*   Regular expressions are used for complex routing (prefer structured routers).

---

## 📊 Performance & Quality Control

### 1. Quality Gates
*   **Linting**: Enforce consistent whitespace, semicolons (mandatory), and single-quotes.
*   **Documentation**: Every new function must have a JSDoc block describing parameters and return values.
## 🖋️ Prose Governance (The Orwell Protocol)

These govern prose: docs, PR text, messages. Never touch code or technical terms; swap in everyday words only where precision survives.

1. Never use a metaphor, simile or other figure of speech which you are used to seeing in print.
2. Never use a long word where a short one will do.
3. If it is possible to cut a word out, always cut it out.
4. Never use the passive where you can use the active.
5. Never use a foreign phrase, a scientific word or a jargon word if you can think of an everyday English equivalent.
6. Break any of these rules sooner than say anything outright barbarous.

Review every prose output against these rules before delivering.

### 2. Latency Thresholds
*   **Cold Starts**: Minimize dependencies to keep worker startup time below 50ms.
*   **Processing**: Complex routing should complete in <10ms to maximize concurrent capacity on the Edge.

### 3. Visibility, Navigation & Narrative Governance
*   **Navigation Hardening**: Headers across all brands must be consolidated into a high-intent, 3-4 link structure plus a primary CTA. 
    *   **Goal**: Minimize choice paralysis and drive users toward the core diagnostic or sales entry point.
    *   **Consistency**: Use the `mr-header` or `tsd-header` classes to ensure brand-appropriate visual manifestation while sharing underlying structural logic.
*   **Narrative Manifestation**: Critical conversion text (hero, price cards, sample issues) MUST NOT use scroll-reveal classes (`.reveal`). Visibility must be immediate to account for local environment friction.
*   **Direct HTML Manifestation**: High-iteration premium assets (Dad Mode Kit) are manifest directly in HTML to ensure aesthetic and structural integrity. Do NOT attempt to sync these with Markdown unless explicitly requested.
*   **Relative Pathing**: All asset links must use context-aware relative paths (e.g., `/images/`) to ensure rendering stability across local and production environments.

### 4. Product Fulfillment Standards (The Premium Asset Pipeline)
*   **Source Fidelity**: Premium tools (Dad Mode Kit & Kit Pro) are authored directly in HTML.
*   **Naming Convention (Kit Pro)**: All Pro-tier assets MUST start with the `kit-pro-` prefix (e.g., `kit-pro-weight-audit.html`) to ensure distinct tracking and edge-routing governance.
*   **Packaging: Gated HTML Experience**: Prioritize high-authority HTML manifestation over brittle PDF generation. 
    *   **Architecture**: Use the `premium-doc-wrapper` and `print-section` system for consistent 8.5x11 browser-to-PDF rendering.
    *   **Branding**: Enforce TSD Premium styling (Warm Cream `#F8F4EF`, Deep Sage Green `#1B4332`, Muted Gold `#D4A017`) and Plus Jakarta Sans typography.
    *   **Native Print Fidelity**: Every premium asset must include a floating "Print to PDF" button and a robust `@media print` CSS block to ensure perfect browser-based PDF generation.
*   **Edge Gating**: Use "Stealth Routing" (unlinked, underscored directories like `/_tsd/`) for premium assets. Users access via direct email links or the [Kit Pro Vault Hub](file:///c:/Users/Test/OneDrive/Documents/1%20Projects/104%20Christopher%20Lynn%20Systems%20Website/_tsd/kit-pro-vault.html).
*   **Interactive Diagnostics**: Pro-tier assets should transition from static checklists to interactive JS-driven diagnostics (Total Score calculation, threshold-based interpretation, and dynamic next-step rendering).
*   **Deployment Automation**: Every product must have a corresponding `publish:[product]` script in `package.json` that triggers a site rebuild and edge deployment.

### 5. Dynamic Checkout & Split-Test Architecture
*   **API Hardening**: Use the `POST /api/create-checkout-session` endpoint to generate on-the-fly Stripe sessions. This bypasses static Whop/Stripe links and allows for dynamic pricing and metadata injection.
*   **Attribution Mandate**: Every checkout call must include a `variant` parameter in the request body. This variant must be passed into Stripe's `metadata[variant]` field to ensure conversion tracking across A/B/C split tests.
*   **Email Capture**: When a visitor provides an email on a sales page (e.g., Variant C), it must be passed into Stripe's `customer_email` field to reduce checkout friction and preserve lead fidelity.
*   **Stealth Manifestation**: All checkout logic must reside in a global `handleStripeCheckout` function within `scripts.html` to allow for rapid multi-brand deployment.

### 6. Agentic Task Governance
*   **Task Ingestion**: The agent must accept assignments primarily through GitHub Issues in the main repository.
*   **Tagging Standard**: Use the label `agent-task` (singular) to flag issues for immediate AI processing.
*   **Synchronization**: The agent executes `sync_agent_tasks.py` at the start of every session to pull and manifest the active backlog into a local dashboard.

### 7. Autonomous Lead Gen Infrastructure
*   **Engine**: `tsd_lead_engine.py` (v2.4+) utilizing the Google Gemini 2.0 API for high-latency intent scoring.
*   **Persistence**: Leads are manifest in local timestamped CSVs and appended to the centralized Google Sheet via a Service Account (`DiscordBot/google_service_account.json`).
*   **Calibration**: Scoring thresholds are set to 7+ for production, with 6+ used for expansive testing.

---

## 🛣️ Advisor Mode: Framework Selection
When advising on new libraries (e.g., Hono):
*   **Constraint 1**: Does it increase the bundle size significantly?
*   **Constraint 2**: Does it simplify the mental model for future developers?
*   **Constraint 3**: Is it native to the Cloudflare Worker runtime environment?

### 8. Build vs. Source Integrity (The Manifestation Rule)
*   **The Source of Truth**: For all pages using the modular build system (`build_site.py` and `build_blog.py`), the files in `components/`, `templates/`, and `_posts/` are the absolute source of truth.
*   **Prohibition of Direct Artifact Edits**: Never edit `.html` files in generated output directories (`vault_cls`, `vault_tsd`, `vault_mr`) or the `public/` directory directly. Manual edits will be overwritten by the build script and cause server sync drift.
*   **Mandatory Rebuild**: Every modification to a source component, template, or markdown post MUST be followed by a local execution of `npm run build` (which triggers `build_site.py` and `build_blog.py`) to manifest the changes into the deployable artifacts.
*   **Sync Verification**: After rebuilding, verify that the generated artifacts match the intended source changes before committing or running `npm run deploy`.

### 9. Stealth Segmented Build System (Hybrid Aggregator)
*   **Segmented Post Compilations**: Ensure brand-specific blog feeds (`blog.html` for CLS and `vault_tsd/blog.html` for TSD) maintain a strict post-filtering regimen in `build_blog.py` to prevent B2C posts from bleeding into pure B2B indices and vice-versa.
*   **Dynamic Aggregation Architecture**: The hybrid aggregator (`vault_mr/blog.html`) compiles chronologically by merging post lists natively (`list(cls_posts.values()) + list(tsd_posts.values())`).
*   **Dynamic Accenting Logic**: Card components on the hybrid index must receive contextual inline styling parameters or tailwind borders based on post metadata (e.g., gold borders for TSD vs blue borders for CLS).
*   **Root-Relative Manifestation**: All dynamic aggregator post URLs must map to root-relative routing paths (e.g., `/blog/{slug}.html`) to integrate perfectly with the Edge Worker's routing engine.
*   **Purging Standard Overwrites**: Statically tracked placeholder template files (e.g., `templates/mr/blog.template.html`) must be purged to prevent standard site builder scripts (`build_site.py`) from overwriting dynamically compiled feeds during site compilation.

**Status: Monitoring Architecture Integrity 🏛️**
