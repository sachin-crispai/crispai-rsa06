# Cluster 01 — Identity & Access Management (IAM)

**Stack:** Who are you? Can you prove it? What are you allowed to do?

IAM is the backbone of every security architecture — managing digital identities, enforcing access policies, and governing privileged access across hybrid environments.

---

## Key Vendors

| Vendor | Focus | Booth | Notes |
|--------|-------|-------|-------|
| **Okta** | Workforce & customer identity platform | Gold Sponsor | CIAM, SSO, MFA, lifecycle mgmt |
| **CyberArk** | Privileged Access Management (PAM) | — | PAM leader; also expanding to identity security |
| **Ping Identity** | Enterprise identity platform | — | Federation, SSO, adaptive MFA |
| **Saviynt** | Cloud-native IGA | — | Identity governance & administration |
| **SailPoint** | Identity security platform | — | IGA for enterprise; AI-driven |
| **ForgeRock** | Digital identity (now part of Ping) | — | Consumer-scale identity |
| **IDEMIA** | Digital identity & biometrics | S-2452 | Physical + digital identity convergence |
| **1Password** | Enterprise password & secrets mgmt | Gold Sponsor | Teams, developers, passkeys |
| **Entrust** | Digital identity + certificates | Gold Sponsor | PKI, digital signing, identity verification |
| **GlobalSign by GMO** | PKI & digital certificates | N-5181 | TLS, code signing, IoT identity |
| **Teleport** | Infrastructure access (SSH, K8s, DB) | S-3111 | Zero-trust access for infra teams |

---

## Technology Landscape

### Workforce IAM
SSO, MFA, adaptive authentication, lifecycle management for employees and contractors.
- **Leaders:** Okta, Microsoft Entra (Microsoft booth N-5744), Ping Identity

### Customer IAM (CIAM)
Identity management at scale for consumers — registration, login, consent.
- **Leaders:** Okta CIAM, ForgeRock/Ping, Transmit Security

### Privileged Access Management (PAM)
Vaulting, session recording, just-in-time access for privileged accounts.
- **Leaders:** CyberArk, BeyondTrust, Delinea

### Identity Governance & Administration (IGA)
Access certification, role management, SOD enforcement.
- **Leaders:** SailPoint, Saviynt, Omada

### PKI & Certificate Management
TLS/SSL, code signing, IoT identity, certificate lifecycle automation.
- **Leaders:** Entrust, GlobalSign, DigiCert, Venafi (acquired by CyberArk)

### Infrastructure Access
Zero-trust SSH, Kubernetes, database, and RDP access without VPNs.
- **Leaders:** Teleport, HashiCorp Vault, StrongDM

---

## Key Questions to Ask at Booths
- How do you handle NHI (Non-Human Identity) — service accounts, API keys, tokens?
- What's your approach to identity in AI/LLM agent workflows?
- How do you integrate with existing AD/LDAP environments?
- Passkey/FIDO2 roadmap?

---

## CrispAI Watch List
- [ ] **SailPoint** — AI-driven IGA demo
- [ ] **CyberArk** — NHI (secrets + service accounts) expansion
- [ ] **Teleport** — infrastructure access for cloud-native teams
- [ ] **IDEMIA** — biometric + digital identity convergence

---

*→ Next: [Cluster 02 — Zero Trust Architecture](02-zero-trust.md)*
