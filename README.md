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
| `scripts/scout` | **Scout** — offline text agent, ask questions against the redbook |
| `scripts/hawk` | **Hawk** — vision agent, analyzes booth photos → structured vendor notes |
| `scripts/convert-photos.sh` | HEIC (iPhone) + NEF (Nikon) → JPEG converter |

## Operating Manual

### Python Environment Setup (Run Once Per Machine)

This project uses `uv` with a `.venv` at `GOLDEN/.venv`.

**Add to `~/.zshrc`** for auto-activation in any terminal (including IntelliJ):

```zsh
# alias python -> python3 (macOS has no bare 'python')
alias python=python3

# Auto-activate .venv when entering a project directory
_auto_venv() {
  local dir="$PWD"
  while [[ "$dir" != "/" ]]; do
    if [[ -f "$dir/.venv/bin/activate" ]]; then
      if [[ "$VIRTUAL_ENV" != "$dir/.venv" ]]; then
        source "$dir/.venv/bin/activate"
        echo "activated: $dir/.venv"
      fi
      return
    fi
    dir="$(dirname "$dir")"
  done
  if [[ -n "$VIRTUAL_ENV" ]]; then deactivate; echo "deactivated venv"; fi
}
chpwd_functions+=(_auto_venv)
_auto_venv   # run on shell init
```

Then reload: `source ~/.zshrc`

For scripts, always prefer `uv run python ...` over invoking `python` directly — it guarantees the correct interpreter regardless of shell state.

---

### Prerequisites — Run Once Before the Conference (on WiFi)

```bash
# Install Ollama + pull models (qwen2.5:32b + qwen2.5vl:7b, ~26GB total)
bash scripts/setup-ollama.sh
```

### Starting the LLM Engine

Start Ollama before using Scout or Hawk. Run this in a terminal and leave it open:

```bash
OLLAMA_FLASH_ATTENTION=1 OLLAMA_KV_CACHE_TYPE=q8_0 \
  /opt/homebrew/opt/ollama/bin/ollama serve
```

---

### Scout — Field Intelligence Agent (Text)

Scout answers questions about RSA vendors, booth locations, and clusters using the redbook. Works fully offline.

```bash
# Single question
./scripts/scout "Which booths should I visit for CNAPP?"
./scripts/scout "What should I ask at the Wiz booth?"
./scripts/scout "Compare CrowdStrike and SentinelOne"
./scripts/scout "Which vendors are in the North Hall?"

# Interactive chat mode (multi-turn)
./scripts/scout --chat

# Use a different model
./scripts/scout --model qwen2.5:7b "Quick question about IAM vendors"
```

---

### Hawk — Vision Agent (Photo Analysis)

Hawk analyzes booth photos and extracts vendor name, booth number, product category, and key messaging. Results are automatically logged to `docs/field-notes/photo-log.md`.

**Step 1 — Convert photos from iPhone/Nikon to JPEG:**

```bash
bash scripts/convert-photos.sh ~/Desktop/RSA-Day1/
# Output lands in ~/Desktop/RSA-Day1/jpeg/
```

**Step 2 — Analyze photos:**

```bash
# Single photo
./scripts/hawk ~/Desktop/RSA-Day1/jpeg/booth_001.jpg --day 1

# Entire directory (batch)
./scripts/hawk ~/Desktop/RSA-Day1/jpeg/ --day 1

# Day 2, Day 3, Day 4
./scripts/hawk ~/Desktop/RSA-Day2/jpeg/ --day 2
```

**Results appear in:** `docs/field-notes/photo-log.md`

---

### Daily Workflow On-Site

```bash
# Morning — start the engine
OLLAMA_FLASH_ATTENTION=1 OLLAMA_KV_CACHE_TYPE=q8_0 \
  /opt/homebrew/opt/ollama/bin/ollama serve

# On the floor — ask Scout for intel
./scripts/scout "What are the top booths for Zero Trust?"

# After the floor — process today's photos
bash scripts/convert-photos.sh ~/Desktop/RSA-DayN/
./scripts/hawk ~/Desktop/RSA-DayN/jpeg/ --day N
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
