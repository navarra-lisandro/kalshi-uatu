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
- The action only runs when `ai-review.yml` on the PR is identical to `main`, so a PR cannot rewrite its own reviewer. When it skips, it still exits 0, so a final step fails the job unless a bot review comment was posted during the run. PRs that change `ai-review.yml` therefore always fail `ai-review` and are merged via maintainer bypass after manual review.
- Triggered on `pull_request` (never `pull_request_target`), so fork PRs receive no secrets; the job is skipped for forks and drafts.
- Chosen over Devin because it runs inside our own workflow, under our pinned version, permissions, and prompt, and is versioned in the repo.

## Consequences
- Every PR gets a documented second opinion focused on the project's real risks.
- If the token expires, `ai-review` fails and blocks merges until it is renewed (or the maintainer bypasses).
- Changes to the reviewer itself are always human-reviewed, which is the right place for that trust boundary.
- Fork contributions get no AI review until a maintainer re-opens them from a branch in this repo.
