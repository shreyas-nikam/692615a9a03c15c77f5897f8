id: 692615a9a03c15c77f5897f8_user_guide
summary: Lab 1: Principles of AI Risk and Assurance User Guide
feedback link: https://docs.google.com/forms/d/e/1FAIpQLSfWkOK-in_bMMoHSZfcIvAeO58PAH9wrDqcxnJABHaxiDqhSA/viewform?usp=sf_link
environments: Web
status: Published
# Navigating AI Risk: SR 11-7 and NIST AI RMF in a Modern Landscape

## 1. Understanding the Imperative: AI Assurance for a New Era
Duration: 00:07:00

Welcome to this comprehensive guide on AI assurance! In today's rapidly evolving technological landscape, Artificial Intelligence (AI) is transforming industries and daily life. While AI offers immense opportunities, it also introduces novel and complex risks that traditional risk management frameworks may not fully address.

This codelab is designed for risk managers and anyone interested in understanding how to effectively govern and assure AI systems. We will clarify the relationship and complementary nature of **SR 11-7** (Guidance on Model Risk Management) and the **NIST AI Risk Management Framework (AI RMF 1.0)**. Our goal is to provide you with a deeper understanding of the evolution from traditional model risk management to comprehensive AI assurance, highlighting key differences, shared objectives, and practical integration points for robust AI governance, especially in the context of advanced AI systems like Large Language Models (LLMs) and autonomous agents.

By the end of this codelab, you will be able to:
*   Understand AI risk and assurance in the context of large-scale AI systems.
*   Review and comprehend Model Risk Management (MRM) principles as outlined in SR 11-7.
*   Categorize AI risks systematically using a multidimensional taxonomy.
*   Explore and understand the NIST AI RMF 1.0 and its core objectives and trustworthiness attributes.
*   Apply these principles to generative and agentic AI systems.
*   Develop and understand essential AI assurance artifacts (Model Cards, Data Cards, Risk Registers).
*   Trace the evolution of assurance practices from traditional MRM to comprehensive AI assurance.

The application you are interacting with is designed to guide you through these concepts step by step. You can navigate through the different sections using the sidebar on the left. Let's begin by understanding the unique challenges of AI risk management.

## 2. The Imperative of AI Risk Management
Duration: 00:10:00

The rapid adoption of AI across industries brings unprecedented opportunities but also introduces novel and complex risks. Traditional risk management frameworks, while foundational, often fall short in addressing the unique challenges posed by sophisticated AI systems. This section, accessible via **"The Imperative of AI Risk Management"** in the sidebar, explores the critical need for specialized AI risk management and introduces a comprehensive taxonomy to categorize these emergent risks.

### Emergent AI Risks
As AI systems become more sophisticated and integrated into critical applications, new categories of risks emerge. These include:

*   **Bias Amplification:** AI models can learn and even amplify biases present in training data, leading to unfair or discriminatory outcomes.
*   **Lack of Explainability (Opacity):** The "black box" nature of complex AI models makes it difficult to understand their decision-making process, hindering auditing and accountability.
*   **Adversarial Attacks:** Malicious actors can manipulate AI inputs to force erroneous or harmful outputs, compromising system integrity.
*   **Systemic Risks:** Widespread deployment of similar AI models can lead to correlated failures with broad societal and economic impacts.
*   **Loss of Human Oversight:** Over-reliance on autonomous AI systems can diminish human judgment and control, leading to unintended consequences.

### Five Key Dimensions of AI Risk
To understand AI risks systematically, the application categorizes them across five key dimensions:

1.  **Data Risks:** Pertain to the quality, provenance, privacy, and inherent bias within the data used to train AI models.
2.  **Model Risks:** Relate to the AI algorithm itself, including issues like bias, accuracy, reliability, robustness, and interpretability.
3.  **System Risks:** Involve the broader technical ecosystem in which AI operates, such as integration challenges, architectural vulnerabilities, and supply chain dependencies.
4.  **Human Risks:** Focus on how humans interact with and manage AI, including misuse, over-reliance, loss of oversight, and misinterpretation of AI outputs.
5.  **Organizational Risks:** Encompass the governance structures, policies, culture, and accountability mechanisms within an organization that manages AI.

The application provides a "Deep Dive" into each of these categories, explaining common issues like data quality, algorithmic bias, integration risks, automation bias, and the absence of clear AI policies.

### Interconnected Risks and Emerging Threats
It's important to recognize that these risk dimensions are interconnected. For instance, data bias can lead to model bias, which then contributes to human misuse, ultimately posing an organizational risk. The application also highlights emerging threats from large language models (LLMs) and agentic AI, such as hallucinations, intellectual property infringement, and unintended autonomous actions.

### Conceptual Metrics for AI Risk
While this codelab doesn't delve into the mathematical details of the metrics, the application mentions conceptual metrics used to quantify aspects of AI risk, particularly fairness and performance. For example:
*   **Demographic Parity:** Ensures that a positive outcome from the AI ($\hat{Y}=1$) is equally likely across different demographic groups ($P(\hat{Y}=1 | A=a) = P(\hat{Y}=1 | A=b)$).
*   **Equalized Odds:** A more refined fairness metric that requires equal true positive rates and false positive rates across groups ($P(\hat{Y}=1 | Y=y, A=a) = P(\hat{Y}=1 | Y=y, A=b)$).
*   **Accuracy:** A common performance metric, calculated as $$Accuracy = \frac{\text{True Positives} + \text{True Negatives}}{\text{Total Samples}}$$.
*   **F1-Score:** Another performance metric that balances precision and recall, calculated as $$F1-Score = 2 \times \frac{Precision \times Recall}{Precision + Recall}$$.

These metrics help in systematically evaluating and quantifying AI risks.

## 3. Foundations of Model Risk Management (SR 11-7)
Duration: 00:08:00

To build a robust AI assurance framework, it's crucial to understand the foundational principles of traditional model risk management. Navigate to **"Foundations of SR 11-7"** in the sidebar to explore this.

**SR 11-7**, officially "Guidance on Model Risk Management," was issued by the Federal Reserve and the Office of the Comptroller of the Currency (OCC) in 2011. While primarily aimed at banking organizations to manage risks associated with financial models, its principles provide a foundational understanding for managing risks in any sophisticated analytical system, including AI.

### Core Principles and Pillars of SR 11-7
SR 11-7 outlines three core pillars for effective model risk management:
1.  **Governance:** Strong oversight by senior management and the board, clear policies, and defined roles and responsibilities.
2.  **Validation:** Independent and robust validation of models to assess their conceptual soundness, implementation, and ongoing performance.
3.  **Model Development and Use:** Sound practices for model design, implementation, and use, coupled with comprehensive documentation.

The application displays a table that further breaks down these pillars into specific operational areas:

| SR 11-7 Pillar                   | Description                                                                                             |
| :- | : |
| Model Development & Implementation | Robust processes for model design, data quality, and implementation controls.                         |
| Model Validation                 | Independent assessment of model logic, data, and performance; includes outcomes analysis and backtesting. |
| Model Governance                 | Clear roles, responsibilities, policies, and senior management oversight for model risk management.       |
| Ongoing Monitoring               | Continuous monitoring of model performance, data characteristics, and model limitations.                |

### Broadening Model Definition & Risk Tiering
While SR 11-7 focused on quantitative models, the spirit of its guidance can be extended to AI. However, the definition of "model" and the approach to risk tiering need to evolve. The application provides a comparative view between traditional SR 11-7 and modern frameworks like NIST AI RMF:

| Aspect            | Traditional SR 11-7 View                          | Modern Frameworks (e.g., NIST AI RMF)                                |
| :- | : | :- |
| Model Definition  | Focus on quantitative methods for financial decisions. | Includes AI/ML systems, their outputs, and even decision-making processes. |
| Model Tiering     | Categorization by materiality and complexity.     | Categorization by risk level (impact, complexity, data sensitivity, interpretability). |
| Risk Management   | General model risk management.                    | Tailored risk management strategies based on tier.                   |
| Validation        | Standard validation practices.                    | Enhanced validation (e.g., third-party, continuous) and more documentation for higher-tier AI models. |

<aside class="positive">
<b>Key Takeaway:</b> While SR 11-7 provides a robust foundation, AI systems introduce complexities that necessitate expanding the definition of "model" and evolving risk management approaches to incorporate broader impacts and new forms of risk.
</aside>

## 4. Introduction to NIST AI Risk Management Framework (AI RMF 1.0)
Duration: 00:08:00

Now, let's explore a framework specifically designed for AI. Navigate to **"Introduction to NIST AI RMF"** in the sidebar.

The National Institute of Standards and Technology (NIST) AI Risk Management Framework (AI RMF 1.0), released in January 2023, provides a comprehensive, voluntary framework for managing risks associated with the design, development, deployment, and use of AI systems. It is designed to be sector-agnostic and applicable across the entire AI lifecycle.

### Core Objectives of AI RMF: The Four Functions
The NIST AI RMF is built around four core, continuous, and iterative functions designed to foster trustworthy AI systems:

*   **Govern:** This function is about establishing a culture of AI risk management, defining roles and responsibilities, and ensuring accountability within an organization.
*   **Map:** This involves identifying and characterizing AI risks, potential impacts, and vulnerabilities throughout the AI lifecycle, from data collection to deployment.
*   **Measure:** This function focuses on evaluating, analyzing, and tracking AI risks and the effectiveness of mitigation strategies through appropriate metrics and testing.
*   **Manage:** This entails prioritizing, implementing, and communicating AI risk mitigation strategies based on the risks identified and measured.

### Trustworthy AI Attributes
Central to the NIST AI RMF is the concept of "Trustworthy AI," defined by a set of characteristics or attributes that promote responsible and beneficial AI systems. The application presents these attributes in detail:

*   **Validity, Reliability, Safety:**
    | Attribute   | Description                                                                                                   |
    | :- | : |
    | Validity    | Ensuring the AI system accurately performs its intended function and produces correct outputs.                  |
    | Reliability | Guarantees consistent and stable performance of the AI system over time and across operational conditions.      |
    | Safety      | Minimizing the potential for the AI system to cause harm to individuals, society, or the environment.          |
*   **Security, Transparency, Fairness:**
    | Attribute    | Description                                                                                                   |
    | :-- | : |
    | Security     | Protecting AI systems from adversarial attacks and ensuring data integrity and access governance.             |
    | Transparency | Understanding how AI systems arrive at outputs through interpretability methods and counterfactuals.          |
    | Fairness     | Identifying and mitigating biases in AI to ensure equitable and just outcomes for all.                         |
*   **Accountability & Privacy-Preserving:**
    | Attribute           | Description                                                                                                   |
    | : | : |
    | Accountability      | Establishing clear roles, policies, and governance for AI risk oversight to ensure responsibility for AI outcomes. |
    | Privacy-Preserving | Implementing strategies to address data sensitivity and integrating privacy by design throughout the AI lifecycle. |

<aside class="positive">
<b>Key Takeaway:</b> These attributes provide a holistic view of what makes an AI system trustworthy, extending beyond mere performance metrics to encompass ethical, societal, and operational considerations. The AI RMF encourages organizations to integrate these attributes throughout their AI risk management processes.
</aside>

## 5. Framework Comparison & Interactive Mapping
Duration: 00:12:00

Now that we've explored both SR 11-7 and NIST AI RMF, let's understand how they relate and complement each other. Navigate to **"Framework Comparison & Interactive Mapping"** in the sidebar.

While SR 11-7 and NIST AI RMF originate from different regulatory landscapes and address distinct scopes, they are not mutually exclusive. Instead, they offer complementary perspectives that, when integrated, can form a more robust approach to AI risk management.

### Distinct Scopes & Shared Objectives
*   **SR 11-7:** Primarily focused on financial models within the banking sector, emphasizing quantitative model risk, and is mandatory for regulated financial institutions. Its key objective is to minimize adverse outcomes from model use.
*   **NIST AI RMF:** Broadly applicable to all types of AI systems across various industries, with a strong emphasis on trustworthy AI attributes and societal impacts. It is voluntary but rapidly becoming industry best practice, aiming to foster the development and use of trustworthy AI.

Despite their differences, both frameworks share fundamental objectives: **Risk Mitigation**, **Governance & Oversight**, and **Continuous Monitoring**.

### Integration Benefits
Integrating principles from both frameworks can provide a comprehensive strategy:
*   SR 11-7's rigor in financial model validation can inform the technical assurance of AI.
*   NIST AI RMF's focus on trustworthiness attributes (fairness, transparency, privacy) can broaden SR 11-7's scope to address ethical and societal AI risks.
*   SR 11-7's established governance structures can be extended to cover the broader AI lifecycle as defined by NIST.

The application presents a summary comparison table that consolidates these points.

### Interactive Mapping: SR 11-7 to NIST AI RMF
This section of the application provides an interactive tool to illustrate how the core pillars and principles of SR 11-7 align with and contribute to the functions of the NIST AI RMF.

You will see a radio button group labeled "Select an SR 11-7 Element." As you select different elements, the application dynamically displays how that SR 11-7 concept connects to the NIST AI RMF functions (Govern, Map, Measure, Manage) and its trustworthiness attributes.

Let's try selecting a few:

1.  **Select "Model Risk Governance"**:
    *   The application explains that SR 11-7's emphasis on strong oversight, clear policies, and defined roles directly aligns with the NIST AI RMF's **Govern** function. It highlights that the **Accountability** attribute is foundational here.
    *   You'll see a table mapping SR 11-7 MRM Pillars to the NIST AI RMF Govern Function, with the "Model Governance" row highlighted, detailing how it contributes to establishing AI risk oversight.

2.  **Select "Model Development & Implementation"**:
    *   The application indicates this maps to both the **Map** and **Manage** functions of NIST AI RMF. It explains how identifying risks during development (Map) and implementing controls early (Manage) are critical. Trustworthiness attributes like **Validity**, **Reliability**, and **Security** are key during this phase.
    *   Corresponding tables for "Map & Manage Functions" will be displayed, highlighting relevant aspects.

3.  **Select "Effective Challenge"**:
    *   The application clarifies that SR 11-7's requirement for independent validation and critical assessment maps strongly to the **Measure** and **Govern** functions of NIST AI RMF. It ensures that AI systems are rigorously evaluated and that processes for objective review are established. Attributes like **Transparency** and **Accountability** are crucial for effective challenge.
    *   Associated trustworthiness attributes will be explained, reinforcing the connection.

This interactive feature helps you visualize the practical integration points between the two frameworks, showing how established MRM practices can be adapted and expanded for AI.

## 6. Framework Application to Generative & Agentic AI
Duration: 00:07:00

The advent of Generative AI (e.g., Large Language Models - LLMs) and Agentic AI systems introduces a new frontier in AI risk management. Navigate to **"Framework Application to Generative & Agentic AI"** in the sidebar. While SR 11-7 and NIST AI RMF provide foundational principles, these advanced AI paradigms necessitate tailored considerations and mitigation strategies.

### Heightened Model Risk with Generative AI
Generative AI models, due to their emergent capabilities and less predictable outputs, introduce heightened model risks:

*   **Hallucinations & Factual Inaccuracy:** LLMs can generate plausible-sounding but incorrect or fabricated information.
*   **Misinformation & Disinformation:** Potential for generating and spreading harmful or deceptive content at scale.
*   **Intellectual Property (IP) Infringement:** Generative models trained on vast datasets may reproduce copyrighted material.
*   **Bias Propagation:** Can perpetuate and amplify societal biases present in their training data, leading to unfair outputs.
*   **Data Leakage/Privacy Concerns:** Risk of inadvertently revealing sensitive information from training data.
*   **Adversarial Prompting/Prompt Injection:** Malicious inputs designed to manipulate the model's behavior or extract sensitive information.

### Specific Risks of Agentic AI
Agentic AI systems, capable of autonomous decision-making and action, introduce further complexities:

*   **Loss of Control:** Difficulty in establishing clear boundaries and ensuring human oversight over autonomous actions.
*   **Emergent Behaviors:** Unpredictable and unintended behaviors arising from complex interactions within the environment.
*   **Ethical Dilemmas:** Agents making decisions in ethically ambiguous situations without human intervention.
*   **Safety Criticality:** High stakes when agents operate in physical environments or make irreversible decisions.
*   **Dependency Risks:** Over-reliance on agents can lead to critical failures if the agent malfunctions or is compromised.

### Tailored Mitigation and Oversight
Managing risks in Generative and Agentic AI requires a combination of traditional MRM principles and new, AI-specific approaches:

*   **Enhanced Prompt Engineering & Guardrails:** Developing robust techniques to guide model outputs and implementing explicit content filters.
*   **Human-in-the-Loop & Human-on-the-Loop:** Designing systems where humans retain ultimate control, either by actively reviewing outputs or monitoring performance with intervention capabilities.
*   **Rigorous Red Teaming:** Proactively testing AI systems for vulnerabilities, biases, and unintended behaviors using adversarial techniques.
*   **Transparency & Explainability:** Investing in methods to understand model reasoning, even for complex generative models.
*   **Continuous Monitoring & Drift Detection:** Implementing sophisticated monitoring for changes in output quality, factual accuracy, and alignment.
*   **AI Bill of Materials (AI-BOM) & Supply Chain Security:** Documenting all components of an AI system, including third-party models and datasets.
*   **Clear Accountability Frameworks:** Establishing who is responsible for AI actions and outcomes.
*   **Ethical AI Review Boards:** Incorporating independent ethical review during design and deployment.

By adapting and extending the principles of SR 11-7 and NIST AI RMF, organizations can build a more resilient and responsible approach to managing the risks of advanced AI systems.

## 7. Essential AI Assurance Artifacts
Duration: 00:08:00

Effective AI risk management and assurance rely heavily on robust documentation. Just as financial models require detailed records, AI systems demand specialized artifacts to ensure transparency, accountability, and ongoing trustworthiness. These artifacts serve as critical communication tools for developers, risk managers, auditors, and regulators. Navigate to **"Essential AI Assurance Artifacts"** in the sidebar to explore them.

### Introduction to AI Assurance Documentation
Beyond traditional software documentation, AI assurance artifacts focus specifically on the unique characteristics and risks of AI systems. Key examples include:

*   **Model Cards:** Summarize key information about an AI model.
*   **Data Cards:** Detail the characteristics and provenance of datasets used to train AI.
*   **Risk Registers:** Document identified risks, their assessment, and mitigation strategies.

### Model Cards: AI Model Information Summary
Inspired by product labels, Model Cards provide a structured summary of an AI model's characteristics, intended uses, performance, and ethical considerations. They are crucial for transparency and responsible deployment. The application shows example fields for a Model Card:

| Model Card Field                    | Example Content/Purpose                                                |
| :- | : |
| Model Name/ID                       | Financial Fraud Detection Model v1.2                                   |
| Version                             | 1.2                                                                    |
| Owner                               | Risk Management Dept.                                                  |
| Date Developed                      | 2023-10-26                                                             |
| Intended Use Cases                  | Detecting suspicious credit card transactions.                         |
| Out-of-Scope Uses                   | Loan application scoring, customer service chatbots.                   |
| Training Data Description           | Synthetic transaction data, anonymized customer profiles (2020-2023).  |
| Evaluation Metrics (Overall)        | Accuracy: 95%, F1-Score: 0.88                                          |
| Fairness Metrics/Subgroup Performance | Equal Opportunity (False Negative Rate for different demographics).    |
| Known Limitations                   | May struggle with novel fraud patterns.                                |
| Ethical Considerations              | Potential for false positives impacting legitimate users; need clear appeal process. |
| Deployment/Monitoring Guidelines    | Continuous monitoring for drift, quarterly re-evaluation.              |

### Data Cards: Dataset Characteristics and Provenance
Data Cards complement Model Cards by providing detailed information about the datasets used to train and evaluate AI models. Understanding the data is fundamental to understanding potential biases and limitations of the AI system. The application shows example fields for a Data Card:

| Data Card Field         | Example Content/Purpose                                              |
| :- | :- |
| Dataset Name/ID         | Customer Transaction History                                         |
| Version                 | 1.0                                                                  |
| Source(s)               | Internal CRM, Third-Party Payment Processor                          |
| Collection Method       | Automated API pull, Manual entry                                     |
| Date Collected/Created  | 2018-01-01 to 2023-09-30                                             |
| Last Updated            | 2023-10-15                                                           |
| Data Description        | Anonymized transaction details for credit card usage.                |
| Number of Samples/Features | 10M rows, 50 features                                                |
| Annotation/Labeling Process | Fraudulent transactions labeled by human experts.                      |
| Known Biases/Limitations | Geographical bias towards urban areas; potential underrepresentation of certain demographics. |
| Privacy Considerations  | All PII anonymized; GDPR compliant.                                  |
| Data Retention Policy   | Data retained for 7 years as per regulatory requirements.            |

### Risk Registers: Systematic Risk Tracking
An AI Risk Register is a critical tool for systematically identifying, assessing, tracking, and mitigating risks throughout the AI lifecycle. It provides a living document for ongoing risk management. The application shows example fields for an AI Risk Register:

| Risk Register Field    | Example Content/Purpose                                              |
| : | :- |
| Risk ID                | AI-001                                                               |
| Risk Category          | Model (Bias)                                                         |
| Risk Description       | Algorithmic bias leading to discriminatory loan decisions.           |
| Potential Impact (Severity) | High (Reputational, Legal, Financial)                                |
| Likelihood             | Medium                                                               |
| Risk Score (Impact x Likelihood) | High (3x2 = 6)                                                     |
| Mitigation Controls    | Fairness audit; re-weighting training data; human-in-the-loop review for high-risk applications. |
| Response Plan          | Alert risk team; pause model deployment; initiate remediation plan; notify affected parties. |
| Owner                  | Chief Risk Officer                                                   |
| Status                 | In Progress                                                          |
| Date Identified        | 2023-08-01                                                           |
| Last Review Date       | 2023-10-20                                                           |

<aside class="positive">
<b>Key Takeaway:</b> These assurance artifacts are not static documents but should be continuously updated throughout the AI lifecycle, reflecting changes in the model, data, or operating environment. They are foundational for auditing, regulatory compliance, and building trust in AI systems.
</aside>
