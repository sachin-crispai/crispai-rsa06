# Cluster 03 — Cloud Security (CNAPP / CSPM / CWPP)

**Stack:** Secure the cloud estate — posture, workloads, pipelines, and runtime.

CNAPP (Cloud-Native Application Protection Platform) consolidates CSPM, CWPP, CIEM, and IaC scanning. This is one of the hottest categories at RSAC 2026.

---

## Key Vendors

| Vendor | Focus | Booth | Notes |
|--------|-------|-------|-------|
| **Wiz** | CNAPP — cloud graph, risk prioritization | Gold Sponsor | Fastest growing cloud security co. |
| **Orca Security** | Agentless CNAPP | — | SideScanning™ technology |
| **Lacework** | Behavioral cloud security + CNAPP | — | Polygraph data platform |
| **Prisma Cloud (Palo Alto)** | Full CNAPP suite | — | Note: Palo Alto not exhibiting, but product exists |
| **Aqua Security** | Cloud-native / container security | — | Runtime protection + CNAPP |
| **Sysdig** | Runtime security + CNAPP | — | Falco-based; strong in K8s |
| **Rubrik** | Cloud data security & resilience | Platinum Sponsor | Data backup + ransomware recovery |
| **Commvault** | Data protection & cloud security | Gold Sponsor | Backup, recovery, threat detection |
| **Google Cloud Security** | Chronicle, Security Command Center | Platinum Sponsor | Native GCP security |
| **IBM Security** | QRadar, Guardium, Verify | Platinum Sponsor | Full-stack cloud + data security |
| **Expel** | Cloud detection & response (MDR) | Gold Sponsor | Cloud-native SOC |

---

## Technology Landscape

### CSPM (Cloud Security Posture Management)
Continuously assess cloud configuration against CIS benchmarks, compliance frameworks.
- **Leaders:** Wiz, Orca, Prisma Cloud, AWS Security Hub, Microsoft Defender for Cloud

### CWPP (Cloud Workload Protection Platform)
Runtime protection for VMs, containers, serverless workloads.
- **Leaders:** Aqua, Sysdig, CrowdStrike (Falcon Cloud Security), SentinelOne

### CIEM (Cloud Infrastructure Entitlement Management)
Identify and remediate over-privileged cloud IAM roles and permissions.
- **Leaders:** Wiz, Orca, Sonrai Security, CloudKnox (Microsoft)

### CNAPP (Combined Platform)
Unified platform covering the full cloud security lifecycle — code to cloud.
- **Leaders:** Wiz, Lacework, Orca, Prisma Cloud, Aqua, Sysdig

### Cloud Data Security
Protect data at rest and in motion across cloud storage, databases, SaaS.
- **Leaders:** Rubrik, Commvault, Varonis, BigID

---

## Key Questions to Ask at Booths
- Agentless vs. agent-based: what's the coverage tradeoff?
- How do you prioritize the thousands of findings — risk scoring approach?
- How does your platform handle multi-cloud (AWS + Azure + GCP)?
- What's your AI/LLM integration story for cloud workloads?
- How do you integrate with developer workflows (shift-left)?

---

## CrispAI Watch List
- [ ] **Wiz** — cloud graph + AI security posture
- [ ] **Orca** — agentless approach for quick deployment
- [ ] **Rubrik** — data resilience + cyber recovery

---

*→ Next: [Cluster 04 — Endpoint / EDR / XDR](04-endpoint-edr-xdr.md)*
