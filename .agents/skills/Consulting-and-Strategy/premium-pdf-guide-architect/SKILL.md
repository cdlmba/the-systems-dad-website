---
name: premium-pdf-guide-architect
description: A high-precision skill for architecting premium, printable PDF guides using HTML/CSS. Optimized for landscape orientation, full-bleed aesthetics, and zero-margin printing.
---

# Premium PDF Guide Architect

This skill defines the "Systems Dad" standard for high-authority PDF companion guides. It supports two primary modes: **Executive Landscape** (Compact Dashboards) and **Strategic Portrait** (Fluid Content Flow).

## Core Design Principles

1.  **Orientation Selection**: 
    *   **Landscape (11x8.5)**: Best for 5-Day Resets, Dashboard Worksheets, and side-by-side prompt comparisons.
    *   **Portrait (8.5x11)**: Best for content-heavy Protocols (e.g., Digital Sabbath), multi-step checklists, and deep narrative guides.
2.  **The 10.25" Safe Zone**: To prevent cross-browser clipping, always architect for a **10.25in Safe Height** and **7.75in Safe Width**. This 0.75" buffer accounts for browser-specific "phantom margins."
3.  **Visual Anchors**: Pair every technical section with a high-impact hero image (Contained row, not full-page background).
4.  **Standard Closing**: Every guide MUST end with the **"The Baseball Game"** narrative and author headshot to cement trust and authority.

## Technical CSS Specification

### 1. Page & Container Setup (Strategic Portrait Mode)
```css
@page {
  size: Letter portrait; /* Or landscape for Dashboards */
  margin: 0;
}

.print-section {
  width: 7.75in;       /* Safety Width */
  min-height: 10.25in; /* Safety Height */
  padding: 0.5in 0.75in;
  position: relative;
  break-after: page;
  display: flex;
  flex-direction: column;
}
```

### 2. Intelligent Breaking
To prevent headers from being orphaned or cards from being chopped in half:
```css
.prompt-card, 
.checklist-block, 
.activity-card, 
.callout {
  break-inside: avoid !important;
  page-break-inside: avoid !important;
}
```

### 3. The "Baseball Game" Closing Standard
```css
.closing-grid {
  display: grid;
  grid-template-columns: 2.5in 1fr; /* Image left, text right */
  gap: 2rem;
  align-items: flex-start;
}

.closing-photo-container {
  height: 4in;
  border-radius: 10px;
  overflow: hidden;
  border: 1px solid var(--teal-border);
}
```

## Content Density Guidelines

- **Typography**: 
    - Body: `10pt` or `10.5pt` with `1.55` line-height for Portrait.
    - Title: `32pt` (Page 1) or `20pt` (Internal Headers).
- **Safe Padding**: Keep content at least `0.5in` from any physical edge to prevent "printer bleed" issues.

## Workflow Checklist

1. [ ] Choose **Portrait** (Fluid) or **Landscape** (Dashboard).
2. [ ] Wrap every section in `.print-section`.
3. [ ] Confirm **Safe Height (10.25in)** to pre-empt clipping.
4. [ ] Ensure **"The Baseball Game"** narrative is the final page.
5. [ ] Run Print Preview with **"Margins: None"** and **"Background Graphics: On"**.
6. [ ] Verify no "ghost pages" (tiny overflows causing blank sheets).
7. [ ] Verify no "sliced cards" (Ensure `break-inside: avoid` is active).
