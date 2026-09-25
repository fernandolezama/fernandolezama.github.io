# Academic website redesign, review draft

Open `index.html` directly in Chrome or another browser. No installation or server is required to review it.

The six views are Home, Research, Publications, Team, News, and About & contact. The homepage shows the three newest news entries and featured publications. Publications can be filtered by text, year and type.

## Updating content

The easiest workflow is to provide a DOI or full citation, an announcement, or a role update in the conversation. Changes can then be prepared for review before publication.

For direct editing, the content lives in separate files:

- `publications.json`: bibliography; add a record with `type` (Journal, Conference or Book), `year`, `citation`, and `links` (a list of label/url pairs). To feature it on the homepage, add `featured: true`, `title`, and `venue`. Keep featured selections short.
- `news.json`: announcements; add `date` (YYYY-MM), `category`, `title`, `text`, and optionally `link` (label/url). News is sorted newest first. The homepage shows the first three; the News view shows the complete archive. To remove a homepage item without deleting it from the archive, add newer dated items; date entries accurately.
- `profile.json`: research affiliations and professional roles. Each entry uses `organization`, `role`, and `detail`.
- `template.html`: visual layout, biography and team content.

After editing the data, run `python redesign/build.py` from the repository root. This regenerates the self-contained `index.html`; opening it shows the updated content. Data file changes alone do not change the generated page. There is no automatic GitHub publishing workflow configured for this draft yet.

The original bibliography was imported from `publication.md`: 47 journals, 84 conference entries, and 6 books/chapters. These are source counts, not independently verified career totals. The legacy import script `import-publications.py` overwrites `publications.json` and should not be used for ordinary updates.

## Review before publication

- Review the design, biography and research descriptions.
- Confirm ITES-Opt naming, student role labels and project wording.
- Professional roles use the supplied signature: IEEE Senior Member, IEEE CIS Conference Competitions Subcommittee member, IEEE ISATC TF3 Vice-Chair, and Artificial Intelligence Review Associate Editor.
- Check inherited bibliography details and links.
- Add a current CV and approved portraits if wanted.
- Preserve existing public paths and downloadable resources when publishing.

This draft has not replaced the current homepage or been pushed to GitHub. JavaScript syntax, internal link targets, form labels and imported counts were checked. Browser rendering and mobile interaction still need visual review.
