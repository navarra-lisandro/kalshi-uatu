# ADR-0017: Solo-maintainer branch ruleset for `main`

- **Status:** Accepted (amends ADR-0015, "Code review" clause)
- **Date:** 2026-11-26

## Context
ADR-0015 required owner review on money-moving code. With a single maintainer this is unsatisfiable: GitHub never lets a PR author approve their own PR. Only accounts with write access can merge or cast counting reviews, and the maintainer is the only one.

## Decision
A GitHub **ruleset** on `main`:
- Pull request required; **0** required approvals.
- Required status checks: `lint`, `typecheck`, `test`, `secret-scan`, `dependency-audit`, `codeql (python)`, `codeql (actions)`, `ai-review`. Branch must be up to date before merge.
- Block force pushes and branch deletion; require linear history (squash merge).
- **Bypass:** repository admin (the maintainer) only, for emergencies.
- No other collaborators get write access; CODEOWNERS stays as documentation of sensitive paths.

## Consequences
- Every change to `main` is a PR with a green CI and an AI review on record, and only the maintainer can merge.
- Human second review is replaced by automated gates plus AI review (ADR-0019). Revisit when a second maintainer joins.
- Bypasses are visible in the ruleset's bypass log.
