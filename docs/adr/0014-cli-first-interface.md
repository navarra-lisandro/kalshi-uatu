# ADR-0014: CLI-first interface with Typer and Rich

- **Status:** Accepted
- **Date:** 2026-11-14

## Context
The engine and safety model must be correct before investing in a UI. Approval still needs a clear, readable prompt.

## Decision
- Build a `uatu` CLI with `Typer`, rendering proposals and positions with `Rich`.
- Commands: `propose`, `run` (exit monitor), `positions`, `kill`, `secrets set`, `audit verify`, `config show`.
- The CLI is a thin adapter over application services, so a future UI calls the same services.

## Consequences
- Fast iteration on core logic.
- A later UI ADR adds an API adapter without changing the domain or execution layers.
