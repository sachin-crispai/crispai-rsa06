<!-- Auto-generated 2026-03-24 15:46 via Gemini 2.5-flash + Google Search -->
<!-- Category: Identity & Access Management | Booth: S-3111 | RSA 2026 -->

# Teleport

## RSA 2026
- **Booth number and hall**: S-3111
- **Any updated booth info from the conference floor**: Information from the conference floor is not available via web search at this time.

## Company Profile
- **Employee count (approximate)**: Approximately 276 employees (as of February 28, 2026).
- **Founded year**: 2015.
- **HQ location**: Oakland, California, United States.
- **Funding stage or public status / ARR if known**: Privately held, Venture Capital-Backed. Teleport has raised a total of $169 million across four funding rounds, with its latest being a Series C round of $110 million in May 2022, valuing the company at $1.1 billion. ARR is not publicly disclosed.
- **Website URL**: www.goteleport.com

## Technology Stack
- **Core technology and architecture**: Teleport provides an Infrastructure Identity Platform that modernizes identity, access, and policy for infrastructure. Its core architecture is based on a "cluster" concept, comprising the Teleport Auth Service and Teleport Proxy Service. The Auth Service manages certificate authorities for signing host and client certificates, stores cluster configurations, and collects audit events and session recordings. The Proxy Service enables secure communication with the Auth Service and allows users to access infrastructure in private networks via an SSH server, eliminating the need for VPNs. Teleport agents proxy traffic from users (human or machine) to resources, verifying user certificates against the Auth Service's certificate authority. It uses certificate-based authentication with automatic expiration for all protocols, eliminating shared secrets like SSH keys or Kubernetes tokens.
- **AI/ML frameworks or capabilities used**: Teleport's technology focuses on securing AI infrastructure rather than directly using AI/ML frameworks within its core product for general operations. It has recently launched an "Agentic Identity Framework" designed to secure AI agents across enterprise infrastructure. This framework treats AI agents as first-class identities, uses cryptographic identity, ephemeral privileges, and access guardrails, and provides auditability and real-time enforcement for AI systems. It also incorporates a "governed MCP and LLM control plane" to unify identity governance across agents, tools, and data, including budgets, rate limits, and guardrails.
- **Cloud infrastructure and key integrations**: Teleport can be deployed as a cloud service, on-premises, or in hybrid modes. It integrates with major cloud providers like AWS, Azure, and Google Cloud Platform (GCP) for securing access to their consoles, APIs, and CLI tools. Key integrations include Kubernetes distributions (e.g., GKE, EKS), various databases (e.g., AWS Aurora, DynamoDB, PostgreSQL, MySQL), CI/CD tools, observability platforms (e.g., Datadog, Grafana, Splunk), and Identity Providers (IdPs) such as Okta, GitHub, Google Workspace, Microsoft Active Directory, and AWS IAM Identity Center.
- **Any proprietary models or data sources**: Teleport's core is built on an open-source foundation, allowing for transparency and customization. While its implementation of identity-aware access and certificate authorities is central to its offering, there's no explicit mention of proprietary AI/ML models or unique data sources beyond its own audit logs and cluster data.

## Key Customers
- **Notable customer logos or named references**: Specific customer logos are not explicitly named in the provided search results, but Teleport states it is "trusted by the world's most innovative companies."
- **Key industries served**: Teleport serves various industries that require secure infrastructure access, including those utilizing cloud-native applications, DevOps, and increasingly, AI infrastructure. It also has a specific focus on healthcare organizations for HIPAA compliance.
- **Any RSA 2026 customer stories or case studies mentioned**: No specific RSA 2026 customer stories or case studies were found in the search results.

## Product Brief
- **Main products and what problems they solve**: Teleport offers an Infrastructure Identity Platform that consolidates connectivity, authentication, authorization, and audit for infrastructure access. Its main products include:
    *   **Teleport Zero Trust Access**: Provides just-in-time, least-privileged access to applications, servers, databases, Kubernetes clusters, MCP servers, and other resources, replacing VPNs and shared credentials. It solves problems related to credential sprawl, overprivileged accounts, and slow engineering velocity.
    *   **Teleport Machine & Workload Identity**: Manages non-human identity and access control, securing system and data access between machines and workloads. This addresses the growing challenge of securing automated processes and AI agents.
    *   **Teleport Identity Governance**: Hardens and monitors identities for both human and non-human entities, improving infrastructure resiliency against identity-based attacks. It helps identify weak access patterns and enforce stringent policies.
    *   **Teleport Identity Security**: Exposes and eliminates hidden risks across infrastructure.
    *   **Teleport Connect**: A cloud infrastructure browser that provides a unified UI for accessing SSH servers, Kubernetes clusters, databases, and web services, eliminating the need for VPNs and static credentials.
- **How the core technology works**: Teleport operates as a unified access plane. Users and machines authenticate once to the Teleport cluster, which acts as a certificate authority, issuing short-lived, cryptographically signed certificates instead of long-lived passwords or keys. This enables zero-trust authentication, where every access request is verified explicitly based on identity and context. The Teleport Proxy Service routes encrypted traffic to resources, and agents deployed near target resources enforce access policies based on the user's or machine's roles encoded in their certificates. All activity is recorded for auditability.
- **Pricing model (if known)**: Teleport uses a usage-based pricing model, billed monthly. Billing metrics include Monthly Active Users (MAU), Machine/Workload Identities (MWI), and Teleport Protected Resources (TPR) (e.g., Kubernetes clusters, SSH servers, database instances). Pricing requires contacting Teleport for a custom quote. A free "Community Edition" is available for eligible small organizations (fewer than 100 employees and less than $10M revenue).

## RSA 2026 Announcements
- **New product launches or demos at this conference**: Teleport recently unveiled its **Agentic Identity Framework** in January/February 2026. This framework is designed to help enterprises securely deploy autonomous and semi-autonomous AI agents across cloud and on-premises environments by treating AI agents as trusted identities. It provides a roadmap for AI security, including cryptographic identity, ephemeral privileges, access guardrails, auditability, and real-time enforcement.
- **Partnerships announced**: No specific new partnerships were announced in the provided search results for RSA 2026.
- **Key messages from their booth/keynote**: Based on recent announcements, a key message would likely revolve around "securing AI agents and LLM pipelines" and establishing "identity as the foundation of trust for agentic systems." They would emphasize their Agentic Identity Framework as a solution

## Sources
- https://www.google.com/search?q=time+in+Municipiu+Cluj-Napoca,+RO
- https://vertexaisearch.cloud.google.com/grounding-api-redirect/AUZIYQGje5SCaSBC4Te5f1SsAdzP4Fn8UrUKVAfF_c7oOEJ-PXg2PnHcC8dxuCxn1qe2osTnI26qM7nR7Z01oaq__JVSb4BrjmR3LfwPC7rGLQlmbZCMd7ADfVibjZYBpjaIm76WazD2ZlIV03-tkSpoA2otkgeaCAyzhbAuZy3Yf9LDbJQkl4LIuoNz1NRz7nGAjvY=
- https://vertexaisearch.cloud.google.com/grounding-api-redirect/AUZIYQHfIMnvnp_fWtFvgY6GOGuppK-eHMtQFTmcWQqrJTgL9Ltqa54UmNPxyWyyaKRRiuk0SynRqLROT5nL5f5-Y2R3Z7pI3rccJDp_FdUrL3JVT0cQiLnSTNYXUxt0cLcmYQDZsgIaJGvR_dMiVg==
- https://vertexaisearch.cloud.google.com/grounding-api-redirect/AUZIYQH06tGfDM2RfNec1Jz79m6_LjFDsXTxxJmZv9I724h3XD0R8Gza0aRhAYHkGiVG330ir781kATZ1HY_7_Bx6F2s3IDaTCyV7Kv4OUKb3J3-BFLd1gigxYUjj0YyOo1zCjM=
- https://vertexaisearch.cloud.google.com/grounding-api-redirect/AUZIYQHdbgiJB0y133oQPRwOrODYHla2pw_IMcZbWjz2HbZyW4DH9Ql9NMNV4lkXo2ZXqfqaEZUaHK2kvE3OPbkTbiZciAGzXcm1NhvE4R6u5HJUxJKkBoKSmURgJZ6ODJ3KiLHFbw==
- https://vertexaisearch.cloud.google.com/grounding-api-redirect/AUZIYQF8hy5QlUUb1czVFIpFLt5Xh8yULAgMOtPGaqAzdNSOJoXCytwjmFNuM0CtJAT-so3mErNnc6acvSwYhz1t1UpmWk4uaFvpwEgPtgdQir4ZGYM9G6Id5yy8sm62wyEZhe0=
