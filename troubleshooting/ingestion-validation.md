# Log Ingestion & Validation Troubleshooting

## Purpose

This document documents the troubleshooting and validation steps performed to ensure
correct log ingestion from endpoints into the SIEM stack.

The goal is not tool installation, but **verifying data flow end-to-end**, identifying
ingestion gaps, and validating assumptions — exactly as done in a real SOC environment.

---

## Context

During the initial setup of the SOC Home Lab, alerts were visible in the Wazuh dashboard,
but it was necessary to **prove** that:

- logs were correctly collected at source,
- logs were parsed and normalized,
- logs reached the indexing layer,
- alerts were generated from validated data.

This section documents how that validation was performed.

---

## Environment Overview

- **Wazuh Manager (All-in-One)** running on Ubuntu (VirtualBox)
- **OpenSearch** for indexing and alert visualization
- **Filebeat (Wazuh module)** for log ingestion
- **Windows 11 endpoint** with Wazuh agent installed

---

## Initial Observation

- Wazuh dashboard was accessible
- Agent appeared as *Active*
- Alerts were visible

However, the following questions needed explicit confirmation:

- Are logs actually ingested, or only alerts?
- Are archives enabled?
- Is Filebeat ingesting raw events?
- Are indices created as expected?

---

## Investigation Steps

### 1. Filebeat Service Validation

The Filebeat service was checked to confirm it was running:

```bash
sudo systemctl status filebeat
