#!/usr/bin/env python3
"""Generate object reference markdown from Cotiza/fieldDocs HTML tables."""

import re
import html as html_lib
from pathlib import Path

FIELD_DOCS = Path(__file__).resolve().parents[2] / 'Cotiza' / 'fieldDocs'
DOCS_OUT = Path(__file__).resolve().parents[1] / 'docs' / 'objects'

OBJECTS = {
    'System_Settings__c': ('admin', 'CPQ System Settings', 'Base configuration source. Used to determine main display for the CPQ Container component, Quote Approval Submitter and more.'),
    'Playbook__c': ('admin', 'Playbook', 'High level container that can be used to define a specific operating motion.'),
    'Playbook_Scenario__c': ('admin', 'Playbook Scenario', 'Outlines a specific scenario that can be referenced by Rules, Approvals and View Sections.'),
    'Playbook_Scenario_Criterion__c': ('admin', 'Playbook Scenario Criterion', 'Individual criterion evaluation that contributes to the evaluation of a Playbook Scenario record.'),
    'Playbook_Question_Group__c': ('admin', 'Playbook Question Group', 'Container for Playbook Questions to be grouped visually within a Playbook.'),
    'Playbook_Question__c': ('admin', 'Playbook Question', 'Prompt for user input that dictates how a Quote should be configured within a Playbook.'),
    'Playbook_Rule__c': ('admin', 'Playbook Rule', 'Container for Playbook Rule Actions to be performed under specific circumstances within a Playbook.'),
    'Playbook_Rule_Action__c': ('admin', 'Playbook Rule Action', 'Individual action that can modify Question answers, line items and more.'),
    'Playbook_Rule_Calculation_Item__c': ('admin', 'Playbook Rule Calculation Item', 'Reference used to dynamically pull and combine information for a Rule Action.'),
    'Playbook_Approval__c': ('admin', 'Playbook Approval', 'Flag to oversee proper configuration within a Playbook.'),
    'Playbook_Approver_Group__c': ('admin', 'Playbook Approver Group', 'Container for Playbook Approvers grouped into order segments within an Approval.'),
    'Playbook_Approver__c': ('admin', 'Playbook Approver', 'Individual User that has power to approve/reject an Approval.'),
    'Playbook_View_Section__c': ('admin', 'Playbook View Section', 'Blueprint to generate a view for a Quote Proposal or an Approval Email.'),
    'Pricing_Set__c': ('admin', 'Pricing Set', 'Container for Pricing Thresholds to use in product pricing.'),
    'Pricing_Threshold__c': ('admin', 'Pricing Threshold', 'Individual number range for pricing determination within a Pricing Set.'),
    'Pricebook2': ('admin', 'Price Book', 'Standard SFDC Pricebook2 object referenced by a Playbook.'),
    'PricebookEntry': ('admin', 'Price Book Entry', 'Standard SFDC PricebookEntry object referenced by line items.'),
    'Product2': ('admin', 'Product', 'Standard SFDC Product2 object referenced by line items.'),
    'User': ('admin', 'User', 'Standard SFDC User object.'),
    'Quote': ('transaction', 'Quote', 'Standard SFDC Quote object. Primary output record from a Playbook configuration.'),
    'QuoteLineItem': ('transaction', 'Quote Line Item', 'Standard SFDC QuoteLineItem object. Output record for a product line item.'),
    'Playbook_Answer__c': ('transaction', 'Playbook Answer', 'Output for Playbook Question answer from a Quote Playbook configuration.'),
    'Quote_Approval__c': ('transaction', 'Quote Approval', 'Output for Playbook Approval from a Quote Playbook configuration.'),
    'Quote_Approval_Step__c': ('transaction', 'Quote Approval Step', 'Output for Playbook Approver Group from a Quote Playbook configuration.'),
    'Quote_Approver__c': ('transaction', 'Quote Approver', 'Output for Playbook Approver from a Quote Playbook configuration.'),
    'Quote_Proposal__c': ('transaction', 'Quote Proposal', 'Generated document based on View Sections from a Quote Playbook configuration.'),
    'Opportunity': ('transaction', 'Opportunity', 'Standard SFDC Opportunity object. Parent of Quote records.'),
    'OpportunityLineItem': ('transaction', 'Opportunity Product', 'Standard SFDC OpportunityLineItem object generated from synced Quote Line Items.'),
    'Contract': ('transaction', 'Contract', 'Standard SFDC Contract object. Representation of Opportunity/Quote after deal finalization.'),
    'Contract_Entitlement__c': ('transaction', 'Contract Entitlement', 'Entitlement record associated with a Contract.'),
    'Contract_Playbook_Answer__c': ('transaction', 'Contract Playbook Answer', 'Stored Playbook Question answers associated with a Contract.'),
    'ContentVersion': ('transaction', 'Content Version', 'Standard SFDC ContentVersion object used for generated proposal documents.'),
    'Opportunity_Field_Mapping__mdt': ('metadata', 'Opportunity Field Mapping', 'Facilitates field mappings from a synced Quote to the corresponding Opportunity.'),
    'OppLineItem_Field_Mapping__mdt': ('metadata', 'OppLineItem Field Mapping', 'Facilitates field mappings from QuoteLineItem to OpportunityLineItem records.'),
    'Entitlement_Field_Mapping__mdt': ('metadata', 'Entitlement Field Mapping', 'Facilitates field mappings from OpportunityLineItem to Contract Entitlement records.'),
    'Entitlement_Combination_Mapping__mdt': ('metadata', 'Entitlement Combination Mapping', 'Facilitates field mappings when Contract Entitlement records are combined upon Contract adjustment.'),
}


def escape_mdx(text: str) -> str:
    text = text.replace('\\', '\\\\')
    text = text.replace('{', '\\{')
    text = text.replace('}', '\\}')
    text = text.replace('|', '\\|')
    text = text.replace('<', '&lt;')
    return text


def html_table_to_md_rows(html_content: str) -> list[list[str]]:
    rows = []
    for tr in re.findall(r'<tr>(.*?)</tr>', html_content, re.DOTALL):
        cells = re.findall(r'<t[dh][^>]*>(.*?)</t[dh]>', tr, re.DOTALL)
        if not cells:
            continue
        cells = [html_lib.unescape(re.sub(r'<[^>]+>', '', c).strip()) for c in cells]
        cells = [escape_mdx(c.replace('\n', ' ')) for c in cells]
        rows.append(cells)
    return rows


def main() -> None:
    count = 0
    for stem, (category, title, description) in OBJECTS.items():
        src = FIELD_DOCS / f'{stem}.html'
        if not src.exists():
            print(f'Skipping missing source: {src.name}')
            continue
        rows = html_table_to_md_rows(src.read_text(encoding='utf-8', errors='replace'))
        md = f'# {title}\n\n{description}\n\n'
        md += '| API Name | Label | Description |\n'
        md += '| --- | --- | --- |\n'
        for row in rows[1:]:
            while len(row) < 3:
                row.append('')
            md += f'| `{row[0]}` | {row[1]} | {row[2]} |\n'
        out_dir = DOCS_OUT / category
        out_dir.mkdir(parents=True, exist_ok=True)
        (out_dir / f'{stem.lower()}.md').write_text(md, encoding='utf-8')
        count += 1
    print(f'Generated {count} object reference pages in {DOCS_OUT}')


if __name__ == '__main__':
    main()
