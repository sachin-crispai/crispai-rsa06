# Cluster 07 — Network Security & NDR

**Stack:** See everything on the wire — detect lateral movement, C2, and anomalous traffic.

Network Detection & Response (NDR) uses ML on full-packet capture and flow data to detect threats that bypass perimeter controls.

---

## Key Vendors

| Vendor | Focus | Booth | Notes |
|--------|-------|-------|-------|
| **Fortinet** | NGFW + Security Fabric | N-5762 | Platinum Sponsor; broadest network portfolio |
| **Vectra AI** | AI-driven NDR | Platinum Sponsor | Cognito platform; behavior-based detection |
| **ExtraHop** | Network detection & response | Platinum Sponsor | Reveal(x) — deep packet inspection |
| **Check Point** | NGFW + unified security | Platinum Sponsor | Quantum firewall + CloudGuard |
| **Cisco (SecureX)** | Network security + telemetry | Booth 6044 | Stealthwatch/Cisco XDR |
| **Akamai** | DDoS + WAF + network security | Gold Sponsor | Edge-based protection |
| **AT&T Business** | Managed network security | Gold Sponsor | USM Anywhere; managed NDR |
| **Arista Networks** | Network telemetry + security | — | CloudVision for network visibility |
| **Corelight** | Open NDR (Zeek-based) | — | Best-in-class network metadata |

---

## Technology Landscape

### NGFW (Next-Gen Firewall)
Deep packet inspection, application awareness, IPS/IDS built-in.
- **Leaders:** Fortinet FortiGate, Check Point Quantum, Palo Alto (not exhibiting), Cisco Firepower

### NDR (Network Detection & Response)
ML on flow/packet data to detect C2, lateral movement, data exfiltration.
- **Leaders:** Vectra AI, ExtraHop Reveal(x), Corelight, Cisco Stealthwatch

### DDoS Protection
Volumetric, protocol, and application-layer attack mitigation.
- **Leaders:** Akamai, Cloudflare, Imperva, Radware

### Network Visibility & Flow Analysis
NetFlow, IPFIX, and packet capture for forensics and detection.
- **Leaders:** Corelight, ExtraHop, Darktrace (network AI)

---

## Key Questions to Ask at Booths
- How do you handle encrypted traffic (TLS 1.3) without decryption?
- What's your east-west visibility story inside cloud VPCs?
- How do you integrate NDR alerts into SIEM/SOAR workflows?
- Cloud-native deployment: how does NDR work in AWS/Azure/GCP?

---

## CrispAI Watch List
- [ ] **Vectra AI** — lateral movement + identity threat detection
- [ ] **ExtraHop** — encrypted traffic analysis capabilities
- [ ] **Corelight** — open NDR for budget-conscious teams

---

*→ Next: [Cluster 08 — SASE / SSE](08-sase-sse.md)*
