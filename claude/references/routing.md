# Local Claude routing policy

This is a user preference snapshot, not a claim that every host exposes these models. Confirm with the installed Claude CLI or host before dispatch.

## Model preference

1. Prefer **Fable** for orchestration, ambiguous architecture/product judgment, difficult research or writing, and multi-lane synthesis.
2. Use **Opus** selectively for an independent Claude-family view or deep single-lane analysis when available and useful.
3. Do not route this user's delegated work to Sonnet or Haiku. Use an appropriate Codex tier for cheaper mechanical work instead.

## Effort preference

- `low`: obvious and tightly bounded.
- `medium`: normal consultation or clear implementation.
- `high`: obscure behavior, architecture, or difficult diagnosis.
- `xhigh`: competing hypotheses or unfamiliar cross-system work.
- `max`: exceptional quality-first work with consequential uncertainty.

Prefer a clearer brief over higher effort. If a requested model/effort combination is unsupported, report the mismatch and choose the nearest policy-consistent option rather than silently substituting.
