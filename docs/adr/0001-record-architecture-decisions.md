# ADR-0001: Record architecture decisions

- **Status:** Accepted
- **Date:** 2026-11-14

## Context
This project places real-money orders. Every design choice must be traceable and reviewable.

## Decision
Use lightweight ADRs (MADR-style) in `docs/adr/`, numbered sequentially, one decision per file.
Sections: Status, Context, Decision, Consequences. ADRs are immutable once accepted; changes are made by a new ADR that supersedes the old one.

## Consequences
- Design rationale lives next to the code and is versioned with it.
- A PR that changes a decided behavior must include a new or superseding ADR.
