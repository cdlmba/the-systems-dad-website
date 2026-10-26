---
name: The Systems Dad
description: Warm, practical, high-trust design system for thesystemsdad.com — editorial serif + clean sans, cream ground, forest accent. Built for busy executive dads who need to understand the site in 5 seconds and act without thinking.
version: alpha

colors:
  # Core palette (current site extracted + refined)
  background: "#FAF8F5"          # Warm cream — the page feels like paper, not a dashboard
  surface: "#F3EFE6"             # Soft beige for cards and sections
  surface-elevated: "#FFFFFF"
  text-primary: "#24221F"        # Near-black warm ink
  text-secondary: "#6B665E"      # Muted taupe for supporting text
  text-muted: "#C4C2BC"
  accent: "#244234"              # Deep forest green — calm authority, not startup blue
  accent-hover: "#1A2F25"
  accent-soft: "rgba(36, 66, 52, 0.08)"
  gold: "#B8860B"                # Sparingly for 936 Saturdays / legacy moments
  border: "#E8E4DC"
  on-accent: "#FAF8F5"

typography:
  display: 
    fontFamily: "Lora, Georgia, serif"
    fontWeight: 600
    letterSpacing: "-0.015em"
  heading:
    fontFamily: "Lora, Georgia, serif"
    fontWeight: 600
  body:
    fontFamily: "Plus Jakarta Sans, system-ui, sans-serif"
    fontWeight: 400
  body-medium:
    fontFamily: "Plus Jakarta Sans, system-ui, sans-serif"
    fontWeight: 600
  caption:
    fontFamily: "Plus Jakarta Sans, system-ui, sans-serif"
    fontWeight: 400

spacing:
  xs: 4px
  sm: 8px
  md: 16px
  lg: 24px
  xl: 40px
  xxl: 64px
  section: 96px

rounded:
  sm: 6px
  md: 12px
  lg: 16px
  pill: 9999px

---

# The Systems Dad Design System

## Overview

The Systems Dad site should feel like a clear, calm conversation with a smart friend who has already solved the problem you’re about to have. Not a productivity dashboard. Not a guru landing page. Not a corporate consulting site.

The reader is a high-performing dad who is winning at work and drowning at home. He arrives tired, half-scanned, phone in hand, between Slack and school pickup. Every element must answer three questions instantly: What is this? Who is it for? What do I do next?

Current site (as of Oct 2026): Warm cream background (#FAF8F5), Lora serif headlines, deep forest green accents, single-column editorial flow with numbered offers and strong personal story. It works but feels dense and text-heavy. Goal of redesign: more breathing room, clearer visual hierarchy, stronger information scent, and patterns proven on high-converting personal-brand and systems sites — researched via Mobbin.

## Brand & Voice Lock (Non-Negotiable)

- Target: Executive dads (PMs, operators, leaders) who manage complex work and chaotic home logistics.
- Core problem: Ghost Dad — physically present, mentally still at the office. Work Residue. 936 Saturdays.
- Tone: Real dad. Anti-guru. Specific logistics. Coffee on the porch. No hustle myth, no corporate jargon above the fold.
- Key phrases to protect: Ghost Dad, 5:15, Home Operating System, DadOps, MarginReset (soft link only), 936 Saturdays, Sunday Check-In, Kitchen Board, Zero Residue.
- Never: productivity guru energy, “unlock your potential,” stacked benefits, three-column feature grids that feel like SaaS, or blending CLS corporate language.

## Usability Principles (Krug + Norman)

1. **Don’t Make Me Think.** Hero must communicate purpose in <5 seconds. One primary action per section.
2. **Scanning first.** Strong visual hierarchy, short paragraphs (max 3 lines), high contrast, clear section breaks.
3. **Affordances & Signifiers.** Buttons look clickable. Links have clear destination. Phone-on-charger and kitchen-board concepts are visualized, not just described.
4. **Mindless choices.** Persistent simple nav. Obvious next step. No mystery meat.
5. **Feedback.** Immediate visual response on hover/focus. Clear success states on forms.
6. **Mobile-first.** Busy dads read this on phones. Touch targets ≥44px. No horizontal scroll. Text never smaller than 16px on mobile.
7. **Whitespace is confidence.** Generous section padding. Avoid density that signals anxiety.

## Colors

Warm cream ground creates a paper/editorial feel that signals “this is written by a person, not a growth team.” Deep forest green is the single action color — calm, grounded, not startup-blue or hustle-orange. Gold is reserved for the 936 Saturdays / legacy framing only. Never use more than two accent moments on one screen.

## Typography

Lora for display and headings gives literary weight, warmth, and thoughtful cadence without pretension. Plus Jakarta Sans for body provides a clean, contemporary, highly readable structure with generous air, perfectly balancing the warmth of Lora without feeling cold or overly technical. Hierarchy is strict: one display size per page, clear H1 → H2 → body. Line length capped at ~65 characters. No all-caps except tiny labels.

## Layout & Spacing

- Max content width: 720px for prose, 1100px for full sections.
- Section rhythm: large vertical padding (section token).
- Cards: soft surface background, subtle border or none, generous internal padding.
- No three-column grids unless the content is truly parallel and scannable.
- Sticky simple nav with logo + 3 links max + one CTA.

## Components

- **Primary CTA**: Accent fill, cream text, pill or 12px radius, clear verb (“Get the House System →”). One per viewport.
- **Secondary CTA**: Outline or text link with arrow.
- **Offer cards**: Numbered (01, 02, 03), short headline, one sentence, price or “Free”, single button. No feature lists longer than 3 bullets.
- **Story block**: Large pull quote or short scene + photo of Christopher (real, not stock).
- **Testimonial**: Short quote + role, no star ratings.
- **Habit cards**: Icon or simple illustration + title + one-sentence how-to.

## Do’s and Don’ts

**Do**
- Open every major section with a specific scene or object (phone on charger, kitchen board, Sunday night).
- Show the after-state more than the pain.
- Link MarginReset only as the tactical 10-minute bridge, never as the main offer.
- Keep personal story honest and short.
- Use real photos of Christopher and family context where appropriate.

**Don’t**
- Use corporate stock photos of smiling dads in suits.
- Stack three short punchy sentences in a row as a closer.
- Add “framework,” “ecosystem,” “unlock,” “seamless,” or any banned jargon.
- Make the user scroll through long feature lists before seeing the price or CTA.
- Use pure white or pure black. Keep the warm paper feeling.
- Create mystery CTAs (“Learn more”).

## Mobbin Research Brief (for Antigravity)

When researching redesign inspiration:

Search Mobbin (Sites + relevant flows) for:
- Personal brand / creator landing pages with strong story + offer ladder
- Editorial / magazine-style sites that convert
- High-trust SaaS or systems sites that feel human (not Linear-clone dark mode)
- Pricing / offer selection patterns that reduce decision friction
- Testimonial and founder story sections that feel authentic
- Mobile navigation and sticky CTA patterns for content-heavy sites

Prioritize patterns that support scanning, clear hierarchy, and low cognitive load. Capture specific examples (app/site name + section) and note why each fits or doesn’t fit the TSD voice. Output a short design direction document + recommended layout changes before any code.

## Agent Prompt Guide

When generating or editing the site, always:
1. Read this DESIGN.md first.
2. Prefer the tokens above over inventing new colors or fonts.
3. Run the Coffee Test on any new copy: would Christopher say this to a tired friend?
4. Prioritize Krug/Norman: self-evident, scannable, strong affordances.
5. Keep TSD voice locked — real dad, specific logistics, no guru.

End of system. Treat as living document. Update after each major redesign pass.
