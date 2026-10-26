---
name: markdown-docs-generator
description: Generates professional, structured, and agent-optimized Markdown documentation from code, requirements, specs, or artifacts. Use when creating READMEs, API docs, architecture documents, or converting agent outputs into clean Markdown.
---

# Markdown Documentation Generator

## Use this skill when
- You need to create or improve README.md, API documentation, architecture docs, or user guides
- Converting code comments, tickets, or conversation history into structured documentation
- Producing clean Markdown artifacts for other agents or humans

## Do not use this skill when
- The output needs to be code (use code-generation skills instead)
- You need HTML/PDF rendering (use converter skills)

## Step-by-step instructions
1. **Analyze input**: Thoroughly read the source material (code, specs, previous messages).
2. **Choose structure**: Use appropriate template (project README, API reference, etc.).
3. **Frontmatter**: Always include YAML frontmatter with title, description, date/version.
4. **Core sections**:
   - Executive Summary or Overview
   - Key Features / Capabilities (with tables when useful)
   - Installation / Setup
   - Usage examples with code blocks (specify language)
   - Architecture / How it works (use Mermaid for diagrams)
   - Configuration options (tables)
5. **Optimize for agents**: Use short paragraphs, consistent ATX headings (# ## ###), lists, tables, and callouts.
6. **Add quality touches**: Include TOC if >8 sections, "Next Steps" section, and agent checklist.

## Best practices
- Prefer tables over long lists for comparisons
- Embed Mermaid diagrams for flows and architecture
- Use proper code block language tags
- Keep token efficiency in mind (clear, concise language)
- End every doc with a "Review Checklist" section

## Templates available
See `templates/` folder for ready starters.
