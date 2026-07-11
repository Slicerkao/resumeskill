---
name: update-career-kb
description: Propose and, only after explicit approval, apply updates to experience evidence, reusable claims, profile, or resume strategy.
---

# Update Career KB

Classify input as one or more of:
- experience context;
- atomic evidence correction/addition;
- reusable claim addition/correction;
- durable resume strategy;
- job-local preference.

Before modifying canonical files, create a proposal under `career_kb/proposals/` showing old/new content, source, confidence, caveats, affected claim IDs, and claims enabled or disabled. Ask for explicit content approval.

After approval, apply only the approved patch and run `python scripts/validate_kb.py`. Show the staged diff and ask separately before committing. Content approval is not commit approval.
