# ADR-0020: Private strategy companion repository

- **Status:** Accepted (extends ADR-0002)
- **Date:** 2026-11-27

## Context
ADR-0002 keeps strategy material out of the public repo via `.gitignore`. That leaves it unversioned and unbacked-up on one laptop, and gitignore alone does not stop `git add -f`.

## Decision
- Strategy material (`strategy/` prompts, theses, filters, and `strategy/strategy.toml`) lives in a **private** repo, `kalshi-uatu-strategy`, cloned into the gitignored `strategy/` directory of the public checkout.
- The engine reads config from `strategy/strategy.toml` when present, falling back to `config/strategy.toml`.
- CI fails if any private path (`strategy/`, `config/strategy.toml`, `*.pem`, `*.key`, `*.db`) appears anywhere in the public repo's history.
- Public surfaces stay strategy-free: CI logs never print strategy contents; commit messages, PRs, issues, and review comments describe changes generically.
- `config/strategy.example.toml` holds neutral placeholder values only.

## Consequences
- Strategy changes get history and backup without ever touching the public repo.
- Two repos to keep in sync locally; acceptable for the separation it buys.
- A leak caught by CI after push means the public history is already exposed; the guard is a backstop, and push protection plus pre-commit hooks are the first line.
