# Playbook

High level container that can be used to define a specific operating motion.

| API Name | Label | Description |
| --- | --- | --- |
| `Add_Products_Column_Fields__c` | Add Products Columns | Semicolon delimited list of field API names on the PricebookEntry object to be shown in the Product Summary view in CPQ. Product2 fields are also supported by using 'Product2.' followed by the Product2 field API name. |
| `Add_Products_Page_Size_Default__c` | Add Products Page Size Default | Default number of records to show per page in the Add Products table. If left unpopulated, no pagination will be shown. |
| `Add_Products_Sort_By_Default__c` | Add Products Sort By Default | Default Product Column by which products will be sorted. To specify the sort direction, append ';Down' to the field API name to sort ascending and ';Up' to sort decending. |
| `Contract_View_Display_Fields__c` | Contract View Display Fields | Semicolon delimited list of Contract Field API names to be shown in CPQ when viewing a Contract records configuration. Sections can be created by inputting a label preceded by the '#' character (e.g. #Header). Blank spaces can be created by inputting a value that is not a valid field API name. |
| `Default_Term_in_Months__c` | Default Term (in Months) | Newly created quotes will be created with the term specified here |
| `End_Date_Editable__c` | End Date Editable | Determines if users can manually adjust the end date of the quote in CPQ. NOTE: End Date is always locked for Contract Amendments |
| `Entitlement_Summary_Column_Fields__c` | Entitlement Summary Columns | Semicolon delimited list of field API names on the Cotiza__Contract_Entitlement__c object to be shown in the Entitlement Summary view in CPQ. |
| `Entitlement_Summary_Group_By_Default__c` | Entitlement Summary Group By Default | Default Entitlement Column by which entitlements will be grouped |
| `Entitlement_Summary_Page_Size_Default__c` | Entitlement Summary Page Size Default | Default number of records to show per page in the Entitlement Summary. If left unpopulated, no pagination will be shown. |
| `Entitlement_Summary_Sort_By_Default__c` | Entitlement Summary Sort By Default | Default Entitlement Column by which entitlements will be sorted. To specify the sort direction, append ';Down' to the field API name to sort ascending and ';Up' to sort decending. |
| `IsActive__c` | Is Active | Determines if playbook is active and should appear in CPQ |
| `Label__c` | Label | Displayed label Users see in CPQ |
| `Pricebook__c` | Price Book | Price book used for products added in playbook. The price book must be active in order for the playbook to be visible in CPQ |
| `Product_Summary_Column_Fields__c` | Product Summary Columns | Semicolon delimited list of field API names on the QuoteLineItem object to be shown in the Product Summary view in CPQ. |
| `Product_Summary_Group_By_Default__c` | Product Summary Group By Default | Default Product Column by which products will be grouped |
| `Product_Summary_Page_Size_Default__c` | Product Summary Page Size Default | Default number of records to show per page in the Product Summary. If left unpopulated, no pagination will be shown. |
| `Product_Summary_Sort_By_Default__c` | Product Summary Sort By Default | Default Product Column by which products will be sorted. To specify the sort direction, append ';Down' to the field API name to sort ascending and ';Up' to sort decending. |
| `Proposal_Footer__c` | Proposal Footer | Footer display for Proposal PDF. Quote Question Answers can be piped directly into text with the following format: \{%QuestionVariableName%\}. |
| `Proposal_Header_Image_Link_Path__c` | Proposal Header Image Link | Link to image to display for Proposal PDF Header if the Proposal Header Type field is set to 'Image' |
| `Proposal_Header_Type__c` | Proposal Header Type | Determines if Proposal Header will display an attached image (Proposal Header Image Link Path) or text (Proposal Header) |
| `Proposal_Header__c` | Proposal Header | Header display for Proposal PDF if the Proposal Header Type field is set to 'Text'. Quote Question Answers can be piped directly into text with the following format: \{%QuestionVariableName%\}. |
| `Quote_View_Display_Fields__c` | Quote View Display Fields | Semicolon delimited list of Quote Field API names to be shown in CPQ when viewing a Quote records configuration. Sections can be created by inputting a label preceded by the '#' character (e.g. #Header). Blank spaces can be created by inputting a value that is not a valid field API name. |
| `Rules_Formula_Fields_Recalculation__c` | Rules Formula Fields Recalculation | When to run recalculation of QuoteLineItem Formula fields when configuring a Quote. Allows recalculation of formula fields used for scenario criteria and rule calculation in addition to those displayed in the product summary table. The recalculation will cause runtime to be marginally slower. Formula fields referencing fields through the Quote will not calculate. |
| `Start_Date_Editable__c` | Start Date Editable | Determines if users can manually adjust the start date of the quote in CPQ |
| `Term_Editable__c` | Term Editable | Determines if users can manually adjust the term (in months) of the quote in CPQ |
