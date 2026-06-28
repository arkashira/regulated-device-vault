```markdown
# breakeven.md — regulated-device-vault

> Unit economics for a vertical DevSecOps + compliance platform serving medical-device software teams (Class II/III, IEC 62304 / FDA 21 CFR 820 / EU MDR). "Active user" = one engineer/QA/RA seat actively pushing to a managed device project in a given month.

## 1. Cost per Active User (monthly, USD)

This is a build-heavy workload: embedded firmware compilation, HIL/simulation runs, SBOM + static analysis, and tamper-evident document/artifact retention (audit trail must survive ~10–15 yrs per FDA records-retention norms). Cost is dominated by CI/compute and long-tail compliant storage, not bandwidth.

| Cost driver | Assumption per active seat/mo | Unit cost | $/seat/mo |
|---|---|---|---|
| CI/build compute | 40 build-hrs (firmware + cloud) @ 4 vCPU spot | $0.045/vCPU-hr | $7.20 |
| SAST / SBOM / fuzz jobs | 12 hrs @ 8 vCPU | $0.06/vCPU-hr | $5.76 |
| HIL/sim orchestration overhead | amortized control plane | — | $1.80 |
| Hot storage (active artifacts, DB) | 25 GB | $0.023/GB | $0.58 |
| Compliance cold storage (WORM audit, 10-yr) | 8 GB/mo accrual @ Glacier-class + integrity index | $0.012/GB | $0.10 |
| Egress/bandwidth | 15 GB | $0.085/GB | $1.28 |
| Logging/observability/security tooling | flat allocation | — | $1.40 |
| **Total variable COGS / active seat** | | | **≈ $18.12** |

- **Blended fully-loaded COGS** (incl. support + SOC2/MDR infra overhead spread): **~$24/seat/mo**.
- Gross margin target ≥ **80%**, so floor effective price ≈ **$120/seat/mo**. Storage liability compounds — model a +$0.10/seat/mo annuity per retained year (the audit-retention tail is a real long-term cost, price it in).

## 2. Pricing Tiers

Per-seat with a project/device floor. Regulated buyers pay for *evidence generation* (audit-ready artifacts), not raw compute — pricing is value-anchored to "cost of a failed audit / 510(k) delay," which runs $250K–$2M+.

| Tier | Price | Target | Key features |
|---|---|---|---|
| **Team** | **$249 / seat / mo** (min 3 seats) | Seed/Series-A device startups, 1 product | Managed embedded→cloud CI, auto-SBOM, IEC 62304 traceability matrix, signed build provenance, 1 audit-export/mo, 2-yr retention |
| **Compliance** | **$649 / seat / mo** (min 5 seats) | Series B / multi-product | Everything in Team + 21 CFR 820 + EU MDR templates, HIL test orchestration, tamper-evident WORM audit vault (10-yr), DHF/DMR auto-assembly, SSO, validation (IQ/OQ/PQ) docs |
| **Enterprise** | **Custom, ~$1,200+/seat** (annual, $60K+ floor) | Established MedTech / contract mfrs | Everything + on-prem/VPC deploy, validated-environment SLA, dedicated compliance engineer, FDA-submission package export, custom retention, audit-defense support |

Anchor metric: Compliance tier @ ~$650/seat is <1 hr of a regulatory consultant's billable rate — trivially justified.

## 3. CAC Range

Vertical B2B with a long, evidence-heavy sales cycle (QA/RA stakeholders + procurement + security review).

- **Team (PLG-assisted + outbound):** **$3,500 – $6,000** per logo. Inbound from device-dev communities + founder-led demos.
- **Compliance (sales-led):** **$9,000 – $18,000** per logo. SE-supported, 60–120 day cycle, security questionnaire + pilot.
- **Enterprise:** **$25,000 – $45,000** per logo. Field sales, POC, validation review.
- **Blended target CAC:** **~$11K**, held against a payback-period ceiling of **≤ 12 months**.

## 4. LTV Estimate

| Tier | Avg seats | ARPA/mo | Gross margin | Monthly churn | Avg life | **LTV** |
|---|---|---|---|---|---|---|
| Team | 4 | $996 | 80% | 3.0% | 33 mo | **~$26K** |
| Compliance | 8 | $5,192 | 82% | 1.5% | 67 mo | **~$285K** |
| Enterprise | 25 | $30,000 | 83% | 0.8% | 125 mo | **~$3.1M** |

- Regulated buyers churn *low* — switching means re-validating tooling, which is expensive and audit-risky. This is the core economic moat. **Blended LTV ≈ $190K**, **LTV:CAC ≈ 17:1** (well above 3:1 floor; signals room to spend harder on growth).

## 5. Break-Even Users Count

Assume fixed monthly burn (lean team of 6 + infra base + SOC2/compliance overhead): **~$95,000/mo**.

Contribution margin per account/mo:
- Team: $996 × 80% = **$797**
- Compliance: $5,192 × 82% = **$4,257**

Break-even, single-tier scenarios:
- **All Team:** $95,000 / $797 ≈ **120 accounts** (~480 seats)
- **All Compliance:** $95,000 / $4,257 ≈ **23 accounts** (~180 seats)
- **Realistic blend** (70% Team / 30% Compliance by account): ≈ **57 accounts** to cover fixed burn.

Per-seat break-even (variable-only, ignoring fixed): instant — margin positive at $249 vs ~$24 COGS. The hurdle is the fixed compliance/infra base, not unit economics.

## 6. Path to $10K MRR

Fastest credible route leans on the **Compliance** tier — fewer logos, anchored to audit-cost avoidance, far less sales friction per dollar.

| Path | Mix | Math | Accounts needed |
|---|---|---|---|
| **A — Compliance-led (recommended)** | Compliance @ ~$5,192/acct | $10,000 / $5,192 | **2 accounts** (~16 seats) |
| B — Team-led | Team @ ~$996/acct | $10,000 / $996 | **11 accounts** (~44 seats) |
| C — Blend (target) | 1 Compliance + 5 Team | $5,192 + $4,980 | **6 accounts** |

**Recommendation:** Land **2 Compliance-tier design-partner accounts** (target Series-A/B device startups already in or approaching 510(k)/CE submission). At ~$5.2K/acct/mo, two paying logos clears $10K MRR while validating the audit-vault as the wedge feature. Anchor early deals annual-prepaid to fund the SOC2/MDR infra base before scaling outbound.
```