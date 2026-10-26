---
name: systems-logic-gap-analyzer
version: 1.0.0
description: |
  Analyzes CSV response data from The Systems Dad Audit.
  Identifies broad Logic Gaps across your audience.
  Suggests strategic content (Kit, X, LinkedIn) to address them.
allowed-tools:
  - Read
  - Write
---

# Logic Gap Analyzer: Market Intelligence Engine

Use this skill to process batches of user audit data (CSV format) and transform raw points into strategic insight.

> **Operational Truth**: Don't guess what your audience needs. Analyze the actual failures of their current systems.

## Data Interpretation Logic

The Audit measures four critical System Layers. When analyzing CSV data, look for these common manual (Low Score) patterns:

| Audit Layer | The Failure (Low Score) | The "Systems Dad" Fix |
| :--- | :--- | :--- |
| **01 Mental Hand-Off** | Ghost at the Table; checking Slack during dinner. | **Shutdown Protocol**: A tactical move to buy back presence. |
| **02 Logistics Engine** | Shoe Chaos; System Crash on contingency. | **Family API**: A centralized hub for logistics. |
| **03 Rituals** | The Bottleneck Dad; Friday chores dread. | **Automated Rituals**: Friday Shutdown & Sunday Prep. |
| **04 Margin** | "I can't remember" phone-free time. | **Infrastructure of Focus**: Phone-free rituals. |

## CSV Analysis Workflow

### 1. The Summary Pass
Look at the distribution of scores. Are you attracting the manual dad (<=7), the scripting dad (<=14), or the automated dad (>14)?

### 2. The Logic Gap Heatmap
Identify which specific question has the highest frequency of low scores.
- **Example**: If 80% of users answer Scattered texts for Category 02, your audience has a Logistics API Gap.

### 3. The Content Multiplier
Based on the heatmap, suggest:
- **X Thread**: "How to fix the [Category] logic gap."
- **LinkedIn Post**: "Why a [Category] failure is the #1 cause of PM burnout."
- **Kit Draft**: A deep dive into the "Lever" required to automate that specific failure.

## Output Requirement

1. **Audience Breakdown**: % distribution of Audit Personas (Manual vs. Scripting vs. Automated).
2. **The High-Priority Gap**: Identify the #1 systemic failure identified in the batch.
3. **The Content Roadmap**: 3 specific post ideas to bridge that gap.

Analyze the raw data. Define the Gap. Architect the Fix.
