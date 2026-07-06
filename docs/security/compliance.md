# Compliance

## AppExchange security review

Cotiza CPQ is distributed through the Salesforce AppExchange and undergoes Salesforce security review before publication.

## Platform alignment

Cotiza runs entirely on Salesforce infrastructure and inherits:

- Salesforce data center certifications and compliance programs available to your org's edition
- Salesforce audit trail capabilities (Field History, Setup Audit Trail)
- Event monitoring available through Salesforce platform tools

## Code quality

- Apex is bulkified for governor limit safety
- CRUD and FLS checks are applied through platform security models
- No external credential storage in the managed package

## Customer compliance responsibilities

While Cotiza operates within Salesforce security boundaries, customers remain responsible for:

- Org-wide security policies (password policies, MFA, IP restrictions)
- Data classification and retention policies
- User provisioning and deprovisioning
- Regulatory requirements specific to their industry (configure Salesforce accordingly)

## Audit trail

Approval decisions, Quote changes, and Contract events are stored on Salesforce records. Use standard Salesforce reporting and Field History Tracking (where enabled) for audit requirements.

## Related documentation

- [Solution Architecture and Usage](./solution-architecture-and-usage.md)
- [Data Handling](./data-handling.md)
- [Permissions](../getting-started/permissions.md)
