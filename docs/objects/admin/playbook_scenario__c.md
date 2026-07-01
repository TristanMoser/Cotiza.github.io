# Playbook Scenario

Outlines a specific scenario that can be referenced by Rules, Approvals and View Sections.

| API Name | Label | Description |
| --- | --- | --- |
| `Criteria_Evaluation__c` | Criteria Evaluation | How to determine if Scenario is met based on active criteria records |
| `Custom_Criteria_Evaluation_Logic__c` | Custom Criteria Evaluation Logic | Custom logic to be met for Criteria Evaluation. Enter the Identifier value (Integer) for each Criterion arranged with any valid combination of parentheses, the  "&" character to indicate an AND operator, or the "\|" character to indicate an OR operator. NOTE: any unevaluated integers (due to being inactive or not being found) will evaluate to FALSE. |
| `Description__c` | Description | None |
| `IsActive__c` | Is Active | Determines if Scenario is active and is valid in playbook. If false, the Scenario is assumed to not be met. |
| `Lower_N__c` | Lower N | Determines the lower bound of critiera needed for 'Between Lower N and Upper N criteria are met' evaluations. Assumes no lower bound if blank. |
| `Playbook__c` | Playbook | Playbook in which this Scenario is to be evaluated |
| `Upper_N__c` | Upper N | Determines the upper bound of critiera needed for 'Between Lower N and Upper N criteria are met' evaluations. Assumes no upper bound if blank. |
