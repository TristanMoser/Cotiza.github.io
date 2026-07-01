# Entitlement Combination Mapping

Facilitates field mappings when Contract Entitlement records are combined upon Contract adjustment.

| API Name | Label | Description |
| --- | --- | --- |
| `Custom_Operation_Formula__c` | Custom Operation Formula | Custom formula to be calculated when the Operation value is 'Custom'. If populated, the Entitlement Field field is disregarded. Can be any valid, simple expression with numbers, operators (+ - * /), and parentheses and valid piped information. Cotiza__Contract_Entitlement__c fields can be piped in using \{%Field_API_Name%\} |
| `Entitlement_Field__c` | Entitlement Field |  |
| `Field_Type__c` | Field Type | Denotes the type of field being operated upon. |
| `Operation__c` | Operation | Determines how values should be combined in the event that multiple Entitlement records should be mapped to one Entitlement. |
