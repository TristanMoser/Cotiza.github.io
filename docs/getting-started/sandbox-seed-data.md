# Sandbox Seed Data

Use [SFDMU](https://help.sfdmu.com/) (SFDX Data Move Utility) to copy **your own** Cotiza CPQ configuration from one Salesforce org to another—for example, from production to a sandbox, or from a configured sandbox to a fresh one.

This page does **not** ship Cotiza test data. It provides an `export.json` migration template and step-by-step instructions so you can move configuration you already built in a **source org** into a **target org** without rebuilding playbooks, products, and rules by hand.

## Download export.json

Save this file to a folder on your machine. SFDMU reads `export.json` from your current working directory when you run a migration.

**[Download export.json](/files/export.json)**

Example layout:

```text
~/cotiza-migration/
  export.json
```

## What gets transferred

The `export.json` template defines which Cotiza CPQ objects to read from the source org and upsert into the target org, in dependency order:

| Order | Object | Purpose |
| --- | --- | --- |
| 1 | Account, Contact | Customer records referenced by your configuration |
| 2 | System Settings | Org-wide CPQ defaults |
| 3 | Pricebook2, Product2, PricebookEntry | Product catalog |
| 4 | Pricing Set, Pricing Threshold | Tiered pricing |
| 5 | Playbook | Active playbook shell |
| 6 | Playbook Scenario → Criterion | Rule/approval conditions |
| 7 | Playbook Question Group → Question | Guided quote inputs |
| 8 | Playbook Rule → Action → Calculation Item | Automation |
| 9 | Playbook Approval → Approver Group → Approver | Approval path |
| 10 | Playbook View Section | Proposal/email layout |

**Not included in `export.json`:**

- **User** records — Playbook Approvers reference users; those users must exist in the target org
- **Opportunity** / **Quote** transaction data — create test Opportunities after the migration
- **Custom Metadata** records — package defaults apply; deploy CMDT separately if needed

## Prerequisites

### Target org

The org you are copying **into** (typically a sandbox):

1. Install the **Cotiza CPQ** managed package
2. Enable Quotes: **Setup → Quote Settings → Enable Quotes**
3. Assign yourself **Cotiza CPQ Admin**
4. Authenticate with Salesforce CLI:

```bash
sf org login web --alias cotiza-target --instance-url https://test.salesforce.com
```

Use `https://login.salesforce.com` instead of `test.salesforce.com` when the target is production.

### Source org

The org that already contains the Cotiza configuration you want to copy **from**:

```bash
sf org login web --alias cotiza-source
```

Use the production or sandbox login URL that matches your source org.

### SFDMU plugin

Install the SFDMU Salesforce CLI plugin:

```bash
sf plugins install sfdmu
```

Verify installation:

```bash
sf sfdmu --version
```

See the [SFDMU Get Started guide](https://help.sfdmu.com/get-started) if the plugin command is not found.

## Transfer your data

### 1. Prepare the working directory

Create a folder, save [export.json](/files/export.json) into it, and open a terminal there:

```bash
mkdir -p ~/cotiza-migration
cd ~/cotiza-migration
# Save export.json into this folder, then confirm:
ls export.json
```

### 2. Dry run (recommended)

Run with diagnostic logging first:

```bash
sf sfdmu run \
  --sourceusername cotiza-source \
  --targetusername cotiza-target \
  --diagnostic
```

Review the generated `.log` file for errors before re-running without `--diagnostic`.

### 3. Execute the migration

```bash
sf sfdmu run \
  --sourceusername cotiza-source \
  --targetusername cotiza-target
```

Replace aliases with full usernames if you did not set aliases during login (for example, `--sourceusername user@company.com`).

SFDMU reads records from your source org and upserts them into the target org using the object order and external ID keys defined in `export.json`.

### Alternative: CSV round-trip

If you prefer to inspect or edit data between orgs, export to CSV first, then import into the target org:

```bash
# Export from source to CSV files in the export.json directory
sf sfdmu run --sourceusername cotiza-source --targetusername csvfile

# Import CSV into target org (files named Account.csv, Cotiza__Playbook__c.csv, etc.)
sf sfdmu run --sourceusername csvfile --targetusername cotiza-target
```

## Post-migration steps

### 1. Resolve missing User references

SFDMU may report missing parent records for **Playbook Approver** when approver Users do not exist in the target org (referenced by `Name`). Either:

- Create matching Users in the target org with the same names as the source org, then re-run the migration, or
- Update Playbook Approver records manually to point at target org Users

Check `reports/MissingParentRecordsReport.csv` in your working directory if SFDMU generates one.

### 2. Verify configuration records

In the target org, confirm:

- [ ] One **System Settings** record with **Default Playbook** populated
- [ ] At least one active **Playbook** linked to an active **Price Book**
- [ ] **Products** and **PricebookEntry** records are active
- [ ] **Playbook Questions** and **Rules** are active

### 3. Complete org setup

Steps not covered by `export.json`:

| Step | Guide |
| --- | --- |
| Place CPQ Container on Opportunity page | [UI Components](../ui-components/overview.md) |
| Assign permission sets to test users | [Permissions](./permissions.md) |
| Set Power User values if testing elevated features | [Power Users](../admin-guide/power-users.md) |

### 4. Create test transaction data

Create manually in the target org:

1. **Account** and **Contact** (if not already loaded)
2. **Opportunity** on the Account
3. Open **Cotiza CPQ** → create a Quote using the migrated Playbook

Follow the [Quick Start](./quick-start.md) and [Workflow Overview](../user-guide/workflow-overview.md) to validate end-to-end.

## External ID keys

SFDMU upserts use composite external IDs defined in `export.json`. Examples:

| Object | External ID fields |
| --- | --- |
| Playbook | `Name`, `Label`, `Pricebook.Name` |
| Playbook Question | `Variable_Name` |
| Playbook Rule Action | `Name`, `Playbook Rule.Name` |
| PricebookEntry | `Product2.Name`, `UnitPrice`, `Pricebook2.Name` |

Do not change external ID field combinations without updating both source data and `export.json`. See [SFDMU external ID documentation](https://help.sfdmu.com/full-documentation/export-json-file-objects-specification/export-json-file-overview).

Re-running the same migration is safe when external IDs match—the records are updated in place rather than duplicated.

## Troubleshooting

| Issue | Resolution |
| --- | --- |
| Missing parent User on Approver | Create Users in target org or update Approver records |
| Playbook not visible in CPQ | Confirm Playbook **Is Active** and Price Book is active |
| PricebookEntry errors | Ensure Product2 records loaded before PricebookEntry |
| Duplicate records on re-run | Upsert uses external IDs; verify keys match source |
| Field not accessible | Confirm Cotiza CPQ Admin permission set is assigned |

See [Common Errors](../troubleshooting/common-errors.md) for runtime CPQ issues after migration.

## Related resources

- [SFDMU documentation](https://help.sfdmu.com/)
- [Download export.json](/files/export.json)
- [Configuration Guide](../admin-guide/configuration.md)
