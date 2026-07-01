# Rule Evaluation

Playbook Rules drive dynamic behavior in Cotiza CPQ. Understanding when Rules run and how execution order works is essential for building reliable automation.

## How often should a Rule run?

Each Rule has an **Evaluate When** value that determines how often the Rule is considered for execution. Since each Rule is unique, they may benefit from running less often or only when a specific action occurs.

| Evaluate When | Behavior |
| --- | --- |
| **Always** | Run after every user interaction |
| **Always when TRUE** | Run after every user interaction where the associated Scenario is met |
| **On first evaluation** | Run exactly once when the Playbook is first loaded |
| **On first TRUE evaluation** | Run exactly once when the Scenario is first met |
| **Evaluation change** | Run after every user interaction that caused the associated Scenario's evaluation to change |
| **When TRUE with evaluation change** | Run after every user interaction that caused the associated Scenario's evaluation to change to being met |

:::note Always
An associated Scenario record is not respected when **Always** is used. The Rule acts as though the Scenario is always met.
:::

:::note Evaluation change
If the Scenario is no longer met, CPQ will try to undo any changes previously made by the Rule.
:::

See [Playbook Rule](../objects/admin/playbook_rule__c.md) for field reference.

## Why order matters

### Rules

After each user interaction, CPQ runs the Rules Engine to determine which Rules should be evaluated and executed. As each Rule runs, the current state of the Playbook changes. The Playbook may have different values when the first Rule runs versus when the nth Rule runs.

You may have Rules that depend on another Rule. For example, you might dynamically populate a value that is then referenced in another Rule's associated Scenario. Each Rule has an **Execution Order** that determines the sequence in which Rules are evaluated.

### Actions and Calculation Items

Actions are ordered within their respective Rules, and Calculation Items are ordered within their respective Actions using **Execution Order** fields. It may be simpler to handle dependencies within the same Rule by applying specific execution order and Scenarios to individual Actions or Calculation Items.

Utilizing multiple, ordered Actions with Calculation Items allows for powerfully dynamic configuration. You could configure a Rule that manipulates a Playbook Question's answer value multiple times to perform complex operations.

### Example: calculating ARR

To calculate ARR as `SUM(product total price) / (1/12) / term`, configure the following Actions within one Rule:

**Action 1** — stamp a Playbook Question answer, calculation type **Add**

- Calculation Item 1 — source **Product**, **All Products**, field `Cotiza__Total_Price__c`

**Action 2** — stamp Playbook Question answer, calculation type **Divide**, numeric math operator **Round**

- Calculation Item 1 — source **Question**
- Calculation Item 2 — source **Static Value**, type **Decimal**, value `0.083333`
- Calculation Item 3 — source **Quote Term**

See [Playbook Rule Action](../objects/admin/playbook_rule_action__c.md) and [Playbook Rule Calculation Item](../objects/admin/playbook_rule_calculation_item__c.md) for field reference.
