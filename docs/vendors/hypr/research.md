<!-- Auto-generated 2026-03-24 15:57 via Gemini 2.5-flash + Google Search -->
<!-- Category: Passwordless Authentication / MFA | Booth: ? | RSA 2026 -->

# HYPR

## Field Intelligence Report: HYPR at RSA Conference 2026

## RSA 2026
- **Booth number and hall**: Unknown. Specific booth information for HYPR at RSA Conference 2026 was not found in public search results.
- **Any updated booth info from the conference floor**: As the conference is currently ongoing (March 23-26, 2026), real-time updates from the conference floor are not available through general web search.

## Company Profile
- **Employee count (approximate)**: Approximately 112 employees as of February 28, 2026.
- **Founded year**: 2014.
- **HQ location**: New York, NY, United States (1001 Avenue of the Americas, 10th Floor).
- **Funding stage or public status / ARR if known**: HYPR is a private company and is in its Series D funding stage. The company has raised a total of $131 million in funding over 10 rounds. Its latest funding round was a Later Stage VC for $30 million on June 5, 2024. HYPR's estimated annual revenue is $23.7 million.
- **Website URL**: www.hypr.com

## Technology Stack
- **Core technology and architecture**: HYPR's core technology is a passwordless authentication and identity assurance platform built on FIDO standards and public-key cryptography. Its architecture is decentralized, eliminating the need for a centralized credential store. The private cryptographic key is stored securely on the user's device (e.g., in a Trusted Execution Environment or secure enclave), while the corresponding public key is stored on the HYPR True Passwordless Server. This approach transforms a smartphone into a FIDO2 certified token. For workstations, HYPR uses certificate-based authentication.
- **AI/ML frameworks or capabilities used**: HYPR Affirm, their automated identity verification product, leverages AI-powered chat, video, document verification, liveness detection, and facial recognition. HYPR's 2026 report also highlights "AI-driven identity threats" and "rising deepfakes," indicating their focus on AI's impact on identity security.
- **Cloud infrastructure and key integrations**: HYPR integrates with existing identity infrastructure and supports various identity providers (IdPs) and cloud applications. Key integrations include Microsoft Entra ID (Azure AD), Okta, Ping Identity, ForgeRock, Google Workspace, Symantec SiteMinder, and OneLogin. They also integrate with FIDO hardware authenticators like YubiKey, IDEMIA, HID, and Feitian. For workforce management, HYPR integrates with Applicant Tracking Systems (ATS) and Human Capital Management (HCM) platforms such as Workday and Greenhouse. Other integrations include SIEM systems and CrowdStrike for enhanced security posture. HYPR's True Passwordless MFA is available on AWS Marketplace, suggesting cloud infrastructure compatibility.
- **Any proprietary models or data sources**: The decentralized storage of private keys on individual user devices is a core proprietary architectural element, ensuring credentials never leave the user's device.

## Key Customers
- **Notable customer logos or named references**: Mastercard, Samsung, Aetna/CVS Health, Aon, First Citrus Bank, Thomson Reuters, T-Mobile, Norwegian Airlines, Rakuten, Takeda Pharmaceuticals, Fiserv, City National Bank. They also serve a Fortune 500 Manufacturer, a Top 10 Healthcare Corporation, a Top 5 US Financial Institution, and various insurance companies.
- **Key industries served**: Financial Services, Critical Infrastructure, Energy, Retail & Hospitality, Healthcare and Biotech, and Manufacturing.
- **Any RSA 2026 customer stories or case studies mentioned**: No specific customer stories or case studies for RSA 2026 were found. However, HYPR has a range of customer success stories available, including a U.S. healthcare giant that slashed account takeover (ATO) fraud and a global fintech firm that consolidated MFA tools.

## Product Brief
- **Main products and what problems they solve**:
    *   **HYPR Identity Assurance Platform**: This comprehensive platform secures the entire identity lifecycle for both workforce and customer identities. It combines passwordless authentication with adaptive risk mitigation and automated identity verification, aiming to create trust in the identity lifecycle.
    *   **HYPR Authenticate**: Provides phishing-resistant, passwordless Multi-Factor Authentication (MFA) utilizing FIDO passkeys. It secures workforce and customer access from desktop to cloud by eradicating shared secrets and credential-based attacks, thereby solving problems like password-related breaches, phishing, and credential stuffing.
    *   **HYPR Adapt**: Offers Adaptive Risk Mitigation, employing a dynamic risk engine to continuously assess threats and adjust security controls in real-time. This helps mitigate third-party attacks and provides customizable identity risk orchestration.
    *   **HYPR Affirm**: Delivers Automated Identity Verification solutions for confirming identities through AI-powered chat, video, document verification, liveness detection, and facial recognition. It addresses needs for day-one onboarding, account recovery, annual identity audits, and dynamic workflows for risk-based events.
    *   **HYPR Enterprise Passkeys**: These are device-bound passkeys with enhanced features and controls specifically designed for organizational and enterprise use cases.
- **How the core technology works**: HYPR's True Passwordless architecture replaces shared secrets (passwords, PINs, SMS codes, OTPs) with public-key cryptography. During registration, a pair of cryptographic keys is generated: the private key is stored on the user's mobile device at the hardware level within a secure, isolated Trusted Execution Environment (TEE) or secure enclave, and the public key is stored on the HYPR True Passwordless Server. Biometric sensors (e.g., Apple Touch ID, Face ID, Android/Windows counterparts) are used to unlock these credentials for verification via secure cryptographic protocols. The HYPR Mobile App effectively functions as a FIDO2 Certified token. For workstation logins, HYPR uses certificate-based authentication, where a virtual smartcard is created upon device pairing to perform the authentication.
- **Pricing model (if known)**: HYPR employs a custom, enterprise-grade pricing model. The investment is determined by factors such as user count, specific passwordless MFA deployment use cases (e.g., desktop, SSO, apps), and required features/integrations. Publicly available pricing indicates editions like "Identity Assurance Access" at $3 per month per user, "Identity Assurance Plus" at $6 per month per user, and "Identity Assurance Advanced" at $9 per month per user. Pricing for Customer Identity and Access Management (CIAM) deployments and HYPR Affirm (identity verification) is not publicly disclosed and is usage-based, requiring direct consultation with sales. A free pilot program is available for up to 50 users.

## RSA 2026 Announcements
- **New product launches or demos at this conference**: No specific new product launches or demos for RSA Conference 2026 have been announced or found in public search results.
- **Partnerships announced**: No specific new partnerships for RSA Conference 2026 have been announced or found in public search results.
- **Key messages from their booth/keynote**: No specific key messages from their RSA 2026 booth or keynote have been found. However, HYPR's 2026 State of Passwordless Identity Assurance report mentions "AI-driven identity threats" and "rising deepfakes," indicating a focus on evolving identity security challenges.

## CrispAI Relevance

### LLM / AI Agents
HYPR's passwordless authentication technology can significantly enhance the security of LLM pipelines, AI agents, and agentic workflows by ensuring that access to these critical systems and the data they process is phishing-resistant and free from shared secrets.
- **Securing or enabling LLM pipelines, AI agents, MCP servers, or agentic workflows**: By implementing HYPR's FIDO-based passwordless MFA, organizations can secure access for human operators, developers, and potentially even other authenticated systems to LLM development environments, AI agent control panels, and data repositories. This prevents unauthorized access through compromised credentials, which is a major attack vector. The decentralized nature of HYPR's authentication means that even if an AI system itself were compromised, the underlying user credentials would remain secure on individual devices.
- **Specific LLM security features, prompt injection protection, model integrity tools**: While HYPR's core offering is authentication, its robust identity verification capabilities (HYPR Affirm) could be crucial for verifying the identity of users interacting with or deploying LLMs, especially in sensitive contexts. This could indirectly contribute to model integrity by ensuring only authorized and verified individuals can make changes or provide prompts. The mention of "AI-driven identity threats" and "deepfakes" in their 2026 report suggests HYPR is actively considering how AI impacts identity fraud, which is relevant for securing AI systems from malicious input or impersonation.

### Robotics Security
HYPR's technology is relevant to robotics security primarily through securing access to robotic systems and their operational environments.
- **Relevance to securing embedded AI, robotic systems, edge AI, ROS security, autonomous vehicles**: Passwordless authentication can be applied to secure access for human operators, maintenance personnel, or even other authenticated machines to robotic control interfaces, embedded AI systems, and edge AI devices. This is critical for preventing unauthorized control or data exfiltration from sensitive robotic platforms, including those in autonomous vehicles or industrial settings.
- **OT/ICS capabilities applicable to robotic manufacturing or field robots**: While HYPR does not explicitly detail OT/ICS capabilities, its focus on securing critical infrastructure and manufacturing clients implies an understanding of the stringent security requirements in these environments. Passwordless MFA can secure access to the IT systems that manage OT/ICS, thereby indirectly protecting robotic manufacturing lines or field robots from credential-based attacks.

### Medical / Healthcare AI
HYPR's identity assurance platform is highly relevant to the medical and healthcare AI sector

## Sources
- https://vertexaisearch.cloud.google.com/grounding-api-redirect/AUZIYQGsudfCH3U_5iMIZU58T6lismYKWDlz0YkTmOoomQFiwBtm-UeGIixuBmWDLc_Ij3M1vhZQFUBK3_9UZkCB9WqILTbCggDe3xMPQ_fmg2YQkbuWSoNxYQifkAvHvl1LMJhY
- https://vertexaisearch.cloud.google.com/grounding-api-redirect/AUZIYQEfZ1tx6DwehV3INLsPmkcptC5vpaAkdjBOVTI2go211DyLUuE19rGU0dnAO2GmopUi3wb3XvcibSePPf3HFtX0-XXm0SbRuPw8IB7IJjKnF91KQqrlWN27rNORMoo_MjGMRy7ilZNVeQ==
- https://vertexaisearch.cloud.google.com/grounding-api-redirect/AUZIYQFmRVmDxmb5zz4hMznC6tJXhHwF5Mm3J9g5t1xhQ8BjGOElyWaNoDDJYj8Z8WLUF_RSgrnW5LlyzyW0plyE69GU4Ehbnp2ob4zPNzUniShvUek30i0Ttes5SPyX0slC6rztf0wnCyDE31cBaraRTS2gEG4sXn-8
- https://vertexaisearch.cloud.google.com/grounding-api-redirect/AUZIYQFDSbxw8LCQj-z3tWQxwGIgsCx7h6ICs_nKEIUWhwwDgGgnt4_kh_FzRjHU7x-ufCeUbEDWP5w_tyy4scfxwH1GQ7G0TDwla_AOQ-o_lUHKLoeqJfKFdhWNPPOEug==
- https://vertexaisearch.cloud.google.com/grounding-api-redirect/AUZIYQHIRMB8jkM7j3iaqhoL6l0ZWCp1c95szhajvURrJztcF6gwumR2kUPds7cQDrLcQ2DrqhoiM5b6Ks6IlRlyyn55yIu8aPmehij5Ki2_4SL4IjSiEh7812F0OHrP9ss=
- https://vertexaisearch.cloud.google.com/grounding-api-redirect/AUZIYQFOFFUJ9fJ8XtZ3O3j8OSo4w667RZRKkPwTcfTNozNuaSjY6vYNiVdkD1FfiDgtLNIY-zxVRjA7ocnFNsgpLNTq9a8QctJyx5p8InBXYPkKUfvnlA==
