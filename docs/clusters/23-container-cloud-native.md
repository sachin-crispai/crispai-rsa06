# Cluster 23 — Container & Cloud-Native Security

**Stack:** Secure Kubernetes, containers, serverless, and the CI/CD pipelines that deploy them.

Cloud-native security spans image scanning, runtime protection, Kubernetes security posture, and pipeline integrity — from code commit to running pod.

---

## Key Vendors

| Vendor | Focus | Booth | Notes |
|--------|-------|-------|-------|
| **Aqua Security** | Full lifecycle container + cloud-native security | — | Image scanning + runtime + CSPM |
| **Sysdig** | Runtime security + CNAPP (Falco-based) | — | Open-source Falco; strong K8s runtime |
| **Lacework** | Behavioral CNAPP + anomaly detection | — | Polygraph for container behavior |
| **Wiz** | Cloud-native vulnerability + posture | Gold Sponsor | Agentless; deep K8s integration |
| **Snyk** | Container image + IaC security | Gold Sponsor | Developer-first image scanning |
| **Chainguard** | Minimal, hardened container images | — | Zero CVE base images |
| **Anchore** | SBOM + container image policy | — | Enterprise container compliance |
| **StackRox (Red Hat)** | Kubernetes security platform | — | Part of Red Hat OpenShift security |
| **NeuVector (SUSE)** | Full-lifecycle K8s security | — | Network policy + runtime |
| **Prisma Cloud (Palo Alto)** | Broad CNAPP | — | Not exhibiting but widely deployed |

---

## Technology Landscape

### Container Image Scanning
Scan Docker/OCI images for CVEs, misconfigurations, and secrets before deployment.
- **Leaders:** Snyk, Aqua, Sysdig, Trivy (open-source), Anchore

### Kubernetes Security Posture (KSPM)
Assess K8s cluster configuration — RBAC, network policies, pod security standards.
- **Leaders:** Wiz, Aqua, Sysdig, StackRox, Checkov

### Runtime Security
Detect anomalous behavior in running containers — syscall monitoring, drift detection.
- **Leaders:** Sysdig (Falco), Aqua, NeuVector, Lacework

### Supply Chain Security (Containers)
SBOM generation, image signing, build pipeline integrity (Sigstore/cosign).
- **Leaders:** Chainguard, Sigstore, Snyk, JFrog Xray, Anchore

### Serverless Security
Protect AWS Lambda, Azure Functions, GCP Cloud Run from injection and over-privilege.
- **Leaders:** Aqua, Prisma Cloud, Lacework, Orca

---

## Key Questions to Ask at Booths
- Agent vs. agentless in K8s: eBPF-based agents — overhead on production clusters?
- How do you handle security for service mesh environments (Istio/Linkerd)?
- CI/CD integration: how do you gate deployments on security policy without killing velocity?
- Falco vs. proprietary runtime: what are the tradeoffs?
- Secrets in containers: how do you detect hardcoded secrets and API keys in images?

---

## CrispAI Watch List
- [ ] **Chainguard** — zero-CVE hardened images approach
- [ ] **Sysdig** — Falco-based open-source runtime + enterprise
- [ ] **Wiz** — cloud-native risk graph including containers

---

*→ Next: [Cluster 24 — Early Stage / Innovation Sandbox](24-early-stage.md)*
