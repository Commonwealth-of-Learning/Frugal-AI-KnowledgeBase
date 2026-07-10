# AGENTS.md

Guidance for AI agents working in this repository, following the convention described in `docs/getting-started/coding-agent.md`.

## Repository layout

- The published site root is `docs/`, set by `.gitbook.yaml`. The repo-root `README.md` and `SUMMARY.md` are inert stubs; edit `docs/README.md` and `docs/SUMMARY.md` instead.
- Public navigation is `docs/SUMMARY.md`. Every public page must be linked from it.
- `internal/` holds maintainer material (editorial guide, naming registry, plans, reviews, tools). Never link it from public navigation.

## Conventions

- Follow `internal/editorial-guide.md`: British and Commonwealth spelling, no direct second person in public pages, sober tone, no long shell scripts on public pages.
- Use names, role labels, and port allocations from `internal/naming-registry.md`. Register any new host port there.
- The hexagon graphics in `docs/.gitbook/assets/` are generated. Edit `internal/tools/generate_hexagons.py` and rerun it; do not hand-edit the SVGs.

## Checks before committing public changes

```bash
python3 internal/tools/editorial_audit.py
```

Run it from the repository root and again from inside `docs/`, then run `git diff --check`. The audit enforces navigation entries, frontmatter, role labels, internal links and anchors, port allocations, and site-name usage.
