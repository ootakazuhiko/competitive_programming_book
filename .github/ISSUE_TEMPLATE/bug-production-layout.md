---
name: "Bug: Production chapter pages not using book layout"
about: Deployed chapter pages render with minimal template instead of `_layouts/book.html`.
labels: bug, pages
---

## Summary

On https://ootakazuhiko.github.io/competitive_programming_book/, chapter pages under `/src/` show a minimal template, empty H1, and no sidebar/theme — not the custom `book` layout.

## Expected

- `<title>` contains chapter title
- Sidebar, theme toggle, search UI visible
- Page navigation shows previous/next

## Actual

- `<title>` equals site title only
- Minimal styles, no sidebar
- H1 is empty in the rendered HTML

## Suspected causes

- GitHub Pages source misconfigured (publishing from `docs` or cached build)
- Conflicting root `index.html` influencing routing
- Jekyll not applying `layout: book` to `src/**/index.md`

## Tasks

- [ ] Verify Pages source folder/branch in repo settings
- [ ] Ensure GitHub Pages builds Jekyll (not static)
- [ ] Confirm `src/**/index.md` front matter has `layout: book` (it does)
- [ ] Purge/retire legacy root `index.html` (renamed to `legacy-index.html` in PR)
- [ ] Trigger a fresh Pages build and re-check

## References

- `_layouts/book.html`
- `src/chapter-*/index.md`

