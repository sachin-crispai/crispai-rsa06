# Cluster 09 — Threat Intelligence

**Stack:** Know your adversary — TTPs, IOCs, actor tracking, and intelligence-driven defense.

Threat intel is the force multiplier for every other security control — context that turns raw alerts into prioritized, attributable threats.

---

## Key Vendors

| Vendor | Focus | Booth | Notes |
|--------|-------|-------|-------|
| **Recorded Future** | Threat intelligence platform | — | Largest commercial TI provider |
| **Mandiant (Google)** | Threat intel + IR | Platinum Sponsor | Nation-state & APT expertise |
| **ThreatConnect** | TIP + SOAR integration | — | Intelligence-driven operations |
| **MISP Project** | Open-source threat intel sharing | — | Community-driven IOC sharing |
| **Flashpoint** | Deep & dark web intelligence | — | Illicit community monitoring |
| **Intel 471** | Cybercriminal intelligence | — | Underground forum access |
| **Anomali** | TI platform + SIEM integration | — | ThreatStream; strong STIX/TAXII |
| **Cyberint (Check Point)** | Attack surface + threat intel | Platinum Sponsor | External threat monitoring |
| **GreyNoise** | Internet noise filtering | — | Distinguish targeted vs. mass attacks |
| **Cybersixgill** | Dark web intelligence | — | Real-time underground monitoring |

---

## Technology Landscape

### Strategic Intelligence
Nation-state attribution, geopolitical risk, long-range threat forecasting.
- **Leaders:** Mandiant, Recorded Future, CrowdStrike Intelligence (not exhibiting)

### Operational Intelligence
Campaign tracking, malware family analysis, TTPs mapped to MITRE ATT&CK.
- **Leaders:** Recorded Future, ThreatConnect, Anomali

### Tactical Intelligence (IOCs)
IP addresses, domains, hashes, URLs — feed directly into security controls.
- **Leaders:** MISP, GreyNoise, Recorded Future, IBM X-Force

### Dark/Deep Web Intelligence
Monitor criminal forums, paste sites, leaked credentials, early-warning breach detection.
- **Leaders:** Flashpoint, Intel 471, Cybersixgill, Recorded Future

### Attack Surface Intelligence
External asset discovery + exposure monitoring + brand protection.
- **Leaders:** Cyberint, Recorded Future, Mandiant, CyCognito

---

## Key Questions to Ask at Booths
- How do you operationalize threat intel into security controls automatically?
- MITRE ATT&CK coverage — which tactics/techniques do you track?
- How do you reduce IOC false positives from stale indicators?
- Dark web coverage — how current is the data? What's the refresh rate?
- Integration with SIEM/SOAR — STIX/TAXII support?

---

## CrispAI Watch List
- [ ] **Recorded Future** — AI-driven intel summarization
- [ ] **GreyNoise** — noise reduction for SOC alert triage
- [ ] **Flashpoint** — dark web early warning capabilities

---

*→ Next: [Cluster 10 — Vulnerability Management](10-vuln-mgmt.md)*
