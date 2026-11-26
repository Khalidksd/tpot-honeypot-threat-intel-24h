# 6. Recommendations and lessons learned

[Back to README](../README.md)

## 6.1 Recommendations for real systems

| # | Recommendation | Finding it answers |
| --- | --- | --- |
| 1 | Use SSH keys, disable password and root logins, add Fail2ban | Cowrie took about 3,000 events, mostly root logins |
| 2 | Remove or change default accounts before going online, ban common passwords | root, admin, pi, postgres with 123456 and P@ssw0rd |
| 3 | Do not expose SMB, RDP, VNC, SNMP or Redis to the internet; use a VPN | Dionaea, RDP, VNC and SNMP CVE traffic |
| 4 | Patch old systems, apply MS17-010, retire unpatchable devices | 1,445 DoublePulsar alerts, CVEs from 2001 and 2002 |
| 5 | Restrict SIP to known providers and use strong SIP credentials | 965 Sentrypeer events |
| 6 | Limit admin panels to trusted IPs | My own web UI was open to 0.0.0.0/0 |
| 7 | Feed DShield and Talos block lists into the firewall | 960 DShield alerts, 77.239.124.64 on the Talos list |
| 8 | Alert on DoublePulsar and Nmap signatures in real networks | SIDs 2024766 and 2009582 |

## 6.2 Limitations

* **Time window.** The study covers a 24-hour window, enough for a clear sample of automated attacks; a longer run would also surface slower, targeted activity.
* **Single vantage point.** The honeypot ran from one AWS region (Stockholm), so the mix of countries and services reflects what is visible from there.
* **Observation, not attribution.** An IP shows where traffic came from, not who was behind it, so sources are reported as observations rather than named attackers.
* **Automated activity.** A honeypot mainly draws scanners and bots, so the findings represent opportunistic, internet-wide attacks rather than a targeted intrusion.
* **Reading the figures.** Figures come from the live Kibana dashboards; a few summary tiles show large totals rounded, so exact counts are taken from the top-ten tables.

## 6.3 Lessons learned

1. **Exposure is found fast.** Attacks began almost as soon as the ports were open.
2. **Most attacks are lazy.** Default passwords and very old exploits make up the bulk of the traffic. Basic hygiene stops most of it.
3. **Read dashboards critically.** Rounded numbers, gaps in collection and packet versus connection counts all change what a chart seems to say.
4. **Correlate tables.** Matching the top source IPs against the ASN data confirmed each attacker's network and showed that one IP produced over a third of all events.
5. **Use more than one intelligence source.** Kibana and Talos disagreed on who owns the top IP.
6. **Secure the honeypot as well.** I left the web UI open to everyone. It is a small but real risk.

## 6.4 Next steps

* Run for at least a week and compare weekdays with weekends.
* Restrict port 64297 to my own IP.
* Export raw logs to CSV for exact counts and deeper queries.
* Pull Cowrie session logs to see commands typed after a fake successful login.
* Add a second sensor in another region to compare traffic.
* Send alerts to a SIEM or a chat channel for near real time monitoring.
