# IIT Kanpur student organisations directory

A static, searchable prototype and research dataset for an IIT Kanpur student directory. Listings are incomplete; a source listing does not by itself establish a current term.

## Files

- `index.html` is the static directory prototype; it reads the JSON at runtime.
- `data/organisations.json` lists clubs, societies, teams and other bodies.
- `data/people.json` lists office-bearers and references organisations by ID.
- `data/quiz-club-2026-27.json` records a user-supplied Quiz Club roster and its uncertainty.
- `scripts/validate.py` checks JSON structure, identifiers and references. Run `python3 scripts/validate.py`.

## Updating the data

Use stable, unique lowercase hyphenated IDs. Categories are `snt`, `cultural`, and `others`; preserve the council and type separately. Add a source URL and date checked for each record. Distinguish being listed on a source from being confirmed current. Older cultural listings need additional verification. The directory is incomplete; other councils, cells, festivals and contacts still need research.

Add a contact only if publicly provided for direct contact and verified from a source. For example, use `{"type": "email", "value": "name@example.org", "source_url": "https://example.org/team", "checked_on": "YYYY-MM-DD"}`. Leave `contacts` empty when not verified; never guess addresses. `term: null` means unknown, not a current appointment. Update or remove outdated information on request.

## Run and publish

Run `python3 -m http.server 8000` in the repository root and visit `http://localhost:8000/`. Opening `index.html` as a local file will not load the JSON in most browsers.

For GitHub Pages, in the repository's Settings → Pages, choose **Deploy from a branch**, select `main` and `/ (root)`, then save. The expected project URL is `https://chaapulaundi.github.io/infoiitk/` after GitHub finishes deployment. Do not commit private data or credentials.
