---
name: Mobile Experience Architect
description: High-authority responsive design, touch-optimized UI, and performance-first mobile rendering.
---

# 📱 Mobile Experience Architect Agent Skill

This skill codifies the "Mobile-First" technical standards for Christopher Lynn Systems (CLS) and The Systems Dad (TSD). It ensures that all web assets are optimized for high-authority presence on mobile devices, where the majority of technical leadership and executive traffic originates.

## 🛡️ Response Design Standards

### 1. Viewport Hygiene
*   **Mandate**: Every HTML asset must include the standard meta-viewport tag: `<meta name="viewport" content="width=device-width, initial-scale=1.0">`.
*   **Scalability**: Users must be able to zoom (do not use `user-scalable=no` unless in a high-intensity dashboard context authorized by the CTO).

### 2. Touch-Proximity Logic (The 44px Mandate)
*   **Interactive Targets**: All buttons, links, and menu items must have a minimum interactive area of **44x44px**. 
*   **Spacing**: Ensure adequate white space around CTAs to prevent "Fat-Finger" errors and mis-clicks on mobile.

### 3. Hero Split-Layout Logic
*   **Desktop (992px+)**: Implement side-by-side architecture with text on the left and high-impact visual (e.g., Ghost Dad) on the right.
*   **Mobile (<992px)**: Automatically stack components vertically.
*   **Visual Priority**: In mobile viewports, ensure the **Hero Text (The Hook)** remains above the fold. The **Hero Image** should either follow the text or be used as a subtle background element to maintain high-authority narrative resonance.
*   **Shadows & Borders**: Mobile images must use `box-shadow: var(--shadow-glow)` and `border: 1px solid var(--border-color)` to maintain brand consistency on high-DPI screens.

---

## 🎨 Mobile Typography & Readability

### 1. The 16px Baseline
*   **Inputs**: All form fields must use a minimum font-size of **16px** (mobile safari standard) to prevent the browser from automatically zooming in on focus, which breaks the layout.
*   **Body Copy**: Enforce high-legibility font weights and line-heights (min 1.6) for mobile readability.

### 2. One-Sentence-Per-Line (OSPL)
*   **Resonance**: For mobile narrative sections (TSD particularly), follow the OSPL rule. Technical dads scan; they do not read walls of text.

---

## ⚙️ Performance & Loading

### 1. Asset Optimization
*   **Lazy Loading**: Every image (unless in the initial viewport/hero) must include `loading="lazy"`.
*   **Dimensions**: Always specify `width` and `height` to prevent Layout Shift (CLS) on slow mobile connections.

### 2. Reduced Motion
*   **Preference**: Honor use-prefers-reduced-motion for complex scroll-reveals on mobile to ensure a smooth, stable experience.

---

## 🔄 Verification Protocol

1.  **Ingest**: Receive a template or component.
2.  **Audit**: Check for meta-viewport, touch-target sizing (44px), and 16px font baseline.
3.  **Refactor**: Consolidate media queries into a unified "Mobile-First" block at the bottom of the style manifest.
4.  **Test**: Verify rendering on simulated `375x667` (iPhone SE) and `414x896` (iPhone 11/Pro Max) viewports.
## 🖋️ Prose Governance (The Orwell Protocol)

These govern prose: docs, PR text, messages. Never touch code or technical terms; swap in everyday words only where precision survives.

1. Never use a metaphor, simile or other figure of speech which you are used to seeing in print.
2. Never use a long word where a short one will do.
3. If it is possible to cut a word out, always cut it out.
4. Never use the passive where you can use the active.
5. Never use a foreign phrase, a scientific word or a jargon word if you can think of an everyday English equivalent.
6. Break any of these rules sooner than say anything outright barbarous.

Review every prose output against these rules before delivering.

**Status: Enforcing Mobile Excellence 📱**
