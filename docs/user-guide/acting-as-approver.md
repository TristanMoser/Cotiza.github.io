# Acting as an Approver

Approvers review and decide on submitted Quotes from the **Cotiza CPQ Approvals** tab or via approval email links.

## Approvals Hub

Open the App Launcher and select **Cotiza CPQ Approvals**.

The Approvals Hub organizes pending and historical approvals by:

- Opportunity
- Quote
- Individual approval and step

Use filters to view:

![Description](/img/screenshots/cpq-approvals-hub.png)

- Approvals assigned to you
- Quotes you submitted
- Submitted, approved, or rejected status

## Reviewing a Quote

When acting on an approval, you can view the full Quote context including:

- Playbook answers
- Product line items
- Approval reason and notes from the submitter
- Related Opportunity and Account information

Approval email sections configured on the Playbook can also surface Quote details directly in notification emails.

## Approve or reject

1. Locate the pending approval in the Approvals Hub.
2. Expand the Opportunity → Quote → Approval hierarchy.
3. Select **Approve** or **Reject** on your approver step.
4. Enter a decision reason if prompted.
5. Confirm your decision.

![Description](/img/screenshots/approval-decision.png)

### Individual vs. bulk approval

By default, when an approver acts on one approval step, the same decision applies to all pending approvals on that Quote where they are the assigned approver.

Playbook Approvals marked **Require Individual Approval** bypass this behavior—each approval must be explicitly approved.

### Manager approvers

Approvers can be resolved dynamically from the Opportunity Owner's management chain (1st through 5th line manager). The resolved user is determined at Quote save time.

## Power User approvers

Users with **Approvals** Power User access can view and act on any approval in the org, not only those assigned to them.

See [Power Users](../admin-guide/power-users.md).

## Email notifications

When configured on Playbook Approval records, emails are sent for:

| Event | Recipient |
| --- | --- |
| Submitted | Approver(s) |
| Recalled | Approver(s) |
| Approved | Submitter |
| Rejected | Submitter |

## Related guides

- [Submitting for Approval](./submitting-approvals.md)
- [Approvals Setup](../admin-guide/approvals.md)
- [Playbook Approver](../objects/admin/playbook_approver__c.md)
