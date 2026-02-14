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

## Investigation Flow

The investigation followed a structured SOC Tier 1 workflow:

1. Alert validation — confirmed event authenticity and log ingestion.
2. Context gathering — reviewed affected accounts and event patterns.
3. Pattern analysis — evaluated repetition and automation indicators.
4. Impact assessment — verified absence of successful authentication.
5. Classification — activity categorized as potential brute force attempt.

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

## Analyst Thinking Process

During investigation, the main objective was to distinguish between normal user behavior and malicious authentication attempts.

Key reasoning steps:

- Multiple failures occurring in a short timeframe suggest automation rather than human typing errors.
- Repeated attempts against authentication mechanisms are commonly associated with brute force techniques.
- Absence of successful logons reduced immediate impact but required continued monitoring.

Decision:
The alert was classified as **medium severity**, requiring monitoring but not immediate escalation.
