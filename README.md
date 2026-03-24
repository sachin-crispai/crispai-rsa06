# CrispAI — RSA Conference 2026 Redbook

**Prepared by:** CrispAI
**Event:** RSA Conference 2026
**Dates:** March 23–26, 2026
**Venue:** Moscone Center, 747 Howard Street, San Francisco, CA 94103

---

## What's in This Repo

| Path | Contents |
|------|----------|
| `docs/redbook/rsa_redbook.md` | Master field guide — schedule, floor map, quick reference |
| `docs/clusters/` | 24 vendor technology clusters with key players & booth numbers |
| `docs/field-notes/` | Per-day capture templates + photo log |
| `scripts/setup-ollama.sh` | One-command local LLM install (Ollama + models) |
| `scripts/crisp-rsa` | Offline CLI: ask questions against the redbook |
| `scripts/photo-ingest.py` | Batch photo → vendor notes via local vision LLM |
| `scripts/convert-photos.sh` | HEIC (iPhone) + NEF (Nikon) → JPEG converter |

## Quick Start — On-Site Setup

```bash
# 1. Install local LLM stack (do this on WiFi before the conference)
bash scripts/setup-ollama.sh

# 2. Convert photos to JPEG for LLM analysis
bash scripts/convert-photos.sh ~/Pictures/RSA2026/

# 3. Analyze a booth photo
python scripts/photo-ingest.py ~/Pictures/RSA2026/booth_crowdstrike.jpg

# 4. Ask the redbook offline
./scripts/crisp-rsa "What booths are in the North Hall?"
```

## 24 Vendor Clusters

| # | Cluster | Key Players |
|---|---------|-------------|
| 01 | Identity & Access Management | Okta, CyberArk, Ping, Saviynt |
| 02 | Zero Trust Architecture | Zscaler, Illumio, Appgate |
| 03 | Cloud Security (CNAPP/CSPM) | Wiz, Orca, Lacework, Prisma |
| 04 | Endpoint / EDR / XDR | CrowdStrike, SentinelOne, Carbon Black |
| 05 | SIEM & Log Management | Splunk, Elastic, Exabeam |
| 06 | SOAR & Automation | XSOAR, Swimlane, Torq, Tines |
| 07 | Network Security & NDR | Fortinet, Vectra, ExtraHop |
| 08 | SASE / SSE | Netskope, Cloudflare, Cato Networks |
| 09 | Threat Intelligence | Recorded Future, Mandiant, ThreatConnect |
| 10 | Vulnerability Management | Tenable, Rapid7, Qualys |
| 11 | AppSec / DevSecOps | Veracode, Checkmarx, Snyk, Semgrep |
| 12 | API Security | Salt Security, Noname, Traceable |
| 13 | Data Security & Privacy | Varonis, BigID, Securiti |
| 14 | Email & Messaging Security | Proofpoint, Mimecast, Abnormal |
| 15 | OT / ICS / IoT Security | Claroty, Dragos, Nozomi, Armis |
| 16 | Fraud & Financial Security | BioCatch, Feedzai, Sift, Socure |
| 17 | Risk / GRC / Compliance | ServiceNow, MetricStream, Archer |
| 18 | Managed Security (MSSP) | Optiv, Arctic Wolf, GuidePoint |
| 19 | Security Awareness & Training | KnowBe4, SANS, Proofpoint SA |
| 20 | Incident Response & Forensics | Mandiant, Kroll, Secureworks |
| 21 | Passwordless / MFA | Duo/Cisco, Yubico, Beyond Identity, 1Password |
| 22 | AI / ML Security | Darktrace, HiddenLayer, Protect AI |
| 23 | Container & Cloud-Native | Aqua, Sysdig, Lacework |
| 24 | Early Stage / Innovation Sandbox | RSAC Sandbox, ESE kiosks, RSAC Next Stage |

---

*CrispAI RSA Redbook v1.0 — March 2026*
