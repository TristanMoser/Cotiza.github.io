# Quote Approver

Output for Playbook Approver from a Quote Playbook configuration.

| API Name | Label | Description |
| --- | --- | --- |
| `Approval_Emails_To_Send__c` | Approval Email(s) To Send | Approval Email scenarios in which an email should be sent. Submitted and Recalled emails go to the approver(s). Approved and Rejected emails go to the submitter. |
| `Approval__c` | Approval | Quote Approval to which the Approver belongs |
| `Approved_Date_Time__c` | Approved Date | Most recent date where status changed to Approved |
| `Approver__c` | Approver | User that is responsible for the Approver record |
| `Cancelled_Date_Time__c` | Cancelled Date | Most recent date where status changed to Cancelled |
| `Decision_Maker__c` | Decision Maker | User that ultimately approved/rejected/recalled/cancelled this Approver record |
| `Decision_Reason__c` | Decision Reason | Reason/Justification for user's decision to reject/approve the Approver record |
| `Playbook_Approver__c` | Playbook Approver | Approver that dictates how this Approver is configured |
| `Quote_Approval_Step__c` | Quote Approval Step | Quote Approval Step to which the Approver belongs |
| `Quote__c` | Quote | Quote to which the Approver belongs |
| `Recalled_Date_Time__c` | Recalled Date | Most recent date where status changed to Recalled |
| `Rejected_Date_Time__c` | Rejected Date | Most recent date where status changed to Rejected |
| `Require_Individual_Approval__c` | Require Individual Approval | By default any action by an approver on a quote approval record will transfer to all other approvals on the quote with the same approver. Selecting TRUE for this field will bypass that default behavior and require that the approvers for this approval explicitly approve this approval individually. |
| `Status__c` | Status | Current status of Approver on Step |
| `Submitted_Date_Time__c` | Submitted Date | Most recent date where status changed to Submitted |
