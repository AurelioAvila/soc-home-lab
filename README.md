# SOC Home Lab — SIEM Monitoring, Detection Engineering & Alert Triage

A hands-on portfolio project focused on SOC (Security Operations Center) Tier 1 workflows: log ingestion, alert triage, and investigation-driven decision making.

---

## Why this project exists

Reading about SOC operations is easy. Demonstrating practical ability is not.

This repository exists to show how I approach real SOC Tier 1 activities, with an emphasis on:

- verifying data sources,
- validating alerts end-to-end,
- triaging events using context,
- documenting findings clearly.

The focus is on **process and reasoning**, not on “just installing tools”.

---

## Architecture

This lab uses a realistic SOC-style architecture:

- **Wazuh Manager (All-in-One)** running on Ubuntu (Oracle VirtualBox)
- **OpenSearch** for indexing and search
- **OpenSearch Dashboards** for alert visualization and investigation
- **Filebeat (Wazuh module)** for structured log ingestion
- **Windows 11 endpoint** with Wazuh Agent installed

This setup mirrors common entry-level SOC environments focused on host-based telemetry.

---

## What is monitored

The lab prioritizes real endpoint telemetry (not synthetic demo data), including:

- authentication activity (logon events, sudo/PAM where applicable),
- privilege-related activity and suspicious access patterns,
- host and process activity relevant to alert triage,
- agent status and heartbeat monitoring.

Alerts are enriched with:

- **MITRE ATT&CK** technique mapping,
- compliance metadata (e.g., PCI DSS, GDPR) when available in rule fields.

---

## SOC activities performed

This project demonstrates hands-on SOC Tier 1 activities, including:

- endpoint onboarding (agent deployment, enrollment, and connectivity checks),
- validation of log ingestion and normalization (ensuring events reach the SIEM),
- alert triage using contextual fields (host, user, rule metadata, timestamps),
- investigation of authentication and privilege-related events,
- troubleshooting ingestion and access issues (service status, permissions, authentication behavior),
- verification of OpenSearch indices and data flow into dashboards.

The emphasis is on understanding **why** alerts are generated and **how** to validate them, not merely enabling services.

---

## Tools and technologies

- SOC (Security Operations Center) concepts and workflows
- SIEM (Security Information and Event Management): **Wazuh**
- HIDS (Host-based Intrusion Detection System): **Wazuh Agent**
- **OpenSearch** and **OpenSearch Dashboards**
- **Filebeat** (Wazuh module)
- **Linux** (Ubuntu on VirtualBox)
- **Windows 11** endpoint
- **Oracle VirtualBox**

---

## Design decisions

Wazuh archives ingestion is handled through the official **Filebeat Wazuh module**, rather than custom ingestion inputs, to:

- reduce configuration drift,
- keep the deployment maintainable,
- better reflect production-style SOC environments.

---

## Evidence (screenshots)

Screenshots and artifacts are stored under:

- `screenshots/` — dashboards, agent status, alert examples  
- `configs/` — sanitized configuration excerpts  

> **Note:** Screenshots do not include credentials or sensitive host details.

---

## Project status

Core monitoring, ingestion validation, and alert triage workflows are implemented and tested.

**Planned next improvements:**

- a small set of custom detection rules,
- documented triage write-ups (alert → analysis → conclusion),
- additional endpoint scenarios for investigation practice.

---

## Troubleshooting & validation

Real SOC work is not about perfect setups, but about identifying and resolving ingestion and visibility issues.

During the build of this lab, multiple real-world problems were encountered and resolved, including:

- endpoint log ingestion verification,
- index visibility and data availability checks,
- authentication and permission-related errors,
- end-to-end data flow validation from source to SIEM.

The complete troubleshooting and validation process is documented here:

👉 **Log Ingestion & Validation Troubleshooting**

---

## Disclaimer

This project is for educational and portfolio purposes only.  
No production systems or real sensitive data are involved.
