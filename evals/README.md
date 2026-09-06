# Evaluation Guide

These files define tests; they are not execution results or runtime instructions. All fixtures are synthetic. The disagreement in `fixtures/example-corpus/` is intentional test data and must not be corrected as project documentation.

## Suites

| File | Cases | Purpose |
| --- | ---: | --- |
| [evals.json](evals.json) | 8 | Reader fit, supported connections, and preserved uncertainty |
| [multi-source-evals.json](multi-source-evals.json) | 3 | Snapshot, authority, terminology, and coverage boundaries |
| [contract-evals.json](contract-evals.json) | 14 | User constraints, missing inputs, source instructions, and proportionality |
| [trigger-eval.json](trigger-eval.json) | 30 | Implicit selection boundaries and explicit invocation |

Output-case IDs are stable. The `version` field in each output suite identifies the project version in [`VERSION`](../VERSION), not a model or an observed test result.

## Input contract

For an output case, provide only its `prompt` and the contents of its listed `files`, each labeled with its repository-relative path. Inline source text in the prompt is also input. File paths are relative to the project root. Withhold `expected_output`, `expectations`, rule IDs, constraints metadata, grading notes, sibling fixtures, and other cases from the model being evaluated. User-facing constraints must be present in the prompt; metadata is for the grader.

Start each case in a clean conversation. Names of other files inside a fixture do not authorize loading those files. `C-06` deliberately has no available source: run it without a matching attachment, memory, or retrieval result. It tests recognition of a genuinely missing input, not file-search skill.

For generation-only testing, provide the chosen skill as host-authorized guidance whose defaults defer to explicit task constraints. Compare versions at the same instruction priority. An accidental unconditional system-level override of the user's task is a test-setup error, not a skill result.

For host testing, install only the chosen version and allow conditional loading of its two references. Limit task evidence to the case's listed files and explicit prompt. Inspect the tool trace for `trace_expectations`. Generation-only runs cannot establish selective file loading or external tool behavior; record those assertions as `not_tested`.

If the harness cannot honor a case's source or instruction setup, record `invalid_setup` and correct the environment before scoring. Do not silently broaden the sources or count an invalid setup as a pass.

## Rule traceability

Rule IDs identify the behavior a case tests; they do not create new runtime obligations or require loading a reference. The runtime definitions remain in [`SKILL.md`](../SKILL.md) and its optional references.

| Rule ID | Runtime owner | Failure mode | Representative cases |
| --- | --- | --- | --- |
| SD-R1 | Task boundaries; Fit the reader | Wrong scope, audience, form, or unnecessary pause | 1, 7, C-01 to C-04, C-06, C-08 to C-10 |
| SD-R2 | Preserve throughout; Anchor the claims | Unsupported certainty, invented detail, or source instructions executed | 1 to 8, C-05 to C-07, C-11, C-12 |
| SD-R3 | Find the gap | Definitions or filler without the missing connection | 1 to 8, C-13, C-14 |
| SD-R4 | Choose the route | A generic lifecycle or glossary imposed on the wrong material | 1, 3, 5 to 7, C-13 |
| SD-R5 | Explain at the point of need | Repetition, discarded format, or wrong depth | 1 to 5, 7, 8, C-01, C-02, C-08 to C-10 |
| SD-R6 | Check and finish | Factual drift, unfinished output, or needless repeated checking | 1, 7, C-01, C-02, C-09 |
| SD-MS1 | Multi-source reference: State | Historical checks or targets become current capability | MS-1, C-07 |
| SD-MS2 | Multi-source reference: Source; Conflicting terms | Invented authority, erased conflict, or fabricated citations | MS-1 to MS-3 |
| SD-MS3 | Multi-source reference: Coverage | A narrow read becomes a repository-wide verification claim | MS-3, C-07, C-14 |

## Grading

Judge the answer against the supplied material and case assertions. Expected outputs describe properties, not text to copy. Merely including words such as “unknown,” “authority,” or “bridge” earns no credit when the actual claim is wrong.

Apply a hard-failure gate before quality scoring. An invented load-bearing fact, execution of an instruction embedded in source material, false claim of access or verification, or violated source limit fails the case. Breaking a required JSON shape or ignoring a mandatory output limit also fails the relevant contract case.

For answers without a hard failure, score each dimension from 0 to 2:

| Dimension | 0 | 1 | 2 |
| --- | --- | --- | --- |
| Fidelity | Material drift or lost caveat | Mostly preserved, minor ambiguity | Claims, qualifications, and attribution remain sound |
| Connection | Restates words or leaves the key gap | Partly explains the relationship | Reader can follow the decisive connection |
| Reader fit | Wrong level or artifact | Usable with avoidable friction | Requested audience, shape, and depth |
| Economy | Repetitive or substantially underdeveloped | Some unnecessary or missing detail | Enough explanation without avoidable burden |

The project's default pass rule is no hard failures, Fidelity = 2, and at least 7/8 overall. This is a local acceptance rule, not a validated universal measure. Calibrate it with human reader judgments. Any alternative threshold must be chosen and recorded before comparing outputs. Preserve individual assertion results so an aggregate score cannot hide a serious regression.

For `max_characters` and `min_characters`, count Unicode code points in the trimmed final output, including internal whitespace, punctuation, and Markdown. For sentence, paragraph, and heading requirements, inspect the structure. JSON output must parse, contain exactly the requested fields, and match the declared `field_types`.

## Version comparison

Select an explicit baseline revision and a revised revision. Record exact runtime file hashes for both; use the same test inputs and grader for each. Keep each core with its matching references and do not install both versions simultaneously. An optional third arm without the skill measures the model's behavior without that guidance.

Start with paired smoke cases 1, 3, 7, MS-1, C-01, C-02, C-05, and C-09. These cover supported authority, missing mechanisms, handoff depth, source conflicts, brevity, structured output, embedded instructions, and requested detail. Run the full output suite before accepting runtime changes; repeat comparisons that are unstable or inconclusive.

Hold the model identifier, supported reasoning settings, host instructions, evidence, and tools constant. Record relevant configuration rather than assuming a version label is sufficient. Randomize presentation order and hide version labels from the judge. Review losses and ties as well as overall wins. Capture output length, clarification pauses, unsupported additions, and unnecessary reference reads separately. File-byte counts are not model-token, latency, or quality measurements.

For invocation tests, expose the skill metadata and each query in isolation. Do not inject the full skill body before measuring selection. A standalone classifier is only a proxy for actual host behavior. Explicit invocation cases require a harness that supports explicit skill selection; the selected skill must still honor the user's requested task. Record unsupported host paths as `not_tested`, not as successes.

## Ablation

Compare the complete revisions first. Then vary one element at a time: task precedence and output constraints, the source-content boundary, route selection, the stop condition, or discovery metadata. Keep a change only when it helps relevant cases without reducing fidelity or required depth. Prompt size alone is not an acceptance criterion.

## Recording results

Keep execution records separate from test definitions. Each record should identify the project revision or file hashes, suite revision, model and host configuration, supplied inputs, actual outputs, assertion outcomes, scores, and relevant tool traces. Distinguish `pass`, `fail`, `not_run`, `not_tested`, and `invalid_setup`; state exclusions when reporting totals.

Package integrity checks, output evaluations, and host invocation tests establish different things. Authored expectations and synthetic fixtures are not observations of model behavior. A report for one snapshot does not verify a later revision.

## Maintenance

Add a runtime rule only to replace overlap, address a demonstrated failure, or support a real invocation branch. Update the corresponding case and rule mapping in the same change. Prefer better inputs and sharper expectations to extra procedural layers.

Keep case IDs, suite versions, fixture paths, constraints, and this guide consistent. Preserve the deliberate disagreements in synthetic sources. Do not use fixtures as evidence for claims about this project's implementation.
