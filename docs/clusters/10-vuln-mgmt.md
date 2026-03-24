# Cluster 10 — Vulnerability Management

**Stack:** Find, prioritize, and remediate weaknesses before attackers exploit them.

Vuln management has evolved from periodic scanning to continuous, risk-based exposure management — integrating asset context, threat intel, and business impact.

---

## Key Vendors

| Vendor | Focus | Booth | Notes |
|--------|-------|-------|-------|
| **Tenable** | Vulnerability management platform | Platinum Sponsor | Nessus / Tenable.io / Tenable One |
| **Rapid7** | InsightVM + threat-informed prioritization | — | Strong PSIRT + cloud integration |
| **Qualys** | VMDR — vulnerability + detection + response | — | Cloud-native, agent + agentless |
| **Tanium** | Real-time endpoint vulnerability data | — | Sub-15s query of entire fleet |
| **Axonius** | Asset intelligence + vuln correlation | Platinum Sponsor | Connect the asset-to-vuln-to-owner dots |
| **Action1** | Patch management SaaS | — | Remote patch deployment |
| **Armis** | Asset visibility + vulnerability for OT/IoT | Platinum Sponsor | Agentless for unmanaged devices |
| **Claroty** | OT vulnerability management | — | ICS/SCADA CVE tracking |

---

## Technology Landscape

### Traditional Vulnerability Scanning
Network-based or agent-based scanning for CVEs on assets.
- **Leaders:** Tenable (Nessus), Qualys, Rapid7 InsightVM

### Continuous Exposure Management (CTEM)
Gartner framework: scoping → discovery → prioritization → validation → mobilization.
- **Leaders:** Tenable One, Qualys TruRisk, Armis, XM Cyber

### Risk-Based Prioritization
Go beyond CVSS scores — factor in exploitability (EPSS), asset criticality, threat intel.
- **Leaders:** Tenable, Rapid7, Kenna Security (Cisco), Nucleus Security

### Patch Management
Automate patching workflows, enforce SLAs, track compliance.
- **Leaders:** Tanium, Action1, ManageEngine Patch Manager Plus, Ivanti

### Attack Surface Management (ASM)
Discover unknown external assets and expose attack surface.
- **Leaders:** Tenable, Qualys, CyCognito, Axonius

---

## Key Questions to Ask at Booths
- How do you correlate vulnerability data with actual threat actor exploitation activity?
- EPSS vs. CVSS — how do you blend them in prioritization scoring?
- Cloud/container vulnerability coverage — image scanning, runtime?
- How do you handle patching for OT/ICS systems that can't be taken offline?
- Integration with ticketing (Jira/ServiceNow) for remediation workflow?

---

## CrispAI Watch List
- [ ] **Tenable** — Tenable One unified exposure management
- [ ] **Axonius** — connecting asset inventory to vulnerability prioritization
- [ ] **Action1** — cloud-native patch management for remote/hybrid

---

*→ Next: [Cluster 11 — AppSec / DevSecOps](11-appsec-devsecops.md)*
