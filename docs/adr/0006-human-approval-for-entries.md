# ADR-0006: Human approval required for every entry; exits are automatic

- **Status:** Accepted
- **Date:** 2026-11-14

## Context
The user approves every LLM-proposed trade. Exits must fire without waiting for a human, or the take-profit/stop-loss logic is useless.

## Decision
- **Entries:** every entry order requires an explicit CLI approval showing ticker, side, limit price, count, max cost, and which risk gates passed. The default answer is *reject*. There is no flag to bypass approval.
- **Exits:** run automatically, but only as `reduce_only` limit orders sized to at most the currently held position (ADR-0009).
- Each approval is bound to a hash of the exact proposal. Any change (price, size) invalidates it.
- Approvals expire after a configurable TTL (default 60s), so stale prices are never executed.

## Consequences
- The bot can never open or increase exposure without the user present.
- Automatic exits can only reduce risk, never add it.
