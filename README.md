# IIT Kanpur student organisations directory

A research dataset for a future student directory and GitHub Pages website. This is an initial, incomplete inventory—not a claim that every listing or term is current. No site is included yet.

## Files

- `data/organisations.json` lists clubs, societies, teams and other bodies.
- `data/people.json` lists office-bearers and references organisations by ID.
- `scripts/validate.py` checks JSON structure, identifiers and references. Run `python3 scripts/validate.py`.

## Updating the data

Use stable, unique lowercase hyphenated IDs. Categories are `snt`, `cultural`, and `others`; preserve the council and type separately. Add a source URL and date checked for each record. Distinguish being listed on a source from being confirmed current. Older cultural listings need additional verification. The directory is incomplete; other councils, cells, festivals and contacts still need research.

Add a contact only if publicly provided for direct contact and verified from a source. For example, use `{"type": "email", "value": "name@example.org", "source_url": "https://example.org/team", "checked_on": "YYYY-MM-DD"}`. Leave `contacts` empty when not verified; never guess addresses. `term: null` means unknown, not a current appointment. Update or remove outdated information on request.

## Publish to GitHub

Create an empty GitHub repository, then from this directory run `git remote add origin <repository-url>` followed by `git push -u origin main`. Do not commit private data or credentials.
