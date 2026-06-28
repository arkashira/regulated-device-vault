# user-stories.md — regulated-device-vault

> Scope note: stories target the validated pain — building/validating regulated medical-device software (IEC 62304, FDA 21 CFR 820 / ISO 13485, IEC 62443 cybersecurity) across the embedded-to-cloud stack. Roles reflect the regulated-SDLC org: Embedded Engineer, QA/V&V Engineer, RA/QA (Regulatory Affairs), Cybersecurity Lead, Release Manager.

---

## Epic 1 — Compliant SDLC & Traceability

### US-1.1 — Requirements-to-test traceability matrix
**As a** QA/V&V engineer, **I want** every requirement auto-linked to its design element, source commit, and verifying test, **so that** I can produce an IEC 62304 §5.1–§5.7 traceability matrix without manual spreadsheet stitching.
- **AC:**
  - Bidirectional links rendered for requirement ↔ design ↔ code ↔ test ↔ risk-control.
  - Orphan detection: any requirement with no verifying test or any test with no requirement is flagged.
  - Export to PDF/CSV with timestamp, baseline tag, and tool version.
  - Matrix regenerates on each merge to a release branch.
- **Complexity:** L

### US-1.2 — Software safety classification gating
**As a** RA/QA lead, **I want** to assign each software item an IEC 62304 safety class (A/B/C) and have the platform enforce class-appropriate process artifacts, **so that** Class C items can't pass a gate missing required documentation.
- **AC:**
  - Class assigned per software item/unit and inherited by sub-items unless overridden (with justification).
  - Gate blocks promotion if class-required artifacts (e.g., detailed design for Class C) are absent.
  - Override requires named approver + rationale captured in the audit log.
- **Complexity:** M

### US-1.3 — Immutable design history record (DHF)
**As a** RA/QA lead, **I want** an append-only, signed record of every design change, review, and approval, **so that** I can hand an auditor a complete Design History File on demand.
- **AC:**
  - Each entry is cryptographically hashed and chained to the prior entry.
  - Records include author, reviewer, e-signature, UTC timestamp, and linked artifacts.
  - Tampering or gaps are detectable and surfaced in an integrity report.
  - Read-only auditor view with no edit/delete capability.
- **Complexity:** L

---

## Epic 2 — Embedded-to-Cloud Build & Verification

### US-2.1 — Reproducible cross-compilation for target hardware
**As an** embedded engineer, **I want** firmware built in a pinned, reproducible toolchain container per target MCU, **so that** the binary I validate is bit-identical to the one submitted to the FDA.
- **AC:**
  - Toolchain version, flags, and SBOM captured and pinned per build.
  - Two builds of the same commit produce identical hashes (reproducibility check in CI).
  - Build provenance attestation (SLSA-style) attached to each artifact.
- **Complexity:** L

### US-2.2 — Hardware-in-the-loop (HIL) test orchestration
**As a** V&V engineer, **I want** to trigger automated test suites against physical or simulated target devices from a release pipeline, **so that** verification evidence is generated against real hardware behavior, not just host emulation.
- **AC:**
  - Test runs target either a connected device pool or a simulator, selectable per suite.
  - Pass/fail results, logs, and captured signals are stored as verification records linked to requirements.
  - Flaky/inconclusive runs are flagged separately from failures.
- **Complexity:** L

### US-2.3 — Coverage & static-analysis evidence capture
**As a** V&V engineer, **I want** MC/DC coverage and MISRA-C/static-analysis results captured per build as signed evidence, **so that** I can demonstrate code-level verification rigor expected for Class B/C software.
- **AC:**
  - Coverage and static-analysis reports attach to the build artifact automatically.
  - Configurable thresholds block promotion when unmet (with documented deviation path).
  - Deviations require justification and RA/QA approval.
- **Complexity:** M

---

## Epic 3 — Risk Management & Cybersecurity (ISO 14971 / IEC 62443)

### US-3.1 — Risk-control to verification linkage
**As a** RA/QA lead, **I want** each ISO 14971 risk control linked to the test that verifies its effectiveness, **so that** I can prove every identified hazard is mitigated and verified.
- **AC:**
  - Risk register items link to risk controls and to verifying tests.
  - Unverified or unmitigated hazards appear on a risk-coverage dashboard.
  - Residual-risk summary exportable for the risk management report.
- **Complexity:** M

### US-3.2 — Vulnerability monitoring against device SBOM
**As a** cybersecurity lead, **I want** continuous CVE monitoring against each release's SBOM, **so that** I'm alerted when a dependency in a fielded device version becomes vulnerable.
- **AC:**
  - SBOM generated per release in CycloneDX/SPDX format.
  - New CVEs matched to affected released versions and triaged by severity.
  - Alerts route to the security lead with affected-device-version list.
  - Supports premarket and postmarket (FDA 524B) cybersecurity reporting.
- **Complexity:** M

### US-3.3 — Threat-model artifact gating
**As a** cybersecurity lead, **I want** a current threat model required before a release gate passes, **so that** no regulated build ships without documented IEC 62443 / FDA premarket cybersecurity analysis.
- **AC:**
  - Threat-model artifact must be present and dated within the current baseline.
  - Stale threat model (predating significant design change) triggers a warning.
  - Linkage from threats to mitigating requirements/controls is checked.
- **Complexity:** S

---

## Epic 4 — Release, Audit & e-Signature

### US-4.1 — Gated, signed release packaging
**As a** release manager, **I want** a one-click release bundle containing the binary, SBOM, traceability matrix, test evidence, and risk summary — all e-signed, **so that** I have a submission-ready package that passes a notified-body audit.
- **AC:**
  - Bundle assembles only when all configured gates are green.
  - Every included artifact carries its provenance hash and signer identity.
  - Bundle manifest is e-signed per 21 CFR Part 11.
  - Bundle is reproducible from the release tag.
- **Complexity:** L

### US-4.2 — 21 CFR Part 11 compliant e-signatures
**As a** RA/QA lead, **I want** electronic signatures with identity binding, meaning/intent, and re-authentication, **so that** approvals are legally equivalent to handwritten signatures under FDA rules.
- **AC:**
  - Signature captures signer name, UTC timestamp, and meaning (authored/reviewed/approved).
  - Re-authentication required at signing.
  - Signatures are non-repudiable and cannot be copied/reused.
- **Complexity:** M

### US-4.3 — Auditor read-only access with full activity log
**As a** RA/QA lead, **I want** to grant an external auditor scoped read-only access with a complete activity trail, **so that** audits run without exporting data or risking record modification.
- **AC:**
  - Time-boxed, role-scoped auditor accounts with no write/delete.
  - All access and record views logged immutably.
  - Auditor can view but not export beyond approved artifact bundles.
- **Complexity:** S

---

**Summary:** 12 stories / 4 epics — Complexity mix: 5×L, 5×M, 2×S. Critical path runs through Epic 1 (traceability backbone) and Epic 2 (build/verification evidence), which the rest depend on.