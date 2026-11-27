# ADR-0021: Ruleset hardening for `main`

- **Status:** Accepted (amends ADR-0017)
- **Date:** 2026-11-27

## Context
ADR-0017's status checks prove that the gates *ran*, not what they *found*, and its bypass was unconstrained. The live ruleset adds controls ADR-0017 does not record.

## Decision
Add to the `main-protection` ruleset:
- **Code scanning results:** block merges when CodeQL reports alerts at SARIF level `error`, or security alerts with severity `high` or `critical`.
- **Signed commits:** GitHub signs squash merges made through the UI or API, so merged commits satisfy this. Direct pushes of unsigned commits are rejected.
- **Merge method:** squash only (redundant with linear history by design; the ruleset enforces both independently).
- **Bypass:** repository admin, mode **pull requests only**: the bypass can merge a PR with failing checks, never push to `main`.
- **Bypass discipline:** a bypass merge of any PR touching `src/uatu/executor/`, `src/uatu/risk/`, `src/uatu/secrets/`, or `.github/workflows/` requires a PR comment from the maintainer stating which check was waived and why.
- Merged branches are deleted automatically.

## Consequences
- A vulnerability found by CodeQL blocks merging, not just a scan that failed to run.
- Every waived gate on sensitive code leaves a written justification on the PR.
