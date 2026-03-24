# RSA 2026 Vendor Research Index

Auto-populated via `./scripts/vendor-research`. Each vendor has a dedicated directory
with a `research.md` covering: booth location, company profile, tech stack, customers,
product brief, RSA 2026 announcements, and CrispAI relevance (LLM / Robotics / Medical).

## Usage
```bash
# Research a single vendor
./scripts/vendor-research --vendor "CrowdStrike"

# Research multiple vendors
./scripts/vendor-research --vendor "HiddenLayer,Protect AI,Lakera"

# Research all AI-priority vendors (LLM/Robotics/Medical focus)
./scripts/vendor-research --priority

# Research all 221 vendors
./scripts/vendor-research --all
```

## Visit Status Legend
| Symbol | Meaning |
|--------|---------|
| ⬜ | Not yet visited |
| ✅ | Visited |
| 🔁 | Follow-up required |
| ⭐ | High priority for CrispAI |

---

## AI / LLM Security
| Vendor | Booth | Status | AI Relevance |
|--------|-------|--------|--------------|
| [HiddenLayer](./hiddenlayer/research.md) | ? | ⬜ | AI/ML model protection |
| [Protect AI](./protect-ai/research.md) | ? | ⬜ | AI security posture |
| [Lakera](./lakera/research.md) | ? | ⬜ | LLM guardrails |
| [Operant AI](./operant-ai/research.md) | ? | ⬜ | Agent ScopeGuard |
| [CalypsoAI](./calypsoai/research.md) | ? | ⬜ | AI model security |
| [Unbound AI](./unbound-ai/research.md) | ESE-09 | ⬜ | LLM security startup |
| [Darktrace](./darktrace/research.md) | ? | ⬜ | AI-native detection |
| [Vectra AI](./vectra-ai/research.md) | Platinum | ⬜ | AI-powered NDR |

## Agentic AI / Platform
| Vendor | Booth | Status | AI Relevance |
|--------|-------|--------|--------------|
| [CrowdStrike](./crowdstrike/research.md) | N-5845 | ⬜ | Charlotte AI, agentic |
| [SentinelOne](./sentinelone/research.md) | Platinum | ⬜ | Purple AI |
| [Wiz](./wiz/research.md) | Gold | ⬜ | AI App Protection Platform |
| [Arctic Wolf](./arctic-wolf/research.md) | ? | ⬜ | Agentic SOC |
| [Apiiro](./apiiro/research.md) | S-3316 | ⬜ | AI coding security agent |
| [Snyk](./snyk/research.md) | Gold | ⬜ | Snyk Agent Security |
| [Palo Alto Networks](./palo-alto-networks/research.md) | Diamond | ⬜ | AI-powered XSIAM |
| [Microsoft Security](./microsoft-security/research.md) | N-5744 | ⬜ | Copilot for Security |
| [Google / Mandiant](./google-mandiant/research.md) | Platinum | ⬜ | Gemini for Security |
| [Cisco Security](./cisco-security/research.md) | Booth 6044 | ⬜ | Zero Trust for AI |
| [Rubrik](./rubrik/research.md) | Platinum | ⬜ | AI governance, semantic |

## Medical / Robotics / OT Security
| Vendor | Booth | Status | AI Relevance |
|--------|-------|--------|--------------|
| [Armis](./armis/research.md) | Platinum | ⬜ | IoT/medical device AI |
| [Claroty](./claroty/research.md) | ? | ⬜ | Medical/OT security |
| [Cylera](./cylera/research.md) | ? | ⬜ | Medical IoT security |
| [Dragos](./dragos/research.md) | ? | ⬜ | OT / robotics ICS |
| [Nozomi Networks](./nozomi-networks/research.md) | ? | ⬜ | OT/IoT AI analytics |

## API / Agent Security
| Vendor | Booth | Status | AI Relevance |
|--------|-------|--------|--------------|
| [Traceable AI](./traceable-ai/research.md) | ? | ⬜ | AI-powered API security |
| [Cequence Security](./cequence-security/research.md) | ? | ⬜ | API bot/agent defense |
| [Acalvio](./acalvio/research.md) | ? | ⬜ | Cyber deception AI |

---

_Last updated: 2026-03-24 · Linked issue: [#6](https://github.com/sachin-crispai/crispai-rsa06/issues/6)_
