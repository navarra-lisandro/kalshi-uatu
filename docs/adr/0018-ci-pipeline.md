# ADR-0018: CI pipeline on GitHub Actions

- **Status:** Accepted
- **Date:** 2026-11-26

## Context
ADR-0003 and ADR-0015 define quality and security gates. They need to run on every PR and on `main`.

## Decision
Three workflows:

| Workflow | Jobs | Trigger |
|---|---|---|
| `ci.yml` | `lint` (ruff check + format), `typecheck` (mypy strict), `test` (pytest, coverage ≥ 90%), `secret-scan` (gitleaks, full history), `dependency-audit` (pip-audit on the exported `uv.lock`, hash-verified) | PR, push to `main` |
| `codeql.yml` | `codeql (python)`, `codeql (actions)` with `security-extended` queries | PR, push to `main`, weekly |
| `ai-review.yml` | `ai-review` (ADR-0019) | PR |

Hardening rules for every workflow:
- Third-party actions pinned by **full commit SHA** with the version in a comment; Dependabot bumps them weekly.
- `permissions` default to `contents: read`; jobs request only what they need.
- `actions/checkout` with `persist-credentials: false`.
- `concurrency` cancels superseded runs; every job has a `timeout-minutes`.
- `uv sync --locked`: CI fails if `uv.lock` is out of date.
- Python version comes from `.python-version` (3.12), so local and CI match.

## Consequences
- Jobs are parallel and independent, so a failure points straight at one gate.
- Each job name is a stable required-check name in the ruleset (ADR-0017); renaming a job requires a ruleset update.
