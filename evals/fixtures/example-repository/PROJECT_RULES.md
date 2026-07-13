# Project Rules

Authority is divided by question domain:

- `docs/authority.md` owns canonical terms and invariants.
- Accepted ADRs under `docs/decisions/` own architectural tradeoffs.
- Current code and tests describe implementation, but do not establish product promises by themselves.
- Reports prove only commands actually run, in the environment and snapshot they name.
- `docs/proof/claims.json` owns Claim status. Only `accepted` Claims may be treated as project-accepted conclusions.
- Specs and product-direction documents describe scope or targets until promoted.
- README is an entry point, not a source of current implementation truth.
