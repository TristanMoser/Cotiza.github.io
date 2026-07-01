# Playbook Question

Prompt for user input that dictates how a Quote should be configured within a Playbook.

| API Name | Label | Description |
| --- | --- | --- |
| `Amendments_Take_Latest_Answer__c` | Amendments Take Latest Answer | Determines if the answer to this Question should overwrite an existing Contract Answer when performing a Contract Amendment and the existing Contract is being maintained. |
| `Answer_Type__c` | Answer Type | Type of field where Users will place the question's answer |
| `Default_Field_Value__c` | Default Field Value | Field from CPQ data objects to use for default value for answer. Valid objects include: 'Account', 'Opportunity', 'Quote', 'Contract', 'Profile', 'UserRole', and 'User'. Example: "Profile.Name" |
| `Default_Value_Boolean__c` | Default Value (Boolean) | If related question answer type is 'Boolean', default value to use for answer. If Default Field Value is populated, that takes precedence over this value. |
| `Default_Value_Currency__c` | Default Value (Currency) | If related question answer type is 'Currency', default value to use for answer. If Default Field Value is populated, that takes precedence over this value. |
| `Default_Value_Date__c` | Default Value (Date) | If related question answer type is 'Date', default value to use for answer. If Default Field Value is populated, that takes precedence over this value. |
| `Default_Value_Decimal__c` | Default Value (Decimal) | If related question answer type is 'Decimal', default value to use for answer. If Default Field Value is populated, that takes precedence over this value. |
| `Default_Value_Integer__c` | Default Value (Integer) | If related question answer type is 'Integer', default value to use for answer. If Default Field Value is populated, that takes precedence over this value. |
| `Default_Value_Text__c` | Default Value (Text) | If related question answer type is 'Picklist', 'Multi-Select Picklist', 'Text', or 'Text Area', default value to use for answer. If Default Field Value is populated, that takes precedence over this value. NOTE: if using for the 'Record Lookup' answer type, enter a semicolon delimited list of records IDs. |
| `Display_Label__c` | Display Label | Displayed label Users see in CPQ |
| `Display_Order__c` | Display Order | Order in which question should be displayed in its group. Lower numbers appear first |
| `Do_Not_Create_Answer__c` | Do Not Create Answer | Scenario(s) where answer should not be created. Allows Question to potenially only serve as a dynamic calculation item in a Quote. |
| `Do_Not_Upgrade_Answer__c` | Do Not Upgrade Answer | Contract upgrade scenario(s) where answer should not be pulled in from a contract answer |
| `Help_Text__c` | Help Text | Extra information about question to be displayed to Users in a help text tooltip |
| `IsActive__c` | Is Active | Determines if question is active and should be evaluated in its group |
| `IsHidden__c` | Is Hidden | Determines if Users can see this question in CPQ. If not, the question is still evaluated, but not shown |
| `IsReadOnly__c` | Is Read Only | Determines if Users can modify the question's answer |
| `IsRequiredWithTouch__c` | Is Required With Touch | Determines if question is both required to have an answer populated and have been "touched" by the User in order to complete the quote. If TRUE, Users must interact with the question to mark it as complete even if a default value exists. NOTE: if the question is hidden, the requirement is not enforced. |
| `IsRequired__c` | Is Required | Determines if question is required to have an answer populated in order to complete the quote. NOTE: if the question is hidden, the requirement is not enforced. |
| `Maximum_Record_Selections__c` | Maximum Record Selections | If question answer type is 'Record Lookup', maximum number of records that Users are allowed to select as an answer. |
| `Maximum_Value__c` | Maximum Value | If question answer type is 'Currency', 'Decimal' or 'Integer', maximum value Users are allowed to input in as an answer. |
| `Minimum_Value__c` | Minimum Value | If question answer type is 'Currency', 'Decimal' or 'Integer', minimum value Users are allowed to input in as an answer. |
| `Picklist_Answers__c` | Picklist Answers | Semi-colon delimited list of answer choices when question answer type is 'Picklist' or 'Multi-Select Picklist' |
| `Playbook_Question_Group__c` | Playbook Question Group | Playbook Question Group to which this question belongs |
| `Proposal_Label__c` | Proposal Label | Displayed label Users see in Proposal if used in an Answer Table |
| `Query_String__c` | Query String | Query string used to query records if question answer type is 'Record Lookup'. This should NOT include any binded variables. Any dynamic alterations to this query should be handled in a CPQ Rule. Subqueries are NOT supported. Ensure all fields from the Record Display Fields field are also included here. |
| `Quote_Answers_Count__c` | Quote Answers Count | Number of Quote Answer records that are associated to this Question |
| `Quote_Save_Field__c` | Quote Save Field | If populated, the question's answer will be populated in this Quote field. Only the Quote field API name should be placed in this field |
| `Record_Display_Fields__c` | Record Display Fields | Semi-colon delimited list of Field API names to display for each queried record when the question answer type is 'Record Lookup'. Ensure that all fields listed here are also included in the Query String. |
| `Record_Page_Size_Default__c` | Record Page Size Default | Default number of records to show per page in the 'Record Lookup' table. If left unpopulated, no pagination will be shown. |
| `Record_Selection_Behavior__c` | Record Selection Behavor | Record selection behavior utilized when the question answer type is 'Record Lookup'. 'Automatic Record Selection': All records returned (up to maximum if applicable) are automatically selected upon load and whenever the query string is dynamically adjusted. |
| `Step_Value__c` | Step Value | If question answer type is 'Currency', 'Decimal' or 'Integer', step/increment value Users are allowed to input in as an answer. |
| `Variable_Name__c` | Variable Name | Unique Variable Name used to identify piped text in Proposal PDF |
