# Contract

Standard SFDC Contract object. Representation of Opportunity/Quote after deal finalization.

| API Name | Label | Description |
| --- | --- | --- |
| `Adjusted_by_Contract__c` | Adjusted by Contract | Contract that holds this Contract's adjustment |
| `Adjustment_Type__c` | Adjustment Type | Type of adjustment the Contract performed |
| `Adjustment_of_Contract__c` | Adjustment of Contract | Contract of which this Contract is an adjustment |
| `Contract_Status__c` | Status | Current status of Contract |
| `End_Date__c` | End Date | Latest end date of Contract Entitlements (Defaulted to Quote.Cotiza__End_Date__c on creation) |
| `IsVoid__c` | Is Void | Override to mark Contract as having been voided |
| `Latest_Amendment_Opportunity__c` | Latest Amendment Opportunity | Latest Opportunity that amended the Contract (if Amendments are configured to maintain existing Contract) |
| `Opportunity__c` | Opportunity | Original Opportunity that generated Contract |
| `Playbook__c` | Playbook | Playbook used to configure Contract |
| `Quote__c` | Quote | Original synced Quote that generated Contract |
| `Start_Date__c` | Start Date | Earliest start date of Contract Entitlements (Defaulted to Quote.Cotiza__Start_Date__c on creation) |
| `Total__c` | Total | SUM of Total Price for all Contract Entitlements (Defaulted to Quote.Cotiza__Total_Price__c on creation) |
