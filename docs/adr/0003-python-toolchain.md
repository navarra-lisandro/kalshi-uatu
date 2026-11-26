# ADR-0003: Python 3.12 and toolchain

- **Status:** Accepted
- **Date:** 2026-11-14

## Context
Code must be clean, pythonic, and safe to change. Errors in types or units (cents vs. dollars) carry monetary risk.

## Decision
| Concern | Choice | Why |
|---|---|---|
| Runtime | Python 3.12 | Mature typing, broad library support. |
| Packaging | `uv` + `pyproject.toml` + committed `uv.lock` | Fast, reproducible, hash-pinned installs. |
| Lint/format | `ruff` (lint + format) | Single tool, PEP 8 enforced. |
| Types | `mypy --strict` | Catch unit/shape errors before runtime. |
| Models/config | `pydantic` v2 + `pydantic-settings` | Validated, immutable domain models and config. |
| Tests | `pytest`, `pytest-asyncio`, `hypothesis`, `respx` | Property tests for risk math; HTTP mocking for the exchange. |
| Money | `decimal.Decimal` / integer cents only | No floats in any price, size, or P&L path. |

## Consequences
- CI fails on lint, type, or test errors.
- All monetary values use an explicit `Cents` type; mixing units is a type error.
