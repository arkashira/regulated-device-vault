# ROADMAP.md – regulated‑device‑vault

## Vision
Create a secure, auditable, end‑to‑end platform that enables medical‑device OEMs and software teams to **develop, test, and validate** regulated software across the embedded‑to‑cloud stack while staying compliant with FDA 21 CFR 820, IEC 62304, and related standards.

---

## MVP (Minimum Viable Product) – **Launch‑Ready Core** *(Critical)*

| Milestone | Description | Acceptance Criteria | Owner |
|-----------|-------------|---------------------|-------|
| **M1 – Secure Project Workspace** | Multi‑tenant workspace with role‑based access (Engineer, QA, Regulatory, Admin). | • OAuth2 + SSO integration<br>• Audit‑log of every action<br>• Data isolation per tenant | Platform |
| **M2 – Embedded Build & Test Harness** | Containerised build environment for ARM Cortex‑M and RISC‑V targets with deterministic builds. | • CI pipeline (GitHub Actions) that produces reproducible binaries<br>• Unit‑test runner with coverage reports<br>• Artifact signing (ECDSA) | Build |
| **M3 – Cloud‑Side Service Stubs** | Mocked cloud services (MQTT broker, OTA update service, data lake) with programmable failure injection. | • Configurable latency & error rates<br>• Exportable OpenAPI spec<br>• Integrated with embedded test harness | Cloud |
| **M4 – Compliance Artefact Generator** | Automatic generation of required documentation (Software Development Plan, Traceability Matrix, Risk Log). | • Export to PDF/Word<br>• Links artefacts to code commits and test results<br>• Supports IEC 62304 work‑product taxonomy | Compliance |
| **M5 – Continuous Validation Dashboard** | Real‑time view of test results, risk status, and regulatory gaps. | • Dashboard shows pass/fail, coverage, risk severity<br>• Alerts on non‑compliant changes<br>• Role‑based view filters | UI |
| **M6 – Deployment & Release Workflow** | End‑to‑end pipeline from source to OTA package with signed release bundle. | • One‑click “Create Release” that packages firmware, cloud config, and compliance artefacts<br>• Release artefact hash stored immutably in ledger (e.g., blockchain‑style audit) | Release |

**MVP Success Metric:** 2 pilot OEMs can complete a full development cycle (design → OTA release) and produce a complete FDA‑style submission package within 8 weeks.

---

## Phase 1 – **Enterprise Enablement** (v1)

| Theme | Key Features | Target Release |
|-------|--------------|----------------|
| **Scalable Multi‑Tenant Architecture** | • Namespace isolation via Kubernetes operators<br>• Tenant quota & billing integration<br>• SAML & SCIM provisioning | Q3 2026 |
| **Advanced Risk Management** | • Integrated FMEA/FTA tooling<br>• Automated risk propagation from code changes<br>• Export to FDA‑compatible XSLX templates | Q4 2026 |
| **Regulatory Change Engine** | • Rules engine that maps new regulations to required artefacts<br>• Notification system for impacted projects | Q4 2026 |
| **Extensible Test Library** | • Pre‑built test suites for common medical‑device protocols (BLE, IEEE 11073, HL7)<br>• Plug‑in SDK for custom test modules | Q1 2027 |
| **Audit‑Ready API** | • Full REST & gRPC API with OpenAPI spec<br>• API‑level access logs for regulator review | Q1 2027 |

**Milestone Gate:** ≥ 5 external OEMs adopt the platform for at least one regulated product line; compliance audit passes external reviewer.

---

## Phase 2 – **AI‑Assisted Development** (v2)

| Theme | Key Features | Target Release |
|-------|--------------|----------------|
| **LLM‑Powered Specification Drafting** | • Prompt‑based generation of Software Requirements Specification (SRS) aligned to IEC 62304<br>• Inline traceability suggestions | Q3 2027 |
| **Automated Code Review for Safety** | • Static analysis tuned for safety‑critical patterns (MISRA‑C, CERT‑C)<br>• Real‑time risk impact scoring on PRs | Q4 2027 |
| **Predictive Validation** | • Model trained on historic test data to forecast test coverage gaps<br>• Suggest optimal test cases to achieve target coverage | Q4 2027 |
| **Digital Twin Simulation** | • Cloud‑hosted digital twin of target hardware for early‑stage functional testing<br>• Integration with CI pipeline | Q1 2028 |
| **Regulatory Submission Assistant** | • End‑to‑end generation of 510(k) / PMA submission bundles with auto‑filled sections from platform artefacts | Q1 2028 |

**Milestone Gate:** Demonstrated reduction of validation cycle time by ≥ 30 % on a partner’s next‑gen device; regulatory submission accepted without major reviewer comments.

---

## Phase 3 – **Ecosystem & Marketplace** (post‑v2)

| Initiative | Description |
|------------|-------------|
| **Third‑Party Plugin Marketplace** | Enable vendors to sell certified test modules, risk templates, or compliance checklists. |
| **Standard‑Body Collaboration Hub** | Direct feed of platform‑generated artefacts to bodies like FDA’s Digital Health Center of Excellence. |
| **Cross‑Domain Certification** | Extend support to other regulated domains (e.g., automotive ISO 26262, aerospace DO‑178C). |

---

## Governance & Success Metrics

| Metric | Target |
|--------|--------|
| **Time‑to‑Compliance** | ≤ 12 weeks for MVP pilots |
| **Test Coverage** | ≥ 85 % unit + integration coverage on every release |
| **Customer Retention** | ≥ 80 % renewal after 6 months |
| **Regulatory Pass Rate** | ≤ 5 % of artefacts flagged in external audit |
| **Revenue** | $1.2 M ARR by end of 2027 |

---

*All dates are provisional and tied to resource allocation and pilot feedback.*
