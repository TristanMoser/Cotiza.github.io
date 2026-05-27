import React from 'react';
import Layout from '@theme/Layout';
import Link from '@docusaurus/Link';
import styles from './index.module.css';

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

          {/* HERO IMAGE (ADD SCREENSHOT HERE) */}
          <div style={{ marginTop: '2rem' }}>
            <img
              src="/img/hero-cotiza-dashboard.png"
              alt="Cotiza CPQ Salesforce interface"
              style={{
                width: '100%',
                borderRadius: '12px',
                boxShadow: '0 10px 30px rgba(0,0,0,0.15)',
              }}
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

      {/* VISUAL SECTION (LIKE GOOGLE SITES STYLE CALLOUTS) */}
      <section style={{ padding: '4rem 0', background: '#f9fafb' }}>
        <div className={styles.container}>
          <h2 style={{ textAlign: 'center', marginBottom: '2rem' }}>
            Built for Salesforce teams who move fast
          </h2>

          <div className={styles.grid}>
            <div className={styles.card}>
              <img
                src="/img/dynamic-quoting.png"
                alt="Dynamic quoting example"
                style={{ width: '100%', borderRadius: '8px', marginBottom: '1rem' }}
              />
              <h3>Interactive Quoting</h3>
              <p>Build quotes through guided inputs instead of static forms.</p>
            </div>

            <div className={styles.card}>
              <img
                src="/img/approval-flow.png"
                alt="Approval workflow"
                style={{ width: '100%', borderRadius: '8px', marginBottom: '1rem' }}
              />
              <h3>Smart Approvals</h3>
              <p>Automatically route deals based on configurable business rules.</p>
            </div>

            <div className={styles.card}>
              <img
                src="/img/proposal-pdf.png"
                alt="Proposal document preview"
                style={{ width: '100%', borderRadius: '8px', marginBottom: '1rem' }}
              />
              <h3>Proposal Output</h3>
              <p>Generate clean, branded PDFs directly from Salesforce data.</p>
            </div>
          </div>
        </div>
      </section>

      {/* CTA */}
      <section style={{ padding: '4rem 0' }}>
        <div className={styles.container} style={{ textAlign: 'center' }}>
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