# Pricing Threshold

Individual number range for pricing determination within a Pricing Set.

| API Name | Label | Description |
| --- | --- | --- |
| `Custom_Unit_Price_Formula__c` | Custom Unit Price Formula | Formula used for Unit Price. If populated, the Unit Price field is disregarded. Valid only for numbers, standard operators (+ - * /), comparison operators (===, !==, ==, !=, <, >, <=, >=), ternary expressions (? :), and piped info: QuoteLineItem field: \{%Field_API_Name%\}. QuoteLineItem summaries: \{%Products.Field_API_Name:Add\|Subtract\|Multiply\|Divide\|Max\|Min\|Count:Filter_Field_API_Name:Equals\|Does not equal\|Greater than\|Greater than or equal\|Less than\|Less than or equal\|Contains\|Does not contain\|Is empty\|Is not empty:Filter_Value%\}. Question Answers: \{%Question.Variable_Name%\}. |
| `IsActive__c` | Is Active | Determines if threshold is active and should be utilized in CPQ |
| `Lower_Bound__c` | Lower Bound | Value (inclusive) at which the parent Pricing Set's Tiering Field enters the threshold. If no value is provided, the lower bound is met by default and assumed to be 0. For continuity, the Lower Bound should match the value of the pervious tier's Upper Bound. |
| `Pricing_Set__c` | Pricing Set | Pricing Set to which the Threshold belongs |
| `Unit_Price__c` | Unit Price | Price to apply if the Threshold is met |
| `Upper_Bound__c` | Upper Bound | Value (inclusive) at which the parent Pricing Set's Tiering Field exits the threshold. If no value is provided, the upper bound is met by default. For continuity, the Upper Bound should match the value of the next tier's Lower Bound. |
