<p align="center">
  <strong>English</strong> · <a href="README.zh.md">简体中文</a>
</p>

# Semantic Decompression

Make dense material understandable without losing its meaning.

Semantic Decompression is an instruction-only skill that restores the context and connections an author assumed the reader already knew. It preserves formal terms, source claims, and uncertainty while explaining who acts, what changes, why a conclusion follows, and where the evidence stops.

## When to use it

Use the skill when understanding requires more than a summary or a glossary: onboarding to an unfamiliar architecture, following a compressed argument, interpreting a measurement, or turning expert notes into a companion guide or handoff.

The depth follows the task. A narrow distinction may need two sentences; a complete tutorial may need a map, one continuing example, and a discussion of boundaries. The skill does not impose a fixed output template.

Pure summaries, literal translations, copyediting, archive extraction, and code fixes are not implicit triggers. In a mixed request, the skill handles the explanatory portion without taking over the rest of the task.

## Example

The following fragment is a teaching example, not a rule for a real legal system.

**Source**

> The statutory review period starts after substantive completeness, and requests for additional material stop the clock.

**Explanation**

> Submission alone is not the stated condition for starting the review clock; the submission must reach substantive completeness. A request for additional material stops that clock. The fragment does not identify who decides completeness, the applicable deadline, or what restarts the clock. In particular, it does not say that merely sending the additional material is enough to resume counting.

The missing distinction becomes clear without inventing the missing rule.

## Installation

Place the runtime files in a directory named `semantic-decompression` inside your host's supported skill location:

```text
semantic-decompression/
  SKILL.md
  references/
    decompression-lenses.md
    multi-source-boundaries.md
```

Keep the relative paths intact. Copying the complete repository is also supported; only the files above are runtime guidance. Before updating, preserve local modifications and avoid enabling duplicate copies of the same skill.

The host controls discovery, activation, permissions, and model selection. Use its documented skill location and invocation mechanism. This project does not require a specific model, executable scripts, package dependencies, or API keys. Source retrieval, when needed, uses the tools provided by the host.

## Usage

Ask for the explanation you need, including any audience, source, or format constraints:

> Explain this architecture to a new teammate. Preserve the canonical terms, walk through the supported flow, and leave missing recovery behavior unknown.

> I know the basics. Explain only the distinction between accepted input and committed output, in two sentences.

> Translate this paragraph, then explain its assumptions. Return only the requested JSON fields.

The workflow is defined in [`SKILL.md`](SKILL.md). It fits the reader, anchors the claims, identifies the missing connection, chooses an appropriate route, explains at the point of need, and checks the result against the source.

The references are optional. [Decompression lenses](references/decompression-lenses.md) helps diagnose a difficult comprehension gap. [Multi-source boundaries](references/multi-source-boundaries.md) handles source differences that change a claim's status, provenance, or coverage. A source being stored in a repository does not by itself call for a repository audit.

## Project files

| Path | Purpose |
| --- | --- |
| [`SKILL.md`](SKILL.md) | Runtime entry and workflow |
| [`references/`](references/) | Conditional guidance for specific gaps |
| [`evals/`](evals/) | Evaluation cases, synthetic fixtures, and grading guidance |
| [`VERSION`](VERSION) | Project version |
| [`CHANGELOG.md`](CHANGELOG.md) | User-visible changes |
| [`LICENSE`](LICENSE) | MIT license |

README files, version history, and evaluation materials are for users and maintainers; they are not additional runtime instructions.

## Evaluation

The [evaluation guide](evals/README.md) defines source isolation, rule traceability, grading, and version comparisons. The suites cover explanation quality, source boundaries, output constraints, and skill selection.

Test definitions are not execution results. Package integrity, explanation quality, and host activation are separate forms of evidence; passing one does not establish the others.

## Limits

A fluent explanation cannot replace missing evidence. The skill may explain general concepts, identify unknowns, and label supported inferences or hypothetical examples, but must not present them as facts established by the source. Source fidelity does not require endorsing an error: a supported correction is distinguished from the original claim.

The user's requested audience, language, structure, length, and source scope govern the explanation within the host's system and developer constraints.
