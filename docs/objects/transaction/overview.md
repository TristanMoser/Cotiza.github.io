# Transaction Objects

Transaction objects are the output of Cotiza CPQ. User decisions—guided by Admin Object records—determine how these records are populated and updated throughout the quoting lifecycle.

## Record lifecycle

| Stage | Primary objects |
| --- | --- |
| Quoting | Quote, Playbook Answer, QuoteLineItem |
| Approval | Quote Approval, Quote Approval Step, Quote Approver |
| Proposal | Quote Proposal, ContentVersion |
| Sync | Opportunity, OpportunityLineItem (updated from Quote) |
| Contract | Contract, Contract Entitlement, Contract Playbook Answer |

## Objects

| Object | Description |
| --- | --- |
| [Quote](./quote.md) | Standard SFDC Quote; primary output record from a Playbook |
| [Quote Line Item](./quotelineitem.md) | Standard SFDC QuoteLineItem; product line item output |
| [Playbook Answer](./playbook_answer__c.md) | Stored answer for a Playbook Question |
| [Quote Approval](./quote_approval__c.md) | Output for a Playbook Approval |
| [Quote Approval Step](./quote_approval_step__c.md) | Output for a Playbook Approver Group |
| [Quote Approver](./quote_approver__c.md) | Output for a Playbook Approver |
| [Quote Proposal](./quote_proposal__c.md) | Generated proposal document from View Sections |
| [Opportunity](./opportunity.md) | Standard SFDC Opportunity; parent of Quote records |
| [Opportunity Product](./opportunitylineitem.md) | Standard OpportunityLineItem generated from synced Quote Line Items |
| [Contract](./contract.md) | Standard SFDC Contract after deal finalization |
| [Contract Entitlement](./contract_entitlement__c.md) | Entitlement record on a Contract |
| [Contract Playbook Answer](./contract_playbook_answer__c.md) | Stored Playbook answers on a Contract |
| [Content Version](./contentversion.md) | Standard ContentVersion used for generated proposal files |

## Related guides

- [Creating Quotes](../../user-guide/creating-quotes.md)
- [Quote Line Items](../../user-guide/quote-line-items.md)
- [Generating PDFs](../../user-guide/generating-pdfs.md)
