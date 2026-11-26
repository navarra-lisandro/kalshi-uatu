# ADR-0005: LangChain for the proposal layer only, provider-agnostic

- **Status:** Accepted
- **Date:** 2026-11-14

## Context
Entries are proposed by an LLM from the user's thesis and Kalshi market data. The provider should be swappable.

## Decision
- Use LangChain's `BaseChatModel` interface with `with_structured_output(TradeProposal)`. The provider is selected via config (`init_chat_model`), so Anthropic, OpenAI, etc. are interchangeable.
- The LLM receives **only**: the user's thesis text and a pre-fetched snapshot of candidate markets (ticker, prices, volume, close time). It is given **no tools**.
- Output is validated against the `TradeProposal` schema. Anything invalid is discarded and logged, never repaired by guessing.
- The prompt is loaded from the private strategy directory (ADR-0002).
- LLM API keys use the same `SecretProvider` as Kalshi keys (ADR-0007).

## Consequences
- LangChain adds value here: provider abstraction and structured output. It is not used anywhere else.
- No tools means no agent loop and no side effects, so there is no path from the model to the order API.
- Market data is fetched by deterministic code before the LLM call, which keeps runs reproducible and auditable.
