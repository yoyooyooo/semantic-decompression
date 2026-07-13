---
name: semantic-decompression
description: >-
  Use semantic decompression when dense expert material must become teachable without losing canonical terms, evidence, uncertainty, or causal structure. Trigger for newcomer explanations, companion guides, handoffs, or rewrites that need hidden premises, actors, state changes, distinctions, and one end-to-end path restored. Works for a passage, document, or a few related sources. Not for plain summarization, translation, copyediting, or code repair.
---

# Semantic Decompression

High-entropy material compresses more meaning than the reader's current context can recover. Restore the missing bridges so the reader can move continuously from their starting point to the source conclusion.

Default reader: intelligent, new to the local context, and missing the background that the author assumed.

## Outcome Contract

- **Outcome:** the reader can explain what is happening, why it happens, who acts, how the sequence runs, how certain each conclusion is, and where the boundaries are.
- **Done when:** the source meaning, canonical vocabulary, evidence strength, and uncertainty are preserved, and one representative path can be followed from trigger to result.
- **Evidence:** supplied material, cited sources, verified artifacts, and clearly marked assumptions or hypothetical examples.
- **Output:** the requested rewrite, explanation, companion guide, tutorial, or handoff. Internal ledgers stay internal unless the user asks to see them.

## Invariants

Keep these stable throughout the rewrite:

- facts, numbers, quotations, source attribution, and chronology;
- the source's actual conclusion and level of confidence;
- distinctions between fact, decision, proposal, assumption, inference, unknown, and action;
- canonical domain terms after their local meaning has been established;
- material disagreements, edge cases, costs, and uncertainty.

Missing information stays unknown. A useful explanation can state what is missing and why it matters. It cannot fill the gap with a plausible invention.

## Process

### 1. Lock the Reader Contract

Determine four things before expanding the material:

1. What the reader already knows.
2. What the reader must be able to do after reading.
3. Which output form the user requested.
4. How much scope and depth the task allows.

When the user gives no audience, use the default newcomer. When the user gives a strict length, preserve the claim ledger and the most load-bearing bridges before adding examples.

**Done when:** reader starting point, after-reading task, output form, and scope are explicit or deliberately defaulted.

### 2. Build the Claim Ledger

Classify every load-bearing statement as one of:

- **Fact:** directly supported by the material or verified artifact.
- **Decision:** an adopted choice, rule, or commitment.
- **Proposal:** a suggested future choice.
- **Assumption:** a premise the reasoning depends on.
- **Inference:** a conclusion derived from evidence rather than stated directly.
- **Unknown:** information the material does not establish.
- **Action:** a requested or recommended next step.

Keep the source's recognition state. A proposal remains proposed. A historical result remains historical. A local observation does not become a universal rule.

When one load-bearing conclusion depends on several files, versions, or reports and state, source, or coverage could change its meaning, read [`references/multi-source-boundaries.md`](references/multi-source-boundaries.md). Do not load that reference for ordinary single-source work or merely because the material is stored in a repository.

**Done when:** every load-bearing conclusion has a stable recognition state and no statement has gained certainty during rewriting.

### 3. Map the Missing Bridges

Find what the reader must currently guess. Common gaps include:

- local terminology and assumed background;
- hidden premises and omitted causal steps;
- actors, ownership, authority, and handoffs;
- sequence, state transitions, failure, recovery, and exit conditions;
- jumps between business, architecture, implementation, and user impact;
- missing baselines, denominators, time windows, or comparison classes;
- ambiguous references, compressed exceptions, and absent next actions.

For long, cross-domain, or hard-to-diagnose material, read only the relevant sections of [`references/decompression-lenses.md`](references/decompression-lenses.md).

**Done when:** every planned addition closes a named comprehension gap. Content that closes no gap is removed.

### 4. Design a Walkable Route

Prefer a natural route over a glossary or component inventory:

1. Start with the real situation the reader encounters.
2. Show the pressure, failure, or decision that makes the system necessary.
3. Give the smallest useful map of actors, objects, and relationships.
4. Follow one representative object from trigger to result.
5. Introduce each formal term where that walkthrough needs it.
6. Return to the map to explain alternatives, tradeoffs, boundaries, and important failure paths.
7. End with the decision, action, or reading path the user needs.

Use one through-line example when possible. Mark an invented example as hypothetical and never let it supply evidence for a factual claim.

**Done when:** one representative path includes its trigger, actors, state changes, result, and any failure or recovery branch that changes the reader's decision.

### 5. Decompress Locally

Add only the explanation needed at the current point.

For a **term**, explain its local role, why it exists, who uses it, where it appears in the flow, and what nearby concept it is often confused with.

For a **process**, restore trigger, actor, input, action or state change, output, next step, and relevant failure or recovery conditions.

For a **decision**, restore the problem, constraints, rejected alternatives, tradeoffs, assumptions, and evidence that would change the choice.

For an **argument**, restore claim, premises, intermediate reasoning, counterarguments, scope, and confidence.

For **data**, restore measure, denominator, baseline, sample, time window, uncertainty, and practical consequence.

For a **policy or rule**, restore who triggers it, who decides, deadlines, state changes, exceptions, remedies, and what the affected person should do.

Introduce canonical vocabulary after plain-language grounding, then continue using the canonical term. Keep examples concrete, bounded, and subordinate to the source.

**Done when:** each paragraph contributes a new bridge, distinction, example, or boundary. It does not restate the preceding paragraph in different words.

### 6. Run the Reader Check

Before delivery, test whether the intended reader can answer:

- What is this and why does it exist?
- Who acts, owns, decides, approves, executes, or observes?
- What happens first, next, and last?
- Which states or concepts must remain distinct?
- Which claims are established, proposed, inferred, assumed, or unknown?
- What fails, what recovers, and where does the explanation stop?
- What should the reader do or read next?

Then compare the output with the source. Confirm that terms, numbers, chronology, conclusion, evidence strength, and uncertainty have not drifted.

**Done when:** the reader can traverse the explanation without guessing a load-bearing bridge, and the output makes no stronger claim than the source supports.

## Output Shapes

Match the user's requested artifact:

- **Rewrite:** return the rewritten material and preserve the original conclusion and useful structure.
- **Companion guide:** keep the source intact and add a separate map, walkthrough, distinctions, and boundaries.
- **From-zero tutorial:** establish the global model before local detail and keep one example running through the explanation.
- **Handoff:** add ownership, maintenance entry points, failure paths, current unknowns, and next actions.
- **Length-constrained answer:** keep the conclusion, recognition state, and key bridge; reduce the number of examples before cutting boundaries.

Do not expose the Reader Contract, Claim Ledger, or Bridge Map as a template unless the user asks for the analysis itself.

## Reference Loading

- Read [`references/decompression-lenses.md`](references/decompression-lenses.md) only when a named comprehension gap needs a diagnostic lens or technique.
- Read [`references/multi-source-boundaries.md`](references/multi-source-boundaries.md) only when multiple sources materially affect state, provenance, or coverage.

The main process remains the source of truth. References supply branch-specific detail and do not define a second workflow.
