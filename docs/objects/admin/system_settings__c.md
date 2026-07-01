# CPQ System Settings

Base configuration source. Used to determine main display for the CPQ Container component, Quote Approval Submitter and more.

| API Name | Label | Description |
| --- | --- | --- |
| `Amendments_Maintain_Contract__c` | Amendments Maintain Contract | Determines if Contract Amendments should maintain the existing Contract and just append to/adjust existing Contract Entitlements and Answers. If FALSE, a new Contract record is created for each Amendment allowing for a full history of each iteration. |
| `Approval_Allowed_Override_Fields__c` | Approval Allowed Override Fields | Semicolon delimited list of field API names on the Cotiza__Playbook_View_Section__c object available to be overriden for Approval Quote Redline records. Any Cotiza__Playbook_View_Section__c Field API names are supported. If blank, all fields are able to be overriden. |
| `Approval_Submitter__c` | Approval Submitter | Quote field API name that houses User Id of user to use as the submitter when submitting quotes for approval. If no field is populated here, the current user is used. |
| `Contract_Table_Actions__c` | Contract Table Actions | Contract actions CPQ Users have available |
| `Contract_Table_Display_Columns__c` | Contract Table Display Columns | Semicolon delimited list of field API names on the Contract object to be shown in the Contract Table view in CPQ. Any Contract Field API names are supported. |
| `Contract_Table_Page_Size_Default__c` | Contract Table Page Size Default | Default number of records to show per page in the Contract table. If left unpopulated, no pagination will be shown. |
| `Contract_Table_Sort_By_Default__c` | Contract Table Sort By Default | Default Contract Field by which to sort contracts. To specify the sort direction, append ';Down' to the field API name to sort ascending and ';Up' to sort decending. |
| `Default_Playbook__c` | Default Playbook | Default playbook to be used when creating a new Quote in the Quote table. |
| `Display_Playbook_as_Modal__c` | Display Playbook as Modal | If checked, any view of Playbook configuration will be displayed in a modal. |
| `Force_Quote_From_Contract__c` | Force Quote from Contract | If checked, the 'Create' button for Quote creation will only appear in the event that there are no active / upcoming Contracts on the Account. To create a Quote with Contracts on the Account, they must be made by acting upon a Contract. |
| `Line_Item_Pricing_Fields_Refresh__c` | Line Item Pricing Fields Refresh | When to run refresh pricing fields on QuoteLineItem based on the current values of the related PricebookEntry record. Unless specified here, line items edited or created from an Entitlement (Amended Entitlements always persist) will persist the pricing field values already populated. Pricing fields refreshed: 'Cotiza__Original_Unit_Price__c', 'Cotiza__Proration_Base__c', 'Cotiza__Pricing_Set_Identifier__c', 'Cotiza__Quantity_Increments__c', and 'Cotiza__Removable__c' |
| `Proposal_Allowed_Override_Fields__c` | Proposal Allowed Override Fields | Semicolon delimited list of field API names on the Cotiza__Playbook_View_Section__c object available to be overriden for Proposal Quote Redline records. Any Cotiza__Playbook_View_Section__c Field API names are supported. If blank, all fields are able to be overriden. |
| `Proposal_Quote_Piped_Fields__c` | Proposal Quote Piped Fields | Semicolon delimited list of field API names on the Quote object available to be piped into a Playbook View Section in the format of \{%Quote.fieldName%\}. Any Quote Field API names are supported. |
| `Proposal_Table_Actions__c` | Proposal Table Actions | Proposal actions CPQ Users have available |
| `Proposal_Table_Page_Size_Default__c` | Proposal Table Page Size Default | Default number of records to show per page in the Proposal table. If left unpopulated, no pagination will be shown. |
| `Quote_Table_Actions__c` | Quote Table Actions | Quote actions CPQ Users have available |
| `Quote_Table_Display_Columns__c` | Quote Table Display Columns | Semicolon delimited list of field API names on the Quote object to be shown in the Quote Table view in CPQ. Any Quote Field API names are supported. |
| `Quote_Table_Page_Size_Default__c` | Quote Table Page Size Default | Default number of records to show per page in the Quote table. If left unpopulated, no pagination will be shown. |
| `Quote_Table_Sort_By_Default__c` | Quote Table Sort By Default | Default Quote Field by which to sort quotes. To specify the sort direction, append ';Down' to the field API name to sort ascending and ';Up' to sort decending. |
| `Show_Most_Active_Contract_Snapshot__c` | Show Most Active Contract Snapshot | If checked, when viewing the Account Contracts UI component, a quick product snapshot of the "Most Active Contract" will appear above the list of Contracts. |
