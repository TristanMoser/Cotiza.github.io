module.exports = {
  title: 'Cotiza CPQ',
  tagline: 'Native Salesforce CPQ for fast quoting workflows',
  favicon: 'img/logo.png',

  url: 'https://tristanmoser.github.io',
  baseUrl: '/Cotiza.github.io/',

  organizationName: 'tristanmoser',
  projectName: 'Cotiza.github.io',

  onBrokenLinks: 'warn',
  markdown: {
    hooks: {
      onBrokenMarkdownLinks: 'warn',
    },
  },

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
        src: 'img/logo.png',
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