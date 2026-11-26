# ADR-0019: AI pull-request review with Claude Code Action

- **Status:** Accepted
- **Date:** 2026-11-26

## Context
With one maintainer (ADR-0017), a second reviewer is valuable, especially for secret handling and order-safety code. Candidates: Claude Code GitHub Action, Devin.

## Decision
- Use `anthropics/claude-code-action`, authenticated with the maintainer's Claude subscription via the `CLAUDE_CODE_OAUTH_TOKEN` repository secret (no per-token API billing).
- The reviewer is **read-only and advisory**: tools limited to reading files and `gh pr diff/view/comment`; it posts one comment and never approves, requests changes, pushes, or merges.
- The prompt ranks review priorities to match this project's risks: secrets, order safety, money correctness, CI supply chain, then code quality, and checks changes against accepted ADRs.
- `ai-review` is a **required check that verifies the review ran**, not that the model liked the change. LLM verdicts are non-deterministic and must not gate merges on their own (same principle as ADR-0005).
- Triggered on `pull_request` (never `pull_request_target`), so fork PRs receive no secrets; the job is skipped for forks and drafts.
- Chosen over Devin because it runs inside our own workflow, under our pinned version, permissions, and prompt, and is versioned in the repo.

## Consequences
- Every PR gets a documented second opinion focused on the project's real risks.
- If the token expires, `ai-review` fails and blocks merges until it is renewed (or the maintainer bypasses).
- Fork contributions get no AI review until a maintainer re-opens them from a branch in this repo.
