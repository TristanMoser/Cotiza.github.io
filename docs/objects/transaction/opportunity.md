# Opportunity

Standard SFDC Opportunity object. Parent of Quote records.

| API Name | Label | Description |
| --- | --- | --- |
| `Adjustment_Type_Override__c` | Adjustment Type | Override to denote type of Contract adjustment the Opportunity outlines. If populated, takes precedence over value on synced Quote |
| `Adjustment_of_Contract_Override__c` | Adjustment of Contract | Override to denote the Contract of which the Opportunity is an adjustment. If populated, takes precedence over value on synced Quote |
| `Create_Contract__c` | Create Contract | Automation flag to create Contract and Entitlements based on Synced Quote when value moved from FALSE to TRUE. |
| `Lock_CPQ__c` | Lock CPQ | Determines if CPQ is locked and therefore no edits can be made |
| `Synced_Quote_Adjustment_of_Contract__c` | Synced Quote Adjustment of Contract | Internal logic helper field to facilitate Cotiza Contract updates |
