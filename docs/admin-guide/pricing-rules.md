# Pricing Rules

Cotiza CPQ supports flexible pricing through a combination of standard PricebookEntry records, Pricing Sets, and Playbook Rules.

## Standard price book pricing

The simplest pricing model uses the **UnitPrice** field on PricebookEntry records. When a product is added to a Quote, CPQ uses the list price from the Price Book associated with the Playbook.

See [Price Book Entry](../objects/admin/pricebookentry.md) for field reference.

## Tiered pricing with Pricing Sets

When pricing is more complex than price × quantity, use **Pricing Set** and **Pricing Threshold** records:

1. Create a [Pricing Set](../objects/admin/pricing_set__c.md) that defines which field to tier on and how tiers produce the line item Total Price.
2. Add [Pricing Threshold](../objects/admin/pricing_threshold__c.md) records for each tier range.
3. Reference the Pricing Set from your Playbook or product configuration as needed.

Custom formulas on Pricing Sets and Pricing Thresholds support comparison operators (`===`, `!==`, `==`, `!=`, `<`, `>`, `<=`, `>=`) and ternary expressions (`? :`) in addition to standard arithmetic and piped CPQ tokens.

## Dynamic pricing with Playbook Rules

Playbook Rules can calculate and stamp pricing values dynamically using Rule Actions and Calculation Items. Common patterns include:

- Calculating totals from product line items
- Applying discounts based on Scenario conditions
- Deriving metrics such as ARR from quote term and product totals

See [Rule Evaluation](./rule-evaluation.md) for execution order guidance and a worked ARR calculation example.

## Related objects

| Object | Purpose |
| --- | --- |
| [Playbook Rule](../objects/admin/playbook_rule__c.md) | Container for pricing automation logic |
| [Playbook Rule Action](../objects/admin/playbook_rule_action__c.md) | Individual pricing or calculation action |
| [Playbook Rule Calculation Item](../objects/admin/playbook_rule_calculation_item__c.md) | Value source for calculations |
| [Quote Line Item](../objects/transaction/quotelineitem.md) | Output record for priced products |
