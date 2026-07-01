# Cotiza CPQ Documentation

Documentation site for Cotiza CPQ — native Salesforce configure-price-quote.

## Local Development

```bash
npm install
npm start      # local dev server
npm run build  # production build
```

## Regenerating object field reference

When `Cotiza/fieldDocs` HTML is updated via `fieldDocsTable.py`:

```bash
python3 scripts/generate_object_docs.py
```

## Documentation structure

| Section | Audience |
| --- | --- |
| Getting Started | Install and first configuration |
| Sandbox Seed Data | Copy configuration between orgs via SFDMU |
| For Administrators | Playbook, rules, pricing, approvals, contracts, proposals |
| For End Users | Quoting, approvals, proposals, contracts |
| Object Reference | Field-level API documentation (36 objects) |
| Reference | Glossary |