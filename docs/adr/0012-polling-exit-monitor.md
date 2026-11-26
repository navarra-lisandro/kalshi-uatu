# ADR-0012: REST polling for the v1 exit monitor

- **Status:** Accepted
- **Date:** 2026-11-14

## Context
Exit rules need current best-bid prices for held positions. Prediction-market positions are not latency-sensitive at the millisecond level.

## Decision
- v1 polls the orderbook for each open position at a configurable interval (default 5s), within rate limits.
- Positions and fills are reconciled against the exchange on every cycle; the exchange is the source of truth, local state is a cache.
- The monitor runs as an `asyncio` loop inside the `uatu run` process, with a heartbeat log line per cycle.

## Consequences
- Simple, deterministic, and easy to test with a fake clock.
- Worst-case exit delay is one interval. If that proves too slow, a superseding ADR moves to the WebSocket feed behind the same `MarketDataSource` port.
