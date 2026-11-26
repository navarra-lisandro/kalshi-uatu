# ADR-0011: Thin in-house Kalshi client behind an `ExchangeGateway` port

- **Status:** Accepted
- **Date:** 2026-11-14

## Context
We need a small set of endpoints: markets, orderbook, balance, positions, create/cancel order, fills. Signing code handles the most sensitive secret.

## Decision
- Implement a typed client on `httpx` (async) behind an `ExchangeGateway` protocol.
- Signing: RSA-PSS over `timestamp + METHOD + path` with SHA-256, using `cryptography`. Lives in one module, ~50 lines, 100% test coverage.
- Every order carries a deterministic `client_order_id` derived from the approval hash, so retries are idempotent and can't double-submit.
- Retries with exponential backoff only on idempotent reads and on order creates that carry a `client_order_id`. Respect rate limits.
- Response payloads are parsed into pydantic models. Unknown or invalid responses fail closed.
- Contract tests run against the demo environment in a dedicated CI job (manual trigger, demo keys only).

## Consequences
- Full control and auditability of signing and logging; no third-party code touches the private key.
- We own keeping up with API changes, mitigated by the small surface and demo contract tests.
- An `InMemoryGateway` fake lets the whole system be tested offline.
