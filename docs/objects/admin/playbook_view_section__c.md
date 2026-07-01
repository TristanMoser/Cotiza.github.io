# Playbook View Section

Blueprint to generate a view for a Quote Proposal or an Approval Email.

| API Name | Label | Description |
| --- | --- | --- |
| `Allow_Mid_Section_Page_Break__c` | Allow Mid-Section Page Break | If true, the section may appear split between the bottom of one page and the top of the next. If false, all attempts to keep the section on the same page are made |
| `Answer_Table_Questions__c` | Answer Table Questions | Semicolon delimited list of Question Variable Names to display in answer table section |
| `Approval_Base_Email_Section__c` | Approval Base Email Section | If true, the section is defined as an email section to appear on all approvals on the playbook and will NOT appear in the proposal. |
| `Approval_Emails_Where_Included__c` | Approval Email(s) Where Included | If an Approval Base Email Section or linked directly to a Playbook Approval, Approval Email Types in which this section should be included. |
| `Body_Text_Block_1__c` | Body (Column 1) | Text for the first column of text or header of table where applicable. Quote Question Answers can be piped directly into text with the following format: \{%QuestionVariableName%\}. For Approval Email Sections, the following approval information can be piped in: \{%Approval.approver%\}, \{%Approval.submitter%\}, \{%Approval.status%\}, \{%Approval.labels%\}, \{%Approval.reasons%\}, \{%Approval.notes%\}, \{%Approval.quote%\}, \{%Approval.quoteApprovalNotes%\}, \{%Approval.opportunity%\}, and \{%Approval.account%\}. |
| `Body_Text_Block_2__c` | Body (Column 2) | Text for the second column of text where applicable. Quote Question Answers can be piped directly into text with the following format: \{%QuestionVariableName%\}. For Approval Email Sections, the following approval information can be piped in: \{%Approval.approver%\}, \{%Approval.submitter%\}, \{%Approval.status%\}, \{%Approval.labels%\}, \{%Approval.reasons%\}, \{%Approval.notes%\}, \{%Approval.quote%\}, \{%Approval.quoteApprovalNotes%\}, \{%Approval.opportunity%\}, and \{%Approval.account%\}. |
| `Body_Text_Block_3__c` | Body (Column 3) | Text for the third column of text where applicable. Quote Question Answers can be piped directly into text with the following format: \{%QuestionVariableName%\}. For Approval Email Sections, the following approval information can be piped in: \{%Approval.approver%\}, \{%Approval.submitter%\}, \{%Approval.status%\}, \{%Approval.labels%\}, \{%Approval.reasons%\}, \{%Approval.notes%\}, \{%Approval.quote%\}, \{%Approval.quoteApprovalNotes%\}, \{%Approval.opportunity%\}, and \{%Approval.account%\}. |
| `Display_Order__c` | Display Order | Order in which section should be displayed in its email or proposal. Lower numbers appear first. |
| `Force_Page_Break_After__c` | Force Page Break After | Determines if the next section after should be placed at the top of a new page |
| `Force_Page_Break_Before__c` | Force Page Break Before | Determines if this section should be placed at the top of a new page |
| `Image_Link_Path__c` | Image Link | Link to image to display for 'Image' section types. |
| `Image_Width__c` | Image Width | CSS Width Size to apply to the image (input the number with '%' or other CSS parameter appended). If null, the image will default to '100%' |
| `Inputs_Column_1__c` | Inputs (Column 1) | Semi-colon delimited list of Input labels for the first column in the User Input section |
| `Inputs_Column_2__c` | Inputs (Column 2) | Semi-colon delimited list of Input labels for the second column in the User Input section |
| `Inputs_Column_3__c` | Inputs (Column 3) | Semi-colon delimited list of Input labels for the third column in the User Input section |
| `Inputs_Font_Color__c` | Inputs Font Color | CSS Font Color for Inputs |
| `Inputs_Font_Size__c` | Inputs Font Size | CSS Font Size for Inputs (input the number with 'px' or other CSS parameter appended) |
| `Inverse_Scenario__c` | Inverse Scenario | If true, the linked scenario must NOT be met in order for the section to appear. |
| `IsActive__c` | Is Active | Determines if section is active and should be pulled in for evaluation of Proposal PDF or Approval Email |
| `Margin_Bottom__c` | Margin Bottom | CSS Margin Size to apply below the section (input the number with 'px' or other CSS parameter appended) |
| `Margin_Left__c` | Margin Left | CSS Margin Size to apply to the left of the section (input the number with 'px' or other CSS parameter appended) |
| `Margin_Right__c` | Margin Right | CSS Margin Size to apply to the right of the section (input the number with 'px' or other CSS parameter appended) |
| `Margin_Top__c` | Margin Top | CSS Margin Size to apply above the section (input the number with 'px' or other CSS parameter appended) |
| `Playbook_Approval__c` | Approval | Approval in which this section is pulled in for the Approval Email. If populated, will NOT appear in the proposal. |
| `Playbook_Scenario__c` | Scenario | Scenario that must be met in order for the section to appear. If no record is linked, the Scenario is assumed to be met. |
| `Playbook__c` | Playbook | Playbook in which this section is sourced |
| `Quote_Redline__c` | Quote Redline | Quote to which the View Section overrides the Base View Section |
| `Record_Table_Column_Widths__c` | Record Table Column Widths | Semicolon delimited list of column width percentage values (do not include the % character). If this value is null, the values do not sum to 100 or the number of values does not match the number of fields, all column widths will be equal. |
| `Record_Table_Group_Field__c` | Record Table Group Field | Field on Record Table Query that should be used to create separate tables for each unique value among the returned records |
| `Record_Table_Group_Font_Color__c` | Record Table Group Font Color | CSS Font Color for Record Table Groupings |
| `Record_Table_Group_Font_Size__c` | Record Table Group Font Size | CSS Font Size for Record Table Groupings |
| `Record_Table_Query__c` | Record Table Query | SOQL query for records in table. Every field included will be displayed. Accepted binded variables are :quoteRecordId, :opportunityRecordId, :accountRecordId, :adjustedContractRecordId, :currentUserId, :submitterId, and :approverId (e.g. WHERE QuoteId=:quoteRecordId). Piped text from Question Answers and Approval info is also supported. When using a bind variable or piped text that returns a string value, the values will automatically be wrapped in ''. Parent fields and Subqueries are NOT supported. |
| `Record_Table_Summary_Fields__c` | Record Table Summary Fields | Semicolon delimited list of field on Record Table Query that should be summarized across all records found. Must match up to order of Record Table Summary Types. |
| `Record_Table_Summary_Label__c` | Record Table Summary Label | Label to display in first column of the Summary row for the Record Table. Defaults to 'Totals' if no value provided. |
| `Record_Table_Summary_Only__c` | Record Table Summary Only | If true, the Record Table will not show any headers or record rows. Instead only the defined Summary row will be displayed. |
| `Record_Table_Summary_Types__c` | Record Table Summary Types | Semicolon delimited list of summary types for the corresponding summary fields. Valid options are SUM and AVG. |
| `Section_Type__c` | Section Type | Determines content type to display in section |
| `Table_Entries_Background_Color__c` | Table Entries Background Color | CSS Background Color for Table Entries |
| `Table_Entries_Font_Color__c` | Table Entries Font Color | CSS Font Color for Table Entries |
| `Table_Entries_Font_Size__c` | Table Entries Font Size | CSS Font Size for Table Entries (input the number with 'px' or other CSS parameter appended) |
| `Table_Headers_Background_Color__c` | Table Headers Background Color | CSS Background Color for Table Headers |
| `Table_Headers_Font_Color__c` | Table Headers Font Color | CSS Font Color for Table Headers |
| `Table_Headers_Font_Size__c` | Table Headers Font Size | CSS Font Size for Table Headers (input the number with 'px' or other CSS parameter appended) |
| `View_Section_Override__c` | View Section Override | View Section to which the View Section overrides for the Quote Redline |
| `View_Source__c` | View Source | Where section will be pulled into |
| `Visualforce_Source__c` | Visualforce Source | Name of Apex Class that implements the Cotiza.Proposal_Custom_VF_Interface Apex Class and will return the desired Visualforce Component using the ApexPages.Component generateProposalComponent(Id quoteId, Id proposalSectionId) method. Must adhere to namespace.className. Use 'c' for your own org's namespace. |
