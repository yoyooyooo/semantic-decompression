# Semantic Decompression Lenses

Consult only the sections that help a specific comprehension gap. These are diagnostic questions, not facts to supply or a checklist to print. The six moves in `SKILL.md` remain the workflow. Skip irrelevant dimensions; mark unsupported details as unknown.

## Terminology

**Signal:** a familiar word has an unfamiliar local role.

**Restore:** the role, nearest confusing concept, and a bounded example when useful. Introduce the formal term at the point of need and then retain it. Do not invent an owner or lifecycle for every abstract concept.

## Background

**Signal:** an earlier problem, choice, or constraint is silently assumed.

**Restore:** only the history needed to understand the present statement. Distinguish source history from general background.

## Causality

**Signal:** the material jumps from A to C.

**Restore:** the supported mechanism or premise connecting them, conditions, and relevant alternative explanations. When the mechanism is absent, say what relationship is observed and what causal inference remains unproven.

## Relationships

**Signal:** an inventory of components or metrics hides their interactions.

**Restore:** the dependencies, ownership, constraints, or information flow relevant to the reader. A small map followed by one case often helps.

## Actors and Authority

**Signal:** passive wording hides who requests, decides, approves, executes, or observes.

**Restore:** the named roles and the distinction between proposing a change and making it effective. Identify an unspecified decision-maker as unspecified; do not silently appoint one.

## Time and State

**Signal:** present capability, future intent, event order, or recovery is mixed together.

**Restore:** the relevant before-and-after conditions, transitions, and limits. Existence of a state does not establish its persistence, retry behavior, or recovery guarantees.

## Abstraction Level

**Signal:** a sentence jumps between a business goal, an architecture rule, and an implementation detail.

**Restore:** the connection between adjacent levels that the source supports. Do not derive an implementation from a goal as though it already exists.

## Claim Status

**Signal:** observations, decisions, proposals, and inferences share one confident voice.

**Restore:** what is established, who adopted a decision, what is merely proposed, and what remains unknown. Label at consequential points rather than mechanically prefixing every sentence.

## Quantity

**Signal:** a percentage, score, cost, or trend has no comparison frame.

**Restore:** the measure, unit, denominator, baseline, sample, time window, and uncertainty that are available. Explain the consequence of missing fields. Never substitute invented numbers for missing evidence.

## Reference

**Signal:** “it,” “this,” or “the mechanism” has several plausible meanings.

**Restore:** the actual object name at points where ambiguity matters. Useful local repetition is better than an unclear pronoun.

## Exceptions

**Signal:** permissions, failures, cancellation, or scope restrictions alter the normal story.

**Restore:** the relevant exception next to the step or claim it qualifies. Do not add a generic risk checklist to an otherwise bounded explanation.

## Action

**Signal:** the requested handoff or decision guide leaves the reader unable to act.

**Restore:** the supported owner, maintenance entry point, next check, or decision consequence. A conceptual explanation does not automatically need a follow-up task.

## Techniques

**Map, walkthrough, return:** orient the reader, follow one supported case, then explain the limits. Best for processes and systems.

**Through-line example:** reuse one bounded example when it saves the reader from learning several scenarios. Mark hypothetical details at introduction; they are not evidence about the real system.

**Paired contrast:** explain two easily confused concepts together, including the practical mistake caused by merging them.

**State ladder:** show entry, change, exit, and relevant recovery only when lifecycle is the actual gap. Preserve unknown transitions.

**Premise bridge:** for an argument, connect premises to the conclusion and expose the extra assumption required by a disputed step. Do not force actors or runtime stages onto an argument.

## Stop

Stop when the important connection is clear at the requested depth. Another definition, example, or analogy must earn its place by closing a remaining gap.
