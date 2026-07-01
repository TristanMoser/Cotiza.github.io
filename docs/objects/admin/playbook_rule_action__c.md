# Playbook Rule Action

Individual action that can modify Question answers, line items and more.

| API Name | Label | Description |
| --- | --- | --- |
| `Action_Type__c` | Action Type | Type of action to be performed on question, question group, product, or system value |
| `All_Products__c` | Evaluate All Products | If true, all products in the playbook's price book will be acted upon |
| `Calculation_Type__c` | Calculation Type | How to determine the calculated value if Value Source Type is 'Dynamic' |
| `Entitlement_Additions_Behavior__c` | Entitlement Additions Behavior | When to execute product action when considering products added from a contract entitlement |
| `Execution_Order__c` | Execution Order | Order in which action should be executed in its rule. Lower numbers execute first |
| `Field_Value_Boolean__c` | Field value (Boolean) | Static value to populate in target if target type is 'Boolean' and Value Source Type is 'Static' |
| `Field_Value_Currency__c` | Field Value (Currency) | Static value to populate in target if target type is 'Currency' and Value Source Type is 'Static' |
| `Field_Value_Date__c` | Field Value (Date) | Static value to populate in target if target type is 'Date' and Value Source Type is 'Static' |
| `Field_Value_Decimal__c` | Field Value (Decimal) | Static value to populate in target if target type is 'Decimal' and Value Source Type is 'Static' |
| `Field_Value_Integer__c` | Field Value (Integer) | Static value to populate in target if target type is 'Integer' and Value Source Type is 'Static' |
| `Field_Value_Text__c` | Field Value (Text) | Static value to populate in target if target type is 'Text' and Value Source Type is 'Static' |
| `Inverse_Scenario__c` | Inverse Scenario | If true, the linked scenario must NOT be met in order for the action to execute. |
| `IsActive__c` | Is Active | Determines if action is active and should be executed in rule |
| `Manual_Additions_Behavior__c` | Manual Additions Behavior | When to adjust product when considering products added manually by a User |
| `Multiplicity_Behavior__c` | Multiplicity Behavior | Behavior in the event that multiple records are found for adjustment. 'Adjust critieria contributing records only' will only consider records that were evaluated with a successful evaluation in this action's scenario's criteria. For 'Add product' actions, Entitlement or Price book entry records are used as criteria contributing records. For 'Adjust product field', 'Adjust product field editability', and 'Remove product' actions, added Products are used as criteria contributing records. |
| `Numeric_Math_Operator__c` | Numeric Math Operator | If populated, Math operation to be performed on calculated value for Numeric Calculations |
| `Playbook_Question_Group__c` | Playbook Question Group | Playbook Question Group to be acted upon |
| `Playbook_Question__c` | Playbook Question | Playbook Question to be acted upon |
| `Playbook_Rule__c` | Playbook Rule | Playbook Rule in which Action is executed |
| `Playbook_Scenario__c` | Scenario | Scenario that must be met in order for action to execute. If no record is linked, the Scenario is assumed to be met. |
| `Prevent_Post_Action_Recalculation__c` | Prevent Post Action Recalculation | By default, after an action is executed, date and pricing information will be recalculated so that subsequent actions, rules and/or approvals have up to date information. If true, that recalculation is not performed. |
| `Product_Adjustment_Field_Type__c` | Product Adjustment Field Type | Type of field the Product Adjustment Field represents. Directly influences which static Field Value field is used. |
| `Product_Adjustment_Field__c` | Product Adjustment Field | Field on product that should be adjusted. Any QuoteLineItem field API name can be placed here and it will be saved to the product's QuoteLineItem record upon CPQ save. Exceptions include: 'PricebookEntry.Cotiza__Max_Manual_Additions__c' to adjust manual additions of a given product. |
| `Product_Adjustment_Target_Rule_Action__c` | Product Adjustment Target Rule Action | If populated, the product adjustment will only be applied to products added by the action specified here. If not populated, all occurances of the desired products will be adjusted Note this field is only relevant if the 'Manual Additions Behavior' field is set to 'Do Not Calculate Manual Additions' |
| `Product__c` | Product | Product2 record that will be acted upon. Note there must be a price book entry in the playbook's price book |
| `Question_Adjustment_Field_Type__c` | Question Adjustment Field Type |  |
| `Question_Adjustment_Field__c` | Question Adjustment Field | Field on question that should be adjusted |
| `Question_Group_Adjustment_Field_Type__c` | Question Group Adjustment Field Type |  |
| `Question_Group_Adjustment_Field__c` | Question Group Adjustment Field | Field on question group that should be adjusted |
| `System_Value__c` | System Value | System Value to be updated |
| `Value_Source_Type__c` | Value Source Type | Static sources use unchanging values input in the action fields. Dynamic sources use values from other sources as calculation items |
