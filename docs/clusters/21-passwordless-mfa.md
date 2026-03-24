# Cluster 21 — Passwordless Authentication / MFA

**Stack:** Eliminate passwords — the root cause of most credential-based attacks.

Passkeys, FIDO2, hardware tokens, and push MFA are replacing shared secrets. This cluster is seeing rapid enterprise adoption driven by phishing-resistant requirements.

---

## Key Vendors

| Vendor | Focus | Booth | Notes |
|--------|-------|-------|-------|
| **Duo Security (Cisco)** | MFA + Zero Trust access | Booth 6044 | Market-leading MFA; part of Cisco |
| **Yubico** | Hardware security keys (YubiKey) | — | FIDO2/WebAuthn phishing-resistant MFA |
| **Beyond Identity** | Passwordless + device trust | — | No passwords, no push; continuous auth |
| **1Password** | Password manager + passkeys | Gold Sponsor | Enterprise secrets + passkey management |
| **HYPR** | Passwordless MFA | — | True passwordless; strong in enterprise |
| **Nok Nok Labs** | FIDO authentication platform | — | FIDO Alliance founding member |
| **Okta FastPass** | Passwordless for Okta customers | Gold Sponsor | Integrated into Okta identity platform |
| **Microsoft Entra (Hello)** | Passwordless for Azure/M365 | N-5744 | Windows Hello, FIDO2, Authenticator app |
| **Entrust Identity** | Smart card + MFA | Gold Sponsor | PIV, PKI, phishing-resistant MFA |

---

## Technology Landscape

### Phishing-Resistant MFA
FIDO2/WebAuthn-based authentication that cannot be intercepted by phishing proxies.
- **Leaders:** Yubico, Beyond Identity, HYPR, Microsoft (FIDO2 key support), Okta

### Passkeys
Synchronized, device-bound FIDO2 credentials replacing passwords.
- **Leaders:** Apple Passkeys, Google Passkeys, Microsoft, 1Password (passkey storage)

### Hardware Security Keys
Physical FIDO2/U2F tokens — strongest phishing resistance, required for high-assurance.
- **Leaders:** Yubico YubiKey, Google Titan Key, Feitian

### Push-Based MFA
App-based approval (Duo Push, Okta Verify, Microsoft Authenticator) — convenient but MFA-fatigable.
- **Leaders:** Duo, Okta, Microsoft, RSA SecurID

### Continuous / Risk-Based Authentication
Evaluate device health, location, behavior continuously — step up auth on anomaly.
- **Leaders:** Beyond Identity, Okta, Cisco Duo

---

## Key Questions to Ask at Booths
- MFA fatigue attacks — how do you defend against number-matching bypass?
- Passkey adoption: what's the enterprise deployment story for 10,000+ users?
- Legacy app support: how do you extend passwordless to apps that don't support FIDO2?
- Device trust: how do you ensure only managed/healthy devices can authenticate?
- What's your recovery story when a user loses their hardware key?

---

## CrispAI Watch List
- [ ] **Yubico** — phishing-resistant MFA for high-value accounts
- [ ] **Beyond Identity** — device trust + continuous authentication model
- [ ] **1Password** — enterprise passkey management

---

*→ Next: [Cluster 22 — AI / ML Security](22-ai-ml-security.md)*
