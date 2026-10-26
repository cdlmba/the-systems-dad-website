# The Systems Dad (TSD) Website

Canonical website repository for **The Systems Dad** (`thesystemsdad.com`), the operating system and mentorship platform for high-performing fathers reclaiming margin, family presence, and operational calm.

## Repository Overview

- **Local Path**: `c:\Users\Test\OneDrive\Documents\1 Projects\123 The Systems Dad Website`
- **GitHub**: [`cdlmba/the-systems-dad-website`](https://github.com/cdlmba/the-systems-dad-website)
- **Domain**: `thesystemsdad.com`
- **Voice & Offer SSOT**: `cdlmba/control-tower`

## Directory Structure

```text
123 The Systems Dad Website/
├── .agents/                 # Cursor & Antigravity skills, rules, and voice SSOT
├── _posts/                  # Markdown source files for blog & essays
├── agile-at-home/           # Agile at Home interactive modules & resources
├── artifacts/               # Canonical one-pager artifacts (e.g. tsd-onepager.html)
├── blog/                    # Compiled blog & essay static pages
├── components/              # HTML & Markdown components (tsd & shared)
├── images/                  # Core brand imagery, hero graphics, headshots, PDFs
├── js/                      # Frontend JavaScript (audit logic, checkout, telemetry)
├── templates/               # Layout templates for TSD pages
├── *.html                   # Root static pages (index.html, method.html, etc.)
├── briefs.css               # Briefing styles
├── style.css                # Global site stylesheets
├── sitemap.xml              # Search engine index sitemap
├── robots.txt               # Crawler directives
├── package.json             # Build and dev runner scripts
└── wrangler.toml            # Cloudflare Pages deployment configuration
```

## Local Development

Run a local HTTP server to preview:

```bash
npm run dev
# or
python -m http.server 3000
```

Navigate to `http://localhost:3000`.

## Building the Site

To re-compile templates and blog posts:

```bash
npm run build
```

Or individual sub-steps:

```bash
npm run build:site     # Builds HTML pages from templates
npm run build:blog     # Rebuilds blog entries from _posts
npm run build:sitemap  # Updates sitemap.xml
```

## Deployment

Deploy via Cloudflare Pages:

```bash
npm run deploy
```
