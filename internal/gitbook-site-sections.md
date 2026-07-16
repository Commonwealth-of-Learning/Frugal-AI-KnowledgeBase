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

## Scope decision (2026-07-15)

Revisited when planning four content areas (training, partner contributions, model evaluation/benchmarking, latest updates). Decision: **horizontal tabs earn their cost only for a distinct audience or cadence, self-contained content, and a body worth a separate space** (Ultimate plan, per-space assets, heavier cross-linking, a `SECTION_DIRS` audit extension). Verdict per area:

- **Training materials** and **Frugal AI Network / partner contributions** — keep as the two horizontal tabs (`/training/`, `/network/`). Distinct facilitator and contributor audiences; already built and audited; partner contributions are already scoped in the network README. A separate space is also what lets partners be granted write access.
- **Model evaluation, selection, and benchmarking** — **main `docs/` space, not a tab.** It serves the core developer audience and is tightly coupled to `docs/concepts/inference-layer.md` "Choose a model" and the model cards. Placed at `docs/concepts/model-evaluation.md` (under the Inference sidebar group), where the further-work interactive comparison tool will land. A tab would sever those links and duplicate assets.
- **Latest updates** — **no news tab.** The KB already routes programme news out to COL (`docs/README.md` "From the Commonwealth of Learning"); a KB-run feed duplicates COL and goes stale. A single lightweight KB **changelog** (what changed in these docs, with a COL-news pointer) is the only defensible in-KB form: placeholder at `docs/reference/whats-new.md`. Not a competing news feed.

Net: **no new horizontal sections beyond the two already prepared.** `SECTION_DIRS`, the naming registry, and the publish steps below are unchanged.

## Caveats

- `internal/tools/editorial_audit.py` now audits the two section dirs via `check_site_sections()` (`SECTION_DIRS` at the top of the file), applying the public-page checks to every page linked from each section's `SUMMARY.md`. Any new section dir must be added to `SECTION_DIRS` to be covered.
- Assets are per-section: the hexagon SVGs under `docs/.gitbook/assets/` are not automatically available to the other sections.
- Register section names in `internal/naming-registry.md` before adding more.
