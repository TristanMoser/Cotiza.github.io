# Configuration

This section is the starting point for Cotiza CPQ administrators. Use the guides below in recommended order for a new implementation.

## Implementation sequence

| Order | Task | Guide |
| --- | --- | --- |
| 1 | Assign admin permissions | [Permissions](../getting-started/permissions.md) |
| 2 | Copy configuration between orgs (optional) | [Sandbox Seed Data](../getting-started/sandbox-seed-data.md) |
| 3 | Create System Settings | [System Settings](./system-settings.md) |
| 3 | Configure products and pricing | [Products and Pricing](./products-and-pricing.md) |
| 4 | Design playbooks | [Playbook Design](./playbook-design.md) |
| 5 | Build scenarios and rules | [Scenarios](./scenarios-and-criteria.md), [Rules Cookbook](./rules-cookbook.md) |
| 6 | Configure approvals | [Approvals](./approvals.md) |
| 7 | Build proposals | [View Sections](./view-sections-proposals.md) |
| 8 | Set field mappings | [Field Mappings](./field-mappings.md) |
| 9 | Configure contracts | [Contracts Lifecycle](./contracts-lifecycle.md) |
| 10 | Assign users and power users | [Power Users](./power-users.md) |

For a minimal first Quote, start with the [Quick Start](../getting-started/quick-start.md).

## Configuration layers

### System Settings

Org-wide defaults for tables, actions, contract behavior, and proposal options. One record per org implementation.

### Playbook

The core configuration container—questions, rules, approvals, and view sections all belong to a Playbook linked to a Price Book.

### Product catalog

Products, price books, price book entries, and optional pricing sets/thresholds.

### Custom metadata

Deploy field mappings for Quote sync and contract entitlement creation.

## Key admin objects

| Object | Role |
| --- | --- |
| [System Settings](../objects/admin/system_settings__c.md) | Org-wide CPQ defaults |
| [Playbook](../objects/admin/playbook__c.md) | Operating motion container |
| [Playbook Question](../objects/admin/playbook_question__c.md) | User input |
| [Playbook Scenario](../objects/admin/playbook_scenario__c.md) | Conditions |
| [Playbook Rule](../objects/admin/playbook_rule__c.md) | Automation |
| [Playbook Approval](../objects/admin/playbook_approval__c.md) | Approval requirements |
| [Playbook View Section](../objects/admin/playbook_view_section__c.md) | Proposal/email layout |
| [Pricing Set](../objects/admin/pricing_set__c.md) | Tiered pricing |

See [Object Model Overview](../objects/overview.md) for the complete reference.

## Design decisions

- [How Many Playbooks?](./how-many-playbooks.md) — single vs. per-price-book strategy
- [Rule Evaluation](./rule-evaluation.md) — timing and execution order
- [Pricing Rules](./pricing-rules.md) — pricing automation patterns
