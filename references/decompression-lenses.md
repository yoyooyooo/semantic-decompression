# Semantic Decompression Lenses

Use this file as a diagnostic catalog, not a checklist. Read only the sections that match a named comprehension gap. The six-step process in `SKILL.md` remains the workflow.

## Twelve Common Sources of Compression

### 1. Terminology

**Signal:** the reader recognizes the word but not its local meaning, owner, lifecycle, or boundary.

**Restore:** plain meaning, local definition, role in the current flow, nearby distinctions, and one bounded example. Continue with the canonical term after grounding it.

### 2. Background

**Signal:** the material assumes the reader knows the earlier problem, decision, or constraint.

**Restore:** only the history that changes interpretation: the original pressure, important turn, adopted choice, and remaining constraint.

### 3. Causality

**Signal:** the material gives A and C but skips how A produces C.

**Restore:** the intermediate mechanism, necessary conditions, evidence, and plausible alternative causes.

### 4. Relationships

**Signal:** components, views, or metrics are listed without dependencies, constraints, ownership, or information flow.

**Restore:** a small map and an end-to-end walkthrough that turns the list into a connected system.

### 5. Actors and Authority

**Signal:** passive phrases such as “is accepted” or “the system decides” hide who can act.

**Restore:** proposer, owner, approver, executor, observer, and the difference between requesting a change and making it effective.

### 6. Time and State

**Signal:** current state, target state, transitions, versions, and event order share one paragraph.

**Restore:** before, trigger, in progress, after, terminal or recovery state, and the conditions for entering and leaving each state.

### 7. Abstraction Level

**Signal:** a sentence jumps from business goal to architecture rule to function or field.

**Restore:** connect one level at a time: goal requires capability, capability shapes architecture, architecture constrains implementation, implementation changes user behavior.

### 8. Recognition State

**Signal:** fact, decision, proposal, hypothesis, inference, and speculation use the same confident voice.

**Restore:** label the recognition state and state what supports it.

### 9. Quantity

**Signal:** a percentage, score, cost, or trend lacks a denominator, baseline, sample, unit, or time window.

**Restore:** what was measured, against what, over which period, with what uncertainty, and what the change means for a decision.

### 10. Reference

**Signal:** “it,” “this,” “the former,” or “the mechanism” has several possible antecedents.

**Restore:** repeat the real object name at load-bearing points. Local repetition costs less than ambiguity.

### 11. Exceptions

**Signal:** the normal path is clear but permissions, failures, cancellation, recovery, or scope limits are hidden in a note.

**Restore:** explain the normal path first, then place each behavior-changing exception next to the step it changes.

### 12. Action

**Signal:** the reader understands the material but cannot tell what to decide, maintain, inspect, or do next.

**Restore:** decision effect, maintenance entry point, investigation order, next action, or the most useful source to read next.

## Six Techniques

### Map, Walkthrough, Return

Give the smallest useful map, follow one concrete case through the system, then return to the map to explain abstractions, tradeoffs, and limits.

### Through-line Example

Choose one example that activates most core concepts without becoming a second problem to learn. Reuse it when new terms appear.

### Terminology Grounding

At first use, state what the formal term does here. Explain why it exists, who uses it, where it enters the flow, and how it differs from its nearest neighbor. Then use the formal term consistently.

### Paired Contrast

Explain easily confused concepts together: what each solves, when each occurs, who owns each, and which mistake follows from treating them as interchangeable.

### State Ladder

For lifecycles, approvals, tasks, and runtime behavior, show entry condition, allowed actions, exit condition, failure, and recovery for each state. Add one sentence about the human meaning of the state.

### Recognition Labels

Use direct phrases such as “the source establishes,” “the team decided,” “the document proposes,” “this explanation infers,” and “the available material does not show.” Apply labels where confusion would change a decision, not to every sentence.

## Stop Rule

Stop expanding when the reader can traverse the load-bearing route without guessing. Extra definitions, examples, history, or analogies that close no remaining gap are compression in reverse and should be removed.
