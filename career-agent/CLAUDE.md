# Career Agent Rules

This repository is an evidence-grounded career knowledge graph and resume compiler.

## Data flow
Experience context -> atomic evidence -> reusable claims -> job-specific manifest -> rendered resume.

## Hard rules
- Never invent experience, metrics, tools, ownership, scope, or impact.
- Never draft a resume bullet directly from a JD. Select canonical claims first.
- Every generated bullet must cite claim IDs and all supporting evidence IDs.
- Distinguish direct, adjacent, and missing experience.
- Distinguish personal contribution, team outcome, prototype, production deployment, and research result.
- Canonical KB and strategy changes require a proposal and explicit user approval.
- Applying an approved KB patch and committing it are separate approvals.
- Do not overwrite an approved resume version; create a job-specific output directory.
- Job-local wording feedback must not become global strategy unless the user confirms it is durable.

## Validation
Run `python scripts/validate_kb.py` after KB changes and `python scripts/check_resume_claims.py <manifest>` after generating a resume manifest.
