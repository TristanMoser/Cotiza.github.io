# Field Mappings

Cotiza CPQ uses Custom Metadata Types to map field values between records during sync and contract creation. Package defaults are embedded in Apex; orgs can add or override mappings via Custom Metadata records.

## Mapping types

| Custom Metadata Type | When it runs | Maps |
| --- | --- | --- |
| [Opportunity Field Mapping](../objects/metadata/opportunity_field_mapping__mdt.md) | Quote sync | Quote → Opportunity |
| [OppLineItem Field Mapping](../objects/metadata/opplineitem_field_mapping__mdt.md) | Quote sync | QuoteLineItem → OpportunityLineItem |
| [Entitlement Field Mapping](../objects/metadata/entitlement_field_mapping__mdt.md) | Contract creation | OpportunityLineItem → Contract Entitlement |
| [Entitlement Combination Mapping](../objects/metadata/entitlement_combination_mapping__mdt.md) | Contract amendment | Multiple entitlements → one entitlement |

## Opportunity Field Mapping

Deploy records that specify:

- **Quote Field** — source field on Quote
- **Opportunity Field** — target field on Opportunity

Used when a user syncs a Quote to its parent Opportunity.

## OppLineItem Field Mapping

Maps Quote Line Item fields to Opportunity Product fields during sync. Ensures CPQ-specific pricing, quantity, and custom fields flow to the Opportunity.

## Entitlement Field Mapping

When **Create Contract** fires on an Opportunity, Opportunity Products become Contract Entitlements. Entitlement Field Mapping controls which OLI fields copy to entitlement fields.

Standard Cotiza fields map automatically; custom mappings extend this for org-specific fields.

## Entitlement Combination Mapping

During contract amendments, multiple entitlement records may merge. Combination mappings define how to resolve conflicting values:

| Operation | Use when |
| --- | --- |
| **Sum** | Quantities or totals should aggregate |
| **Max / Min** | Take boundary values (e.g., latest end date = Max) |
| **Newest / Oldest** | Take value from most recent or earliest record |
| **Custom** | Formula with piped field tokens |

Example: discount percentage calculated as `{%Cotiza__Base_List_Price__c%} !== 0 ? 1 - ({%Cotiza__Base_Unit_Price__c%} / {%Cotiza__Base_List_Price__c%}) : 0`

## Deployment

1. Create Custom Metadata records in Setup (or deploy via metadata API)
2. Use fully qualified API names including the `Cotiza__` namespace
3. Test sync and contract creation in a sandbox before production

Default mappings ship in `Static_Values.cls` and cover standard Cotiza pricing, quantity, date, and product reference fields.

## Related guides

- [Managing Quotes](../user-guide/managing-quotes.md) — sync workflow
- [Contracts Lifecycle](./contracts-lifecycle.md) — entitlement creation
