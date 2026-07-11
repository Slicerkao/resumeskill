# Resume claim policy

## Confidence levels

- `verified`: explicitly confirmed by the user and safe to state within recorded scope.
- `imported_resume`: present in the supplied resume; retain as baseline but flag conflicts or ambiguity.
- `user_reported`: explicitly stated by the user but not independently documented.
- `needs_confirmation`: inferred from prior context or incomplete wording; do not add to a new resume without clarification.
- `deprecated`: known to be outdated or misleading; do not use.

## Claim construction

A generated claim must:

- cite canonical evidence IDs;
- preserve metric denominators and evaluation context;
- preserve role and ownership boundaries;
- avoid stronger verbs than the evidence supports;
- avoid implying external release, production deployment, clinical validity, or organization-wide ownership unless explicitly supported.

## Adjacent experience

Adjacent experience can support wording such as “related experience” or “applied similar methods,” but cannot be converted into direct tool/domain ownership. Example: vision-model fine-tuning is not LLM fine-tuning.
