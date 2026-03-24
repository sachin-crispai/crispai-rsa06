<!-- Auto-generated 2026-03-24 15:51 via Gemini 2.5-flash + Google Search -->
<!-- Category: Application Security / DevSecOps | Booth: ? | RSA 2026 -->

# Semgrep

## RSA 2026
- **Booth number and hall**: Moscone South, Booth #1743
- **Any updated booth info from the conference floor**: Semgrep is launching the "next generation of AppSec" at RSA, showcasing their new Semgrep Multimodal offering. They are hosting an exclusive RSA launch party, a "Builders Lounge" at their office, and various interactive demo sessions with ecosystem partners. Attendees can also join their "Zero Trust Club" for VIP access to extra sessions and swag. Demos will include AI Detection.

## Company Profile
- **Employee count (approximate)**: Approximately 241-253 employees.
- **Founded year**: 2017.
- **HQ location**: San Francisco, CA, United States.
- **Funding stage or public status / ARR if known**: Private company, Series D funding. They raised $100 million in a Series D round in February 2025, led by Menlo Ventures. Total funding is reported to be between $193 million and $204 million across four rounds. ARR (Annual Recurring Revenue) is not publicly disclosed.
- **Website URL**: semgrep.dev.

## Technology Stack
- **Core technology and architecture**: Semgrep's core technology is a static analysis tool that combines abstract syntax trees (AST) and regular expressions (regex), often referred to as "Semantic Grep". It parses source code into an AST to understand its structure and semantics, enabling granular control and accurate vulnerability detection. The platform uses rules, written in YAML, to define pattern-matching logic and data flow analysis for scanning code. This allows it to detect security issues, style violations, bugs, and more across over 40 coding languages. The same Semgrep engine powers its various products, including first-party code scanning (SAST), third-party code scanning (SCA), and secrets detection.
- **AI/ML frameworks or capabilities used**: Semgrep leverages AI and ML capabilities, particularly Large Language Models (LLMs), to enhance its code security platform. Key features include:
    *   **Semgrep Assistant**: Launched in March 2024, it provides real-time remediation, auto-triage findings, and auto-fix code capabilities, built on OpenAI's GPT-4.
    *   **AI-powered detection**: Combines Semgrep's structured code scanning with LLM contextual reasoning to find logic flaws like IDORs (Insecure Direct Object References) and broken authorization, which traditional tools often miss. This approach aims to improve true positive rates and reduce false positives compared to LLM-only methods.
    *   **Semgrep Multimodal**: A new system announced at RSA 2026 that combines AI reasoning with rule-based analysis for detection, triage, and remediation. It's built on Semgrep Workflows and claims to find 8x more true positives while cutting noise by 50% compared to foundation models alone.
    *   **Autotriage with Assistant Memories**: Uses LLMs and retrieval augmented generation to assess the likelihood of a finding being a true or false positive, learning from an organization's triage decisions to improve accuracy over time.
- **Cloud infrastructure and key integrations**: Semgrep integrates into CI/CD pipelines and Source Code Managers (SCM) like GitHub and GitLab, running scans on pull requests and merge requests. Its tech stack includes Kubernetes for containerization and Cloudflare CDN for content delivery.
- **Any proprietary models or data sources**: Semgrep utilizes "Assistant Memories," a retrieval system that learns from each organization's triage decisions, becoming more accurate over time. They also have a vast registry of rules, including over 3000 community-contributed rules.

## Key Customers
- **Notable customer logos or named references**: Snowflake, Dropbox, Figma, Lyft, Slack, Plaid. Other recorded users include Policygenius, Thinkific Labs, and Copper United Kingdom.
- **Key industries served**: Technology (SaaS, software development), Banking and Financial Services, Insurance, Professional Services.
- **Any RSA 2026 customer stories or case studies mentioned**: Semgrep Secure 2026, a virtual event held in February 2026, featured customer success stories, including from Homebase. Copper United Kingdom deployed Semgrep in 2025, reporting approximately 50% faster remediation and improved compliance. Policygenius also implemented Semgrep in 2025 to shift security left.

## Product Brief
- **Main products and what problems they solve**:
    *   **Semgrep AppSec Platform**: A comprehensive software suite for implementing and tracking security programs, helping AppSec engineers detect, triage, and remediate findings across codebases.
    *   **Semgrep Code**: A static application security testing (SAST) tool that detects security vulnerabilities, style violations, and bugs in first-party code. It aims to reduce noise and provide fast feedback to developers.
    *   **Semgrep Supply Chain**: Focuses on finding and fixing reachable dependency vulnerabilities (SCA).
    *   **Semgrep Secrets**: Detects hardcoded secrets and sensitive data in code.
    *   **Semgrep Assistant**: An AI-powered system for auto-triage and auto-fix of security findings.
    *   **Semgrep Multimodal**: Combines AI reasoning with rule-based analysis for enhanced detection, triage, and remediation, particularly for complex logic issues.
    *   **Semgrep Workflows**: A framework for autonomous code security that allows teams to encode security policies into automated pipelines for detection, triage, remediation, and compliance.
- **How the core technology works**: Semgrep works by parsing source code into an Abstract Syntax Tree (AST), which allows it to understand the code's structure and semantics beyond simple text patterns. It then applies rules, written in YAML, that define specific code patterns, data flows, sources, sinks, and sanitizers to identify vulnerabilities and enforce coding standards. This semantic understanding helps minimize false positives and negatives. The platform integrates into developer workflows, providing feedback in IDEs, CLI, and CI/CD pipelines. With

## Sources
- https://vertexaisearch.cloud.google.com/grounding-api-redirect/AUZIYQEEUqzNCCbhOtMgO_6xEZ44sIFOFELEyLv_v6NSlhimkOGzu4XrXyzVop3IhbNhadvA4ouFOrrrvog5mBDcp1-i-zoF5vbUSM1-suIW92_Ydg0t6EyAD9rtmL8=
- https://vertexaisearch.cloud.google.com/grounding-api-redirect/AUZIYQFJIQy1uYjxjkXTDN5wJ8iAdph0AGxoOCwczdhBMH4bl5cdit9H4hl9KHnDpfXY8Tn-19cR0Dr-VU0YRFhbWuvvd8ZkTTgOfRImdqrxh_eW8GHHkPPesSH_hkSk9hTNtsq3h6_Stcjcz_Dp8h610tAvzr34i6-XiMO0X3EGB29H-kp6Vk0dYFRtTzOhdwW5uyBeX3p_3Al5MhvT7o8uqKvvNrW3PtaYSgktummr1f4RmzibGCrX_sntwccV02P9jcLhHs--gCrYuEc34Y-8XogdFBhY9UlIgrln212rMAoxI92OWfwerCGVnek=
- https://vertexaisearch.cloud.google.com/grounding-api-redirect/AUZIYQFvBtgRdlIkMJyRQSDH7KA99EutOOw-cjgXO4GvE7y7lN87LKx5eSYQlss-NyqEqKILpXh1RyG5PKqhyyHFtPbZ9KkwYdCjDJPlBNOKvWP0Y65aBCD_w7A81g__mWGURAJUO9hYe62AQk0u0SnCi8qHJ76Ip0t4ip799r-8VffCd5CrskvOGh6AJzoUc8K-n4QE97SDUMwnoq4y9_xZ3yAWbrcJ9AyR6yat5fxutAqCllDsRUa6DpMImottNhliQHupKYwiwiEW9zNP_YccbTTAoJgvjvVuYEut4bBCgC0JFlIMg4yH
- https://vertexaisearch.cloud.google.com/grounding-api-redirect/AUZIYQHBv4WgP9lxvDtKM1eGb-_0P50fu0_9HL53dTBps5J6lKomTaXtWxKQlV-YiTGUdnAOg2qHPN8xfoG-9YgbqQhMBubxS5zxRxq7purUFCfe3pSFh11QW0c1uc7lK10L_IbaDQphCHDG7h-HriSJsa1oUWe4ytWyMxtsE9zEj8LoAWc_p-UNAkynTfdn2jN2rHJSvOmvW1w3YXYTRY_lzrxOuCDAB23v8TP0w-0avmkkU-6grGF4
- https://vertexaisearch.cloud.google.com/grounding-api-redirect/AUZIYQGfkwA3-vLAr7-9viE4pkcKb5iVbDqSXIxSVedyv1akKHDkWCVUwMZIuzIPFSDQcraB44DwOYW0LTRN8Mr0sDJSY31p_4Bj0M6tcEbE0jrfe1HpL5ueZxvmomYfH1WciwxFOZ78DJ0=
- https://vertexaisearch.cloud.google.com/grounding-api-redirect/AUZIYQHmPf-_cmCD83l3zCfIJnWaXhTkCKh_J-rwULybk2qQfrqS779Qwl9Y2IYMa5e8Lxi3C3JOyiktlF4P_wwMLv6xlG07LoSbWtrnLVK9yk-bxgyhlbRU-tiW45uncqvSW3BYifCqwO07hJVGv50lLKJ3hPI7UWVHTRD_rVRSceFOXrZApAU-ptscyfzSVCRIWwzHigV0bIgIwVfV8Uk9cYL5juf07toDVxOmAE33qpm0vIckBnl99SUh
