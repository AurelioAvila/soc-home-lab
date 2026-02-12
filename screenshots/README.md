# Screenshots

This folder contains evidence screenshots for the SOC Home Lab project.

---

## Agent Successfully Connected

The Windows 11 agent was successfully deployed and connected to the Wazuh Manager.

This confirms:
- Successful agent registration
- Active communication with the manager
- Proper network configuration

![Agent Active](agent-active.png)

---

## Failed Login Detection (Windows Event ID 4625)

A failed authentication attempt was simulated using a non-existing user account via:

runas /user:fakeuser cmd

This generated a Windows Security Event ID 4625 (Logon Failure).

Wazuh successfully ingested the Security log and generated a Level 5 alert, 
mapped to MITRE ATT&CK techniques:

- T1078 – Valid Accounts
- T1531 – Account Access Removal

The alert confirms:
- Windows Security log collection is working
- Detection rules are active
- MITRE mapping is enabled
- The agent is properly parsing eventchannel logs

![Failed Login Detection](failed-login-detection.png)
