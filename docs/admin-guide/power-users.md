# Power Users

Beyond permission sets, Cotiza CPQ supports elevated capabilities through the **Power User** multi-select field on the User record.

## Power User values

| Value | Elevated capability |
| --- | --- |
| **CPQ** | Full access to all quote configuration options, including pausing the rules engine during edit |
| **Approvals** | View and act on any approval in the org, not only assigned approvals |
| **Contracts** | Void Contracts from the Contracts UI |
| **Proposals** | Override View Sections with quote redlines; generate Word document proposals |

Power User is additive to permission sets. Users still need **Cotiza CPQ User** or **Cotiza CPQ Admin** assigned.

## CPQ Power User

CPQ Power Users see additional controls in the quote configuration UI:

- **Pause Rules** — temporarily disable the rules engine while editing
- Full admin configuration visibility within the quote wizard

Use for CPQ administrators debugging playbooks in production or power users who need unrestricted quote editing.

## Approvals Power User

Approvals Power Users can approve or reject any pending approval in the Approvals Hub, regardless of assignment. Useful for deal desk or escalation teams.

## Contracts Power User

Contracts Power Users can **Void** contracts from the Contract table. Voiding marks a contract inactive while preserving history.

## Proposals Power User

Proposals Power Users can:

- Create **View Section Overrides** (redlines) on individual Quotes
- Generate **Word** format proposals in addition to PDF

Redline sections override base Playbook View Sections for one-off customer documents without changing the Playbook configuration.

## Assignment

1. Navigate to the User record in Setup
2. Edit the **Power User** field
3. Select one or more values
4. Save

4. Save

See [User](../objects/admin/user.md) for field reference.

## Related guides

- [Permissions](../getting-started/permissions.md)
- [View Sections and Proposals](./view-sections-proposals.md)
- [Acting as an Approver](../user-guide/acting-as-approver.md)
