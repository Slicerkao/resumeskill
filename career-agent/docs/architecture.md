# Architecture

The project treats application material generation as a constrained compiler pipeline:

```text
Experience context
    -> atomic evidence
    -> reusable claims
    -> job-specific claim selection
    -> resume manifest
    -> rendered LaTeX/PDF
```

## Experience
Narrative project context, ownership boundaries, caveats, dates, and skills. Experience files are not directly copied into a resume.

## Evidence
Atomic factual records identified by stable IDs. In the initial version, evidence remains embedded in the experience YAML files under `problems`, `actions`, `outcomes`, and `research`. A later migration may normalize these into separate files without changing IDs.

## Claims
Reusable, resume-safe propositions backed by one or more evidence IDs. Claims may specify qualifiers, forbidden inferences, confidence, risk, and target role families. The agent should select claims before drafting prose.

## Resume manifest
A job-specific intermediate representation recording selected claim IDs, ordering, wording, and evidence provenance. Generated prose that cannot cite a canonical claim is invalid.

## Renderer
The existing Awesome-CV LaTeX source remains the baseline renderer. Rendering technology is deliberately downstream of the career knowledge model.
