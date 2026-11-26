# ADR-0015: Repository and supply-chain security controls

- **Status:** Accepted; "Code review" clause amended by ADR-0017
- **Date:** 2026-11-14

## Context
The repo is public (ADR-0002) and the code handles signing keys and money.

## Decision
- **Leak prevention:** `gitleaks` pre-commit hook and CI job; GitHub secret scanning with push protection; `.gitignore` blocks `*.pem`, `*.key`, `.env*`, `strategy/`, `config/strategy.toml`, `*.db`.
- **Dependencies:** `uv.lock` committed; Dependabot for pip and GitHub Actions; `pip-audit` in CI.
- **CI:** GitHub Actions pinned by commit SHA; least-privilege `permissions:`; no secrets available to PR workflows.
- **Code review:** branch protection on `main` (PR required, CI green); `CODEOWNERS` requires owner review for `executor/`, `risk/`, and `secrets/`.
- **Static analysis:** `ruff` security rules (`S`, bandit-equivalent) enabled.
- **Disclosure:** `SECURITY.md` with a private reporting channel.

## Consequences
- A leaked key or strategy file is blocked at commit, push, and CI.
- Changes to money-moving code always get explicit review.
