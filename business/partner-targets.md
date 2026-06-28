# partner-targets.md

> Partner integration roadmap for **regulated-device-vault** — a dev+validation platform for regulated medical device software (IEC 62304 / FDA 510(k) / EU MDR) spanning embedded firmware → cloud. Integrations are ranked by **(a) revenue-share/affiliate availability**, then **(b) value-to-effort ratio**. Effort: S = <1 dev-week, M = 1–3 dev-weeks, L = >3 dev-weeks.

## Priority tiers at a glance

| # | Partner | Category | Effort | Rev-share? | User job solved |
|---|---------|----------|--------|-----------|-----------------|
| 1 | **GitHub / GitHub Advanced Security** | SCM + SCA/SAST | S | Marketplace rev-share (manual approval) | Traceability: link code→requirement→test |
| 2 | **Jira / Jira Service Mgmt (Atlassian)** | ALM/requirements | M | Marketplace 75/25 (Atlassian takes 25%) | Requirements & risk-trace matrix sync |
| 3 | **Polarion / Jama Connect** | Reqs & DHF | L | Reseller/referral margin | Design History File (DHF) of record |
| 4 | **Snyk** | SCA/SBOM/vuln | S | Affiliate + reseller program | Cybersecurity per FDA premarket guidance |
| 5 | **Anchore / Syft+Grype** (OSS) | SBOM gen | S | None (OSS — owned moat) | SBOM (mandatory FD&C §524B) |
| 6 | **DocuSign** | e-signature | S | ISV referral rev-share | 21 CFR Part 11 signed approvals |
| 7 | **AWS Marketplace (HIPAA/GovCloud)** | infra + distribution | M | **AWS Marketplace 3–20% take, co-sell $$** | Validated hosting + procurement channel |
| 8 | **Greenlight Guru** | medical-device QMS | L | Partner/referral program | eQMS + 510(k) submission workflow |

---

## 1. GitHub + GitHub Advanced Security — **S, do first**
- **Why first:** Every embedded/cloud team already lives here. We become the compliance layer *on top of* their existing SCM rather than asking them to migrate.
- **Value-add (job):** Auto-build the **bidirectional traceability matrix** IEC 62304 §5.1 demands — requirement ↔ commit ↔ PR ↔ test result — by reading commits, PRs, checks, and code-scanning alerts via the REST/GraphQL API + a GitHub App.
- **Free-tier limits:** GitHub App API = 5,000 req/hr per installation (15,000 for GH Enterprise Cloud apps). Code Scanning free for public repos; GHAS is paid per-committer for private.
- **Rev-share:** GitHub Marketplace supports paid apps with revenue-share (currently invite/approval-gated; plan a free listing first, paid tier later).
- **Effort: S** — OAuth/App flow + webhook ingestion is well-trodden.

## 2. Jira (Atlassian) — **M**
- **Why:** Dominant requirements/issue backbone in mid-size medtech. Connecting here means we don't fight the customer's existing process.
- **Value-add (job):** Pull epics/stories/risks as **requirements + risk items**, push generated trace matrix and verification status back as a panel. Solves "prove every requirement is verified" for auditors.
- **Free-tier limits:** Jira Cloud REST API ~ rate-limited by cost budget per app/user (no flat number; ~10 concurrent + token-bucket). Free Jira plan = 10 users.
- **Rev-share:** **Atlassian Marketplace = 75% to vendor / 25% to Atlassian** on paid cloud apps — one of the better economics in this list. Strong reason to ship a paid Forge/Connect app.
- **Effort: M** — Forge app + field mapping + the inevitable custom-field variance per customer.

## 3. Polarion / Jama Connect — **L (enterprise wedge)**
- **Why:** These are the **systems of record for the Design History File** in larger, Class II/III shops. Integrating makes us "compatible with what your auditor already trusts."
- **Value-add (job):** Two-way sync of requirements, risks (ISO 14971), and V&V evidence so the DHF stays the single source of truth while devs work in our tooling.
- **Free-tier limits:** Enterprise, no public free tier; both expose REST APIs (Jama REST; Polarion REST/OpenAPI). Sandbox access via partner program.
- **Rev-share:** Jama and Siemens (Polarion) run **referral/reseller programs** — negotiate referral margin or co-sell. Not self-serve; relationship-driven.
- **Effort: L** — enterprise auth, schema mapping, and partner onboarding. Sequence *after* PMF on GitHub+Jira.

## 4. Snyk — **S, highest cybersecurity ROI**
- **Why:** FDA premarket cybersecurity guidance (2023) + §524B make SCA/vuln management non-optional. Snyk is the recognizable name auditors accept.
- **Value-add (job):** Continuous dependency + container vuln scanning feeding our **cybersecurity bill-of-materials** and risk file.
- **Free-tier limits:** Free plan ~ 100 open-source tests/month, 100 container tests/month, limited IaC. API available on free tier (rate-limited).
- **Rev-share:** Snyk has **partner / affiliate + reseller programs** — pursue reseller margin so customers buy Snyk *through* us.
- **Effort: S** — REST API + token; results normalize cleanly into our risk model.

## 5. Anchore (Syft + Grype, OSS) — **S, owned moat**
- **Why:** SBOM is now **legally mandatory** (FD&C §524B(b)(3)). Embedding open-source Syft (SBOM gen) + Grype (vuln match) lets us offer SBOM **for free, in-product**, no per-call vendor cost.
- **Value-add (job):** Generate CycloneDX/SPDX SBOMs for firmware + cloud images automatically and diff them across releases.
- **Free-tier limits:** Apache-2.0 OSS — no API limits, we self-host. (Anchore Enterprise is the paid upsell if customers want governance/dashboards.)
- **Rev-share:** None directly, but it's a **cost-zero differentiator** vs. Snyk-only competitors and an upsell funnel to Anchore Enterprise (negotiate referral).
- **Effort: S** — bundle binaries, run in our scan pipeline.

## 6. DocuSign — **S**
- **Why:** 21 CFR Part 11 requires controlled **electronic signatures** on approvals (design reviews, test protocol sign-off). DocuSign is the safe, auditor-friendly default.
- **Value-add (job):** Route design reviews / V&V protocol approvals for compliant e-signature with audit trail.
- **Free-tier limits:** No perpetual free tier; **developer sandbox is free** (unlimited test envelopes). Production is paid per-envelope.
- **Rev-share:** **DocuSign ISV / referral program** offers rev-share for embedded eSignature partners.
- **Effort: S** — eSignature REST API + embedded signing.
- *Alt to evaluate:* Dropbox Sign (HelloSign) — cheaper API, also referral program; keep as fallback.

## 7. AWS Marketplace (HIPAA-eligible / GovCloud) — **M, distribution play**
- **Why:** Doubles as **infrastructure** (validated, HIPAA-BAA hosting) and a **sales channel** (procurement through customers' existing AWS spend / committed-spend drawdown).
- **Value-add (job):** "Hosting won't fail the audit" + frictionless enterprise procurement.
- **Free-tier limits:** AWS Free Tier (12-mo + always-free); BAA available at no extra cost on HIPAA-eligible services.
- **Rev-share:** **AWS Marketplace takes ~3% (down from 20% via programs); co-sell (ISV Accelerate) can drive sourced pipeline.** This is *channel revenue*, not just an integration.
- **Effort: M** — Marketplace listing + metering + BAA/architecture review.

## 8. Greenlight Guru — **L (ecosystem fit, sequence last)**
- **Why:** Purpose-built medical-device **eQMS**; their customers are exactly our ICP. Integration positions us as the *engineering* half of their *quality* platform.
- **Value-add (job):** Push design/V&V evidence into their QMS and 510(k)/MDR submission workflow so quality + engineering share one record.
- **Free-tier limits:** No public free tier/API; partner-program access required.
- **Rev-share:** **Partner / referral program** — co-marketing + referral fees; relationship-driven.
- **Effort: L** — partner onboarding gated; build after we have reference customers.

---

## Recommended build sequence
1. **Sprint 1–2 (S):** GitHub + Anchore(OSS) + Snyk → instant traceability + SBOM + cybersecurity = the demo that closes deals.
2. **Sprint 3–4 (S/M):** DocuSign (Part 11 signatures) + Jira (best marketplace economics at 75/25).
3. **Sprint 5+ (M/L):** AWS Marketplace (channel revenue) → then Polarion/Jama + Greenlight Guru once reference logos exist.

## Revenue-share scorecard
- **Best vendor economics:** Atlassian Marketplace (75% to us).
- **Best channel leverage:** AWS Marketplace co-sell (sourced enterprise pipeline + drawdown procurement).
- **Best reseller margin to chase:** Snyk + Greenlight Guru referral programs.
- **Strategic free moat:** Anchore/Syft/Grype OSS — zero COGS SBOM as a wedge competitors can't easily undercut.

> ⚠️ **Open data gap:** Market-data input was empty `{}`. Free-tier limits and rev-share percentages above are current-as-of-knowledge estimates and **must be re-verified against each partner's live program terms before being quoted in a customer-facing pricing or partnership commitment.**