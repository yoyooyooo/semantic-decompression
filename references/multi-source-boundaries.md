# Multi-source Boundaries

This is an optional supplement, not a repository workflow. Read it only when a load-bearing conclusion depends on several files, versions, snapshots, reports, or artifacts and their differences could change the explanation.

Do not load it merely because the input is a repository, a directory, or a long document set. Ordinary semantic decompression stays on the six-step process in `SKILL.md`.

## When This Reference Is Needed

Use it when at least one of these conditions holds:

- two sources make materially different claims about the same subject;
- current implementation, target design, proposal, and historical evidence can be confused;
- a report proves a past snapshot but the output could imply current verification;
- the requested conclusion is broader than the material that can actually be inspected or searched;
- one formal term changes meaning across sources in a way that affects the walkthrough.

The goal is modest: preserve the state, provenance, and scope that the sources actually support.

## 1. State Boundary

Classify only the states needed by the task:

| State | Meaning |
| --- | --- |
| Current | Supported as true for the relevant present snapshot. |
| Target | Intended future behavior or architecture. |
| Proposed | Suggested but not adopted or implemented. |
| Historical | True of a named earlier snapshot or event. |
| Unknown | Not established by the inspected material. |

Keep these distinctions visible when they affect the reader's decision:

```text
file exists != behavior is implemented
implementation exists != behavior is verified
static check passed != runtime behavior passed
proposal accepted != product delivered
historical report passed != current snapshot passed
```

Use the strongest available evidence without silently promoting it. When current verification is unavailable, state the strongest supported status and the missing check.

## 2. Source Boundary

For each load-bearing multi-source claim, keep a compact source pointer in the working notes. It can be a path, section, artifact, or named user-provided source. The final output needs visible citations or paths only when the user requests them or when traceability is necessary for trust.

When sources disagree:

1. State the disagreement rather than averaging it away.
2. Identify whether the sources address different scopes, times, or question types.
3. Follow a project-native authority rule only when the material explicitly defines one for that question.
4. Keep the conflict unresolved when the available material does not resolve it.

Do not invent a universal hierarchy such as “code always beats design” or “the newest file always wins.” Semantics, implementation, adopted decisions, tests, reports, and plans can each own different questions.

A report owns only what it actually observed. Record its snapshot, method, and limits before using it as evidence.

## 3. Coverage Boundary

Match the breadth of the conclusion to the breadth of the review. A minimal coverage note answers three questions:

- **Inspected:** which load-bearing sources were read closely;
- **Searched:** which wider scope was searched for conflicts, terms, or counterevidence;
- **Not covered:** which relevant areas were unavailable, out of scope, or sampled only.

One sentence is often enough. Use a longer coverage section only when the user requested an audit, review record, or research appendix.

Avoid claims such as “the repository does X” when only one design file was inspected. Prefer “the inspected design file defines X; current implementation was not checked.”

## Optional Term Mapping

Create a tiny term map only when the same term has conflicting local meanings that change the explanation. Record:

```text
term -> source scope -> local meaning -> nearest conflicting use
```

Do not build a full registry for stable vocabulary or as a default repository step.

## Integration with the Main Output

Keep the main narrative reader-first:

1. Give the smallest useful map.
2. Walk one representative path.
3. Attach state and source boundaries at the claims they qualify.
4. End with a compact coverage note when scope could otherwise be overstated.

Do not turn the output into an inventory of files or an internal audit appendix unless the user asked for that artifact.

## Completion Criterion

This reference is complete when no claim in the output has gained authority, freshness, or coverage that the inspected sources did not possess.
