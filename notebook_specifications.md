
# Technical Specification for Jupyter Notebook: AI Framework Comparator: SR 11-7 vs. NIST AI RMF

## 1. Notebook Overview

*   **Learning Goals:**
    *   Differentiate between the scope and applicability of SR 11-7 and the NIST AI RMF 1.0.
    *   Identify shared objectives between SR 11-7 and NIST AI RMF in enhancing trustworthiness and governance of AI.
    *   Understand how SR 11-7's Model Risk Management (MRM) pillars (Development/Implementation, Validation, Governance, Ongoing Monitoring) map to NIST AI RMF's functions (Govern, Map, Measure, Manage).
    *   Recognize the unique attributes of trustworthy AI introduced by NIST AI RMF, such as validity, reliability, safety, security, transparency, fairness, accountability, and privacy-preserving.
    *   Introduce and explain the core principles and pillars of SR 11-7, including "Effective Challenge" and Model Risk Governance.
    *   Detail the functions and trustworthiness attributes of NIST AI RMF.
    *   Provide a clear comparative analysis of both frameworks, focusing on their differences, shared objectives, and practical integration points.
    *   Include conceptual discussions on emerging AI risks such as hallucinations, goal mis-specification, and autonomy creep.
    *   Understand AI risk categorization across five key dimensions: Data, Model, System, Human, and Organizational.
    *   Learn about essential AI assurance artifacts: Model Cards, Data Cards, and Risk Registers, and how they facilitate effective challenge and audit.

*   **Target Audience:** Risk Managers, particularly those involved in model risk management, aiming to understand the transition and integration from traditional financial model risk management to comprehensive AI assurance.

## 2. Code Requirements

*   **Expected Libraries:**
    *   `pandas`: For creating and displaying structured tabular data (e.g., comparison tables, artifact examples).
    *   `IPython.display`: For displaying rich Markdown content from within code cells and for clarity when constructing complex multi-line markdown tables or diagrams programmatically.

*   **Algorithms or Functions to be Implemented:** (Conceptual descriptions, no actual algorithms for data processing)
    *   `display_markdown_text(text)`: A utility function to display rich Markdown text within a code cell, enhancing readability for conceptual sections.
    *   `create_sr117_pillars_table()`: A function that generates a pandas DataFrame detailing the core pillars of SR 11-7 and their brief descriptions.
    *   `create_sr117_modern_frameworks_comparison_table()`: A function that generates a pandas DataFrame comparing SR 11-7 views with modern AI frameworks (e.g., NIST AI RMF) across aspects like model definition, tiering, risk management, and validation.
    *   `create_ai_risk_taxonomy_diagram_text()`: A function that generates a textual representation (e.g., using newline characters and indentation) illustrating the five key dimensions of AI risk taxonomy.
    *   `create_nist_ai_rmf_attributes_table()`: A function that generates a pandas DataFrame listing the key trustworthiness attributes of NIST AI RMF with brief definitions.
    *   `create_sr117_nist_comparison_summary_table()`: A function that generates a pandas DataFrame summarizing the distinct scopes, shared objectives, and integration benefits of SR 11-7 and NIST AI RMF.
    *   `create_sr117_to_nist_govern_mapping_table()`: A function that generates a pandas DataFrame mapping SR 11-7 MRM pillars (Governance, Development/Implementation, Validation, Ongoing Monitoring) to the NIST AI RMF "Govern" function with key aspects and best practices.
    *   `create_sr117_to_nist_map_measure_mapping_table()`: A function that generates a pandas DataFrame mapping relevant SR 11-7 MRM pillars (Development/Implementation, Validation, Ongoing Monitoring) to NIST AI RMF "Map" and "Measure" functions with key aspects and best practices.
    *   `create_sr117_to_nist_manage_mapping_table()`: A function that generates a pandas DataFrame mapping relevant SR 11-7 MRM pillars (Ongoing Monitoring, Validation, Development/Implementation) to the NIST AI RMF "Manage" function with key aspects and best practices.
    *   `create_model_card_example_fields_table()`: A function that generates a pandas DataFrame illustrating example fields and components of an AI Model Card.
    *   `create_data_card_example_fields_table()`: A function that generates a pandas DataFrame illustrating example fields and components of an AI Data Card.
    *   `create_risk_register_example_fields_table()`: A function that generates a pandas DataFrame illustrating example fields and components of an AI Risk Register.
    *   `present_scenario_question(question, discussion_points)`: A function that displays a scenario question and its associated discussion points in a structured format.

*   **Visualizations:**
    *   **Tables:**
        *   SR 11-7 Pillars table.
        *   Comparison table of SR 11-7 vs. Modern AI Frameworks.
        *   NIST AI RMF Trustworthiness Attributes table.
        *   Summary comparison table of SR 11-7 and NIST AI RMF.
        *   Mapping tables from SR 11-7 MRM pillars to NIST AI RMF functions (Govern, Map, Measure, Manage).
        *   Example Model Card structure (fields and purpose).
        *   Example Data Card structure (fields and purpose).
        *   Example Risk Register structure (fields like risk ID, description, impact, likelihood, mitigation).
    *   **Diagrams (Conceptual/Text-based):**
        *   Simple text-based representation or bulleted list for the five key dimensions of AI risk taxonomy (Data, Model, System, Human, Organizational).
        *   Conceptual flow for "Module Summary" as seen in slide 36.

## 3. Notebook Sections (in detail)

---

### Section 1: Introduction to AI Risk and Assurance

**Markdown Cell:**
# AI Framework Comparator: SR 11-7 vs. NIST AI RMF

## Introduction

Welcome to this educational notebook designed for **Risk Managers**. This module clarifies the relationship and complementary nature of SR 11-7 and the NIST AI Risk Management Framework (AI RMF 1.0). Our goal is to enable a deeper understanding of the evolution from traditional model risk management to comprehensive AI assurance, highlighting key differences, shared objectives, and practical integration points for robust AI governance.

### Module Overview and Learning Objectives

This module aims to provide a comprehensive understanding of AI risk and assurance by:
*   **Module Scope:** Managing risks in large-scale AI systems, including Large Language Models (LLMs) and agentic architectures.
*   **Foundational Frameworks:** Leveraging SR 11-7 and NIST AI RMF 1.0 principles.
*   **Key Learning Outcomes:** Applying SR 11-7 and NIST AI RMF to generative/agentic AI, identifying life cycle risks (data, model, system, human, organizational), and constructing essential assurance artifacts.
*   **Evolution of Assurance:** Tracing the transition from traditional Model Risk Management (MRM) to comprehensive AI assurance practices.

**Code Cell (Function Implementation):**
```python
import pandas as pd
from IPython.display import display, Markdown

def display_markdown_text(text):
    """Displays markdown formatted text."""
    display(Markdown(text))

# No specific function to implement for this introductory section beyond the display_markdown_text helper.
# The content is primarily static markdown for introduction.
```

**Code Cell (Execution):**
```python
# No specific function call needed beyond the initial markdown display.
# This cell is intentionally left empty as the introduction is primarily static text.
```

**Markdown Cell (Explanation for Execution):**
This introductory section sets the stage for the notebook, outlining its purpose, target audience, and the key topics that will be covered. It emphasizes the critical need for adapting existing risk management practices to address the unique challenges posed by modern AI systems.

---

### Section 2: The Imperative of AI Risk Management

**Markdown Cell:**
## The Imperative of AI Risk Management

The rapid advancement and widespread deployment of Artificial Intelligence, particularly sophisticated models like Large Language Models (LLMs), have introduced new layers of complexity and risk that amplify traditional model risks.

### Emergent AI Risks

AI's unique characteristics give rise to **emergent risks** that were not typically considered in traditional model risk management:
*   **Hallucinations:** AI generating false or misleading information with high confidence.
*   **Goal Mis-specification:** AI pursuing unintended objectives due to poorly defined goals.
*   **Autonomy Creep:** AI systems operating beyond their intended scope or human oversight.
*   **Magnified Biases:** Existing societal biases being amplified by AI models due to biased training data or algorithmic design.

### Five Key Dimensions of AI Risk

To systematically manage these diverse risks, AI failures are categorized across five critical dimensions:
*   **Data Risks:** Concerns related to the quality, provenance, privacy, and bias of data used to train and operate AI models.
*   **Model Risks:** Issues concerning algorithmic bias, accuracy, reliability, robustness, and interpretability of AI models.
*   **System Risks:** Risks associated with the integration of AI models into larger systems, architectural challenges, and supply chain vulnerabilities.
*   **Human Risks:** Challenges involving misuse, over-reliance, misinterpretation, and loss of human oversight of AI systems.
*   **Organizational Risks:** Governance gaps, policy deficiencies, and cultural factors that impede responsible AI development and deployment.

The potential impact of AI failures spans across financial, reputational, and operational domains, affecting various industries and demanding robust risk management frameworks.

**Code Cell (Function Implementation):**
```python
def create_ai_risk_taxonomy_diagram_text():
    """
    Generates a textual representation of the five key dimensions of AI risk taxonomy.
    """
    taxonomy_text = """
    AI Risk Taxonomy: A Multidimensional Approach

    1.  **Data Risks:** Quality, Provenance, Privacy, Bias
    2.  **Model Risks:** Bias, Accuracy, Reliability, Robustness, Interpretability
    3.  **System Risks:** Integration, Architecture, Supply Chain Vulnerabilities
    4.  **Human Risks:** Misuse, Over-Reliance, Loss of Oversight, Misinterpretation
    5.  **Organizational Risks:** Governance, Policy, Culture, Accountability
    """
    return taxonomy_text
```

**Code Cell (Execution):**
```python
display_markdown_text(create_ai_risk_taxonomy_diagram_text())
```

**Markdown Cell (Explanation for Execution):**
This section details the critical need for AI risk management, outlining emergent risks and categorizing AI risks into five key dimensions. The text-based "diagram" above provides a quick reference to these dimensions, illustrating a systematic approach to identifying, analyzing, and managing the diverse risks across the entire AI lifecycle.

---

### Section 3: Foundations of Model Risk Management (SR 11-7)

**Markdown Cell:**
## Foundations of Model Risk Management (SR 11-7)

SR 11-7, issued in 2011 by the Board of Governors of the Federal Reserve System and the Office of the Comptroller of the Currency, is the foundational U.S. guidance for model risk management in financial institutions. It defines **model risk** as the potential for adverse consequences from decisions based on incorrect or misused model outputs and reports.

### Core Principles and Pillars of SR 11-7

SR 11-7 emphasizes key pillars and principles for effective model risk management:
*   **Model Definition:** SR 11-7 broadly defines a model as a quantitative method, system, or approach that applies statistical, economic, financial, or mathematical theories, techniques, and assumptions to process input data into quantitative estimates.
*   **Risk Amplification:** Model risk intensifies with greater model complexity, higher uncertainty in inputs/assumptions, broader extent of use, and larger potential impact. Modern AI models, particularly LLMs, significantly amplify these risks due to their inherent complexity and widespread application.
*   **Effective Challenge:** This is a core principle, requiring objective, informed reviewers (independent validation teams) to critically test models, scrutinize model behavior, and identify drift and hidden errors. It mandates a robust independent validation function.
*   **Model Risk Governance:** Mandates board and senior management oversight to ensure model risk stays within organizational tolerance. This includes clear roles, responsibilities, and policies for model development, implementation, use, and validation.
*   **Model Lifecycle Management:** SR 11-7 outlines stages of model risk management covering development, implementation, validation, and ongoing monitoring.

**Code Cell (Function Implementation):**
```python
def create_sr117_pillars_table():
    """
    Generates a pandas DataFrame detailing the core pillars of SR 11-7.
    """
    data = {
        "SR 11-7 Pillar": [
            "Model Development & Implementation",
            "Model Validation",
            "Model Governance",
            "Ongoing Monitoring"
        ],
        "Description": [
            "Robust processes for model design, data quality, and implementation controls.",
            "Independent assessment of model logic, data, and performance; includes outcomes analysis and backtesting.",
            "Clear roles, responsibilities, policies, and senior management oversight for model risk management.",
            "Continuous monitoring of model performance, data characteristics, and model limitations."
        ]
    }
    df = pd.DataFrame(data)
    return df
```

**Code Cell (Execution):**
```python
display_markdown_text("### SR 11-7 Model Risk Management (MRM) Pillars")
display(create_sr117_pillars_table())
```

**Markdown Cell (Explanation for Execution):**
The table above summarizes the fundamental pillars of SR 11-7, which establish a structured approach to managing model risk in financial institutions. These pillars form the basis upon which AI risk management frameworks build, extending the scope to encompass the unique complexities of AI systems.

---

### Section 4: Broadening Model Definition & Risk Tiering

**Markdown Cell:**
## Broadening Model Definition & Risk Tiering

The advent of AI necessitates a broader interpretation of what constitutes a "model" and how risks are categorized and managed. Traditional SR 11-7 focuses primarily on quantitative methods for financial decisions, while modern frameworks like NIST AI RMF encompass a wider range of AI/ML systems and their associated processes.

This expanded view also impacts **risk tiering**, moving beyond simple materiality to consider impact, complexity, data sensitivity, and interpretability.

**Code Cell (Function Implementation):**
```python
def create_sr117_modern_frameworks_comparison_table():
    """
    Generates a pandas DataFrame comparing SR 11-7 views with modern AI frameworks.
    """
    data = {
        "Aspect": ["Model Definition", "Model Tiering", "Risk Management", "Validation"],
        "Traditional SR 11-7 View": [
            "Focus on quantitative methods for financial decisions.",
            "Categorization by materiality and complexity.",
            "General model risk management.",
            "Standard validation practices."
        ],
        "Modern Frameworks (e.g., NIST AI RMF)": [
            "Includes AI/ML systems, their outputs, and even decision-making processes.",
            "Categorization by risk level (impact, complexity, data sensitivity, interpretability).",
            "Tailored risk management strategies based on tier.",
            "Enhanced validation (e.g., third-party, continuous) and more documentation for higher-tier AI models."
        ]
    }
    df = pd.DataFrame(data)
    return df
```

**Code Cell (Execution):**
```python
display_markdown_text("### SR 11-7 vs. Modern AI Frameworks: A Comparative View")
display(create_sr117_modern_frameworks_comparison_table())
```

**Markdown Cell (Explanation for Execution):**
The comparison table highlights the evolution of risk management thinking from SR 11-7's traditional scope to the more expansive perspective of modern AI risk frameworks like NIST AI RMF. This shift is crucial for addressing the unique characteristics and risks associated with contemporary AI systems.

---

### Section 5: AI Risk Taxonomy: Data and Model Risks

**Markdown Cell:**
## AI Risk Taxonomy: Deep Dive

Building on the five key dimensions, let's explore specific risks within each category.

### Data Risks: Quality, Provenance, and Privacy

Data is the lifeblood of AI, and risks associated with it can significantly impact model performance and trustworthiness.
*   **Data Quality and Relevance:** Critical for AI model performance. Regulators increasingly emphasize the role of data quality, completeness, and relevance as emerging AI risks. Poor quality data can lead to inaccurate or biased model outputs.
*   **Data Provenance and Lineage:** Essential for understanding the origin, transformations, and integrity of data used in AI systems. A clear audit trail helps in tracking and mitigating data-related risks.
*   **Data Privacy and Sensitive Information:** Navigating regulatory expectations (e.g., GDPR, CCPA) and ensuring secure, ethical handling of sensitive data is paramount. Privacy-preserving AI techniques are increasingly important.

### Model Risks: Bias, Accuracy, and Robustness

Model risks are inherent to the AI algorithms themselves and how they are trained and deployed.
*   **Algorithmic Bias & Fairness:** Addresses risks from biased training data or model design, leading to unfair, discriminatory, or disparate AI outputs for different groups. Fairness metrics often need to be carefully chosen and monitored, for example:
    *   **Demographic Parity:** $P(\hat{Y}=1 | A=a) = P(\hat{Y}=1 | A=b)$
    *   **Equalized Odds:** $P(\hat{Y}=1 | Y=y, A=a) = P(\hat{Y}=1 | Y=y, A=b)$
    Where $\hat{Y}$ is the predicted outcome, $Y$ is the true outcome, and $A$ is a protected attribute.
*   **Accuracy & Reliability:** Examines issues with the precision, consistency, and trustworthiness of model predictions; highlights potential for flawed outputs. This includes standard performance metrics like $Accuracy$, $F1-Score$, $Precision$, and $Recall$. For example:
    $$Accuracy = \frac{\text{True Positives} + \text{True Negatives}}{\text{Total Samples}}$$
    $$F1-Score = 2 \times \frac{Precision \times Recall}{Precision + Recall}$$
*   **Model Robustness:** Discusses the AI system's ability to maintain stable performance against diverse inputs, unexpected shifts (e.g., concept drift), and adversarial attacks.

**Code Cell (Function Implementation):**
```python
# No specific function to implement for this conceptual section beyond display_markdown_text.
# The focus is on definitions and formulas.
```

**Code Cell (Execution):**
```python
# No specific function call needed. This cell is intentionally left empty.
```

**Markdown Cell (Explanation for Execution):**
This section breaks down Data and Model Risks, defining key concepts like data provenance and model robustness. It also introduces conceptual performance and fairness metrics, illustrating where mathematical concepts would apply in the 'Measure' function of AI risk management.

---

### Section 6: AI Risk Taxonomy: System, Human, and Organizational Risks

**Markdown Cell:**
## AI Risk Taxonomy: System, Human, and Organizational Risks

Continuing our deep dive into the AI risk taxonomy, we now cover the remaining three dimensions.

### System Risks: Integration, Architecture, and Supply Chain

These risks arise from how AI components are integrated into larger systems and the broader ecosystem.
*   **Integration Flaws:** Integrating AI models into larger, complex systems can create architectural weaknesses, performance bottlenecks, and unforeseen interactions.
*   **Architectural Challenges:** Complex agentic AI architectures, where AI systems act with a degree of autonomy, can cause scalability issues and amplify risks through error propagation across multiple steps or agents.
*   **AI Supply Chain Vulnerabilities:** Ensuring the integrity, quality, and security of third-party models, data, and components is critical. This includes rigorous vetting, provenance tracking, and security assessments of all AI supply chain elements.
*   **Supply Chain Security Measures:** Implement hashing for component verification, developer provenance verification, API security for model access, and maintaining an **AI Bill of Materials (AI-BOM)** to track all components.

### Human-Centric AI Risks: Misuse, Over-Reliance, and Oversight

These risks stem from the interaction between humans and AI systems.
*   **Misuse and Misinterpretation:** AI outputs, especially from LLMs, can be factually incorrect yet appear credible (hallucinations), risking dangerous misinterpretation and inappropriate use in high-stakes fields like medicine or finance.
*   **Over-Reliance and Autonomy Creep:** Poorly defined AI goals or excessive trust can cause unintended goal pursuit or "autonomy creep," where agentic systems operate beyond their intended scope, potentially leading to unauthorized or harmful actions.
*   **Loss of Human Oversight:** Effective human control in autonomous AI demands robust governance, human-in-the-loop checks (e.g., validation points, human review for critical decisions), and expanded risk oversight, particularly for agentic AI.

### Organizational AI Risk: Governance, Policy, and Culture

These overarching risks relate to the institutional environment in which AI is developed and deployed.
*   **Robust Governance & Oversight:** Establishing clear roles, responsibilities, and accountability for AI risk oversight, with active board and senior management engagement, guided by frameworks like SR 11-7 and NIST AI RMF.
*   **Policy & Ethical Guidelines:** Develop and enforce comprehensive organizational policies and ethical guidelines for responsible AI development, deployment, and usage to mitigate legal and reputational risks.
*   **Fostering a Responsible AI Culture:** Cultivate an organizational culture that promotes continuous challenge, transparency, and accountability in all AI initiatives, encouraging open discussion of AI risks and ethical considerations.

**Code Cell (Function Implementation):**
```python
# No specific function to implement for this conceptual section beyond display_markdown_text.
# The focus is on definitions and conceptual explanations.
```

**Code Cell (Execution):**
```python
# No specific function call needed. This cell is intentionally left empty.
```

**Markdown Cell (Explanation for Execution):**
This section completes the detailed exploration of AI risk taxonomy, covering System, Human, and Organizational risks. It highlights the interconnectedness of these risk dimensions and the importance of a holistic approach to AI risk management, from architectural design to organizational culture.

---

### Section 7: Interconnected AI Risks & Emerging Threats

**Markdown Cell:**
## Interconnected AI Risks & Emerging Threats

AI risks are not isolated; they are often **interdependent**, with various categories amplifying one another in complex systems. Understanding these connections is crucial for holistic risk management.

### Key Interdependencies and Emerging Concerns

*   **Data Quality and Relevance:** Emerging AI risks are heavily influenced by data quality and relevance, as emphasized by regulators. Poor data quality can directly lead to algorithmic bias, inaccurate models, and ultimately, misinterpretation by human users.
*   **LLM-Specific Hazards:** Large Language Models (LLMs) introduce unique and significant threats:
    *   **Hallucinations:** As discussed, these can lead to critical errors, especially in high-stakes applications.
    *   **Goal Mis-specification:** Complex LLM tasks can lead to AI pursuing unintended objectives.
    *   **Autonomy Creep:** As LLMs become more integrated into agentic systems, their ability to act autonomously without sufficient human oversight poses a significant risk.
*   **Bias and Ethical Concerns:** These are often amplified by opaque LLM training data, which can contain hidden biases that are difficult to detect and mitigate. This opacity makes comprehensive bias audits challenging.

Managing these interconnected and emergent risks requires a proactive and adaptive approach, going beyond traditional model risk management to encompass the full AI lifecycle and its broader societal impacts.

**Code Cell (Function Implementation):**
```python
# No specific function to implement for this conceptual section beyond display_markdown_text.
# The focus is on definitions and conceptual explanations.
```

**Code Cell (Execution):**
```python
# No specific function call needed. This cell is intentionally left empty.
```

**Markdown Cell (Explanation for Execution):**
This section underscores the complex and interconnected nature of AI risks, particularly highlighting emerging threats associated with LLMs. It emphasizes that a comprehensive understanding of these interdependencies is vital for developing effective mitigation strategies.

---

### Section 8: Introduction to NIST AI Risk Management Framework (AI RMF 1.0)

**Markdown Cell:**
## Introduction to NIST AI Risk Management Framework (AI RMF 1.0)

The NIST AI Risk Management Framework (AI RMF 1.0) is a voluntary U.S. framework released in January 2023, developed with extensive industry and government input. Its primary goal is to improve the ability to incorporate **trustworthiness considerations** into AI product design, development, use, and evaluation across various industries.

### Core Objectives of AI RMF

*   **Promote Trustworthy AI:** By providing a flexible, systematic, and comprehensive approach to managing AI risks.
*   **Complement Existing Guidance:** The AI RMF complements existing risk management guidance, like SR 11-7, by emphasizing specific roles, policies, and processes tailored for AI risk oversight.
*   **Encompass Trustworthiness Attributes:** It addresses a broad range of AI trustworthiness attributes, which are crucial for responsible and ethical AI.

**Code Cell (Function Implementation):**
```python
# No specific function to implement for this conceptual section beyond display_markdown_text.
# The focus is on definitions and conceptual explanations.
```

**Code Cell (Execution):**
```python
# No specific function call needed. This cell is intentionally left empty.
```

**Markdown Cell (Explanation for Execution):**
This section introduces the NIST AI RMF 1.0, outlining its purpose as a voluntary framework for promoting trustworthy AI. It highlights the framework's complementary nature to existing guidance like SR 11-7 and its focus on embedding trustworthiness throughout the AI lifecycle.

---

### Section 9: Trustworthy AI Attributes: Validity, Reliability, Safety

**Markdown Cell:**
## Trustworthy AI Attributes: Validity, Reliability, Safety

The NIST AI RMF emphasizes several key attributes that define **trustworthy AI**. These attributes extend beyond traditional model performance metrics to address the broader societal and operational impacts of AI systems.

### Validity

*   **Definition:** Ensuring the AI system accurately performs its intended function and produces correct outputs for its specified purpose. This includes domain validity (is the model fit for its specific use case?) and ethical validity (does it align with ethical principles?).
*   **Importance:** A valid AI system performs as expected, reducing the risk of errors and unintended consequences.

### Reliability

*   **Definition:** Guarantees consistent and stable performance of the AI system over time and across various operational conditions, including different data inputs and environmental changes.
*   **Importance:** A reliable AI system maintains its performance and outputs under varying circumstances, building user trust and preventing unexpected failures.

### Safety

*   **Definition:** Minimizing the potential for the AI system to cause harm to individuals, society, or the environment, particularly in safety-critical applications (e.g., autonomous vehicles, medical diagnostics).
*   **Importance:** Safety is paramount to prevent adverse physical, psychological, or financial outcomes. It involves identifying and mitigating potential hazards before deployment.

**Code Cell (Function Implementation):**
```python
def create_nist_ai_rmf_validity_reliability_safety_attributes_table():
    """
    Generates a pandas DataFrame listing NIST AI RMF trustworthiness attributes for Validity, Reliability, Safety.
    """
    data = {
        "Attribute": ["Validity", "Reliability", "Safety"],
        "Description": [
            "Ensuring the AI system accurately performs its intended function and produces correct outputs.",
            "Guarantees consistent and stable performance of the AI system over time and across operational conditions.",
            "Minimizing the potential for the AI system to cause harm to individuals, society, or the environment."
        ]
    }
    df = pd.DataFrame(data)
    return df
```

**Code Cell (Execution):**
```python
display_markdown_text("### Key Trustworthy AI Attributes (Part 1)")
display(create_nist_ai_rmf_validity_reliability_safety_attributes_table())
```

**Markdown Cell (Explanation for Execution):**
This section defines the critical trustworthiness attributes of Validity, Reliability, and Safety as outlined by the NIST AI RMF. The table provides a concise summary, emphasizing that trustworthy AI must not only function correctly but also perform consistently and without causing undue harm.

---

### Section 10: Trustworthy AI Attributes: Security, Transparency, Fairness

**Markdown Cell:**
## Trustworthy AI Attributes: Security, Transparency, Fairness

Continuing with the NIST AI RMF trustworthiness attributes, we examine security, transparency, and fairness, which are vital for building confidence in AI systems.

### Security

*   **Definition:** Protecting AI systems from adversarial attacks (e.g., prompt injection, data poisoning), unauthorized access, and ensuring data integrity and access governance across the entire AI lifecycle.
*   **Importance:** A secure AI system resists malicious manipulation and protects sensitive data, maintaining its intended function and preventing exploitation.

### Transparency

*   **Definition:** Understanding how AI systems, especially LLMs, arrive at outputs. This involves using interpretability methods (e.g., saliency maps, LIME, SHAP) and counterfactual explanations to reveal the model's decision-making process.
*   **Importance:** Transparency fosters trust and enables effective challenge and audit, allowing stakeholders to understand and question AI decisions.

### Fairness

*   **Definition:** Identifying and mitigating biases encoded and amplified by AI, particularly in LLMs, to ensure equitable and just outcomes for all individuals and groups. This includes addressing disparate impact and treatment.
*   **Importance:** Fairness is critical for preventing discrimination and ensuring that AI systems do not perpetuate or exacerbate societal inequalities.

**Code Cell (Function Implementation):**
```python
def create_nist_ai_rmf_security_transparency_fairness_attributes_table():
    """
    Generates a pandas DataFrame listing NIST AI RMF trustworthiness attributes for Security, Transparency, Fairness.
    """
    data = {
        "Attribute": ["Security", "Transparency", "Fairness"],
        "Description": [
            "Protecting AI systems from adversarial attacks and ensuring data integrity and access governance.",
            "Understanding how AI systems arrive at outputs through interpretability methods and counterfactuals.",
            "Identifying and mitigating biases in AI to ensure equitable and just outcomes for all."
        ]
    }
    df = pd.DataFrame(data)
    return df
```

**Code Cell (Execution):**
```python
display_markdown_text("### Key Trustworthy AI Attributes (Part 2)")
display(create_nist_ai_rmf_security_transparency_fairness_attributes_table())
```

**Markdown Cell (Explanation for Execution):**
This table outlines the crucial attributes of Security, Transparency, and Fairness within the NIST AI RMF. These attributes are particularly salient for AI systems, especially LLMs, where issues like adversarial attacks, model opaqueness, and embedded biases pose significant challenges.

---

### Section 11: Trustworthy AI Attributes: Accountability & Privacy-Preserving

**Markdown Cell:**
## Trustworthy AI Attributes: Accountability & Privacy-Preserving

The final set of NIST AI RMF trustworthiness attributes focuses on establishing responsibility and protecting sensitive information.

### Accountability

*   **Definition:** Establishing clear roles, responsibilities, and policies for AI risk oversight, including robust board-level governance, to ensure responsibility for AI outcomes and decisions. This involves defining who is ultimately answerable for AI system performance and impact.
*   **Importance:** Accountability ensures that there are mechanisms for recourse and responsibility when AI systems cause harm or fail to meet expectations.

### Privacy-Preserving

*   **Definition:** Implementing strategies to address data sensitivity and integrating privacy by design throughout the entire AI lifecycle. This includes techniques like differential privacy, federated learning, and homomorphic encryption.
*   **Importance:** Protecting individual privacy is fundamental for ethical AI and maintaining public trust, especially when handling personal or sensitive data.

**Code Cell (Function Implementation):**
```python
def create_nist_ai_rmf_accountability_privacy_attributes_table():
    """
    Generates a pandas DataFrame listing NIST AI RMF trustworthiness attributes for Accountability and Privacy-Preserving.
    """
    data = {
        "Attribute": ["Accountability", "Privacy-Preserving"],
        "Description": [
            "Establishing clear roles, policies, and governance for AI risk oversight to ensure responsibility for AI outcomes.",
            "Implementing strategies to address data sensitivity and integrating privacy by design throughout the AI lifecycle."
        ]
    }
    df = pd.DataFrame(data)
    return df
```

**Code Cell (Execution):**
```python
display_markdown_text("### Key Trustworthy AI Attributes (Part 3)")
display(create_nist_ai_rmf_accountability_privacy_attributes_table())
```

**Markdown Cell (Explanation for Execution):**
This section concludes the overview of NIST AI RMF's trustworthiness attributes, focusing on Accountability and Privacy-Preserving. These attributes are foundational for ensuring that AI systems are developed and used responsibly, with clear lines of responsibility and robust protection of sensitive data.

---

### Section 12: Complementary Frameworks: SR 11-7 & NIST AI RMF

**Markdown Cell:**
## Complementary Frameworks: SR 11-7 & NIST AI RMF

SR 11-7 (focused on banking model risk) and NIST AI RMF (applicable to all AI systems) are not mutually exclusive but rather **complementary frameworks** for managing risk.

### Distinct Scopes

*   **SR 11-7:** Primarily focuses on model risk management within the **banking sector**, driven by regulatory compliance for financial models.
*   **NIST AI RMF:** Applies to **all AI systems** across diverse industries, offering a broader, voluntary framework for promoting trustworthy AI.

### Shared Objectives

Despite their distinct scopes, both frameworks share critical objectives:
*   **Enhance Trustworthiness:** Both aim to ensure that models/AI systems are reliable and can be trusted.
*   **Ensure Effective Challenge:** Both emphasize the need for objective and independent review.
*   **Establish Robust Governance:** Both mandate clear roles, policies, and senior management oversight for risk management.

### Integration Benefits

Mapping SR 11-7's MRM pillars (Development/Implementation, Validation, Governance, Ongoing Monitoring) to NIST AI RMF's functions (Govern, Map, Measure, Manage) enables comprehensive risk oversight by building upon existing MRM structures and adapting them for AI.

**Code Cell (Function Implementation):**
```python
def create_sr117_nist_comparison_summary_table():
    """
    Generates a pandas DataFrame summarizing the comparison between SR 11-7 and NIST AI RMF.
    """
    data = {
        "Aspect": ["Scope", "Primary Focus", "Regulatory Nature", "Key Objective"],
        "SR 11-7": [
            "Banking sector (financial models)",
            "Model Risk Management (MRM)",
            "Mandatory (for regulated financial institutions)",
            "Minimize adverse outcomes from model use"
        ],
        "NIST AI RMF": [
            "All AI systems across industries",
            "Trustworthy AI (risk management for AI)",
            "Voluntary (but rapidly becoming industry best practice)",
            "Foster development and use of trustworthy AI"
        ]
    }
    df = pd.DataFrame(data)
    return df
```

**Code Cell (Execution):**
```python
display_markdown_text("### SR 11-7 vs. NIST AI RMF: Summary Comparison")
display(create_sr117_nist_comparison_summary_table())
```

**Markdown Cell (Explanation for Execution):**
This table provides a concise summary of the similarities and differences between SR 11-7 and NIST AI RMF. It highlights their distinct scopes and regulatory natures while emphasizing their shared objectives in enhancing trustworthiness and governance, setting the stage for integrating these frameworks.

---

### Section 13: Mapping SR 11-7 MRM to NIST AI RMF: Govern Function

**Markdown Cell:**
## Mapping SR 11-7 MRM to NIST AI RMF: The "Govern" Function

The NIST AI RMF organizes AI risk management activities into four core functions: **Govern, Map, Measure, and Manage**. These functions are designed to be continuous and iterative. We will now explore how SR 11-7 MRM pillars align with these functions, starting with "Govern."

The **Govern** function in NIST AI RMF is about fostering a culture of responsible AI and establishing an AI risk management strategy. This aligns directly with the overall governance and oversight aspects emphasized in SR 11-7.

**Code Cell (Function Implementation):**
```python
def create_sr117_to_nist_govern_mapping_table():
    """
    Generates a pandas DataFrame mapping SR 11-7 MRM pillars to the NIST AI RMF "Govern" function.
    """
    data = {
        "SR 11-7 MRM Pillar": [
            "Model Governance",
            "Development/Implementation",
            "Validation",
            "Ongoing Monitoring"
        ],
        "NIST AI RMF Govern Function": [
            "Govern",
            "Govern",
            "Govern",
            "Govern"
        ],
        "Key Aspects & Best Practices": [
            "Establishing clear roles, policies, and a culture for AI risk oversight, including board-level governance. Ensuring AI risk stays within organizational tolerance and designing governance for human-in-the-loop oversight.",
            "Defining responsibilities for secure AI development and deployment and ensuring ethical considerations are embedded from the outset.",
            "Overseeing the objective review and effective challenge processes for AI models to ensure their accuracy, reliability, and fairness.",
            "Establishing robust procedures for continuous oversight, performance monitoring, and accountability throughout the AI lifecycle."
        ]
    }
    df = pd.DataFrame(data)
    return df
```

**Code Cell (Execution):**
```python
display_markdown_text("### Mapping SR 11-7 MRM Pillars to NIST AI RMF: Govern Function")
display(create_sr117_to_nist_govern_mapping_table())
```

**Markdown Cell (Explanation for Execution):**
This table illustrates how the governance, development, validation, and monitoring pillars of SR 11-7 all contribute to the overarching "Govern" function of NIST AI RMF. It shows that establishing a strong foundation of roles, policies, and culture is essential from the beginning of the AI lifecycle.

---

### Section 14: Mapping SR 11-7 MRM to NIST AI RMF: Map & Measure Functions

**Markdown Cell:**
## Mapping SR 11-7 MRM to NIST AI RMF: The "Map" & "Measure" Functions

Next, we map SR 11-7 pillars to the NIST AI RMF's "Map" and "Measure" functions, which are critical for identifying, analyzing, and quantifying AI risks.

The **Map** function is about identifying contexts, threats, and vulnerabilities related to AI, while the **Measure** function focuses on quantifying risks and evaluating AI trustworthiness.

**Code Cell (Function Implementation):**
```python
def create_sr117_to_nist_map_measure_mapping_table():
    """
    Generates a pandas DataFrame mapping relevant SR 11-7 MRM pillars to NIST AI RMF "Map" and "Measure" functions.
    """
    data = {
        "SR 11-7 MRM Pillar": [
            "Development/Implementation",
            "Validation",
            "Ongoing Monitoring"
        ],
        "NIST AI RMF Function": [
            "Map",
            "Measure",
            "Measure"
        ],
        "Key Aspects & Best Practices": [
            "Identifying AI lifecycle risks (data quality, model bias, system integration flaws, human misuse). Creating risk taxonomies, model cards, and data cards to document purpose, training data, and limitations.",
            "Quantifying risks through rigorous testing and validation (benchmark, scenario-based, backtesting). Developing performance metrics (e.g., $Accuracy$, $F1-Score$) and assessing trustworthiness attributes (e.g., fairness metrics).",
            "Establishing continuous validation processes, ongoing performance checks, and user feedback. Integrating identified risks and controls into a risk register."
        ]
    }
    df = pd.DataFrame(data)
    return df
```

**Code Cell (Execution):**
```python
display_markdown_text("### Mapping SR 11-7 MRM Pillars to NIST AI RMF: Map & Measure Functions")
display(create_sr117_to_nist_map_measure_mapping_table())
```

**Markdown Cell (Explanation for Execution):**
This table demonstrates how the development, validation, and ongoing monitoring activities from SR 11-7 transition into the "Map" and "Measure" functions of NIST AI RMF. It highlights the importance of comprehensive risk identification (Map) and rigorous quantification and assessment of performance and trustworthiness (Measure) using metrics like $Accuracy$ and $F1-Score$.

---

### Section 15: Mapping SR 11-7 MRM to NIST AI RMF: Manage Function

**Markdown Cell:**
## Mapping SR 11-7 MRM to NIST AI RMF: The "Manage" Function

Finally, we map SR 11-7 pillars to the NIST AI RMF's "Manage" function, which focuses on allocating resources and implementing controls to address AI risks.

The **Manage** function involves deploying risk controls, responding to incidents, and continuously improving the AI risk management process.

**Code Cell (Function Implementation):**
```python
def create_sr117_to_nist_manage_mapping_table():
    """
    Generates a pandas DataFrame mapping relevant SR 11-7 MRM pillars to the NIST AI RMF "Manage" function.
    """
    data = {
        "SR 11-7 MRM Pillar": [
            "Ongoing Monitoring",
            "Validation",
            "Development/Implementation"
        ],
        "NIST AI RMF Function": [
            "Manage",
            "Manage",
            "Manage"
        ],
        "Key Aspects & Best Practices": [
            "Implementing continuous validation processes, drift detection, and performance monitoring. Establishing incident reporting and response mechanisms, integrating findings into a risk register, and ensuring accountability and human-in-the-loop oversight.",
            "Utilizing insights from rigorous testing (e.g., adversarial testing, red-teaming) to inform and update mitigation strategies and control measures, including input sanitization and detecting prompt injection.",
            "Integrating risk controls and security measures early in the AI lifecycle, including model supply chain security, access governance, and maintaining an AI Bill of Materials (AI-BOM)."
        ]
    }
    df = pd.DataFrame(data)
    return df
```

**Code Cell (Execution):**
```python
display_markdown_text("### Mapping SR 11-7 MRM Pillars to NIST AI RMF: Manage Function")
display(create_sr117_to_nist_manage_mapping_table())
```

**Markdown Cell (Explanation for Execution):**
This table completes the mapping, showing how SR 11-7's emphasis on ongoing monitoring, validation, and development practices translates into the "Manage" function of NIST AI RMF. It highlights the proactive implementation of controls, continuous monitoring, and adaptive strategies needed to mitigate AI-specific threats.

---

### Section 16: Framework Application to Generative & Agentic AI

**Markdown Cell:**
## Framework Application to Generative & Agentic AI

The principles of SR 11-7 and NIST AI RMF are increasingly vital for managing risks associated with advanced AI paradigms like Generative AI (e.g., LLMs) and Agentic AI systems. These systems introduce heightened complexity and unique challenges that demand adaptive governance.

### Heightened Model Risk

*   Generative and Agentic AI dramatically heighten model risk due to:
    *   **Increased Complexity:** Their intricate architectures and vast parameter spaces make behavior difficult to predict.
    *   **Uncertain Inputs:** Outputs are highly sensitive to prompts and contextual data, often leading to unpredictable responses.
    *   **Wider Application:** Their broad utility across domains amplifies the potential for widespread impact if failures occur.

### Specific Risks of Agentic AI

Agentic AI systems, characterized by autonomy and sequential decision-making, pose specific risks:
*   **Goal Mis-specification:** If an agent's objectives are poorly defined, it can pursue unintended and potentially harmful goals.
*   **Autonomy Creep:** Agents may operate beyond their intended boundaries or without adequate human oversight.
*   **Cross-task Error Propagation:** Errors in one step of an agent's workflow can cascade and amplify through subsequent actions, leading to significant failures.

### Tailored Mitigation and Oversight

*   **Emergent Risks:** LLM hallucinations and societal bias amplification necessitate tailored mitigation strategies and enhanced training data transparency.
*   **Adaptive Governance:** Flexible governance structures are needed to keep pace with rapid AI advancements.
*   **Human-in-the-Loop Oversight:** Essential for novel AI, expanding risk oversight to maintain human final authority and accountability, especially for critical decisions.
*   **Red-teaming and Adversarial Testing:** Rigorous techniques like red-teaming (simulating malicious attacks) and adversarial prompt injection are crucial for identifying vulnerabilities in Generative AI.

**Code Cell (Function Implementation):**
```python
# No specific function to implement for this conceptual section beyond display_markdown_text.
# The focus is on definitions and conceptual explanations.
```

**Code Cell (Execution):**
```python
# No specific function call needed. This cell is intentionally left empty.
```

**Markdown Cell (Explanation for Execution):**
This section discusses the application of SR 11-7 and NIST AI RMF principles to modern generative and agentic AI systems. It highlights the amplified risks and unique challenges these technologies present, emphasizing the need for adaptive governance, specialized testing (like red-teaming), and robust human oversight.

---

### Section 17: Essential AI Assurance Artifacts: Introduction and Model Cards

**Markdown Cell:**
## Essential AI Assurance Artifacts

To operationalize AI risk management and facilitate compliance with frameworks like SR 11-7 and NIST AI RMF, specific documentation artifacts are essential.

### Introduction to AI Assurance Documentation

**AI Assurance Documentation** provides concrete evidence of responsible AI development and deployment practices. These artifacts enhance **transparency** by capturing key facts like purpose, training data, performance metrics, and limitations. They facilitate critical **review and auditing** processes, enabling stakeholders to critically examine AI systems.

Key examples of essential documentation include:
*   **Model Cards**
*   **Data Cards**
*   **Risk Registers**

### Model Cards: AI Model Information Summary

**Model Cards** provide a comprehensive summary of an AI model's key facts, enhancing transparency and accountability. They detail the model's **intended use**, guiding appropriate deployment and preventing misuse.

**Essential components typically include:**
*   **Model Details:** Version, owner, date, intended use cases.
*   **Training Data Characteristics:** Description of the dataset used, its sources, and any preprocessing.
*   **Performance Metrics:** Key metrics (e.g., $Accuracy$, $F1-Score$) reported for various subgroups or conditions, highlighting potential fairness issues.
*   **Fairness Considerations:** Discussion of bias assessments and mitigation strategies.
*   **Known Limitations:** Specific scenarios where the model may perform poorly or fail.
*   **Ethical Implications:** Potential societal impacts or ethical concerns.
*   **Responsible Usage Guidelines:** Recommendations for deployment and monitoring.

This documentation facilitates critical review and auditing, aligning with the principles of SR 11-7's effective challenge and NIST AI RMF's transparency and accountability attributes.

**Code Cell (Function Implementation):**
```python
def create_model_card_example_fields_table():
    """
    Generates a pandas DataFrame illustrating example fields and components of an AI Model Card.
    """
    data = {
        "Model Card Field": [
            "Model Name/ID", "Version", "Owner", "Date Developed",
            "Intended Use Cases", "Out-of-Scope Uses",
            "Training Data Description", "Evaluation Metrics (Overall)",
            "Fairness Metrics/Subgroup Performance", "Known Limitations",
            "Ethical Considerations", "Deployment/Monitoring Guidelines"
        ],
        "Example Content/Purpose": [
            "Financial Fraud Detection Model v1.2", "1.2", "Risk Management Dept.", "2023-10-26",
            "Detecting suspicious credit card transactions.", "Loan application scoring, customer service chatbots.",
            "Synthetic transaction data, anonymized customer profiles (2020-2023).", "Accuracy: 95%, F1-Score: 0.88",
            "Equal Opportunity (False Negative Rate for different demographics).", "May struggle with novel fraud patterns.",
            "Potential for false positives impacting legitimate users; need clear appeal process.", "Continuous monitoring for drift, quarterly re-evaluation."
        ]
    }
    df = pd.DataFrame(data)
    return df
```

**Code Cell (Execution):**
```python
display_markdown_text("### Example Model Card Structure")
display(create_model_card_example_fields_table())
```

**Markdown Cell (Explanation for Execution):**
The example Model Card structure above demonstrates how an AI model's essential information, including its purpose, performance, limitations, and ethical considerations, can be systematically documented. This artifact is crucial for promoting transparency, enabling effective challenge, and demonstrating accountability to stakeholders and regulators.

---

### Section 18: Essential AI Assurance Artifacts: Data Cards

**Markdown Cell:**
## Essential AI Assurance Artifacts: Data Cards

Just as Model Cards document AI models, **Data Cards** are essential for documenting the **provenance** and characteristics of datasets used in AI. They address the critical data risks identified in our taxonomy.

### Key Aspects of Data Cards

*   **Data Provenance and Lineage:** They detail the data collection process, sources, and any labeling methodologies, ensuring transparency regarding where the data came from and how it was prepared. This helps trace potential issues back to their origin.
*   **Dataset Characteristics:** Include descriptions of the data's content, features, size, and any known biases or limitations. This facilitates the identification and documentation of **potential biases** within the data, which is crucial for responsible AI.
*   **Data Quality and Relevance:** Regulators emphasize data quality and relevance as emerging AI risks. Data Cards provide documentation to demonstrate that data used is appropriate for its intended purpose.
*   **Data Privacy and Security:** Information on how sensitive data is handled, anonymization techniques applied, and compliance with privacy regulations (e.g., whether the data is privacy-preserving).

These artifacts contribute to a comprehensive **data inventory**, making data transparent for internal stakeholders, reviewers, and auditors.

**Code Cell (Function Implementation):**
```python
def create_data_card_example_fields_table():
    """
    Generates a pandas DataFrame illustrating example fields and components of an AI Data Card.
    """
    data = {
        "Data Card Field": [
            "Dataset Name/ID", "Version", "Source(s)", "Collection Method",
            "Date Collected/Created", "Last Updated",
            "Data Description", "Number of Samples/Features",
            "Annotation/Labeling Process", "Known Biases/Limitations",
            "Privacy Considerations", "Data Retention Policy"
        ],
        "Example Content/Purpose": [
            "Customer Transaction History", "1.0", "Internal CRM, Third-Party Payment Processor", "Automated API pull, Manual entry",
            "2018-01-01 to 2023-09-30", "2023-10-15",
            "Anonymized transaction details for credit card usage.", "10M rows, 50 features",
            "Fraudulent transactions labeled by human experts.", "Geographical bias towards urban areas; potential underrepresentation of certain demographics.",
            "All PII anonymized; GDPR compliant.", "Data retained for 7 years as per regulatory requirements."
        ]
    }
    df = pd.DataFrame(data)
    return df
```

**Code Cell (Execution):**
```python
display_markdown_text("### Example Data Card Structure")
display(create_data_card_example_fields_table())
```

**Markdown Cell (Explanation for Execution):**
The example Data Card structure highlights the critical information required to document a dataset used in AI development. By detailing provenance, characteristics, biases, and privacy aspects, Data Cards ensure transparency and facilitate the identification and mitigation of data-related risks, aligning with responsible AI practices.

---

### Section 19: Essential AI Assurance Artifacts: Risk Registers

**Markdown Cell:**
## Essential AI Assurance Artifacts: Risk Registers

**Risk Registers** serve as a systematic tool for tracking and managing AI-related hazards throughout their lifecycle. They are dynamic documents that evolve as risks are identified, assessed, and mitigated.

### Key Components of AI Risk Registers

*   **Identified Risks:** Document specific AI hazards across the data, model, system, human, and organizational dimensions.
*   **Potential Impact Ratings:** Assess the severity of consequences if a risk materializes (e.g., Financial, Reputational, Operational, Ethical).
*   **Likelihood Assessments:** Evaluate the probability of a risk occurring.
*   **Mitigation Controls:** Detail associated controls, safeguards, or preventive measures implemented to reduce risk.
*   **Response Plans:** Outline actions to be taken if a risk event occurs (e.g., incident response, rollback procedures).
*   **Evidence of Risk Assessments:** Link to supporting documentation or analysis.
*   **Owner and Status:** Assign responsibility for managing the risk and track its current status (e.g., Open, In Progress, Closed).

This ongoing documentation supports **continuous validation** and ensures **accountability** in AI risk management, providing a clear record for internal oversight and external audits.

**Code Cell (Function Implementation):**
```python
def create_risk_register_example_fields_table():
    """
    Generates a pandas DataFrame illustrating example fields and components of an AI Risk Register.
    """
    data = {
        "Risk Register Field": [
            "Risk ID", "Risk Category", "Risk Description",
            "Potential Impact (Severity)", "Likelihood", "Risk Score (Impact x Likelihood)",
            "Mitigation Controls", "Response Plan", "Owner", "Status", "Date Identified", "Last Review Date"
        ],
        "Example Content/Purpose": [
            "AI-001", "Model (Bias)", "Algorithmic bias leading to discriminatory loan decisions.",
            "High (Reputational, Legal, Financial)", "Medium", "High (3x2 = 6)",
            "Fairness audit; re-weighting training data; human-in-the-loop review for high-risk applications.", "Alert risk team; pause model deployment; initiate remediation plan; notify affected parties.", "Chief Risk Officer", "In Progress", "2023-08-01", "2023-10-20"
        ]
    }
    df = pd.DataFrame(data)
    return df
```

**Code Cell (Execution):**
```python
display_markdown_text("### Example AI Risk Register Structure")
display(create_risk_register_example_fields_table())
```

**Markdown Cell (Explanation for Execution):**
The example AI Risk Register illustrates how organizations can systematically track and manage AI-related hazards. By documenting risks, their potential impact, likelihood, mitigation strategies, and ownership, risk registers provide a clear framework for proactive risk management, continuous monitoring, and demonstrating accountability across the AI lifecycle.

---

### Section 20: Leveraging Assurance Artifacts & Conclusion

**Markdown Cell:**
## Leveraging Assurance Artifacts for Effective Challenge and Audit & Conclusion

AI assurance artifacts—Model Cards, Data Cards, and Risk Registers—are not merely documentation; they are active tools crucial for promoting **effective challenge**, ensuring **regulatory compliance**, and supporting both internal and external **audits** of AI systems.

### Enhancing Transparency and Accountability

*   **Effective Challenge:** These artifacts enable objective and informed review of AI systems by detailing model facts, data provenance, and risk profiles, facilitating stakeholder scrutiny.
*   **Regulatory Compliance:** They provide necessary documentation for demonstrating adherence to regulatory mandates like SR 11-7 and voluntary frameworks like NIST AI RMF.
*   **Transparency:** By openly detailing system components, data sources, and risk assessments, they foster greater understanding and trust.
*   **Accountability:** They reinforce accountability by clearly documenting identified risks, mitigation controls, and evidence of risk assessments, ensuring that responsibility is assigned and traceable.

### Continuous Improvement

Comprehensive documentation supports **continuous improvement** through ongoing monitoring, validation, and feedback loops into risk registers. This iterative process ensures that AI risk management practices adapt and evolve with the AI systems themselves.

## Conclusion

This notebook has explored the foundational aspects of Model Risk Management (SR 11-7) and the comprehensive approach of the NIST AI Risk Management Framework 1.0. We've seen how traditional MRM principles are extended to address emergent AI risks, how risks are taxonomized, and how assurance artifacts are vital for building trustworthy AI.

By integrating the wisdom of SR 11-7 with the forward-looking guidance of NIST AI RMF, organizations can build robust AI governance structures that foster innovation while ensuring safety, fairness, and accountability in the AI era.

**Code Cell (Function Implementation):**
```python
def present_scenario_question(question, discussion_points):
    """
    Displays a scenario question and its associated discussion points in a structured format.
    """
    display_markdown_text(f"### Scenario: {question}")
    display_markdown_text("**Discussion Points:**")
    for point in discussion_points:
        display_markdown_text(f"*   {point}")
    display_markdown_text("---")

# No specific function to implement for this conclusion beyond the scenario presentation.
```

**Code Cell (Execution):**
```python
scenario_q1 = "A financial institution uses an AI model for credit scoring. It performs well on overall accuracy but is found to exhibit lower approval rates for a specific demographic group, despite seemingly neutral input features."
scenario_dp1 = [
    "How would SR 11-7's 'Effective Challenge' principle apply here, and what type of testing would it mandate?",
    "Which NIST AI RMF trustworthiness attributes are primarily violated in this scenario?",
    "What AI assurance artifacts (Model Card, Data Card, Risk Register) would be most critical in identifying and addressing this issue, and what information would they contain?",
    "Discuss potential 'Model Risks' and 'Human-Centric AI Risks' as per the AI Risk Taxonomy in this scenario."
]
present_scenario_question(scenario_q1, scenario_dp1)

scenario_q2 = "An AI-powered chatbot designed for customer support starts generating unhelpful or factually incorrect responses, especially when queried about new product features not explicitly in its training data. This leads to customer frustration and reputational damage."
scenario_dp2 = [
    "How does this situation relate to 'emergent AI risks' like hallucinations and autonomy creep?",
    "Which NIST AI RMF functions (Govern, Map, Measure, Manage) are most relevant for addressing this, and what actions would be taken in each?",
    "What 'System Risks' might be contributing to this problem, particularly if the chatbot integrates with other systems?",
    "How would regular 'Ongoing Monitoring' (SR 11-7) or the 'Measure' function (NIST AI RMF) detect this issue, and what metrics would be used?"
]
present_scenario_question(scenario_q2, scenario_dp2)
```

**Markdown Cell (Explanation for Execution):**
The concluding section summarizes the key takeaways from the notebook, reiterating the importance of integrating traditional model risk management with contemporary AI risk frameworks. The provided scenario-based questions serve as a practical exercise for risk managers to apply the principles and concepts learned, fostering a deeper understanding of how to navigate complex AI risk challenges using both SR 11-7 and NIST AI RMF. Each discussion point encourages reflection on framework applicability, risk identification, and the utility of assurance artifacts in real-world AI scenarios.
