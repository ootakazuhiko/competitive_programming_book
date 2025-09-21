---
name: "Infra: Unify GitHub Pages source and root index"
about: Remove legacy `index.html`, use `index.md` + custom layout consistently.
labels: infra, pages
---

## Summary
`index.html` (legacy) may conflict with `index.md`. Use a single home page and ensure Pages source is set correctly.

## Tasks
- [x] Rename `index.html` -> `legacy-index.html`
- [ ] Confirm Pages publishes from root (`/`) not `docs/`
- [ ] Rebuild Pages, verify new home uses custom layout

