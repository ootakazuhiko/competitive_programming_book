# TODO

High-impact upcoming tasks for the book website.

- [ ] Fix production pages to use custom `book` layout for all chapter pages
  - Validate GitHub Pages source (root vs `docs/`) and Jekyll build settings
  - Ensure `src/**/index.md` renders with `_layouts/book.html`
  - Remove/retire legacy `index.html` to avoid conflicts (renamed to `legacy-index.html`)
- [ ] Add jekyll-seo-tag to layout and verify meta output
  - Confirm `<title>`, OG/Twitter, canonical are correct per page
- [ ] Chapter navigation order verification
  - Ensure every chapter has `order` in front matter
  - Check `_includes/page-navigation.html` previous/next behavior
- [ ] Site-wide search (cross-page)
  - Generate `assets/search-index.json` at build (via GitHub Actions)
  - Update `assets/js/search.js` to consume index for multi-page search
- [ ] Code block UX: copy-to-clipboard buttons
  - Implemented `assets/js/code-copy.js`; verify on multiple devices
- [ ] Chapter endings: checklist, pitfalls, exercises
  - Roll out a consistent template to each chapter
- [ ] Map AtCoder practice problems to sections
  - Add links (A/B中心) with brief rationale and expected complexity
- [ ] Print style improvements
  - Add a print stylesheet for cleaner PDFs/printouts

