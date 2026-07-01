module.exports = {
  title: 'Cotiza CPQ',
  tagline: 'Native Salesforce CPQ for fast quoting workflows',
  favicon: 'img/circlelogo.png',

  url: 'https://cpq.cotiza.dev',
  baseUrl: '/',

  organizationName: 'tristanmoser',
  projectName: 'Cotiza.github.io',

  onBrokenLinks: 'warn',
  markdown: {
    mermaid: true,
    hooks: {
      onBrokenMarkdownLinks: 'warn',
    },
  },

  themes: ['@docusaurus/theme-mermaid'],

  presets: [
    [
      'classic',
      {
        docs: {
          sidebarPath: require.resolve('./sidebars.js'),
        },
        blog: false,
        theme: {
          customCss: require.resolve('./src/css/custom.css'),
        },
      },
    ],
  ],

  themeConfig: {
    navbar: {
      title: 'Cotiza CPQ',
      logo: {
        alt: 'Cotiza Logo',
        src: 'img/namelogo.png',
      },
      items: [
        { to: '/docs/intro', label: 'Docs', position: 'left' },
      ],
    },

    colorMode: {
      defaultMode: 'light',
      disableSwitch: true,
    },
  },
};