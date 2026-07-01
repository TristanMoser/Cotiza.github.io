# Quote Line Item

Standard SFDC QuoteLineItem object. Output record for a product line item.

| API Name | Label | Description |
| --- | --- | --- |
| `Added_From_Entitlement__c` | Added From Entitlement | Entitlement that added this line |
| `Adjustment_Type__c` | Adjustment Type | Type of adjustment the line item performs |
| `Base_List_Price__c` | Base List Price | Non-Prorated List Price per unit of quantity before any discounts |
| `Base_Unit_Price__c` | Base Unit Price | Non-Prorated Actual price per unit of quantity after discounts |
| `Date_Split_Count__c` | Date Split Order | Total count of Date Splits across the unique Date Split Identifier. |
| `Date_Split_Identifier__c` | Date Split Identifier | Identifier to indicate the Date Split to which the line item belongs. |
| `Date_Split_Order__c` | Date Split Order | Position of line item within its Date Split. Order goes from lowest to highest starting with 1 up until the value populated in the Cotiza__Date_Split_Count__c field. |
| `Date_Split_Type__c` | Date Split Types | Selected option for Date Splitting. When populated, indicates that this line item is part of a Date Split and was split according to the Type specfied here. |
| `Discount__c` | Discount | Discount percentage applied to List Price to get to Unit Price |
| `End_Date__c` | End Date | Last day line is active |
| `List_Price__c` | List Price | List Price per unit of quantity before any discounts. Note that this value is prorated where applicable |
| `Original_Unit_Price__c` | Original Unit Price | Original Unit Price as defined on PricebookEntry when the line was created. |
| `Playbook_Rule_Action__c` | Playbook Rule Action | Action that added this line in its Quote configuration |
| `Pricing_Description__c` | Pricing Description | General overview of how pricing was calculated for this line |
| `Pricing_Set_Identifier__c` | Pricing Set Identifier | Identifier of Pricing Set on price book that this line uses to determine price. If empty, the list price of the related price book entry will be used unless overwritten by a rule in CPQ. |
| `Prior_Quantity__c` | Prior Quantity | Number of units from any previous entitlement(s) being amended/replaced |
| `Product_Name__c` | Product Name |  |
| `Proration_Base__c` | Proration Base | Base to use for Proration calculations. 'Year' denotes the list price is annual and will prorate by taking the number of active days divided by 365 days (leap day ignored). 'Month' denotes the list price is per month and will prorate by taking the number of active full months plus the number of active days divided by the total number of days in the last partial month. If blank, no proration is applied. |
| `Proration__c` | Proration | Proration adjustment value applied to List Price to get Unit Price based on price book entry Proration Base value |
| `Quantity_Increments__c` | Quantity Increments | Semicolon delimited list of number values that are the only valid Cotiza__Quantity__c options for user input |
| `Quantity__c` | Quantity | Number of units of product |
| `Removable__c` | Removable | Determines if the line can be manually removed by a User in CPQ. NOTE: Products added manually are always removable. |
| `Start_Date__c` | Start Date | First day line is active |
| `SubTotal_Price__c` | Subtotal Price | Total List Price before any discounts |
| `Total_Price__c` | Total Price | Total Actual Price after any discounts |
| `True_Quantity__c` | True Quantity | Number of units of product after taking into account the number of units from any previous entitlement(s) that were amended/replaced |
| `Unit_Price__c` | Unit Price | Actual price per unit of quantity after discounts. Note that this value is prorated where applicable |
