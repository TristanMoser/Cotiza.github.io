# How Many Playbooks?

When designing your Cotiza CPQ implementation, one of the first decisions is how many Playbooks to create. The two most common approaches are a **single Playbook** and **one Playbook per Price Book**.

## Single Playbook

### Advantages

- Simplest implementation of CPQ
- No duplicate Playbook Questions or other admin object records
- CPQ is built to handle large amounts of Playbook Rule logic; even complex playbooks perform fast operations

### Considerations

- Larger Playbooks can be more difficult to debug
- Different visibility and pricing can still be configured with Playbook Rules instead of maintaining separate Playbooks
- Consider placing fields on the Opportunity object that you need for all deals; formula fields can then be placed on the Quote to surface that information

## Playbook for each Price Book

### Advantages

- Clear difference when selling to different customer types
- Playbooks can be simpler with fewer Playbook Rules

### Considerations

- Duplicate Playbook Questions are likely needed if you want to collect the same information in all Playbooks regardless of the Price Book
- Contract adjustment scenarios can be more complex when changing from one Playbook to another

## Note on contract adjustments

It is strongly discouraged to create separate Playbooks for different Contract adjustment scenarios (Renewal or Replacement). Playbook changes are not allowed during Amendment scenarios.

Try to create each Playbook in a way that captures the correct information for all relevant deal types. Playbook Rules can be configured to pull information from Contract Playbook Answers to help populate a new Playbook in the event of a Playbook switch during a Contract adjustment scenario.

See [Contract Playbook Answer](../objects/transaction/contract_playbook_answer__c.md) for the related object reference.
