# Custom Metadata Types

Custom metadata types provide deployment-friendly configuration for Cotiza CPQ. They are primarily used to facilitate field mappings from one record to another upon sync or creation.

## Types

| Type | Description |
| --- | --- |
| [Opportunity Field Mapping](./opportunity_field_mapping__mdt.md) | Maps fields from a synced Quote to the corresponding Opportunity |
| [OppLineItem Field Mapping](./opplineitem_field_mapping__mdt.md) | Maps fields from QuoteLineItem to OpportunityLineItem records |
| [Entitlement Field Mapping](./entitlement_field_mapping__mdt.md) | Maps fields from OpportunityLineItem to Contract Entitlement records |
| [Entitlement Combination Mapping](./entitlement_combination_mapping__mdt.md) | Maps fields when Contract Entitlements are combined during Contract adjustment |

Standard Cotiza fields map automatically where applicable. Custom metadata records can override those defaults.
