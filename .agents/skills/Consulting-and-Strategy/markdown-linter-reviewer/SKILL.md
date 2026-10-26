---
name: markdown-linter-reviewer
description: Performs comprehensive reviews of Markdown for clarity, consistency, structure, SEO, and agent-friendliness. Returns detailed feedback plus an improved version. Use whenever you want to polish or validate Markdown output.
---

# Markdown Linter & Reviewer

## Use this skill when
- Reviewing agent-generated or human-written Markdown
- Ensuring documentation meets high quality standards
- Checking for consistency across multiple files

## Instructions
1. **Analyze** the provided Markdown on these dimensions:
   - Structure & hierarchy
   - Readability & scannability
   - Consistency (headings, lists, terminology)
   - Technical accuracy (if applicable)
   - Agent optimization (token efficiency, clarity)
2. **Provide structured feedback** with sections: Strengths, Issues, Suggestions.
3. **Output an improved version** with changes clearly marked or in a separate block.
4. **Score** the original on a 1-10 scale across categories.

## Review checklist (always cover these)
- Proper ATX headings only (no setext)
- Language tags on all code blocks
- Tables used for tabular data
- No broken links
- Consistent bullet style
- Good use of whitespace
