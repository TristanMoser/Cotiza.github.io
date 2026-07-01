# Playbook Rule

Container for Playbook Rule Actions to be performed under specific circumstances within a Playbook.

| API Name | Label | Description |
| --- | --- | --- |
| `Description__c` | Description | None |
| `Evaluate_When__c` | Execute When | When the rule should be executed according to how the linked Scenario evaluates. 'Evaluation Change' will only execute the rule when the linked Scenario evaluation changes. When changed to FALSE, CPQ will try to undo any changes previously made by a rule. 'Always' will cause the rule to execute after every update assuming that the linked Scenario evaluated to TRUE regardless of the actual evaluation. |
| `Execution_Order__c` | Execution Order | Order in which rule should be executed in its playbook. Lower numbers execute first |
| `Inverse_Scenario__c` | Inverse Scenario | If true, the linked scenario must NOT be met in order for the rule to execute. |
| `IsActive__c` | Is Active | Determines if rule is active and should be enforced in playbook |
| `Playbook_Scenario__c` | Scenario | Scenario that must be met in order for Rule to execute. If no record is linked, the Scenario is assumed to be met. |
| `Playbook__c` | Playbook | Playbook in which this rule is enforced |
