# Case Study 01 — Failed Logon Investigation (Event ID 4625)

## Scenario
A Windows endpoint generated multiple failed authentication events detected by Wazuh.
The objective was to determine whether the activity represented normal user error or a potential brute force attack.

## Alert Information
- Source: Wazuh SIEM
- Event ID: 4625
- Log Source: Windows Security Log
- Detection Type: Failed Logon Attempt
- MITRE ATT&CK: T1110 – Brute Force

## Initial Triage
Observed multiple failed login attempts within a short time window.

Key fields analyzed:
- TargetUserName
- Source IP Address
- Logon Type
- Failure Reason

## Investigation Steps
1. Verified agent connectivity and log ingestion.
2. Reviewed event frequency in OpenSearch dashboard.
3. Checked whether attempts targeted a single or multiple accounts.
4. Validated timestamps and repetition pattern.

## Findings
Repeated authentication failures suggested automated or scripted login attempts rather than normal user behavior.

## Analyst Assessment
Activity classified as **potential brute force attempt**.
No successful authentication observed.

## Response / Recommendations
- Monitor for Event ID 4624 (successful login).
- Consider account lockout policy tuning.
- Continue monitoring source IP activity.

## Lessons Learned
Validating log ingestion is essential before trusting alert visibility.
