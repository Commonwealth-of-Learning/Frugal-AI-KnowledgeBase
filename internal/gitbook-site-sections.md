# GitBook site sections — horizontal navigation

How the knowledge base gets a horizontal menu (tabs at the top of the published site), and the placeholder sections prepared for it. Researched 2026-07-10 against GitBook's published docs.

## Findings

- **Site sections are the horizontal menu.** "The new section is then added to the table and will be available to visitors as a tab at the top of your site." Grouped sections display as dropdown menus instead. Source: gitbook.com/docs/docs-site/site-structure/site-sections.
- **Each section is a space.** "Each site section is a space in GitBook. You can create site sections from any space you like."
- **Configured in the dashboard, not in the repo**: docs site dashboard → Settings → Structure.
- **Plan requirement**: site sections need the Ultimate site plan.
- **Header links are not an alternative.** GitBook does not allow custom elements in the top header ("It's not possible to customize the layout of the elements on the page"); only the logo and a custom footer are configurable.
- **Monorepo Git Sync is supported.** "GitBook can sync multiple spaces from the same monorepo using different directories." Each space is configured with a Project directory and a branch, and GitBook reads the `.gitbook.yaml` inside that directory. Caveat: "Files/assets referenced in one space aren't automatically available to another space."

## Repo layout

- `/.gitbook.yaml` (`root: ./docs/`) — the existing knowledge base space, unchanged.
- `/training/` — placeholder section **Training materials**: own `.gitbook.yaml`, `README.md`, `SUMMARY.md`.
- `/network/` — placeholder section **Frugal AI Network**: same shape.

## To publish the tabs

1. Confirm the site is on the Ultimate plan.
2. Create two new spaces; enable Git Sync on each against this repository, with Project directory `training/` (respectively `network/`) and branch `main`.
3. In the docs site dashboard, open Settings → Structure and add each space as a site section; order the tabs with the knowledge base first.
4. Check the published URLs and any cross-section links; add redirects if pages later move between sections.

## Caveats

- `internal/tools/editorial_audit.py` scans only `docs/` — the new directories are not audited. Extend the audit before the sections grow beyond placeholders.
- Assets are per-section: the hexagon SVGs under `docs/.gitbook/assets/` are not automatically available to the other sections.
- Register section names in `internal/naming-registry.md` before adding more.
