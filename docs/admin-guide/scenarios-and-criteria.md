# Scenarios and Criteria

Playbook Scenarios define conditions that control Rules, Approvals, and View Sections. Each Scenario is evaluated from one or more **Criteria** records.

## Scenario overview

A [Playbook Scenario](../objects/admin/playbook_scenario__c.md) groups criteria with boolean logic. When the Scenario evaluates to TRUE, dependent configuration can fire.

Scenarios are referenced by:

- [Playbook Rules](../objects/admin/playbook_rule__c.md)
- [Playbook Approvals](../objects/admin/playbook_approval__c.md)
- [Playbook View Sections](../objects/admin/playbook_view_section__c.md)
- Individual [Rule Actions](../objects/admin/playbook_rule_action__c.md) (optional per-action Scenario)

## Building criteria

Each [Playbook Scenario Criterion](../objects/admin/playbook_scenario_criterion__c.md) compares a source value against a target using an operator.

### Criterion sources

| Source | Evaluates |
| --- | --- |
| **Question** | A Playbook Question answer |
| **Product** | Aggregated values from Quote Line Items |
| **Price book entry product** | Values from PricebookEntry records (not valid for View Section evaluation) |
| **System Value** | Built-in CPQ values (quote term, dates, etc.) |

### Comparison operators

Criteria support standard comparisons (equals, not equals, greater than, less than, contains, etc.) depending on field type. Multiple criteria combine using boolean expression logic defined on the Scenario.

### Inverse scenarios

Enable **Inverse Scenario** on Rules, Approvals, or View Sections to trigger when the linked Scenario is **not** met.

## Scenario evaluation in the UI

The rules engine (`configQuoteEvaluator`) evaluates scenarios client-side after each user interaction. Results drive:

- Which Rules execute (based on **Execute When** timing)
- Which Approvals appear in the Approval Summary
- Which View Sections appear in proposal previews

See [Rule Evaluation](./rule-evaluation.md) for execution timing details.

## Common patterns

### Discount threshold approval

Create a Scenario where a discount Question answer exceeds a threshold. Link it to a Playbook Approval requiring manager sign-off.

### Conditional product sections

Create a Scenario where a product exists on the Quote. Link View Sections that only show relevant product tables.

### Rule-gated automation

Create a Scenario tied to a picklist answer. Link Rules that add products or stamp values only when that answer is selected.

## Debugging scenarios

1. Verify each Criterion source references the correct Question or product field
2. Check **Inverse Scenario** flags on dependent records
3. Use **CPQ Power User** to pause rules and inspect intermediate answer values
4. Review **Execution Order** on Rules that may change values mid-evaluation

![Description](/img/screenshots/playbook-scenario-criteria.png)

## Related reference

- [Playbook Scenario](../objects/admin/playbook_scenario__c.md)
- [Playbook Scenario Criterion](../objects/admin/playbook_scenario_criterion__c.md)
- [Rules Cookbook](./rules-cookbook.md)
