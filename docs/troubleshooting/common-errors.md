# Common Errors

## Missing or inactive price book

### Symptoms

- Playbook does not appear when creating a Quote
- Add Products table is empty
- Quote creation fails silently or with a price book error

### Resolution

1. Confirm the Playbook's **Price Book** is active.
2. Confirm products have active **PricebookEntry** records in that price book.
3. Verify the user has read access to Product2, Pricebook2, and PricebookEntry.

---

## Insufficient permissions

### Symptoms

- User cannot see Cotiza CPQ app or components
- Access errors when saving Quotes or editing playbooks

### Resolution

1. Assign **Cotiza CPQ User** (or **Cotiza CPQ Admin** for config users).
2. Verify Salesforce **API Enabled** permission.
3. Confirm Create/Edit access on Quote and related objects.
4. Check field-level security on Cotiza custom fields.

See [Permissions](../getting-started/permissions.md).

---

## Playbook rules not firing

### Symptoms

- Expected products not added automatically
- Question visibility does not change

### Resolution

1. Verify the Rule and Action records are **Is Active**.
2. Check the linked Scenario criteria evaluate to TRUE for your test data.
3. Review **Execute When** timing—rules set to **On first TRUE evaluation** only fire once.
4. Confirm **Execution Order**—earlier rules may need to run first.
5. Check if **Rules Paused** is enabled (CPQ Power Users).

See [Rule Evaluation](../admin-guide/rule-evaluation.md) and [Rules Cookbook](../admin-guide/rules-cookbook.md).

---

## Approval stuck or not progressing

### Symptoms

- Quote remains in **Submitted** status
- Approver cannot see pending approval

### Resolution

1. Confirm Quote Approval Step records were created on submission.
2. Verify approver User is active and matches assigned Quote Approver.
3. For manager approvers, confirm Opportunity Owner has a populated manager chain.
4. Check if **Require Individual Approval** requires separate actions per approval.
5. Approvals Power Users can act on any pending approval for testing.

See [Approvals Setup](../admin-guide/approvals.md).

---

## Proposal shows draft watermark

### Symptoms

- Generated PDF displays draft watermark

### Resolution

1. Confirm Quote is not a **Shell Quote**.
2. Verify all required approvals are **Approved**.
3. Save the Quote before generating the final proposal.

See [Generating Proposals](../user-guide/generating-pdfs.md).

---

## Sync did not update Opportunity

### Symptoms

- Opportunity fields or products do not reflect Quote after sync

### Resolution

1. Confirm **Sync** action completed without errors.
2. Review Opportunity Field Mapping and OppLineItem Field Mapping custom metadata.
3. Verify field API names and data types match between source and target.
4. Check user has edit access on Opportunity and OpportunityLineItem.

See [Field Mappings](../admin-guide/field-mappings.md).

---

## Contract not created

### Symptoms

- **Create Contract** checked but no Contract appears

### Resolution

1. Confirm **Create Contract** changed from false to **true** (trigger fires on change).
2. Verify Quote is synced and approved.
3. Check Apex trigger errors in Debug Logs.
4. Confirm user has create access on Contract and Cotiza entitlement objects.

See [Contracts Lifecycle](../admin-guide/contracts-lifecycle.md).

---

## MDX / configuration formula errors

### Symptoms

- Playbook or View Section save fails with validation error

### Resolution

1. Review inline help on the failing field for formula or SOQL syntax requirements.
2. For Record Table queries, avoid parent relationships and subqueries.
3. For piped text, use exact Variable Name tokens from Playbook Questions.

See [View Sections and Proposals](../admin-guide/view-sections-proposals.md).
