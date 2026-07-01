import React from 'react';
import Layout from '@theme/Layout';
import Link from '@docusaurus/Link';
import useBaseUrl from '@docusaurus/useBaseUrl';
import styles from './index.module.css';

function Screenshot({ src, alt, className }) {
  return (
    <img
      src={useBaseUrl(src)}
      alt={alt}
      className={className}
      loading="lazy"
    />
  );
}

export default function Home() {
  return (
    <Layout
      title="Cotiza CPQ"
      description="Native Salesforce CPQ for fast, flexible quoting workflows"
    >
      {/* HERO */}
      <header className={styles.hero}>
        <div className={styles.container}>
          <h1 className={styles.title}>
            Point. Click. Quote.
          </h1>

          <p className={styles.subtitle}>
            Cotiza CPQ is a fully native Salesforce Sales Cloud companion for end-to-end deal management—
            powering dynamic quoting, automated approvals, and polished proposal generation without leaving Salesforce.
          </p>

          <div className={styles.buttons}>
            <Link className="button button--primary button--lg" to="/docs/intro">
              Get Started
            </Link>

            <Link className="button button--secondary button--lg" to="/docs/getting-started/installation">
              Installation Guide
            </Link>
          </div>

          <div className={styles.heroImage}>
            <Screenshot
              src="/img/screenshots/hero.png"
              alt="Cotiza CPQ hub showing quotes for an Opportunity"
              className={styles.screenshotHero}
            />
          </div>
        </div>
      </header>

      {/* FEATURE GRID */}
      <main className={styles.features}>
        <div className={styles.container}>
          <div className={styles.grid}>

            <div className={styles.card}>
              <h3>Dynamic Quoting</h3>
              <p>
                Show what you want. Hide what you don’t. Automate pricing logic with
                intelligent, form-driven quote configuration.
              </p>
            </div>

            <div className={styles.card}>
              <h3>Approval Automation</h3>
              <p>
                Build configurable approval paths based on real-time deal inputs like
                discounts, products, or deal size.
              </p>
            </div>

            <div className={styles.card}>
              <h3>Proposal Generation</h3>
              <p>
                Generate polished, customer-ready quote documents using Salesforce data,
                product selections, and branded templates.
              </p>
            </div>

            <div className={styles.card}>
              <h3>Subscriptions</h3>
              <p>
                Extend CPQ beyond the initial sale—support renewals, upgrades, and
                subscription lifecycle management.
              </p>
            </div>

            <div className={styles.card}>
              <h3>Native Salesforce Architecture</h3>
              <p>
                No external systems. No sync issues. Cotiza runs entirely inside Salesforce
                with full security alignment.
              </p>
            </div>

            <div className={styles.card}>
              <h3>Data-Driven Configuration</h3>
              <p>
                Adapt quickly to your sales process with toggle-based configuration and
                fully customizable workflows.
              </p>
            </div>

          </div>
        </div>
      </main>

      {/* VISUAL SECTION */}
      <section className={styles.visualSection}>
        <div className={styles.container}>
          <h2 className={styles.visualHeading}>
            Built for Salesforce teams who move fast
          </h2>

          <div className={`${styles.grid} ${styles.visualGrid}`}>
            <div className={`${styles.card} ${styles.visualCard}`}>
              <div className={styles.screenshotFrame}>
                <Screenshot
                  src="/img/screenshots/cpq-playbook-questions.png"
                  alt="Playbook question groups in the quote configuration wizard"
                  className={styles.screenshotCard}
                />
              </div>
              <div className={styles.visualCardBody}>
                <h3>Interactive Quoting</h3>
                <p>Build quotes through guided inputs instead of static forms.</p>
              </div>
            </div>

            <div className={`${styles.card} ${styles.visualCard}`}>
              <div className={styles.screenshotFrame}>
                <Screenshot
                  src="/img/screenshots/cpq-approvals-hub.png"
                  alt="Cotiza CPQ Approvals hub with pending approval levels"
                  className={styles.screenshotCard}
                />
              </div>
              <div className={styles.visualCardBody}>
                <h3>Smart Approvals</h3>
                <p>Automatically route deals based on configurable business rules.</p>
              </div>
            </div>

            <div className={`${styles.card} ${styles.visualCard}`}>
              <div className={styles.screenshotFrame}>
                <Screenshot
                  src="/img/screenshots/generate-proposal.png"
                  alt="Proposals table listing generated quote documents"
                  className={styles.screenshotCard}
                />
              </div>
              <div className={styles.visualCardBody}>
                <h3>Proposal Output</h3>
                <p>Generate clean, branded PDFs directly from Salesforce data.</p>
              </div>
            </div>
          </div>
        </div>
      </section>

      {/* CTA */}
      <section className={styles.cta}>
        <div className={`${styles.container} ${styles.ctaInner}`}>
          <h2>Start building better quoting workflows today</h2>
          <p>
            Install Cotiza CPQ from the Salesforce AppExchange and streamline your entire sales process.
          </p>

          <a
            className="button button--primary button--lg"
            href="https://appexchange.salesforce.com"
            target="_blank"
            rel="noopener noreferrer"
          >
            View on AppExchange
          </a>
        </div>
      </section>
    </Layout>
  );
}
