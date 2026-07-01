# Playbook Approver Group

Container for Playbook Approvers grouped into order segments within an Approval.

| API Name | Label | Description |
| --- | --- | --- |
| `Approval_Order__c` | Approval Order | Order in which group should be enforced in its approval. Lower numbers execute first. Approvers in group will not be submitted for approval until all previous groups are approved. |
| `Approvers_Required__c` | # of Approvers Required | Number of associated approver records needed for group to be approved. If the value is greater than # of associated approvers for a quote approval step, the total # of associated approvers will be used instead. |
| `Inverse_Scenario__c` | Inverse Scenario | If true, the linked scenario must NOT be met in order for the approver group to be enforced. |
| `IsActive__c` | Is Active | Determines if approver group is active and should be enforced in approval |
| `Playbook_Approval__c` | Playbook Approval | Playbook Approval in which the group is enforced |
| `Playbook_Scenario__c` | Scenario | Scenario that must be met in order for the approver group to be enforced. If no record is linked, the Scenario is assumed to be met. |
