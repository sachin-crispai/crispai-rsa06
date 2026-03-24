# Cluster 05 — SIEM & Log Management

**Stack:** Collect, correlate, and query security telemetry — the SOC's nervous system.

SIEM is undergoing a renaissance: cloud-native architectures, AI-driven detection, and next-gen query languages are replacing legacy on-prem stacks.

---

## Key Vendors

| Vendor | Focus | Booth | Notes |
|--------|-------|-------|-------|
| **Splunk (Cisco)** | SIEM + SOAR + Observability | N-6144 | Industry standard; now part of Cisco |
| **IBM Security (QRadar)** | QRadar SIEM + SOAR | Platinum Sponsor | Enterprise SIEM; SaaS migration underway |
| **Elastic** | Elastic Security — SIEM on Elasticsearch | Gold Sponsor | Open, flexible; strong for cloud-native |
| **Exabeam** | AI-driven SIEM + UEBA | Gold Sponsor | Behavior analytics-first approach |
| **LogRhythm (now Exabeam)** | SIEM + NDR | Gold Sponsor | Merged with Exabeam 2024 |
| **Microsoft Sentinel** | Cloud-native SIEM on Azure | N-5744 | Best-in-class Azure integration |
| **Stellar Cyber** | Open XDR platform | Booth 327 | Multi-vendor data lake approach |
| **Securonix** | AI-driven SIEM + UEBA | — | Cloud-native, strong UEBA |
| **ManageEngine** | SIEM for mid-market | Gold Sponsor | Log360 — affordable, comprehensive |

---

## Technology Landscape

### Legacy SIEM
On-prem or hybrid deployments with heavy customization.
- **Players:** Splunk Enterprise, IBM QRadar on-prem, ArcSight (Micro Focus/OpenText)

### Cloud-Native SIEM
SaaS delivery, elastic storage, modern query languages.
- **Leaders:** Microsoft Sentinel, Splunk Cloud, Google Chronicle, Elastic Security

### AI-Driven SIEM / UEBA
Behavioral baselines, anomaly detection, reduced alert fatigue via ML.
- **Leaders:** Exabeam, Securonix, Stellar Cyber

### Open XDR / Data Lake
Ingest all telemetry into a normalized data lake; apply detection on top.
- **Leaders:** Stellar Cyber, Google Chronicle, Hunters.ai

---

## Key Questions to Ask at Booths
- What's your detection-as-code / SIGMA rule support?
- How do you handle the cost explosion of high-volume log ingestion?
- AI/ML detection: what's the false-positive rate in production?
- How do you integrate with threat intel feeds (STIX/TAXII)?
- Migration story from legacy SIEM — how long does a typical cutover take?

---

## CrispAI Watch List
- [ ] **Exabeam** — AI-driven UEBA and SIEM fusion
- [ ] **Stellar Cyber** Booth 327 — open XDR pricing model
- [ ] **Elastic** — open-source SIEM cost model

---

*→ Next: [Cluster 06 — SOAR & Automation](06-soar-automation.md)*
