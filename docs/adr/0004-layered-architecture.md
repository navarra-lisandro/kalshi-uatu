# ADR-0004: Layered architecture with an isolated execution core

- **Status:** Accepted
- **Date:** 2026-11-14

## Context
An LLM generates trade ideas, but money must only move through deterministic, auditable code.

## Decision
Five layers, with dependencies pointing only inward:

```
Proposer (LLM) ─▶ RiskGate ─▶ Approval (human) ─▶ Executor ─▶ Kalshi
                                                     ▲
                              ExitMonitor ───────────┘ (reduce-only)
```

| Layer | Responsibility | Has credentials? |
|---|---|---|
| `proposer` | Turns thesis + market data into a typed `TradeProposal`. | No (read-only market data only) |
| `risk` | Validates a proposal or exit against configured gates. Pure functions. | No |
| `approval` | Shows the proposal to the human; records the decision. | No |
| `executor` | Signs and sends orders. Only module that imports the signer. | Yes |
| `exits` | Watches open positions; emits reduce-only exit intents. | No |

The `domain` package holds immutable pydantic models shared by all layers. Ports (`Protocol` classes) decouple layers from the exchange and secret store.

## Consequences
- An LLM bug, hallucination, or prompt injection cannot place an order; it can only produce a proposal that still must pass risk checks and human approval.
- The executor is small enough to review line by line.
- An import-linter contract in CI enforces the dependency direction.
