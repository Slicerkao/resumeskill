---
name: tailor-resume
description: Analyze a job description, ask high-value factual questions, select evidence-backed claims, and propose a job-specific resume manifest and LaTeX diff.
---

# Tailor Resume

## Non-negotiable pipeline
Do not draft resume bullets directly from experience prose or the JD.

1. Parse the JD into must-have, preferred, and responsibility requirements.
2. Retrieve relevant experience and atomic evidence IDs.
3. Match requirements to canonical claims in `career_kb/claims/`.
4. Produce a coverage matrix: strong, partial, adjacent, missing.
5. Ask only high-impact clarification questions that may materially change coverage.
6. Classify each user correction as factual KB correction, new evidence, durable resume strategy, or job-local preference.
7. Write proposed KB/strategy changes under `career_kb/proposals/`; never apply without explicit approval.
8. Select claims and produce `outputs/<job_id>/resume_manifest.yaml`.
9. Draft bullets only from selected claims. Every bullet must list `claim_ids` and all supporting `evidence_ids`.
10. Produce a readable resume diff and explain each change against a JD requirement.
11. Do not modify canonical resume files until the user approves the resume proposal.
12. Run `python scripts/validate_kb.py` and `python scripts/check_resume_claims.py <manifest>`.

## Question quality
Do not ask “Do you have experience with X?” Give concrete scopes and distinguish direct, adjacent, and platform-mediated experience. Missing experience is an acceptable outcome.

## Truthfulness
Never upgrade adjacent experience into direct experience, team outcome into sole ownership, prototype into production deployment, or gold-set agreement into production accuracy.
