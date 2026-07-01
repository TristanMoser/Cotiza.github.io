# Object Model Overview

Cotiza CPQ extends Salesforce with custom objects, standard object integrations, and custom metadata types. Together they form the data model that powers quoting, approvals, proposals, and contract management.

## Object categories

### Admin Objects

Configuration records that define how Cotiza CPQ behaves. Admins create and maintain these records to control playbooks, pricing, approvals, and display logic. User decisions during quoting are guided by this configuration.

See [Admin Objects](./admin/overview.md) for the full list and field reference.

### Transaction Objects

Output records created and updated as users work through the quoting process. These include Quotes, line items, approvals, proposals, and contract-related records.

See [Transaction Objects](./transaction/overview.md) for the full list and field reference.

### Custom Metadata Types

Deployment-friendly configuration used primarily for field mappings between records during sync and contract creation.

See [Custom Metadata Types](./metadata/overview.md) for the full list and field reference.

## How the categories relate

1. **Admin Objects** define playbooks, rules, questions, and approval paths.
2. Users interact with the CPQ UI, which reads admin configuration and writes **Transaction Objects**.
3. **Custom Metadata Types** control how transaction data maps to Opportunity, Opportunity Product, and Contract records when quotes are synced or finalized.

The diagram has two setup boxes (what admins build vs. what users create) and two exit paths (where quote data lands in Salesforce). Solid arrows show record relationships; the dashed arrow means "configuration drives the quoting UI."

```mermaid
flowchart TB
    subgraph admin ["Layer 1: Admin configuration"]
        SS[System Settings]
        PB[Playbook]
        PB --> PQ[Questions]
        PB --> PR[Rules and pricing]
        PB --> PA[Approval paths]
        PB --> PV[View sections]
    end
    subgraph quoting ["Layer 2: Records created while quoting"]
        Q[Quote]
        Q --> LI[Quote Line Items]
        Q --> AN[Playbook Answers]
    end
    subgraph sync ["Layer 3: Where quote data goes next"]
        OPP[Opportunity and Opportunity Products]
        CTR[Contract and Entitlements]
    end
    admin -.->|drives UI and logic| quoting
    quoting -->|Sync Quote| OPP
    quoting -->|Create Contract| CTR
```
