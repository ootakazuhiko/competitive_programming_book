---
name: "Feature: Site-wide search index"
about: Build a JSON index and enable cross-page search.
labels: enhancement, search
---

## Summary
Current search scans only the current page DOM. Generate `assets/search-index.json` for cross-page search.

## Tasks
- [ ] Add GitHub Actions workflow to build index from `src/**/index.md`
- [ ] Commit `assets/search-index.json` on push to `main`
- [ ] Update `assets/js/search.js` to fetch and query index
- [ ] Add debounce and highlight (reuse existing)

