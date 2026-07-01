# System Settings

The CPQ System Settings record controls org-wide Cotiza CPQ behavior. Create one record after installation and configure it before rolling out to users.

See [CPQ System Settings](../objects/admin/system_settings__c.md) for the complete field reference.

## Core settings

| Field | Purpose |
| --- | --- |
| **Default Playbook** | Pre-select a Playbook when creating Quotes |
| **Display Playbook as Modal** | Show Playbook configuration in a modal vs. full page |
| **Approval Submitter** | Default submitter behavior for approval workflows |
| **Line Item Pricing Fields Refresh** | Controls pricing recalculation timing |

## Quote table configuration

| Field | Purpose |
| --- | --- |
| **Quote Table Display Columns** | Semicolon-delimited Quote fields shown in the Quotes table |
| **Quote Table Actions** | Available actions: View, Edit, Sync, Proposal, Clone, Delete |
| **Quote Table Sort By Default** | Default sort column and direction |
| **Quote Table Page Size Default** | Pagination size (blank = no pagination) |

## Proposal settings

| Field | Purpose |
| --- | --- |
| **Proposal Table Actions** | Actions on the Proposals table |
| **Proposal Table Page Size Default** | Proposals table pagination |
| **Proposal Quote Piped Fields** | Additional Quote fields available in piped text |
| **Proposal Allowed Override Fields** | Quote fields Proposal Power Users may override |

## Approval settings

| Field | Purpose |
| --- | --- |
| **Approval Allowed Override Fields** | Quote fields submitters may override when submitting approvals |

## Contract settings

| Field | Purpose |
| --- | --- |
| **Contract Table Display Columns** | Contract table columns on Account/Contracts UI |
| **Contract Table Actions** | View, Amend, Replace, Renew, Void |
| **Contract Table Sort By Default** | Default contract sort |
| **Contract Table Page Size Default** | Contract table pagination |
| **Amendments Maintain Contract** | Amend in place vs. new Contract per amendment |
| **Force Quote From Contract** | Require contract context for adjustment Quotes |
| **Show Most Active Contract Snapshot** | Display snapshot on Account contract views |

## Semicolon-delimited field lists

Many System Settings and Playbook fields use semicolon-delimited API name lists. Conventions:

- Use valid field API names
- Prefix with `#Label` to create section headers in display views
- Use invalid tokens as blank spacers
- Append `;Down` or `;Up` to sort field names for default sort direction

## Related guides

- [Quick Start](../getting-started/quick-start.md) — create your first System Settings record
- [UI Components](../ui-components/overview.md) — how settings affect CPQ tabs
