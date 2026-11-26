# ADR-0010: Demo environment by default; production is opt-in

- **Status:** Accepted
- **Date:** 2026-11-14

## Context
Kalshi provides a demo environment with separate credentials and endpoints. Accidentally hitting production is the costliest possible mistake.

## Decision
- Default environment is `demo`. Production requires both `--env prod` **and** the config field `allow_production = true`.
- On production startup the CLI prints the account balance and active risk gates, and requires the user to type `PROD` to continue.
- Base URLs are configuration, not constants, because Kalshi has changed hostnames over time.
- The environment is part of every audit record and every keychain entry name.

## Consequences
- A missing flag or config results in demo trading, never production.
- New strategies are validated on demo first.
