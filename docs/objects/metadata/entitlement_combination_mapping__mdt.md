# Entitlement Combination Mapping

Facilitates field mappings when Contract Entitlement records are combined upon Contract adjustment.

| API Name | Label | Description |
| --- | --- | --- |
| `Custom_Operation_Formula__c` | Custom Operation Formula | Custom formula to be calculated when the Operation value is **Custom** or **Sum Product**. If populated for **Custom**, the Entitlement Field field is disregarded. Can be any valid, simple expression with numbers, standard operators (+ - * /), comparison operators (===, !==, ==, !=, <, >, <=, >=), ternary expressions (? :), parentheses, and valid piped information. Cotiza__Contract_Entitlement__c fields can be piped in using \{%Field_API_Name%\} |
| `Entitlement_Field__c` | Entitlement Field | Target Contract Entitlement field to populate when entitlements are combined. |
| `Field_Type__c` | Field Type | **Required.** Denotes the type of field being operated upon. |
| `Operation__c` | Operation | **Required.** Determines how values should be combined when multiple Entitlement records map to one Entitlement. Picklist values: **Average**, **Custom**, **Min**, **Max**, **Newest**, **Oldest**, **Sum**, **Sum Product**. |

## Operation values

| Operation | Behavior |
| --- | --- |
| **Sum** | Add numeric values across combined entitlements |
| **Sum Product** | Evaluate the **Custom Operation Formula** for each adjustment entitlement and sum the results |
| **Min / Max** | Take the minimum or maximum value |
| **Newest / Oldest** | Take the value from the newest or oldest entitlement |
| **Average** | Average numeric values |
| **Custom** | Evaluate a single **Custom Operation Formula** using piped entitlement field tokens |
