# Log Ingestion & Validation Troubleshooting

## Purpose

This document describes the troubleshooting and validation steps performed to ensure correct log ingestion from endpoints into the SIEM stack.

The goal is not tool installation, but **verifying end-to-end data flow**, identifying ingestion gaps, and validating assumptions — exactly as performed in a real SOC environment.

---

## Context

During the initial setup of the SOC Home Lab, alerts were visible in the Wazuh dashboards.  
However, in a SOC context, visibility alone is not sufficient.

It was necessary to **prove** that alerts were generated from correctly ingested and validated data, rather than from partial telemetry or misconfiguration.

Specifically, the following conditions had to be confirmed:

- logs were correctly collected at the source,
- logs were parsed and normalized,
- logs reached the indexing layer,
- alerts were generated from validated events.

This section documents how that validation was performed.

---

## Environment Overview

- **Wazuh Manager (All-in-One)** running on Ubuntu (Oracle VirtualBox)
- **OpenSearch** for indexing and search
- **OpenSearch Dashboards** for alert visualization
- **Filebeat (Wazuh module)** for structured log ingestion
- **Windows 11 endpoint** with Wazuh Agent installed

---

## Initial Observation

At first glance, the environment appeared operational:

- Wazuh dashboards were accessible
- The endpoint agent reported as *Active*
- Security alerts were visible

However, several key questions required explicit verification:

- Are logs actually ingested, or are only alerts visible?
- Are Wazuh archives enabled and forwarded?
- Is Filebeat ingesting raw events as expected?
- Are indices created and populated correctly?

---

## Investigation & Validation Steps

### 1. Filebeat Service Validation

The Filebeat service was checked to confirm that the ingestion pipeline was active and operational:
```bash
sudo systemctl status filebeat
```

### 2. Wazuh Archives Ingestion Verification

To validate that alerts were generated from real event data and not only from pre-processed signals, Wazuh archives ingestion was explicitly verified.

Enabling and validating archives ensures access to raw event logs, which is critical for:
- confirming data collection at the agent level,
- validating parsing and normalization behavior,
- performing deeper investigations beyond alert summaries.

The ingestion pipeline was configured to rely on the official Wazuh Filebeat module rather than custom Filebeat inputs.
This design choice reduces configuration drift and better reflects production SOC environments.

Successful archives ingestion confirmed that raw endpoint events were being forwarded from the Wazuh Manager to the indexing layer.

---

### 3. Index Availability and Data Flow Validation

After confirming that raw logs were being forwarded, OpenSearch indices were inspected to verify that data was correctly indexed and searchable.

This validation focused on:
- confirming that expected indices were created,
- ensuring indices contained recent events,
- verifying that timestamps, hostnames, and event types aligned with endpoint activity.

These checks validated the complete data flow across the pipeline:

Endpoint → Wazuh Agent → Wazuh Manager → Filebeat → OpenSearch

Successful index validation confirmed that the SIEM contained reliable and queryable telemetry rather than partial or stale data.

---

### 4. Authentication and Permission Troubleshooting

During index validation, authentication and permission-related issues were encountered while querying OpenSearch.

These issues were investigated by:
- reviewing OpenSearch security configuration,
- validating service authentication behavior,
- confirming appropriate permissions for index access.

Resolving these issues was critical to avoid false assumptions about data absence when the root cause was access control rather than ingestion failure.

Once authentication and permissions were corrected, index visibility and query results behaved as expected.

---

### 5. End-to-End Validation Outcome

After completing the validation steps above, it was confirmed that:
- logs were collected at the endpoint,
- logs were parsed and normalized by Wazuh,
- events were successfully ingested into OpenSearch,
- alerts were generated from validated and indexed data.

This confirmed the integrity and reliability of the entire ingestion and detection pipeline.

---

## SOC Relevance

This troubleshooting process reflects real SOC workflows, where:
- alerts are never trusted at face value,
- ingestion pipelines must be explicitly validated,
- visibility issues are investigated methodically,
- assumptions are verified through evidence rather than dashboards alone.

The focus throughout this process was on reasoning, validation, and decision-making rather than simply enabling services.

---

## Conclusion

The log ingestion and validation workflow is fully functional and verified.

This troubleshooting exercise demonstrates practical SOC Tier 1 skills in:
- log ingestion validation,
- SIEM troubleshooting,
- data flow verification,
- investigation of authentication and visibility issues.

