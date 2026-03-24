# Cluster 08 — SASE / SSE

**Stack:** Converge networking and security at the cloud edge — access from anywhere, secured everywhere.

SASE (Secure Access Service Edge) merges SD-WAN with SSE (Security Service Edge: SWG, CASB, ZTNA, FWaaS). SSE is the security-only subset.

---

## Key Vendors

| Vendor | Focus | Booth | Notes |
|--------|-------|-------|-------|
| **Zscaler** | Zero Trust Exchange — market-leading SSE | Gold Sponsor | ZTNA, SWG, CASB, DLP |
| **Netskope** | SSE + SASE | — | Strong CASB + data-centric approach |
| **Cloudflare** | SASE — One platform | Platinum Sponsor | Magic WAN + Zero Trust |
| **Cato Networks** | Full SASE (SD-WAN + SSE) | — | Single-vendor, global private backbone |
| **Akamai** | SSE (EAA + SWG + CASB) | Gold Sponsor | Edge-native security |
| **Cisco** | Cisco+ Secure Connect (SASE) | Booth 6044 | Meraki SD-WAN + Umbrella SSE |
| **Fortinet** | FortiSASE | N-5762 | Tight integration with FortiGate on-prem |
| **Check Point** | Harmony SASE | Platinum Sponsor | Harmony Connect + Harmony Browse |
| **Iboss** | Cloud security platform (SASE) | — | Strong in education/government |

---

## Technology Landscape

### SWG (Secure Web Gateway)
URL filtering, malware inspection, SSL decryption for web traffic.
- **Leaders:** Zscaler, Netskope, Cisco Umbrella, Cloudflare Gateway

### CASB (Cloud Access Security Broker)
Visibility and control over SaaS app usage — shadow IT, data leakage.
- **Leaders:** Netskope, Zscaler, Microsoft Defender for Cloud Apps

### ZTNA (Zero Trust Network Access)
Identity-verified, app-level access replacing VPN.
- **Leaders:** Zscaler, Cloudflare Access, Cato, Appgate

### SD-WAN
Software-defined WAN with traffic optimization and application-aware routing.
- **Leaders:** Cato Networks, Cisco Meraki, Fortinet SD-WAN

### FWaaS (Firewall-as-a-Service)
Cloud-delivered NGFW inspection for all traffic.
- **Leaders:** Zscaler, Cloudflare, Cato, Fortinet

---

## Key Questions to Ask at Booths
- Single-vendor SASE vs. best-of-breed SSE: what's the integration cost?
- How do you handle on-prem / legacy app access through your SASE fabric?
- What's the latency impact for remote workers going through your PoPs?
- AI/DLP integration — can you detect sensitive data in LLM prompts/responses?

---

## CrispAI Watch List
- [ ] **Cato Networks** — full single-vendor SASE pricing model
- [ ] **Netskope** — AI/LLM data leakage protection
- [ ] **Cloudflare** — developer-friendly SASE onboarding

---

*→ Next: [Cluster 09 — Threat Intelligence](09-threat-intelligence.md)*
