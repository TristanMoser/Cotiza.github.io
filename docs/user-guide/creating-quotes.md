# Creating Quotes

This guide explains how sales users create and configure Quotes in Cotiza CPQ.

## Prerequisites

- **Cotiza CPQ User** permission set assigned
- An Opportunity record for the deal
- At least one active Playbook configured by your admin
- Products available in the Playbook's price book

## Open Cotiza CPQ

**Option A — App tab**

1. Open the App Launcher.
2. Search for **Cotiza CPQ**.
3. Select an Opportunity (recently viewed or keyword search).

**Option B — Record page**

If your admin placed **Cotiza CPQ Container** on the Opportunity page, open the Opportunity directly—the CPQ UI loads with the Opportunity pre-selected.

See [UI Components](../ui-components/overview.md).

![Description](/img/screenshots/app-launcher-Cotiza-CPQ.png)

## Create a Quote

1. In the Quotes table, click **Create +**.
2. Select a **Playbook** if prompted (or use the default from System Settings).
3. Work through **Question Groups**—answer required prompts.
4. Review products in the **Product Summary** (added manually or by rules).
5. Check the **Approval Summary** for required approvals.
6. Click **Save**.

![Description](/img/screenshots/cpq-playbook-approval-needed.png)

## During configuration

### Playbook questions

Questions appear in groups defined by your admin. Behavior varies by configuration:

- **Required** questions must be answered before save
- **Hidden** questions may be populated automatically by rules
- **Read-only** questions display calculated values
- **Record lookup** questions let you search and select Salesforce records

See [Playbook Design](../admin-guide/playbook-design.md) (admin reference).

### Rules engine

As you answer questions and add products, Playbook Rules may automatically:

- Add or remove products
- Stamp answer values
- Show or hide additional questions
- Adjust pricing fields

Changes happen in real time after each interaction.

### Term and dates

Quote term and start/end dates may be pre-populated from Playbook defaults. End date editability depends on Playbook configuration. End dates are always locked for Contract Amendments.

## After saving

| Next step | Guide |
| --- | --- |
| Add or adjust products | [Quote Line Items](./quote-line-items.md) |
| Submit for approval | [Submitting for Approval](./submitting-approvals.md) |
| Generate proposal | [Generating Proposals](./generating-pdfs.md) |
| Sync to Opportunity | [Managing Quotes](./managing-quotes.md) |

## Related reference

- [Quote](../objects/transaction/quote.md)
- [Playbook](../objects/admin/playbook__c.md)
- [Workflow Overview](./workflow-overview.md)
