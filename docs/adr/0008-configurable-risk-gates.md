# ADR-0008: Configurable, fail-closed risk gates

- **Status:** Accepted
- **Date:** 2026-11-14

## Context
Risk limits must be enforced in code, never by the LLM. The user wants each gate switchable and its threshold adjustable.

## Decision
Each gate is a pure function `check(intent, state, cfg) -> GateResult` with an `enabled` flag and threshold in config:

| Gate | Config key | Blocks when |
|---|---|---|
| Max cost per order | `risk.max_order_cost` | Order max cost > threshold |
| Max daily loss | `risk.max_daily_loss` | Realized loss today ≥ threshold → halt new entries |
| Max open exposure | `risk.max_open_exposure` | Current + new exposure > threshold |
| Kill switch | `risk.kill_switch` | Engaged → cancel all resting orders, halt entries |

Overrides follow config file → CLI flags (`--max-order-cost 2500`, `--no-max-daily-loss`), with CLI taking precedence for that run only.

**Invariants (not configurable):**
- Limit orders only, and entries set `buy_max_cost` equal to the approved max cost.
- Fail closed: if a gate cannot evaluate (missing data, API error), the intent is rejected.
- Disabling any gate in **production** requires typed confirmation at startup and is written to the audit log.
- The kill switch command (`uatu kill`) is always available, even when the gate is disabled.

## Consequences
- The user controls risk posture per run without editing code.
- Gates are pure functions and are property-tested (ADR-0003).
- Gate results are attached to every proposal shown at approval time.
