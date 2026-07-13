<p align="center">
  <strong>English</strong> · <a href="README.zh.md">简体中文</a>
</p>

# Semantic Decompression

Some material is hard even when every word is familiar. The reader still cannot tell who decides, how state changes, which premise supports a conclusion, or whether a statement describes current reality or a future plan.

Semantic Decompression restores those missing bridges while preserving canonical terms, facts, evidence strength, and uncertainty.

## A minimal example

Compressed:

> The statutory review period starts after substantive completeness, and requests for additional material stop the clock.

Decompressed:

> Receiving an application does not start the statutory review period. The agency first decides whether the submission is complete enough for formal review. The clock starts only after that decision. If the agency later requests material needed for review, the clock pauses until the response is received and accepted. The reader therefore needs to distinguish submitted, accepted as complete, and under formal review.

The rewrite keeps the formal rule. It adds the states, trigger, and practical consequence that the original sentence assumed.

## Good fits

- Explain architecture, decisions, research, policy, or dense arguments to a newcomer.
- Turn term-heavy material into a companion guide, handoff, or from-zero tutorial.
- Restore actors, causes, state changes, premises, exceptions, and an end-to-end flow.
- Rewrite for a non-specialist without erasing canonical vocabulary or evidence boundaries.

This is different from summarization, translation, copyediting, and a glossary. Those tasks reduce, convert, polish, or define. Semantic decompression restores the connections between concepts.

## How it works

The Skill uses a six-step process: lock the reader contract, build a claim ledger, locate missing bridges, design a walkable route, decompress locally, and run a reader check. The complete operating procedure lives in [`SKILL.md`](SKILL.md); the README does not maintain a second copy.

A typical output does three things:

1. Preserves the source conclusion and its evidence boundary.
2. Walks one representative object from trigger to result.
3. Introduces formal terms where the real flow needs them instead of front-loading a glossary.

## Multiple sources

Several files, versions, or historical reports can change the status, source, or scope of a conclusion. In those cases, the Skill may read [`references/multi-source-boundaries.md`](references/multi-source-boundaries.md) and apply three narrow safeguards:

- Keep current, target, proposed, historical, and unknown states separate.
- Keep load-bearing claims traceable to supporting sources and preserve conflicts.
- Keep the breadth of the conclusion within the material actually inspected or searched.

This is an evidence boundary, not a repository audit workflow. Material does not trigger an exhaustive inventory, authority ladder, term registry, or full-repository review merely because it lives in a repository.

## Example requests

Single document:

> Explain this architecture to a new teammate. Keep Candidate, accepted frontier, and canonical Utterance, but restore who has authority, how one request runs, and what recovery looks like after a crash.

Decision material:

> Do more than expand NRR, ICP, and CAC payback. Explain what each metric constrains in this decision, how they interact, and which tradeoffs the strategy accepts.

Multiple sources:

> Build a handoff from these design notes, current-state files, and historical reports. Separate verified capability, current scaffolding, target state, and unknowns, then state what you actually covered.

## Installation

Place the entire `semantic-decompression` directory in the Skills directory supported by your host. Keep the references, evals, and scripts with `SKILL.md`.

The Skill remains model-invoked. Natural requests for explanation, onboarding, companion guidance, or a from-zero walkthrough are enough.

## Package layout

```text
semantic-decompression/
  SKILL.md
  README.md
  README_EN.md
  VERSION
  CHANGELOG.md
  references/
    decompression-lenses.md
    multi-source-boundaries.md
  evals/
    evals.json
    trigger-eval.json
    multi-source-evals.json
    fixtures/example-corpus/
  scripts/
    check.py
    check.sh
```

`decompression-lenses.md` is a diagnostic catalog. Read only the sections needed for the current gap. `multi-source-boundaries.md` is a narrow supplement used only when multiple sources materially change the conclusion.

## Validation

Run the static checks with:

```bash
bash scripts/check.sh
```

The checker covers front matter, JSON, referenced fixture files, relative Markdown links, bilingual entry links, stale filenames, private machine paths, and dash characters.

The evals have three roles:

- `evals.json` checks reader fit, claim state, missing bridges, a walkable route, and preserved boundaries.
- `trigger-eval.json` separates this Skill from summarization, translation, polishing, code repair, and ordinary repository work.
- `multi-source-evals.json` tests state, source, and coverage boundaries without turning the Skill into a repository auditor.

## Limits

Semantic decompression can only reconstruct the model supported by the supplied material and available tools. It does not invent missing facts or promote a historical check into current verification. High-risk legal, medical, financial, and security conclusions still require the relevant professional judgment.
