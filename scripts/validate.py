import json
from pathlib import Path

root = Path(__file__).resolve().parents[1]
organisations = json.loads((root / 'data/organisations.json').read_text())
people = json.loads((root / 'data/people.json').read_text())
org_ids = [x['id'] for x in organisations]
people_ids = [x['id'] for x in people]
assert len(org_ids) == len(set(org_ids)), 'duplicate organisation ID'
assert len(people_ids) == len(set(people_ids)), 'duplicate person record ID'
for org in organisations:
    assert org['category'] in {'snt', 'cultural', 'others'}
    assert org['name'] and org['sources']
for person in people:
    assert person['organisation_id'] in org_ids, person['id']
    assert person['name'] and person['role'] and person['sources']
    for contact in person['contacts']:
        assert all(contact.get(k) for k in ('type', 'value', 'source_url', 'checked_on'))
print(f'OK: {len(organisations)} organisations, {len(people)} office-bearer records')
