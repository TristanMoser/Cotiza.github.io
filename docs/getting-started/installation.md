# Installation

## Prerequisites

Before installing Cotiza CPQ, confirm your org meets these requirements:

| Requirement | Details |
| --- | --- |
| Salesforce edition | Professional, Enterprise, Unlimited, or Developer Edition |
| Lightning Experience | Must be enabled |
| Quote object | Enable Quotes in **Setup → Quote Settings** |
| Admin access | System Administrator profile or equivalent for installation |

## Install from AppExchange

1. Open the Cotiza CPQ listing on the [Salesforce AppExchange](https://appexchange.salesforce.com/).
2. Click **Get It Now** and authenticate to your target org.
3. Choose **Install for Admins Only** for initial installation (recommended).
4. Approve third-party access when prompted.
5. Wait for the package installation email confirmation.

:::tip Sandbox first
Install and configure in a sandbox before deploying to production.
:::

## Post-installation checklist

| Step | Guide |
| --- | --- |
| Assign Cotiza CPQ Admin permission set | [Permissions](./permissions.md) |
| Create System Settings record | [Quick Start](./quick-start.md) |
| Enable Quote object (if not already) | Salesforce Setup → Quote Settings |
| Add Cotiza CPQ Container to Opportunity page | [UI Components](../ui-components/overview.md) |
| Configure products, price books, and playbook | [Quick Start](./quick-start.md) |
| Assign Cotiza CPQ User to sales team | [Permissions](./permissions.md) |
| Validate end-to-end with test Quote | [Workflow Overview](../user-guide/workflow-overview.md) |
| Copy configuration between orgs (optional) | [Sandbox Seed Data](./sandbox-seed-data.md) |

## Estimated installation time

| Phase | Time |
| --- | --- |
| Package install | 5–15 minutes |
| Permission and UI setup | 15–30 minutes |
| Initial playbook configuration | 1–4 hours (varies by complexity) |

## Upgrades

When a new package version is available on AppExchange:

1. Review release notes for breaking changes
2. Upgrade in sandbox first
3. Run regression tests on active playbooks
4. Upgrade production during a maintenance window

See [Release Notes](../release-notes/v1-0-0.md).

## Uninstall considerations

Uninstalling removes Cotiza metadata. Export playbook configuration and document custom metadata mappings before uninstalling from production orgs.
