# Quote Approval Step

Output for Playbook Approver Group from a Quote Playbook configuration.

| API Name | Label | Description |
| --- | --- | --- |
| `Approval_Order__c` | Approval Order | Order in which Step should be enforced in its approval. Lower numbers execute first. Approvers in Step will not be submitted for approval until all previous Steps are approved. |
| `Approvers_Approved__c` | # Approvers Approved | Current number of approvers that have approved the Step |
| `Approvers_Rejected__c` | # Approvers Rejected | Current number of approvers that have rejected the Step |
| `Playbook_Approver_Group__c` | Playbook Approver Group | Group that dictates how this Step is approved |
| `Quote_Approval__c` | Quote Approval | Quote Approval to which the Step belongs |
| `Status__c` | Status | Current status of Step on Approval |
| `Total_Approvers__c` | Total Approvers | Total number of approvers in the Step |
