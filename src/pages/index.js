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
      <header className={styles.hero}>
        <div className={styles.container}>
          <h1 className={styles.title}>
            Faster quoting inside Salesforce.
          </h1>

          <p className={styles.subtitle}>
            Cotiza CPQ helps sales teams generate accurate quotes,
            manage approvals, and close deals without leaving Salesforce.
          </p>

          <div className={styles.buttons}>
            <Link className="button button--primary button--lg" to="/docs/intro">
              Get Started
            </Link>

            <Link className="button button--secondary button--lg" to="/docs/getting-started/installation">
              Installation Guide
            </Link>
          </div>
        </div>
      </header>

      <main className={styles.features}>
        <div className={styles.container}>
          <div className={styles.grid}>
            <div className={styles.card}>
              <h3>Native Salesforce CPQ</h3>
              <p>Built directly on Salesforce with full security and governance alignment.</p>
            </div>

            <div className={styles.card}>
              <h3>Fast Quote Creation</h3>
              <p>Create and update quotes in seconds with streamlined workflows.</p>
            </div>

            <div className={styles.card}>
              <h3>Approval Automation</h3>
              <p>Route discounts and deals through configurable approval logic.</p>
            </div>

            <div className={styles.card}>
              <h3>Flexible Pricing</h3>
              <p>Support for dynamic pricing rules and product configurations.</p>
            </div>

            <div className={styles.card}>
              <h3>PDF Generation</h3>
              <p>Generate professional quote documents instantly.</p>
            </div>

            <div className={styles.card}>
              <h3>Admin Friendly</h3>
              <p>Easy setup, permission sets, and full admin control.</p>
            </div>
          </div>
        </div>
      </main>
    </Layout>
  );
}