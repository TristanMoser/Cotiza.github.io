module.exports = {
  tutorialSidebar: [
    'intro',
    {
      type: 'category',
      label: 'Getting Started',
      items: [
        'getting-started/installation',
        'getting-started/permissions',
        'getting-started/setup',
      ],
    },
    {
      type: 'category',
      label: 'Admin Guide',
      items: [
        'admin-guide/configuration',
        'admin-guide/pricing-rules',
        'admin-guide/approvals',
      ],
    },
    {
      type: 'category',
      label: 'User Guide',
      items: [
        'user-guide/creating-quotes',
        'user-guide/quote-line-items',
        'user-guide/generating-pdfs',
      ],
    },
    {
      type: 'category',
      label: 'Security',
      items: [
        'security/data-handling',
        'security/compliance',
      ],
    },
    {
      type: 'category',
      label: 'Troubleshooting',
      items: [
        'troubleshooting/common-errors',
      ],
    },
    {
      type: 'category',
      label: 'Release Notes',
      items: [
        'release-notes/v1-0-0',
      ],
    },
  ],
};