# Canonical knowledge-base change control

## Why this exists

The knowledge base is allowed to evolve linearly, but “linear” does not mean unreviewed. Git already provides historical versioning; the workflow adds semantic review before canonical facts or durable strategy preferences change.

## States

1. **Observed:** information appears in a resume, conversation, or user answer.
2. **Proposed:** the agent writes a patch under `career_kb/proposals/`.
3. **Approved for edit:** the user approves the exact proposed meaning and scope.
4. **Applied, uncommitted:** the agent edits canonical files and runs validation.
5. **Approved for commit:** the user reviews the staged diff and explicitly confirms commit.
6. **Committed:** the canonical history advances.

## Required proposal contents

Every proposal must state:

- target canonical file;
- exact addition, replacement, or deletion;
- source of the information;
- confidence level;
- scope limitations and caveats;
- resume claims newly enabled or disabled;
- whether this is a factual correction or a strategy preference.

## Approval boundary

Approving a generated resume does not approve its inferred facts. Approving a KB edit does not approve a Git commit. Both approvals are explicit and separate.
