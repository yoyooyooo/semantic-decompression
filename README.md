[中文](README_ZH.md) | **English**

# Semantic Decompression

Semantic Decompression turns dense expert material into an explanation a newcomer can follow, retell, and continue working from. It preserves canonical terms, facts, source status, and evidence limits.

It handles two main situations:

- A passage or document compresses too many assumptions, terms, causal links, and process steps.
- A repository or material pack contains semantic authorities, ADRs, code, specs, reports, claims, roadmaps, and stale entry points that each prove different things.

## How it differs from nearby tasks

| Task | Primary goal |
| --- | --- |
| Summarization | Reduce information volume |
| Translation | Change language |
| Polishing | Improve the surface of the prose |
| Glossary | Define terms independently |
| Semantic decompression | Restore omitted context, relationships, process, and limits |

A decompressed explanation may be long or short. Its length follows the reader's missing bridges, not a target word count.

## The agent workflow

`SKILL.md` keeps only the six steps shared by every branch:

```text
Lock the reader contract
  -> build the truth ledger
  -> locate missing bridges
  -> choose a walkable route
  -> decompress at the point of need
  -> deliver and verify
```

Every step has a checkable completion criterion. Domain diagnostics and repository rules live in references loaded only when their branch applies.

## Two branches

### Single source

The default route is map, walkthrough, return. Give the smallest useful overview, carry one running example through the full chain, then return to the important distinctions, limits, and next action.

This branch works for architecture notes, research abstracts, strategy material, policies, arguments, metric reviews, and process documents.

### Repository and Corpus Mode

When the task spans a repository, archive, multiple documents, snapshots, or conflicting sources, the skill loads [`references/repository-corpus-mode.md`](references/repository-corpus-mode.md) and adds:

- a Coverage Contract that states what was read, searched, sampled, and left uncovered;
- Authority discovered by question domain rather than a universal file ranking;
- a Source Ledger for provenance, freshness, conflicts, and claim ceilings;
- a Current-State Gate that separates artifact presence, implementation, observed verification, accepted claims, and delivered capability;
- a Term Registry that preserves canonical names, aliases, definition owners, and scope.

Repository onboarding output uses four layers:

```text
one-screen map
  -> one real route
  -> current facts versus target state
  -> authorities, open questions, and next work
```

## Examples

```text
This architecture RFC is too compressed. Keep Candidate, owner, and canonical,
then explain authority, state transitions, and recovery through one real request.
```

```text
Write onboarding material from this repository. The README, spec, and report conflict.
First determine what each source can prove, then explain current state and the next entry point.
```

```text
Explain this paper result to a new graduate student. Build intuition first,
then state the statistical meaning, evidence ceiling, and unsupported conclusions.
```

## Installation

Place the extracted `semantic-decompression/` directory in your client's Skills directory. Keep `SKILL.md` and `references/` at their existing relative paths.

Expected structure:

```text
semantic-decompression/
├── SKILL.md
├── README.md
├── README_ZH.md
├── VERSION
├── LICENSE
├── CHANGELOG.md
├── references/
│   ├── decompression-lenses.md
│   └── repository-corpus-mode.md
└── evals/
    ├── evals.json
    ├── repository-evals.json
    ├── trigger-eval.json
    └── fixtures/example-repository/
```

## Evaluation assets

The package includes:

- 8 single-document quality evals;
- 4 repository-level evals;
- 27 trigger-boundary cases;
- one fully synthetic repository fixture.

The fixture intentionally contains a stale README, future product direction, a static report, a missing validation path, a dirty snapshot, and an unaccepted claim. It tests whether an agent produces fluent prose that exceeds the evidence. No real test material or user project content is included.

## What changed in 0.2.1

Version 0.2.0 added repository-level reliability, but the agent entry point grew with it. Version 0.2.1 restores the information hierarchy:

- `SKILL.md` contains shared steps, branch selection, and completion criteria.
- Repository-specific Authority, Coverage, Source Ledger, Current-State Gate, and Term Registry rules have one home in their reference.
- General domain lenses remain in a separate reference.
- The README explains the project to people without becoming a second runtime rule set.

No capability was removed. The default context is smaller and every branch has a clearer single source of truth.

## Limits

This skill improves understanding. It does not replace legal, medical, financial, or security expertise. It is not an automatic full-repository auditor, and verification strength remains bounded by the available environment, tools, and actual coverage.

## License

MIT
