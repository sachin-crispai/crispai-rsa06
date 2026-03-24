# Cluster 02 — Zero Trust Architecture

**Stack:** Never trust, always verify. Micro-segmentation, continuous validation, least-privilege access.

Zero Trust has moved from buzzword to architecture — this cluster covers the vendors building the enforcement fabric: network micro-segmentation, software-defined perimeter, and identity-driven access.

---

## Key Vendors

| Vendor | Focus | Booth | Notes |
|--------|-------|-------|-------|
| **Zscaler** | Zero Trust Exchange (cloud-native ZTNA) | Gold Sponsor | Largest pure-play ZT vendor |
| **Illumio** | Micro-segmentation | Platinum Sponsor | Workload-level segmentation |
| **Appgate** | SDP / ZTNA | — | Software-defined perimeter |
| **Elisity** | Identity-based micro-segmentation | — | OT/IoT + enterprise |
| **Akamai** | Zero Trust + CDN security | Gold Sponsor | Enterprise Application Access (EAA) |
| **Cloudflare** | Zero Trust platform (Access, Gateway, WARP) | Platinum Sponsor | Developer-friendly ZT |
| **Cisco** | Zero Trust across portfolio | Booth 6044 | Duo + Cisco ISE + SD-Access |

---

## Technology Landscape

### ZTNA (Zero Trust Network Access)
Replace VPN with identity-verified, application-level access — no implicit network trust.
- **Leaders:** Zscaler, Cloudflare Access, Appgate, Cisco

### Micro-Segmentation
East-west traffic control at the workload level — contain lateral movement post-breach.
- **Leaders:** Illumio, Akamai Guardicore, Cisco Tetration

### Software-Defined Perimeter (SDP)
Create invisible, on-demand encrypted tunnels between verified users and services.
- **Leaders:** Appgate, Zscaler

### Continuous Validation
Ongoing device posture + user behavior assessment — not just at login.
- **Players:** Axonius (asset context), CrowdStrike (endpoint posture), Okta (adaptive MFA)

---

## Key Questions to Ask at Booths
- How do you handle agentless ZTNA for unmanaged/BYOD devices?
- What's your approach for OT/ICS environments where you can't install agents?
- How do you integrate with SIEM/SOAR for automated policy enforcement?
- What does the migration path look like from legacy VPN?

---

## CrispAI Watch List
- [ ] **Illumio** — segmentation for hybrid cloud + OT
- [ ] **Cloudflare** — developer-centric Zero Trust adoption
- [ ] **Zscaler** — AI-powered policy recommendations

---

*→ Next: [Cluster 03 — Cloud Security](03-cloud-security.md)*
