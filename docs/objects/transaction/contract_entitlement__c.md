# Contract Entitlement

Entitlement record associated with a Contract.

| API Name | Label | Description |
| --- | --- | --- |
| `Added_From_Entitlement__c` | Added From Entitlement | Entitlement that added the corresponding Opportunity Line Item that generated this Entitlement |
| `Adjustment_Type__c` | Adjustment Type | Type of adjustment the Entitlement performed |
| `Amendment_Copied_Entitlement__c` | Amendment Copied Entitlement | Entitlement that was cloned to create the Entitlement on an amended Contract |
| `Base_List_Price__c` | Base List Price | Non-Prorated List Price per unit of quantity before any discounts |
| `Base_Unit_Price__c` | Base Unit Price | Non-Prorated Actual Price per unit of quantity before any discounts |
| `Contract_Parent__c` | Contract | Contract to which the Entitlement belongs |
| `Discount__c` | Discount | Discount percentage applied to List Price to get to Unit Price |
| `End_Date__c` | End Date | Last day the Entitlement is valid |
| `Is_Amendment_Copy__c` | Is Amendment Copy | Determines if Entitlement was created as a copy of an existing Entitlement upon contract creation for an Amendment. |
| `List_Price__c` | List Price | List Price per unit of quantity before any discounts. Note that this value is prorated where applicable. |
| `Opportunity_Line_Item__c` | Opportunity Line Item | Original Opportunity Line Item that generated Entitlement |
| `Original_Unit_Price__c` | Original Unit Price | Original Unit Price as defined on PricebookEntry when the Entitlement's base QLI was created. |
| `Playbook_Rule_Action__c` | Playbook Rule Action | Action that added this Entitlement in its Quote configuration |
| `Pricing_Description__c` | Pricing Description | General overview of how pricing was calculated for this Entitlement |
| `Pricing_Set_Identifier__c` | Pricing Set Identifier | Identifier of Pricing Set on price book that this Entitlement uses to determine price. |
| `Prior_Quantity__c` | Prior Quantity | Number of units from any previous entitlement(s) that were amended/replaced |
| `Product_Name__c` | Product Name |  |
| `Product__c` | Product | Product record for Entitlement represents |
| `Proration_Base__c` | Proration Base | Base to used for Proration calculations. |
| `Proration__c` | Proration | Proration adjustment value applied to List Price to get Unit Price based on price book entry Proration Base value |
| `Quantity_Increments__c` | Quantity Increments | Semicolon delimited list of number values that are the only valid Cotiza__Quantity__c options for user input |
| `Quantity__c` | Quantity | Number of units of Entitlement |
| `Removable__c` | Removable | Determines if the Entitlement was able to be manually removed by a User in CPQ. |
| `Start_Date__c` | Start Date | First day the Entitlement is valid |
| `SubTotal_Price__c` | Subtotal Price | Total List Price before any discounts |
| `Total_Price__c` | Total Price | Total Actual Price after any discounts |
| `True_Quantity__c` | True Quantity | Number of units of product after taking into account the number of units from any previous entitlement(s) that were amended/replaced |
| `Unit_Price__c` | Unit Price | Actual price per unit of quantity after discounts. Note that this value is prorated where applicable. |
