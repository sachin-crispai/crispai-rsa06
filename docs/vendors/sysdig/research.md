<!-- Auto-generated 2026-03-24 15:47 via Gemini 2.5-flash + Google Search -->
<!-- Category: Cloud Security | Booth: ? | RSA 2026 -->

# Sysdig

## RSA Conference 2026 Field Intelligence Report: Sysdig

### RSA 2026
- **Booth number and hall:** Unknown. While Sysdig made an announcement at RSA Conference 2026 in San Francisco on March 23, 2026, specific booth numbers for their presence at the Moscone Center were not found in the available search results.
- **Any updated booth info from the conference floor:** Sysdig announced "runtime security for AI coding agents" at RSA Conference 2026 in San Francisco on March 23, 2026. They also had a "Cocktails & Cloud Talk" event with Cloudsmith on March 6, 2026, at the Amber India Restaurant SF Marriott Marquis, though this was prior to the main conference dates.

### Company Profile
- **Employee count (approximate):** Sysdig has approximately 700 total employees as of 2026. Other sources indicate around 643 employees as of February 2026 and 470 employees as of August 2025.
- **Founded year:** Sysdig was founded in 2013.
- **HQ location:** Sysdig is headquartered in San Francisco, CA, United States.
- **Funding stage or public status / ARR if known:** Sysdig is a privately held, private equity-backed company. They are a Series G company, having raised a total of $744 million over 9 rounds. Their latest funding round was a Series G for $350 million on December 15, 2021, valuing the company at $2.5 billion. Their estimated annual revenue is currently $283.6 million per year.
- **Website URL:** www.sysdig.com

### Technology Stack
- **Core technology and architecture:** Sysdig's core technology is built on open-source foundations, including Falco (for cloud-native runtime security) and open-source Sysdig (for deep system call-level introspection into containers). The Sysdig platform provides unified cloud security, monitoring, and compliance for cloud-native environments, with a focus on containers and Kubernetes. It uses a lightweight agent deployed on each host (Kubernetes nodes, VMs, bare metal, cloud environments like AWS, GCP, Azure) to collect runtime data, including system and application metrics, network activity, and system calls. This data is sent to a Sysdig backend for processing and stored in internal databases, accessible via RESTful HTTP JSON-based APIs.
- **AI/ML frameworks or capabilities used:** Sysdig leverages AI/ML capabilities extensively, particularly with "Sysdig Sage™," described as the industry's first agentic AI analyst for cloud security. Sysdig Sage uses a unique autonomous agent architecture with multiple specialized AI agents collaborating to transform cloud security data into actionable insights. It employs multi-step reasoning and multi-domain correlation to discover, prioritize, and remediate risks, and can optimize Falco detection rules. Sysdig also uses AI for risk prioritization, attack path analysis, and AI-powered remediation recommendations. They partner with Google Cloud, utilizing Google Vertex AI for generative AI features.
- **Cloud infrastructure and key integrations:** Sysdig supports integration with popular cloud platforms such as Kubernetes, AWS, GCP, Azure, and IBM Cloud. They integrate with container registries, CI/CD pipelines (GitHub Actions, GitLab CI, Jenkins, CircleCI, Azure DevOps), and SIEM systems.
- **Any proprietary models or data sources:** Sysdig Sage™ is a proprietary AI analyst built on an autonomous agent architecture. Their threat detection is fueled by deep runtime intelligence and Falco rules curated by the Sysdig Threat Research Team. They also integrate with Bedrock Security for data security findings.

### Key Customers
- **Notable customer logos or named references:** Neo4j (powers graph-based insights for organizations like NASA and major U.S. banks), BigCommerce (global e-commerce), Apree Health (healthcare IT provider). More than 60% of Fortune 500 companies use their technology.
- **Key industries served:** Cloud-native environments, heavily regulated industries (e.g., healthcare, finance), e-commerce, government.
- **Any RSA 2026 customer stories or case studies mentioned:** No specific new customer stories or case studies were mentioned for RSA 2026 in the provided search results. However, the Apree Health case study highlights their success in healthcare.

### Product Brief
- **Main products and what problems they solve:**
    *   **Sysdig Secure:** A Cloud-Native Application Protection Platform (CNAPP) that provides unified security for cloud, containers, and Kubernetes. It addresses real-time threat detection, vulnerability management, posture management (CSPM), identity & entitlement management (CIEM), and compliance. It helps organizations detect and respond to threats, vulnerabilities, and compliance issues in real-time, reducing alert noise and prioritizing real risks.
    *   **Sysdig Monitor:** Provides cloud and Kubernetes monitoring, offering full-stack visibility into infrastructure, services, and applications. It helps analyze performance, resource usage, and application behavior to find bottlenecks and solve problems.
    *   **Sysdig Sage™:** An AI-powered security assistant integrated into Sysdig Secure, designed to accelerate search, vulnerability management, threat investigation, and response by providing precise, contextual security insights.
- **How the core technology works:** Sysdig operates by deploying a lightweight agent on each host (physical servers, VMs, containers, Kubernetes nodes) in the environment. This agent collects deep runtime data, including system calls, network activity, and application metrics. This data is then processed by the Sysdig backend, which uses Falco (an open-source threat detection engine) and machine learning to detect suspicious activities, policy violations, and vulnerabilities in real-time. Sysdig provides a unified view of risks through its Cloud Attack Graph, correlating findings across vulnerabilities, misconfigurations, and active threats. It also offers forensic capabilities, allowing investigation even after ephemeral workloads are gone.
- **Pricing model (if known):** Sysdig offers flexible pricing. Sysdig Monitor has entry-level pricing starting at $20 a month per host, with a popular Pro Cloud package at $30 a month. Pricing for the Sysdig Platform (combined monitoring, security, and forensics) and Sysdig Secure varies based on customizable options and is often licensed based on the number of hosts in a customer's environment (per events processed for cloud logs or compute instances for CSPM). They offer free versions of Falco and open-source Sysdig.

### RSA 2026 Announcements
- **New product launches or demos at this conference:** Sysdig announced "runtime security for AI coding agents" at RSA Conference 2026 on March 23, 2026. This solution provides real-time visibility into AI agent behavior across cloud and development environments, detecting risky activities such as unauthorized access to sensitive files, attempts to bypass credential protections, and unsafe command-line arguments. This builds on Sysdig's existing AI Workload Security solution.
- **Partnerships announced:** No new partnerships were explicitly announced at RSA 2026 in the provided search results.
- **Key messages from their booth/keynote:** The key message revolves around securing AI-driven development and cloud environments in real-time. Sysdig emphasizes "open innovation, agentic AI, and the uncompromising truth of runtime" to help security and development teams prevent, detect, and respond to threats. Their focus is on enabling safe adoption of autonomous development tools and providing real-time visibility into AI agent behavior.

### CrispAI Relevance

#### LLM / AI Agents
- **How this vendor's technology applies to securing or enabling LLM pipelines, AI agents, MCP servers, or agentic workflows:** Sysdig is directly addressing the security of LLM pipelines and AI agents. Their new "runtime security for AI coding agents" provides real-time visibility and detection for autonomous development tools like Claude Code, Codex, and Gemini CLI. This helps organizations monitor agent behavior, identify risky activity (e.g., installation of new agents, access to sensitive files, risky command-line arguments, reverse shells, binary tampering), and protect sensitive data and code. Sysdig Sage™, their agentic AI analyst, is designed to simplify and

## Sources
- https://vertexaisearch.cloud.google.com/grounding-api-redirect/AUZIYQHni-4dYWjEhyjNWKfeKp3SEkiWjPwwQuitmQ_Pu_c6WD6c_jNErSwAlK1iOK9-HuIzH4DwBC9sAu2NroBce68XqCDZFhC8_cNJ0CBKMcpwBjGw25F0Gp5O9pAjkeDXwEo3iEmNLuvvLRKgk1Msb98JEVRw4wYtV6mCwFk0g2OqMzQLiKziDs95AThlwV3bEPE8prAePC1MWxBpe6mm_G4r3uUh24cxlFVahAy29A==
- https://vertexaisearch.cloud.google.com/grounding-api-redirect/AUZIYQG4lAyZi9LETzrBu5NAbr3reHPU0pMx2qTKYjA7sEcEE1-D7EsrYwH0rQoQJrALIk5q7rj2KKOa-1dMDGMyku773q80utuW8JbcFDRdI1XHs0u9p6Zxad_Rn0JHpp2vGgQT0gV9WODO40U192OCvLUkBi2uL-Abz4h3d6CCsoCOBqgez4nWPclGb-G5MOPew7uSQ87xwQ==
- https://vertexaisearch.cloud.google.com/grounding-api-redirect/AUZIYQFV-kbiqvtdgYL90NLrW7OrTQRrAmCVMkVwsgvKCR9x3spg6VNH0Zl07CAIwOttDsVslhhW1UL7KqYB0eG7VllOyIx1bCJ4J7AT5mzWJgT317XeMzSn-DYs6RgRdvBUXakEPlBHDdlAjRDSITOaqay2YouGXFzPuPdvpoPdApC9xbKG1d7DgE4f
- https://vertexaisearch.cloud.google.com/grounding-api-redirect/AUZIYQFw-2636xrlrHPAHevQKhKENU7sTr5GyUTAfdGKwyaDQ8ojgnL5QmGxXEe7Otfq0XvVbNi2SZRcj-kCvtTS6wx39SsY0ALm4C_WL6hK9Zgoaqy-bw37UeDWA1naYIhAclC2
- https://vertexaisearch.cloud.google.com/grounding-api-redirect/AUZIYQHfBlwIACI35NDDkxiqTS65PaS42Yw2CSbIFqNvcArZzr1A4rtMOaUUILxlF5GilgXG3kvphkS6HwB6zsBkX5ZcWFFK8J7wiW-a6lqGxrpFf-rb_Ep39NsGWWQdefjpU85Ay9OGHAUOchJt8AR3mcN6hUp5POVXfDfVsbsdgC_Ox7NrdvBJ_zBGj9QfOqdHQzDI70skzxoPhlt43dQ=
- https://vertexaisearch.cloud.google.com/grounding-api-redirect/AUZIYQHHpp8TZBMeVzkSmoqcXwrf0STHWM3t8a4w-YRBUVs6w19ce9RJZNEXyIn8TgsNSmdouVqxZQEZ9ABhPeiyaPsYbGJ7sOCgX--6k7vOYrjTwvE0w97cD4X__Gma4KV_1M0SEW3RlWMfYJSMz0Cbzw==
