# Eval Traceability

Each rule has one owner in `SKILL.md`. Evals reference rule IDs so maintenance can show which behavior a change is meant to affect.

| Rule ID | Source of truth | Failure mode | Primary evals |
| --- | --- | --- | --- |
| SD-R1 | Reader Contract | Wrong reader, task, form, or depth | `evals.json` 1, 2, 5, 7 |
| SD-R2 | Claim Ledger | Proposal, inference, or history promoted to fact | `evals.json` 2, 4, 6, 8; MS-1 |
| SD-R3 | Missing Bridges | More words without closing a comprehension gap | `evals.json` 1 to 6, 8 |
| SD-R4 | Walkable Route | Glossary or inventory replaces an end-to-end explanation | `evals.json` 1, 5, 7 |
| SD-R5 | Local Decompression | Template dumping, repetition, or invented examples | `evals.json` 1 to 5, 8 |
| SD-R6 | Reader Check | Output ends before the reader can act or state the boundary | all output evals |
| SD-MS1 | State Boundary | Current, target, proposed, historical, and unknown are mixed | MS-1 |
| SD-MS2 | Source Boundary | A source gains authority or freshness it does not have | MS-1, MS-2 |
| SD-MS3 | Coverage Boundary | Narrow reading becomes a repository-wide claim | MS-3 |

## Maintenance Rule

Add a runtime rule only when it replaces an existing rule, closes a failure reproduced by an eval, or introduces a real invocation branch. Every new rule must update this table and at least one eval. Merge or remove overlapping guidance in the same change.

Trigger evals test invocation. Output evals test behavior. Static checks test package integrity. Passing one layer does not imply the other two passed.
