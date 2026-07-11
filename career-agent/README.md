# ResumeSkill

An evidence-grounded career knowledge graph and resume compiler for producing truthful, role-specific application materials.

## Model

```text
Experience -> Evidence -> Claims -> Resume Manifest -> LaTeX/PDF
```

- `career_kb/experiences/`: narrative context and atomic evidence records.
- `career_kb/claims/`: reusable resume-safe propositions with provenance and risk controls.
- `career_kb/strategy/`: durable writing and positioning preferences.
- `career_kb/proposals/`: unapproved changes; canonical files are never silently updated.
- `resume/manifests/`: intermediate representation for each tailored resume.
- `resume/current/`: current LaTeX source and section content. Vendor class/font files are intentionally not committed; restore them from the original CV bundle or install the template locally when rendering.
- `.claude/skills/`: workflows for inspection, KB updates, and JD tailoring.

## First local test

```bash
python scripts/validate_kb.py
python scripts/check_resume_claims.py resume/manifests/example.yaml
claude
```

Then ask Claude:

```text
Inspect the career KB. Show imported or risky claims and ask only the highest-impact clarification questions. Do not modify files.
```

For a job description saved under `jobs/`:

```text
/tailor-resume jobs/company-role.md
```

See `docs/architecture.md` for the compiler model and `career_kb/policies/change_control.md` for approval rules.
