# Quote

Standard SFDC Quote object. Primary output record from a Playbook configuration.

| API Name | Label | Description |
| --- | --- | --- |
| `Adjustment_Type__c` | Adjustment Type | Type of Contract Adjustment the Quote outlines |
| `Adjustment_of_Contract__c` | Adjustment of Contract | Contract of which quote is an adjustment |
| `Approval_Status__c` | Approval Status | Current status of quote's approvlas |
| `Approval_Submitter__c` | Approval Submitter | User that submitted this quote for approval |
| `Clone_of_Quote__c` | Clone of Quote | Original Quote that was cloned to create this Quote |
| `End_Date__c` | End Date | Latest end date of Quote Line Items |
| `IsClone__c` | Is Clone | Tracks whether or not quote was created by cloning another quote in CPQ |
| `Notes_for_Approvers__c` | Notes for Approver(s) | Notes/Justification submitted to approver(s) |
| `Playbook_Status__c` | Playbook Status | Status of Playbook Configuration from CPQ. 'Incomplete' if there are required questions not populated or touched |
| `Playbook__c` | Playbook | Playbook used to configure quote in CPQ |
| `Shell_Quote__c` | Shell Quote | Tracks whether or not quote was a shell created to preview a proposal when editing quote in CPQ |
| `Start_Date__c` | Start Date | Earliest end date of Quote Line Items |
| `SubTotal_Price__c` | Subtotal Price | SUM of Sub Total Price for all Quote Line Items |
| `Total_Price__c` | Total Price | SUM of Total Price for all Quote Line Items |
