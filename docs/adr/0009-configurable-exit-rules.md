# ADR-0009: Configurable exit rules

- **Status:** Accepted
- **Date:** 2026-11-14

## Context
The core goal is to exit after a user-adjustable gain. The user also wants a stop-loss and a time-based exit, each switchable.

## Decision
Three independent rules, each with an `enabled` flag and threshold, set globally and overridable per position at approval:

| Rule | Config key | Fires when |
|---|---|---|
| Take-profit | `exits.take_profit_pct` | Best bid ≥ entry × (1 + pct) |
| Stop-loss | `exits.stop_loss_pct` | Best bid ≤ entry × (1 − pct) |
| Time exit | `exits.time_before_close` | Now ≥ market close − duration |

- With all rules disabled, the position is held to settlement. "Take-profit only" is just a config preset.
- Triggers evaluate against the **best bid** (the realizable exit price), not last trade.
- Exit orders are `reduce_only` limit sells for the full held quantity at the best bid. Unfilled orders are re-priced on the next tick, up to a configurable maximum number of attempts.
- The first rule to fire wins. Exit intents still pass through the risk layer (exits are allowed even when the kill switch or daily-loss gate halts entries).

## Consequences
- Exits cannot increase exposure.
- Percentages are computed in integer cents with explicit rounding (toward the conservative side).
