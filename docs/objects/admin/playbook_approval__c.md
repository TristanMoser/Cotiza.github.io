# Playbook Approval

Flag to oversee proper configuration within a Playbook.

| API Name | Label | Description |
| --- | --- | --- |
| `Approval_Emails_To_Send__c` | Approval Email(s) To Send | Approval Email scenarios in which an email should be sent. Submitted and Recalled emails go to the approver(s). Approved and Rejected emails go to the submitter. |
| `Inverse_Scenario__c` | Inverse Scenario | If true, the linked scenario must NOT be met in order for the approval to be enforced. |
| `IsActive__c` | Is Active | Determines if approval is active and should be enforced in playbook |
| `Label__c` | Label | Displayed label Users see in CPQ |
| `Persistent_Approval__c` | Persistent Approval | Determines if approval needs to be reapproved after it has been approved once, but the quote is edited. If TRUE, an approved approval does not need to be reapproved upon the quote being edited. |
| `Playbook_Scenario__c` | Scenario | Scenario that must be met in order for Approval to be enforced. If no record is linked, the Scenario is assumed to be met. |
| `Playbook__c` | Playbook | Playbook in which this approval is enforced |
| `Reason__c` | Reason | Reason Users wee for why this approval is being enforced |
| `Require_Individual_Approval__c` | Require Individual Approval | By default any action by an approver on a quote approval record will transfer to all other approvals on the quote with the same approver. Selecting TRUE for this field will bypass that default behavior and require that the approvers for this approval explicitly approve this approval individually. |
| `Require_Notes__c` | Require Notes | Determines if specific approval level notes are required for submission. |
