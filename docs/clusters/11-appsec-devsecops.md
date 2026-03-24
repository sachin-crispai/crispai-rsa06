# Cluster 11 — Application Security / DevSecOps

**Stack:** Secure software from first commit to production — shift left without slowing down.

AppSec has moved from gated security reviews to embedded tooling in CI/CD pipelines. The focus is developer experience + security outcomes.

---

## Key Vendors

| Vendor | Focus | Booth | Notes |
|--------|-------|-------|-------|
| **Snyk** | Developer-first security | Gold Sponsor | OSS dependencies, code, containers, IaC |
| **Veracode** | SAST + DAST + SCA | — | Enterprise AppSec platform |
| **Checkmarx** | SAST + SCA + ASPM | — | Strong in large enterprise |
| **Semgrep** | Lightweight SAST + supply chain | — | Fast, customizable rules; free tier |
| **Apiiro** | Application security posture mgmt (ASPM) | S-3316 | Code-to-cloud risk graph |
| **Sonatype** | SCA + software supply chain | — | Nexus Lifecycle; OSS governance |
| **JFrog** | DevSecOps platform + Xray SCA | — | Binary security + SBOM |
| **Endor Labs** | Reachability-based SCA | — | Eliminate SCA noise via reachability |
| **Invicti (Netsparker)** | DAST — dynamic app scanning | — | Web app + API automated testing |
| **StackHawk** | API security testing in CI/CD | — | Developer-friendly DAST |

---

## Technology Landscape

### SAST (Static Application Security Testing)
Analyze source code for vulnerabilities without executing it.
- **Leaders:** Checkmarx, Veracode, Semgrep, Fortify (OpenText)

### SCA (Software Composition Analysis)
Find vulnerabilities in open-source dependencies and license risks.
- **Leaders:** Snyk, Sonatype, Black Duck (Synopsys), Endor Labs

### DAST (Dynamic Application Security Testing)
Test running applications for vulnerabilities from the outside.
- **Leaders:** Invicti, StackHawk, Burp Suite (PortSwigger), OWASP ZAP

### ASPM (Application Security Posture Management)
Aggregate findings from all AppSec tools, deduplicate, prioritize by business context.
- **Leaders:** Apiiro, Ox Security, ArmorCode, Backslash Security

### IaC Security
Scan Terraform, CloudFormation, Helm charts for misconfigurations before deployment.
- **Leaders:** Snyk IaC, Checkov (Bridgecrew/Prisma), KICS, Terrascan

### Software Supply Chain Security
SBOM generation, dependency provenance, build pipeline integrity.
- **Leaders:** Snyk, JFrog, Sonatype, Chainguard, Sigstore

---

## Key Questions to Ask at Booths
- How do you reduce false positives in SAST to maintain developer trust?
- SBOM generation — what formats (SPDX, CycloneDX) and how automated?
- How do you handle AI-generated code — does it introduce new vuln patterns?
- ASPM consolidation: can you replace 3-4 point tools with one platform?
- IDE plugin availability — VS Code, JetBrains, GitHub Copilot integration?

---

## CrispAI Watch List
- [ ] **Apiiro** S-3316 — ASPM risk graph demo
- [ ] **Endor Labs** — reachability analysis to kill SCA noise
- [ ] **Snyk** — AI code scanning for LLM-generated code

---

*→ Next: [Cluster 12 — API Security](12-api-security.md)*
