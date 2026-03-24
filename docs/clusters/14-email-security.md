# Cluster 14 — Email & Messaging Security

**Stack:** Block phishing, BEC, and malware delivered through the most-exploited channel in cybersecurity.

Email remains the #1 initial access vector. This cluster covers SEG, API-based email security, and collaboration security.

---

## Key Vendors

| Vendor | Focus | Booth | Notes |
|--------|-------|-------|-------|
| **Proofpoint** | Email security + DLP + awareness | N-6163 | Platinum Sponsor; market leader |
| **Mimecast** | Email security + resilience | N-5245 | Gold Sponsor; strong in BEC defense |
| **Abnormal Security** | AI-native email security | — | Behavioral AI; API-based for M365/Gmail |
| **Darktrace** | AI email security (Antigena Email) | — | Self-learning AI for BEC/phishing |
| **Cofense** | Phishing detection + response | — | Human-driven phishing intel + training |
| **Agari (HelpSystems)** | Email authentication + BEC protection | — | DMARC enforcement + brand protection |
| **Cisco (IronPort/SEG)** | Cisco Secure Email | Booth 6044 | Part of Cisco security portfolio |
| **Tessian** | Human layer email security | — | Behavioral ML for misdirected email |
| **Egress** | Intelligent email security | — | Outbound email DLP + phishing protection |

---

## Technology Landscape

### SEG (Secure Email Gateway)
Inline filtering of inbound/outbound email — anti-spam, anti-phishing, malware scanning.
- **Leaders:** Proofpoint, Mimecast, Cisco IronPort, Broadcom Symantec

### API-Based Email Security
Connect via API to M365/Gmail — behavioral analysis without MX record change.
- **Leaders:** Abnormal Security, Darktrace, Tessian, Cofense

### BEC (Business Email Compromise) Protection
Detect impersonation, supplier fraud, payroll diversion attacks.
- **Leaders:** Abnormal, Proofpoint, Mimecast, Agari

### DMARC / Email Authentication
Enforce SPF, DKIM, DMARC to block domain spoofing.
- **Leaders:** Agari, Proofpoint, Mimecast, Valimail, dmarcian

### Collaboration Security
Extend email security to Teams, Slack, SharePoint file sharing.
- **Leaders:** Proofpoint, Mimecast, Abnormal, Tessian

---

## Key Questions to Ask at Booths
- How do you detect AI-generated phishing that passes grammar checks?
- QR code phishing (quishing) — detection capabilities?
- M365/Google Workspace: native controls vs. your platform — what's the gap?
- How do you handle internal email threats (lateral phishing post-compromise)?
- Time to detect + remediate a BEC attack — average metrics?

---

## CrispAI Watch List
- [ ] **Abnormal Security** — AI-native BEC detection without SEG
- [ ] **Proofpoint** N-6163 — AI-powered threat intel integration
- [ ] **Mimecast** N-5245 — resilience + continuity features

---

*→ Next: [Cluster 15 — OT / ICS / IoT Security](15-ot-ics-iot.md)*
