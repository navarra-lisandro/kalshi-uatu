# ADR-0013: Append-only audit log in SQLite

- **Status:** Accepted
- **Date:** 2026-11-14

## Context
Every proposal, approval, order, fill, gate decision, and config override must be reconstructable after the fact.

## Decision
- Use local SQLite (WAL mode) with an append-only `events` table: `id, ts_utc, env, type, correlation_id, payload_json, prev_hash, hash`.
- Each row hashes the previous one, so tampering or deletion is detectable (`uatu audit verify`).
- One `correlation_id` links proposal → gate results → approval → order → fills → exit.
- No secrets or signatures are ever written (enforced by the same redaction filter as logging).
- Structured JSON logs go to stdout for future Datadog/CloudWatch shipping.

## Consequences
- Zero infrastructure for v1; the schema maps directly to Postgres/RDS when moving to AWS.
- P&L and daily-loss calculations read from this log, reconciled with exchange fills.
