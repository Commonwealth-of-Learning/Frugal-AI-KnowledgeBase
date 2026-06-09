# Frugal AI Knowledge Base

This repository contains the source for the Frugal AI knowledge base, a developer-first reference for building sovereign, local-first AI services for education.

The published GitBook space is rooted in `docs/` through `.gitbook.yaml`. The root `README.md` and `SUMMARY.md` are only repository entry points; public navigation lives in `docs/SUMMARY.md`.

## Maintainer checks

Run the local editorial audit before publishing or changing navigation:

```bash
python3 internal/tools/editorial_audit.py
```

The audit checks naming, frontmatter, summary structure, internal links, guide hints, layer tags, and documented host ports.

## Key files

- `docs/README.md` — public landing page.
- `docs/SUMMARY.md` — public sidebar.
- `internal/editorial-guide.md` — tone, style, and page patterns.
- `internal/naming-registry.md` — approved public names and navigation labels.
- `internal/templates/` — thin scaffolds that point to live exemplars.
