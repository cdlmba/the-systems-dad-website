# Onboarding Roadmap: 60 Days to Architectural Calm

**Goal**: Transform the current codebase into a modular "Cloudflare Worker Core" architecture with zero technical debt in high-impact areas.

## 🏗 Phase 1: Complexity Audit & Baselines (Days 1–15)
*Focus: Mapping the "High-Friction" zones.*

*   **Deep Audit**: Review `src/index.js`, `build_blog.py`, and `build_dist.py`. Identify repeated logic and hardcoded values.
*   **The "Limping" Report**: Create a list of the top 5 technical bottlenecks slowing down development.
*   **Skill Mastery**: Review the [CIO Infrastructure Management](file:///c:/Users/Test/OneDrive/Documents/1%20Projects/104%20Christopher%20Lynn%20Systems%20Website/.agents/skills/cio-infrastructure/SKILL.md) standards to ensure architectural alignment.
*   **Deliverable**: A "Technical Debt Backlog" prioritized by impact on velocity.

## 🚀 Phase 2: The Modularity Sprint (Days 16–45)
*Focus: Decomposing the Monolith.*

*   **Router Evaluation**: Advise on using a formal router (e.g., Hono) vs. a custom modular pattern.
*   **Refactor 01**: Extract API logic (Stripe/Whop) into a dedicated `/api` module.
*   **Refactor 02**: Extract TSD routing and A/B testing logic into a `/brands/tsd` module.
*   **Deliverable**: A "Dry-Run" deployment showing the new modular structure in a dev environment.

## 🎯 Phase 3: Quality Gates & Scalability (Days 46–60)
*Focus: Hardening the Build.*

*   **Testing Protocol**: Implement unit tests for critical business logic (e.g., membership verification).
*   **Quality Gates**: Set up automated linting and formatting rules.
*   **CEO Review**: Present the final "Worker Core" architecture and hand over the maintenance playbook.
*   **Deliverable**: 100% modular code coverage with zero linting errors and passing unit tests.

---

> [!TIP]
> **The Stability Mandate**: During these 60 days, "Working Code" is the baseline. "Clear Code" is the goal. Regressions are unacceptable.
