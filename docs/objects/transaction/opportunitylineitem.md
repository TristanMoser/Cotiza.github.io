# Opportunity Product

Standard SFDC OpportunityLineItem object generated from synced Quote Line Items.

| API Name | Label | Description |
| --- | --- | --- |
| `Added_From_Entitlement__c` | Added From Entitlement | Entitlement that added the corresponding Quote Line Item that generated this line |
| `Adjustment_Type__c` | Adjustment Type | Type of adjustment the line item performs |
| `Base_List_Price__c` | Base List Price | Non-Prorated List Price per unit of quantity before any discounts |
| `Base_Unit_Price__c` | Base Unit Price | Non-Prorated Actual price per unit of quantity after discounts |
| `Discount__c` | Discount | Discount percentage applied to List Price to get to Unit Price |
| `End_Date__c` | End Date | Last day line is active |
| `List_Price__c` | List Price | List Price per unit of quantity before any discounts. Note that this value is prorated where applicable. |
| `Original_Unit_Price__c` | Original Unit Price | Original Unit Price as defined on PricebookEntry when the line was created. |
| `Playbook_Rule_Action__c` | Playbook Rule Action | Action that added this line in its Quote configuration |
| `Pricing_Description__c` | Pricing Description | General overview of how pricing was calculated for this line |
| `Pricing_Set_Identifier__c` | Pricing Set Identifier | Identifier of Pricing Set on price book that this line uses to determine price. |
| `Prior_Quantity__c` | Prior Quantity | Number of units from any previous entitlement(s) being amended/replaced |
| `Proration_Base__c` | Proration Base | Base to use for Proration calculations. |
| `Proration__c` | Proration | Proration adjustment value applied to List Price to get Unit Price based on price book entry Proration Base value |
| `Quantity_Increments__c` | Quantity Increments | Semicolon delimited list of number values that are the only valid Cotiza__Quantity__c options for user input |
| `Quantity__c` | Quantity | Number of units of product |
| `Quote_Line_Item__c` | Quote Line Item | Original Quote Line Item that generated Opportunity Line Item |
| `Removable__c` | Removable | Determines if the line can be manually removed by a User in CPQ. |
| `Start_Date__c` | Start Date | First day line is active |
| `SubTotal_Price__c` | Subtotal Price | Total List Price before any discounts |
| `Total_Price__c` | Total Price | Total Actual Price after any discounts |
| `True_Quantity__c` | True Quantity | Number of units of product after taking into account the number of units from any previous entitlement(s) that were amended/replaced |
| `Unit_Price__c` | Unit Price | Actual price per unit of quantity after discounts. Note that this value is prorated where applicable. |
