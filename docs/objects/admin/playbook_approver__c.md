# Playbook Approver

Individual User that has power to approve/reject an Approval.

| API Name | Label | Description |
| --- | --- | --- |
| `Approver__c` | Approver | User to act as approver |
| `Inverse_Scenario__c` | Inverse Scenario | If true, the linked scenario must NOT be met in order for the approver to be enforced. |
| `IsActive__c` | Is Active | Determines if approver is active and should be enforced in group |
| `Manager_Approver_Level__c` | Manager Approver | Determines if the Approver should a the Manager of the Opportunity Owner. If present, overrides any User placed in the Approver field |
| `Playbook_Approver_Group__c` | Playbook Approver Group | Playbook Approver Group in which Approver is enforced |
| `Playbook_Scenario__c` | Scenario | Scenario that must be met in order for the approver to be enforced. If no record is linked, the Scenario is assumed to be met. |
