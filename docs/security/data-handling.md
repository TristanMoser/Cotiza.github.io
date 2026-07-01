# Data Handling

## Data storage

Cotiza CPQ stores all data natively in your Salesforce org. No Cotiza-operated database receives customer CRM data.

Data resides on standard and custom Salesforce objects including:

- Quote, QuoteLineItem, Opportunity, OpportunityLineItem
- Contract and Cotiza custom objects (Playbook configuration, approvals, proposals, entitlements)
- ContentVersion files for generated proposals

## External data transmission

Customer quote, pricing, and approval data is **not** transmitted to external Cotiza servers during normal operation. All Apex executes within Salesforce platform boundaries.

External transmission occurs only when your org explicitly configures integrations (e.g., email delivery, content distribution links, custom Apex integrations you build).

## Authentication and access

- Users authenticate through Salesforce login
- Access is controlled by Salesforce profiles, permission sets, and sharing rules
- Cotiza permission sets (`Cotiza CPQ User`, `Cotiza CPQ Admin`) grant object and field access
- **Power User** field on User records grants additional UI capabilities

See [Permissions](../getting-started/permissions.md) and [Power Users](../admin-guide/power-users.md).

## Security model

Cotiza respects Salesforce platform security:

| Control | Application |
| --- | --- |
| CRUD permissions | Enforced on all DML via Apex `with sharing` patterns |
| Field-level security | Respected in UI and Apex |
| Sharing rules | Quote, Opportunity, Contract access follows org sharing |
| Role hierarchy | Manager approvers resolved from Opportunity Owner hierarchy |

## Proposal file access

Generated proposals are stored as ContentVersion records. Access to download links follows Salesforce content delivery and sharing configuration in your org.

## Admin responsibilities

- Assign minimum necessary permission sets
- Configure sharing rules for Quote and Contract objects
- Review Power User assignments periodically
- Use sandbox for configuration testing before production
