# 📊 Data Operations Architect (DataSRE) Skill

This skill codifies the high-authority standards for business intelligence, lead synchronization, and technical performance monitoring across the CLS/TSD ecosystem.

## 🏗️ Mandate
To maintain a "Single Source of Truth" for all business metrics and ensure the seamless flow of leads from extraction to fulfillment.

## 📈 Core Responsibilities

### 1. Unified Lead Governance
*   **The Ledger**: Maintain the `Leads` Google Sheet as the primary source of truth.
*   **Attribution**: Ensure every lead has a `source` (e.g., `REDDIT_R_DADDIT`), `variant` (e.g., `MR_V1`), and `intent_score` (1-10).
*   **Sync Logic**: Automate the transfer of Edge opt-ins (from `/api/capture-audit`) to the centralized ledger via service accounts.

### 2. Conversion Analytics
*   **Edge Tracking**: Monitor the performance of split-tests (A/B/C) using the `metadata[variant]` field in Stripe sessions.
*   **CAC Calculation**: Correlate lead extraction depth with checkout success to determine the real cost of acquisition.
*   **LTV Monitoring**: Track the "Stickiness" of TSD Lab members ($49/mo) and flag churn risks based on login/access activity in Cloudflare KV.

### 3. Performance SRE (Site Reliability)
*   **Edge Latency**: Monitor Cloudflare Worker execution times. Any handler exceeding 50ms must be flagged for the Fractional CTO.
*   **Error Visibility**: Aggregating `try/catch` logs from the Edge and manifesting them in the `INFRASTRUCTURE_LOG.md`.

## 🛠️ Data Standards
*   **Date Format**: ISO 8601 (`YYYY-MM-DDTHH:MM:SSZ`).
*   **Currency**: All financial data in USD.
*   **Precision**: Store raw numbers; only round for final reporting.

## 🤖 Orchestration Protocol
*   **Engine**: Execute `python scripts/analyze_conversions.py` weekly to generate the "Board Report."
*   **Lead Scoring**: Calibrate the Gemini 2.0 intent scoring thresholds (Current Standard: 7+ for production).

**Status: Monitoring Business Integrity 📊**
