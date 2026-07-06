# Playbook Rule Calculation Item

Reference used to dynamically pull and combine information for a Rule Action.

| API Name | Label | Description |
| --- | --- | --- |
| `All_Products__c` | Evaluate All Products | If true, all products in the playbook's price book will be considered for calculation |
| `Calculation_Source__c` | Calculation Source | Source of item's value |
| `Entitlement_Additions_Behavior__c` | Entitlement Additions Behavior | When to calculate product when considering products added from a contract entitlement |
| `Entitlement_Calculation_Field_Type__c` | Entitlement Calculation Field Type | Type of field the Entitlement Calculation Field represents |
| `Entitlement_Calculation_Field__c` | Entitlement Calculation Field | Field name from Entitlement housing calculation value. 'Cotiza__Contract_Entitlement__c' API fields names are valid. The only valid related object is: 'Cotiza__Product__r' (Please enter as object.field if using a related object). |
| `Execution_Order__c` | Execution Order | Order in which item should be evaluated in its action calculation. Lower numbers execute first |
| `Formula__c` | Formula | Formula used if calculation source is 'Formula'. Valid only for numbers, standard operators (+ - * /), comparison operators (===, !==, ==, !=, <, >, <=, >=), ternary expressions (? :), and piped info: Question Answers (Record Lookup questions are not supported): \{%Question.Variable_Name%\} or \{%ContractQuestion.Variable_Name%\}. Products: \{%Product.Product2_18CharacterID%\}, \{%AllProducts%\}, \{%ContractProduct.Product2_18CharacterID%\} or \{%AllContractProducts%\}. All calculation field and behavior fields are respected when piping in values. |
| `Inverse_Scenario__c` | Inverse Scenario | If true, the linked scenario must NOT be met in order for the calculation item to run. |
| `IsActive__c` | Is Active | Determines if item is active and should be used in action calculation |
| `Manual_Additions_Behavior__c` | Manual Additions Behavior | When to calculate product when considering products added manually |
| `Multiplicity_Behavior__c` | Multiplicity Behavior | Behavior in the event that multiple records are found for calculation. 'Calculate critieria contributing records only' will only consider records that were evaluated with a successful evaluation in this item's criteria. |
| `Playbook_Question__c` | Playbook Question | Question in which answer is taken for calculation |
| `Playbook_Rule_Action__c` | Playbook Rule Action | Action in which item is used for calculation |
| `Playbook_Scenario__c` | Scenario | Scenario that must be met in order for the calculation item to run. If no record is linked, the Scenario is assumed to be met. |
| `Product_Action_Match_Behavior__c` | Product Action Match Behavior | When to calculate product when considering products or entitlements matching the product being actioned upon |
| `Product_Calculation_Field_Type__c` | Product Calculation Field Type | Type of field the Product Calculation Field represents |
| `Product_Calculation_Field__c` | Product Calculation Field | Attribute name from Product housing calculation value. Any QuoteLineItem Field API name is also valid given that CPQ has stamped the value. Valid related objects are: 'PricebookEntry', 'Product2' and 'Cotiza__Contract_Entitlement__r' (Please enter as object.field if using a related object). |
| `Product_Calculation_Target_Rule_Action__c` | Product Calculation Target Rule Action | If populated, the product value will only be considered in the calculation for the desired product added by the action specified here. If not populated, all occurances of the desired product will have their values considered. Note this field is only relevant if the 'Manual Additions Behavior' field is set to 'Do Not Calculate Manual Additions' |
| `Product_Is_Entitlement__c` | Product Is Entitlement | If true, the product value will be evaluated based on how it is configured in its entitlement for the contract being upgraded |
| `Product__c` | Product | Product in which value is taken for calculation |
| `Question_Is_Contract_Answer__c` | Question Is Contract Answer | If true, the question will be evaluated based on how it is configured in the contract being upgraded |
| `Record_Lookup_Field_Type__c` | Record Lookup Field Type | Type of field the Record Lookup Field represents |
| `Record_Lookup_Field__c` | Record Lookup Field | Field API name from record housing calculation value. Field must be included in the question's query string in order to have a value populated. |
| `Static_Value_Boolean__c` | Static Value (Boolean) | Value used for calculation if static value type is 'Boolean' |
| `Static_Value_Currency__c` | Static Value (Currency) | Value used for calculation if static value type is 'Currency' |
| `Static_Value_Date__c` | Static Value (Date) | Value used for calculation if static value type is 'Date' |
| `Static_Value_Decimal__c` | Static Value (Decimal) | Value used for calculation if static value type is 'Decimal' |
| `Static_Value_Integer__c` | Static Value (Integer) | Value used for calculation if static value type is 'Integer' |
| `Static_Value_Text__c` | Static Value (Text) | Value used for calculation if static value type is 'Text' |
| `Static_Value_Type__c` | Static Value Type | Type of static value to use for calculation |
