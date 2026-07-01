# Admin Objects

Admin objects are the configuration layer of Cotiza CPQ. They define playbooks, pricing structures, approval paths, and display behavior. Most admin records are created and maintained by users with the **Cotiza CPQ Admin** permission set.

## Recommended build order

1. [CPQ System Settings](./system_settings__c.md)
2. [Product](./product2.md) → [Price Book](./pricebook2.md) → [Price Book Entry](./pricebookentry.md)
3. [Pricing Set](./pricing_set__c.md) → [Pricing Threshold](./pricing_threshold__c.md) (if tiered pricing)
4. [Playbook](./playbook__c.md)
5. [Playbook Question Group](./playbook_question_group__c.md) → [Playbook Question](./playbook_question__c.md)
6. [Playbook Scenario](./playbook_scenario__c.md) → [Playbook Scenario Criterion](./playbook_scenario_criterion__c.md)
7. [Playbook Rule](./playbook_rule__c.md) → [Rule Action](./playbook_rule_action__c.md) → [Calculation Item](./playbook_rule_calculation_item__c.md)
8. [Playbook Approval](./playbook_approval__c.md) → [Approver Group](./playbook_approver_group__c.md) → [Approver](./playbook_approver__c.md)
9. [Playbook View Section](./playbook_view_section__c.md)

See [Configuration Guide](../../admin-guide/configuration.md) for narrative walkthroughs.

## Objects

| Object | Description |
| --- | --- |
| [CPQ System Settings](./system_settings__c.md) | Base configuration source for the CPQ Container, approval submitter, and more |
| [Playbook](./playbook__c.md) | High-level container that defines a specific operating motion |
| [Playbook Scenario](./playbook_scenario__c.md) | Scenario referenced by Rules, Approvals, and View Sections |
| [Playbook Scenario Criterion](./playbook_scenario_criterion__c.md) | Individual criterion that contributes to Scenario evaluation |
| [Playbook Question Group](./playbook_question_group__c.md) | Visual grouping container for Playbook Questions |
| [Playbook Question](./playbook_question__c.md) | User input prompt that drives Quote configuration |
| [Playbook Rule](./playbook_rule__c.md) | Container for Rule Actions executed under specific circumstances |
| [Playbook Rule Action](./playbook_rule_action__c.md) | Individual action that modifies answers, line items, and more |
| [Playbook Rule Calculation Item](./playbook_rule_calculation_item__c.md) | Dynamic value source used by Rule Actions |
| [Playbook Approval](./playbook_approval__c.md) | Approval flag that oversees proper Quote configuration |
| [Playbook Approver Group](./playbook_approver_group__c.md) | Ordered group of Approvers within an Approval |
| [Playbook Approver](./playbook_approver__c.md) | Individual user who can approve or reject |
| [Playbook View Section](./playbook_view_section__c.md) | Blueprint for Quote Proposals and Approval Emails |
| [Pricing Set](./pricing_set__c.md) | Container for tiered pricing thresholds |
| [Pricing Threshold](./pricing_threshold__c.md) | Individual number range within a Pricing Set |
| [Price Book](./pricebook2.md) | Standard Pricebook2 referenced by a Playbook |
| [Price Book Entry](./pricebookentry.md) | Standard PricebookEntry referenced by line items |
| [Product](./product2.md) | Standard Product2 referenced by line items |
| [User](./user.md) | Standard User object |

## Related guides

- [Quick Start](../../getting-started/quick-start.md) — initial admin configuration walkthrough
- [How Many Playbooks?](../../admin-guide/how-many-playbooks.md) — playbook design guidance
- [Rule Evaluation](../../admin-guide/rule-evaluation.md) — how Rules, Actions, and Calculation Items execute
