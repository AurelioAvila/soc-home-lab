# SOC Home Lab — SIEM Monitoring, Detection Engineering & Alert Triage
A hands-on portfolio project focused on SOC Tier 1 workflows, alert triage and decision-making.
## Why this project exists
Reading about SOC operations is easy. Demonstrating practical understanding is not.
This repository exists to show how I approach **real SOC Tier 1 activities**, including:

- log ingestion and normalization,
- detection of suspicious behavior,
- alert triage with contextual analysis,
- structured documentation of security events.

The focus is on **process and reasoning**, not just tool installation.

## Scope of the lab
This home lab simulates a small SOC environment focused on **host-based telemetry**
and common attack patterns seen in entry-level SOC roles:

- SSH brute force and password spraying attempts
- Linux privilege escalation activity
- Suspicious authentication behavior

## Lab stack
- **Wazuh** as SIEM (Security Information and Event Management)
- **Ubuntu Server** as monitored endpoint(s)
- **VirtualBox** for virtualization

> Tooling may evolve as the lab grows. Any architectural or tooling change is
explicitly documented in `lessons-learned.md`.

## High-level architecture
- A Wazuh manager collects and correlates events from enrolled agents.
- Linux endpoints generate authentication and system logs.
- Alerts are investigated, classified, and documented following a SOC-style workflow.

Diagrams and details are available in the `architecture/` folder.

## Detection and triage philosophy
Each detection scenario in this repository includes:
- threat context and attacker intent,
- data sources and assumptions,
- detection logic and known limitations,
- alert triage steps used to confirm or dismiss the alert,
- evidence collected during analysis.

The goal is to **think like a SOC analyst**, not to blindly trust alerts.

## Repository structure
- `setup/` — installation and configuration steps (reproducible)
- `detection/` — detection logic, validation and tuning notes
- `incident-response/` — alert triage playbooks and incident summaries
- `screenshots/` — visual evidence of alerts and investigations
- `lessons-learned.md` — mistakes, fixes and improvements over time

## Assumptions and verification
This lab is built on commonly used configurations, but exact behavior can vary
depending on:
- Wazuh version,
- Linux distribution and log paths,
- available system resources.

Whenever a step is version-dependent or environment-specific, it is explicitly
noted and validated with screenshots or command output.
