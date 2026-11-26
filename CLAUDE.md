# Kalshi Uatu: rules for AI assistants and reviewers

This code places real-money orders. Design decisions live in `docs/adr/`; follow them, and propose a new ADR for any change to decided behavior.

## Non-negotiables
- Never read private keys from env vars, `.env`, CLI args, or config; only via `SecretProvider` (ADR-0007). Never log or serialize keys or signatures.
- The LLM layer gets no tools and no credentials (ADR-0005). Only `executor` signs and sends orders (ADR-0004).
- Every entry needs human approval; exits are reduce-only (ADR-0006, ADR-0009).
- Risk gates fail closed (ADR-0008). Demo is the default environment (ADR-0010).
- Money is integer cents or `Decimal`, never `float` (ADR-0003).
- Strategy files (`strategy/`, `config/strategy.toml`) never enter the repo (ADR-0002).

## Workflow
- Python 3.12, `uv`. Before pushing: `uv run ruff check && uv run ruff format --check && uv run mypy && uv run pytest --cov`.
- All changes go through a PR to `main`; CI and `ai-review` must pass (ADR-0017, ADR-0018).
- Pin GitHub Actions by full commit SHA; keep workflow permissions minimal.
