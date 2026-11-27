# ADR-0002: Public engine, private strategy configuration

- **Status:** Accepted; storage extended by ADR-0020
- **Date:** 2026-11-14

## Context
The repo should serve as a public portfolio piece. The trading edge (thresholds, prompts, market filters, theses) must not be published.

## Decision
- The repository is **public** and contains only the engine, risk framework, and safe defaults.
- Strategy material lives in a **gitignored** local directory (`strategy/`) and a local `config/strategy.toml`. The repo ships `config/strategy.example.toml` only.
- Prompts are loaded from the strategy directory at runtime; the repo ships a generic example prompt.

## Consequences
- Anyone can run the engine; nobody gets the strategy.
- Requires secret/strategy leak controls (ADR-0015).
- Strategy config can later move to a private companion repo without code changes.
