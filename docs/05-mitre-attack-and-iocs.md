# 5. MITRE ATT&CK mapping and indicators of compromise

[Back to README](../README.md)

Everything observed sits in the earliest stages of an attack. Because these were honeypots, no attacker got further than reconnaissance, credential attacks and initial access attempts.

## 5.1 Mapping

| Tactic | Technique | ID | Evidence |
| --- | --- | --- | --- |
| Reconnaissance | Active Scanning: Scanning IP Blocks | [T1595.001](https://attack.mitre.org/techniques/T1595/001/) | Honeytrap hits across thousands of ports, Nmap SYN scan alerts (SID 2009582) |
| Reconnaissance | Active Scanning: Vulnerability Scanning | [T1595.002](https://attack.mitre.org/techniques/T1595/002/) | CVE matches for SNMP, RDP, VNC, OpenSSL, Dovecot |
| Discovery | Network Service Discovery | [T1046](https://attack.mitre.org/techniques/T1046/) | Repeated probing of 5060, 22, 445 and 10001 |
| Credential Access | Brute Force: Password Guessing | [T1110.001](https://attack.mitre.org/techniques/T1110/001/) | Cowrie logins with root, admin and 123456 |
| Credential Access | Brute Force: Password Spraying | [T1110.003](https://attack.mitre.org/techniques/T1110/003/) | The same short password list across many usernames |
| Initial Access | Valid Accounts: Default Accounts | [T1078.001](https://attack.mitre.org/techniques/T1078/001/) | pi, postgres, elasticsearch, azureuser and similar |
| Initial Access | Exploit Public Facing Application | [T1190](https://attack.mitre.org/techniques/T1190/) | Exploit attempts against SNMP, VNC, mail and FTP |
| Lateral Movement | Exploitation of Remote Services | [T1210](https://attack.mitre.org/techniques/T1210/) | DoublePulsar and SMB exploit traffic on 445 |
| Command and Control | Proxy | [T1090](https://attack.mitre.org/techniques/T1090/) | HTTP CONNECT open proxy tests (SID 2008284) |
| Impact | Endpoint Denial of Service | [T1499](https://attack.mitre.org/techniques/T1499/) | DoS CVEs such as CVE-2012-0152 and CVE-2001-0540 |

**Note on T1210:** this is usually a lateral movement technique inside a network. I included it because DoublePulsar and EternalBlue are worm tooling built to spread between machines, and here it was pointed straight at an internet facing host.

## 5.2 Kill chain view

```
Reconnaissance  →  Credential Access and Initial Access  →  (stopped: honeypot)
T1595, T1046        T1110, T1078, T1190, T1210
```

## 5.3 Indicators of compromise

CSV: [`data/iocs.csv`](../data/iocs.csv)

| Indicator | Type | Evidence | Action |
| --- | --- | --- | --- |
| 77.239.124.64 | IPv4 | 2,674 events, Talos block listed, Untrusted | Block |
| 181.115.183.74 | IPv4 | 332 events, sender reputation Poor | Block |
| 51.89.235.147 | IPv4 | 312 events, Questionable | Monitor |
| SID 2024766 | Suricata rule | DoublePulsar, 1,445 alerts | Alert on any match |
| root / 123456 | Credential pair | Most attempted | Make sure no real system uses it |

These come from one honeypot on one day. Review them before adding them to a production block list, because cloud and residential IPs are reassigned often.
