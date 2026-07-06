# Cotiza CPQ — Solution Architecture and Usage

**Document version:** 1.0  
**Product:** Cotiza CPQ (Salesforce AppExchange managed package)  
**Audience:** Salesforce security review and technical evaluators  
**Online documentation:** https://cpq.cotiza.dev

---

## 1. Executive Summary

Cotiza CPQ is a native Salesforce Sales Cloud application delivered as a managed package. All application logic, user interface, configuration, and customer data reside within the customer's Salesforce org. The solution does not operate external application servers or Cotiza-operated databases. During normal operation, customer quote, pricing, approval, and proposal data is not transmitted to external Cotiza systems.

This document describes solution architecture, information flow, authentication, encryption, data touchpoints, and basic usage instructions.

---

## 2. Solution Architecture

### 2.1 High-Level Architecture

Cotiza CPQ follows a three-layer model inside a single Salesforce org:

| Layer | Purpose | Primary records |
| --- | --- | --- |
| **Configuration** | Declarative setup by admins | System Settings, Playbook, Questions, Rules, Scenarios, Approvals, View Sections, Pricing Sets |
| **Runtime / Transaction** | Records created during quoting | Quote, Quote Line Item, Playbook Answer, Quote Approval records, Quote Proposal |
| **Sync / Contract** | Downstream Salesforce records | Opportunity, Opportunity Product, Contract, Contract Entitlement, Contract Playbook Answer, ContentVersion |

**Lightning Experience components** provide the user interface. **Apex** executes business logic (rules engine, sync, approvals, contract creation, proposal rendering) within Salesforce governor limits.

### 2.2 Architecture Diagram

```
┌─────────────────────────────────────────────────────────────────────────┐
│                        Customer Salesforce Org                          │
│                                                                         │
│  ┌────────────────────── Admin Configuration ──────────────────────┐   │
│  │ System Settings │ Playbooks │ Questions │ Rules │ Approvals     │   │
│  │ View Sections   │ Pricing Sets │ Custom Metadata (field maps)  │   │
│  └────────────────────────────┬────────────────────────────────────┘   │
│                               │ drives                                 │
│  ┌────────────────────────────▼────────────────────────────────────┐   │
│  │              Lightning UI (App tabs & record components)         │   │
│  │  cpqByOpportunity │ approvalsHub │ contractsByAccount │ etc.   │   │
│  └────────────────────────────┬────────────────────────────────────┘   │
│                               │ read/write                             │
│  ┌────────────────────────────▼────────────────────────────────────┐   │
│  │                    Apex (in-org processing)                      │   │
│  │  Rules engine │ Sync │ Approvals │ Proposals │ Contract create   │   │
│  └────────────────────────────┬────────────────────────────────────┘   │
│                               │                                        │
│  ┌────────────────────────────▼────────────────────────────────────┐   │
│  │ Standard & Custom Salesforce Objects (all data at rest in org)  │   │
│  │ Quote, Opportunity, Contract, ContentVersion, Cotiza custom...  │   │
│  └──────────────────────────────────────────────────────────────────┘   │
└─────────────────────────────────────────────────────────────────────────┘

External Cotiza servers: NOT used during normal operation
```

### 2.3 Salesforce Platform Components

| Technology | Role in Cotiza CPQ |
| --- | --- |
| Lightning Experience | Required UI platform; app tabs and record page components |
| Apex | Server-side rules, sync, approvals, contracts, proposals; `with sharing`, bulkified |
| Custom objects | Playbook configuration and transaction records (namespaced) |
| Custom Metadata Types | Quote/Opportunity/Entitlement field mappings |
| Standard objects | Quote, Opportunity, Contract, Product, Price Book, ContentVersion, User |
| Visualforce | Word proposal output; optional custom proposal sections |
| Permission sets | Cotiza CPQ User, Cotiza CPQ Admin |
| SOQL | Record lookup questions; proposal record tables |

---

## 3. Information Flow

### 3.1 End-to-End Business Flow

1. **Opportunity** — User opens Cotiza CPQ from the app or Opportunity record page.
2. **Quote creation** — User creates a Quote and configures it through an active Playbook.
3. **Playbook configuration** — User answers questions; Playbook Rules evaluate Scenarios and update questions, products, and pricing in real time. Answers persist as Playbook Answer records and may stamp Quote fields.
4. **Approval (conditional)** — If Playbook Approvals are triggered, user submits the Quote. Apex creates Quote Approval, Step, and Approver records. Approvers act in the Approvals hub. Optional approval emails use Salesforce email delivery.
5. **Proposal (optional)** — User generates a proposal PDF (or Word for Proposal Power Users). Output is stored as ContentVersion linked to a Quote Proposal record.
6. **Sync** — User syncs the Quote. Apex maps Quote and Quote Line Item fields to Opportunity and Opportunity Products via Custom Metadata mappings and package defaults.
7. **Contract** — When **Create Contract** on Opportunity changes from false to true, Apex creates Contract, Contract Entitlement, and Contract Playbook Answer records.
8. **Renewals / amendments** — User launches Amend, Replace, or Renew from the Contracts UI to create contract-sourced Quotes.

### 3.2 Data Flow Diagram

```
User (Browser)
    │
    │ HTTPS/TLS (Salesforce platform)
    ▼
Salesforce Lightning UI ──► Apex Controller / Service Layer
                                │
        ┌───────────────────────┼───────────────────────┐
        ▼                       ▼                       ▼
  Custom Objects          Standard Objects         ContentVersion
  (Playbook config,       (Quote, Opportunity,     (Proposal PDFs)
   Answers, Approvals)    Contract, Products)
        │                       │
        └───────────┬───────────┘
                    ▼
            All data at rest in
            customer Salesforce org
```

### 3.3 Configuration-to-Runtime Flow

| Step | Source | Target | Mechanism |
| --- | --- | --- | --- |
| Quote UI rendering | Playbook, Questions, System Settings | Lightning components | SOQL/DML in Apex; client reads config |
| Rule execution | Playbook Rule + Scenario | Quote, Answers, Line Items | Apex rules engine on configured triggers |
| Approval enforcement | Playbook Approval | Quote Approval records | Apex on submit |
| Proposal rendering | Playbook View Section | ContentVersion / Quote Proposal | Apex + Visualforce (PDF/Word) |
| Quote sync | Quote, Quote Line Item | Opportunity, Opportunity Product | Apex + Opportunity/OppLineItem Field Mapping CMDT |
| Contract creation | Opportunity Product, Quote answers | Contract, Entitlement, Contract Playbook Answer | Apex trigger on Create Contract flag + Entitlement Field Mapping CMDT |

---

## 4. Authentication

Cotiza CPQ does **not** implement a separate identity provider or authentication system.

| Topic | Implementation |
| --- | --- |
| **User authentication** | Standard Salesforce login (username/password, SSO, MFA as configured by the customer) |
| **Session management** | Salesforce platform session tokens and timeout policies |
| **Authorization** | Salesforce profiles, permission sets, sharing rules, field-level security, role hierarchy |
| **Cotiza access control** | Cotiza CPQ User and Cotiza CPQ Admin permission sets; optional Power User field on User |
| **API access** | Lightning components require the standard Salesforce **API Enabled** user permission |
| **Approver resolution** | Named User references and/or Opportunity Owner manager chain (role hierarchy) |
| **External credentials** | None stored by the Cotiza managed package |

Users must be authenticated to Salesforce before any Cotiza CPQ UI or Apex logic is accessible. All access checks occur within the customer's org security model.

---

## 5. Encryption and Data Transfer

### 5.1 Data in Transit

| Path | Encryption |
| --- | --- |
| User browser ↔ Salesforce (Lightning UI) | TLS/HTTPS (Salesforce platform standard) |
| Apex execution | In-platform; no external HTTP callouts during normal Cotiza operation |
| Approval notification emails | Delivered via Salesforce email infrastructure (TLS per Salesforce configuration) |
| Proposal download links | Salesforce ContentVersion / content delivery (platform-controlled) |

Cotiza CPQ does **not** initiate outbound connections to external Cotiza-operated endpoints during normal quoting, approval, sync, or proposal operations.

### 5.2 Data at Rest

All Cotiza CPQ data is stored on Salesforce objects within the customer's org. Encryption at rest follows the customer's Salesforce edition and configuration:

- Platform encryption (if enabled by the customer)
- Salesforce data center protections and certifications inherited by the org

The managed package does not store customer data outside Salesforce.

### 5.3 External Transmission

External data transmission may occur **only** when the customer explicitly configures Salesforce platform features or customizations, for example:

- Email notifications to approvers or submitters
- Content distribution or file sharing links
- Custom Apex, Flow, or integration built by the customer

These transmissions are governed by the customer's Salesforce org settings, not by Cotiza-operated infrastructure.

---

## 6. Data Touchpoints

### 6.1 Systems and Services

| System / Service | Role | Customer data stored? | Normal operation connection? |
| --- | --- | --- | --- |
| Customer Salesforce org | Application host, database, UI, logic | Yes — all Cotiza data | Yes — sole runtime environment |
| Cotiza external servers | None | No | No |
| Salesforce email | Approval notifications (optional) | Email content in transit | Optional — customer-configured |
| Customer custom integrations | Optional extensions | Depends on customer | Optional — customer-built |

### 6.2 Salesforce Object Touchpoints

**Standard objects read or written:**

| Object | Typical operations |
| --- | --- |
| Quote | Create, read, update (primary output record) |
| Quote Line Item | Create, read, update, delete |
| Opportunity | Read; update on sync |
| Opportunity Line Item | Create, update on sync |
| Product2, Pricebook2, PricebookEntry | Read (catalog) |
| Contract | Create, read, update |
| User | Read (approvers, owners, submitters) |
| Account | Read (context) |
| ContentVersion | Create (proposal files) |

**Custom objects (Cotiza namespace) — configuration:**

System Settings, Playbook, Playbook Question Group, Playbook Question, Playbook Scenario, Playbook Scenario Criterion, Playbook Rule, Playbook Rule Action, Playbook Rule Calculation Item, Playbook Approval, Playbook Approver Group, Playbook Approver, Playbook View Section, Pricing Set, Pricing Threshold

**Custom objects (Cotiza namespace) — transaction:**

Playbook Answer, Quote Approval, Quote Approval Step, Quote Approver, Quote Proposal, Contract Entitlement, Contract Playbook Answer

**Custom Metadata Types:**

Opportunity Field Mapping, OppLineItem Field Mapping, Entitlement Field Mapping, Entitlement Combination Mapping

### 6.3 Data Touchpoint Summary Table

| Data category | Examples | Stored where | Leaves org in normal ops? |
| --- | --- | --- | --- |
| Quote configuration | Answers, line items, pricing | Quote, Playbook Answer, Quote Line Item | No |
| Approval data | Status, approver, notes, reasons | Quote Approval records | No (email optional) |
| Proposal documents | PDF, Word files | ContentVersion, Quote Proposal | No (unless customer shares link) |
| Admin configuration | Playbooks, rules, approvals | Cotiza admin custom objects | No |
| Synced deal data | Opp fields, products | Opportunity, Opportunity Product | No |
| Contract data | Entitlements, contract answers | Contract, Contract Entitlement | No |

---

## 7. Basic Usage Instructions

### 7.1 Prerequisites

- Salesforce Professional, Enterprise, Unlimited, or Developer Edition
- Lightning Experience enabled
- Standard Quote object enabled (Setup → Quote Settings)
- Cotiza CPQ managed package installed from AppExchange

### 7.2 Initial Setup (Administrator)

1. Install Cotiza CPQ from AppExchange (recommend sandbox first).
2. Assign **Cotiza CPQ Admin** permission set to the implementing admin.
3. Create a **System Settings** record (App Launcher → Cotiza CPQ System Settings).
4. Configure **Products**, **Price Books**, and **Price Book Entries**.
5. Create a **Playbook** linked to a Price Book; add Questions, Rules, Approvals, and View Sections as needed.
6. Assign **Cotiza CPQ User** permission set to sales users and approvers.
7. Add **Cotiza CPQ Container** to Opportunity record pages via Lightning App Builder.
8. Validate an end-to-end test Quote through sync (and contract creation if applicable).

Estimated time: package install 5–15 minutes; initial configuration 1–4 hours depending on complexity.

### 7.3 Sales User Workflow

1. Open an **Opportunity** in Cotiza CPQ (app tab or record page component).
2. Click **Create +** to start a new Quote.
3. Complete the **Playbook** configuration wizard (questions, products, pricing).
4. **Submit for approval** if the Approval Summary indicates approvals are required.
5. **Generate a proposal** PDF when configuration is complete and approvals are satisfied.
6. **Sync** the Quote to update the Opportunity and Opportunity Products.
7. After deal close, an admin or automated process sets **Create Contract** on the Opportunity.
8. For ongoing relationships, use **Amend**, **Replace**, or **Renew** from the Contracts tab.

### 7.4 Approver Workflow

1. Open **Cotiza CPQ Approvals** tab (or follow approval email link if configured).
2. Filter to assigned or submitted approvals.
3. Review Quote context, approval reason, and submitter notes.
4. **Approve** or **Reject** with an optional decision reason.

### 7.5 Roles and Permissions

| Role | Permission set | Typical activities |
| --- | --- | --- |
| CPQ administrator | Cotiza CPQ Admin | Playbooks, rules, approvals, system settings |
| Sales rep | Cotiza CPQ User | Create quotes, submit approvals, generate proposals |
| Approver | Cotiza CPQ User | Approve/reject in Approvals hub |
| Deal desk (optional) | Cotiza CPQ User + Proposals Power User | Word proposals, redlines |
| Operations (optional) | Cotiza CPQ User + Contracts Power User | Void contracts |

---

## 8. Audit and Compliance Notes

- Approval decisions, Quote changes, and Contract events are persisted on Salesforce records.
- Customers may enable Field History Tracking and use standard Salesforce reporting for audit trails.
- Apex is bulkified; CRUD and FLS enforced via `with sharing` patterns.
- Customers remain responsible for org-wide security policies (MFA, IP restrictions, data retention).

---

## 9. Related Documentation

| Topic | URL |
| --- | --- |
| Product overview | https://cpq.cotiza.dev/docs/intro |
| Installation | https://cpq.cotiza.dev/docs/getting-started/installation |
| Permissions | https://cpq.cotiza.dev/docs/getting-started/permissions |
| Data handling | https://cpq.cotiza.dev/docs/security/data-handling |
| Compliance | https://cpq.cotiza.dev/docs/security/compliance |
| Object model | https://cpq.cotiza.dev/docs/objects/overview |
| End-to-end workflow | https://cpq.cotiza.dev/docs/user-guide/workflow-overview |
| Quick start | https://cpq.cotiza.dev/docs/getting-started/quick-start |

---

**Cotiza CPQ** — Point. Click. Quote.
