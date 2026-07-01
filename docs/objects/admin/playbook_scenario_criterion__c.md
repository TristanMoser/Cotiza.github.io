# Playbook Scenario Criterion

Individual criterion evaluation that contributes to the evaluation of a Playbook Scenario record.

| API Name | Label | Description |
| --- | --- | --- |
| `All_Products__c` | Evaluate All Products | If true, all added products will be evaluated. For 'Price book entry product', all active price book entries for the playbook's pricebook will be evaluated. |
| `Comparison_Operator__c` | Comparison Operator | Method in which the Criterion Source should be compared to the Comparison Value |
| `Comparison_Value_Boolean__c` | Comparison Value (Boolean) | If related source type is 'Boolean', the value here will be used for comparison against the source. |
| `Comparison_Value_Currency__c` | Comparison Value (Currency) | If related source type is 'Currency', the value here will be used for comparison against the source. |
| `Comparison_Value_Date__c` | Comparison Value (Date) | If related source type is 'Date', the value here will be used for comparison against the source. |
| `Comparison_Value_Decimal__c` | Comparison Value (Decimal) | If related source type is 'Decimal', the value here will be used for comparison against the source. |
| `Comparison_Value_Integer__c` | Comparison Value (Integer) | If related source type is 'Integer', the value here will be used for comparison against the source. |
| `Comparison_Value_Playbook_Question__c` | Comparison Value Playbook Question | Playbook Question housing dynamic comparison value for Criterion. If populated, will override any other comparison value. Record Lookup Questions are not supported. To evaluate correctly, ensure the corresponding Answer Type is compatible with the source value. |
| `Comparison_Value_Text__c` | Comparison Value (Text) | If related source type is 'Picklist', 'Multi-Select Picklist', 'Text', or 'Text Area', the value here will be used for comparison against the source. |
| `Criterion_Source__c` | Criterion Source | Source of Criterion's value. NOTE: 'Price book entry product' is not applicable to Scenarios being used for View Section evaluation. |
| `Entitlement_Additions_Behavior__c` | Entitlement Additions Behavior | When to evaluate 'Product' source when considering products added from a contract entitlement |
| `Entitlement_Field__c` | Entitlement Field | Attribute name from Entitlement housing source value. Any Cotiza__Contract_Entitlement__c Field API name is valid. The only valid related object is: 'Cotiza__Product__r' (Please enter as object.field if using a related object). |
| `Identifier__c` | Identifier | Identifier to which Scenario can map for custom evaluation logic. |
| `IsActive__c` | Is Active | Determines if criterion is active and should be evaluated for Scenario |
| `Manual_Additions_Behavior__c` | Manual Additions Behavior | When to evaluate 'Product' source when considering products added manually by a User |
| `Multiplicity_Behavior__c` | Multiplicity Behavior | Behavior in the event that multiple records are found for evaluation |
| `Playbook_Question__c` | Playbook Question | Playbook Question housing answer value from which Criterion gets its source when source is 'Question' |
| `Playbook_Scenario__c` | Playbook Scenario | Playbook Scenario in which Criterion is evaluated |
| `Price_Book_Entry_Field__c` | Price Book Entry Field | Attribute name from Price Book Entry housing source value when source is 'Price book entry product'. Any PricebookEntry Field API name is valid. The only valid related object is: 'Product2' (Please enter as object.field if using a related object). |
| `Product_Criterion_Target_Rule_Action__c` | Product Criterion Target Rule Action | If populated (when Manually added products are not being targeted), the product criterion will only be evaluated on products when added by the action specified here. |
| `Product_Field_Type__c` | Product Field Type | Type of field the Product/Price Book Entry/Entitlement Field represents |
| `Product_Field__c` | Product Field | Attribute from Product housing source value when source is 'Product' (not entitlements). Any QuoteLineItem Field API name is valid (only present in quote config if CPQ stamped the value). Valid related objects are: 'PricebookEntry', 'Product2' and 'Cotiza__Contract_Entitlement__r' (Please enter as object.field if using a related object). |
| `Product_Is_Entitlement__c` | Product Is Entitlement | If true, the products will be evaluated based on how they are configured in entitlements for the contract being upgraded |
| `Product__c` | Product | Product from which Criterion gets its source value when source is 'Product' |
| `Question_Is_Contract_Answer__c` | Question Is Contract Answer | If true, the question will be evaluated based on how it is configured in the contract being upgraded |
| `Record_Lookup_Field_Type__c` | Record Lookup Field Type | Type of field the Record Lookup Field represents |
| `Record_Lookup_Field__c` | Record Lookup Field | Field API Name on record(s) housed in the lookup question answer that should be accessed for the source value. |
| `System_Value_Source__c` | System Value Source | Which System Value Source should be referenced for criterion evaluation. NOTE: certain System Sources are irrelevant for criteria being referenced for a View Section and will automatically resolve to FALSE. |
