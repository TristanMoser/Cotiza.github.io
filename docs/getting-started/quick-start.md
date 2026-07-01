# Quick Start

After [installing](./installation.md) Cotiza CPQ, follow this guide for a step-by-step walkthrough of the minimum configuration needed to create your first Quote.

## Configuration checklist

| Step | Section |
| --- | --- |
| Assign Cotiza CPQ Admin permission set | [Step 1](#1-assign-admin-permissions) |
| Create System Settings record | [Step 2](#2-create-system-settings) |
| Configure products and price books | [Step 3](#3-configure-price-books) |
| Create your first Playbook | [Step 4](#4-configure-a-playbook) |
| Create a test Quote | [Step 5](#5-create-a-quote) |
| Copy configuration between orgs (optional) | [Sandbox Seed Data](./sandbox-seed-data.md) |

## 1. Assign admin permissions

Some CPQ configurations may require access to Salesforce Setup, but most can be accomplished using regular Salesforce data provided by CPQ. Before beginning configuration, ensure that whoever is assisting with CPQ setup has the **Cotiza CPQ Admin** permission set assigned.

See [Permissions](./permissions.md) for details on permission sets.

![Description](/img/screenshots/permission-set-assignment-admin.png)

## 2. Create System Settings

1. Open the App Launcher and search for **Cotiza CPQ System Settings**.
2. Select **New** to create your System Settings record.
3. Populate at minimum the **Name** field. You can update other fields later as you refine your configuration.

See [CPQ System Settings](../objects/admin/system_settings__c.md) for all available fields.

![Description](/img/screenshots/system-settings-new.png)

## 3. Configure price books

It is very likely that you will want to sell products in your business process. You may already have this defined in an existing Pricebook2 record, or you may decide to create new price book records for your CPQ implementation.

Whatever your scenario, take some time to ensure your products and price book entries are configured before building playbooks.

:::note
Permissions to modify Pricebook2, PricebookEntry, and Product2 objects must be handled in your org by your Salesforce admins. Cotiza permission sets provide additive access only.
:::

See [Price Book Entry](../objects/admin/pricebookentry.md) for field reference.

If your pricing is more complex than price × quantity, you may not want to rely solely on the PricebookEntry UnitPrice field. Create **Pricing Set** and **Pricing Threshold** records to build more complex pricing structures.

- [Pricing Set](../objects/admin/pricing_set__c.md)
- [Pricing Threshold](../objects/admin/pricing_threshold__c.md)

## 4. Configure a playbook

1. Open the App Launcher and search for **Cotiza Playbooks**.
2. Select **New** to create a new Playbook record.
3. Populate the required fields. You can modify them at any time to adjust your operating motion.

See [How Many Playbooks?](../admin-guide/how-many-playbooks.md) for guidance on playbook design.

See [Playbook](../objects/admin/playbook__c.md) for all available fields.

![Description](/img/screenshots/playbook-new.png)

## 5. Create a quote

You now have everything you need to create a Quote.

1. Ensure you have an Opportunity record.
2. Open the App Launcher and search for **Cotiza CPQ**.
3. Select the Opportunity where you would like to create a Quote.
4. Click **Create +** in the Quotes table to start the Quote creation process.
5. Click **Save**.

![Description](/img/screenshots/cpq-by-opportunity-quote-saved.png)

## Next steps

After creating your first Quote, continue customizing your implementation:

- [Configuration](../admin-guide/configuration.md) — admin object overview
- Configure [Playbook Questions](../objects/admin/playbook_question__c.md) and [Playbook Rules](../objects/admin/playbook_rule__c.md)
- [How Many Playbooks?](../admin-guide/how-many-playbooks.md) — playbook design guidance
- [Rule Evaluation](../admin-guide/rule-evaluation.md) — automation timing and order
- [Approvals](../admin-guide/approvals.md) — approval workflow setup
- [UI Components](../ui-components/overview.md) — tabs and Lightning components
- Update Pricebook2 records to expand product offerings
