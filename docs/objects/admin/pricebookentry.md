# Price Book Entry

Standard SFDC PricebookEntry object referenced by line items.

| API Name | Label | Description |
| --- | --- | --- |
| `Adjustable_Product_Columns__c` | Adjustable Product Columns | Semicolon delimited list of attribute names on the Product level that are adjustable by the User by default in the Product Summary view in CPQ. Any QuoteLineItem Field API names are supported in the event that they are displayed in CPQ. |
| `Currency__c` | Currency | Only populated for multi-currency orgs where a quote is generated in a currency other than the org default currency for the pricebook associated to the CPQ playbook |
| `Date_Split_Types__c` | Date Split Types | Allowed options for Date Splitting. When Date Splitting, the base QuoteLineItem record is split out into multiple records according to the Type specified here. |
| `Max_Manual_Additions__c` | Max Manual Additions | If populated, the value here will cap the number of manual additions Users can add in CPQ. If NOT populated, Users can enter as many manual additions as they desire. |
| `Pricing_Set_Identifier__c` | Pricing Set Identifier | Identifier of Pricing Set on price book that this entry uses to determine price. If empty, the list price of the entry will be used unless overwritten by a rule in CPQ. |
| `Proration_Base__c` | Proration Base | Base to use for Proration calculations. 'Year' denotes the list price is annual and will prorate by taking the number of active days divided by 365 days (leap day ignored). 'Month' denotes the list price is per month and will prorate by taking the number of active full months plus the number of active days divided by the total number of days in the last partial month. If blank, no proration is applied. |
| `Quantity_Increments__c` | Quantity Increments | Semicolon delimited list of number values that are the only valid Cotiza__Quantity__c options for user input |
| `Quantity__c` | Quantity | Default quantity when first added to a quote |
| `Removable__c` | Removable | Determines if the product can be manually removed by a User in CPQ. NOTE: Products added manually are always removable. |
