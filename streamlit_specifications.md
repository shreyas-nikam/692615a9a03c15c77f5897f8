# Streamlit Application Specification: AI Framework Comparator: SR 11-7 vs. NIST AI RMF

## 1. Application Overview

**Application Name:** AI Framework Comparator: SR 11-7 vs. NIST AI RMF
**Target Audience (Persona):** Risk Manager

**Purpose:** This application is designed to clarify the relationship and complementary nature of SR 11-7 and the NIST AI Risk Management Framework (AI RMF 1.0). It aims to provide Risk Managers with a deeper understanding of the evolution from traditional model risk management to comprehensive AI assurance, highlighting key differences, shared objectives, and practical integration points for robust AI governance.

**Learning Goals:**
*   To understand AI risk and assurance in the context of large-scale AI systems, including Large Language Models (LLMs) and agentic architectures.
*   To review and comprehend Model Risk Management (MRM) principles as outlined in SR 11-7.
*   To categorize AI risks systematically using a multidimensional taxonomy (Data, Model, System, Human, Organizational).
*   To explore and understand the NIST AI Risk Management Framework (AI RMF 1.0) and its core objectives and trustworthiness attributes.
*   To apply SR 11-7 and NIST AI RMF principles to generative and agentic AI systems, including identifying life cycle risks and tailored mitigation strategies.
*   To develop and understand essential AI assurance artifacts (Model Cards, Data Cards, Risk Registers).
*   To trace the evolution of assurance practices from traditional MRM to comprehensive AI assurance.

## 2. User Interface Requirements

The application will be structured as a single-page interactive experience with clear sectional dividers and a persistent sidebar for primary navigation, ensuring easy access to different content areas.

### Layout and Navigation Structure

*   **Sidebar (`st.sidebar`):** Will contain main navigation links, acting as a table of contents for the application's sections.
    *   Home/Introduction
    *   The Imperative of AI Risk Management
    *   Foundations of SR 11-7
    *   AI Risk Taxonomy Deep Dive
    *   Introduction to NIST AI RMF
    *   Trustworthy AI Attributes
    *   Framework Comparison & Interactive Mapping
    *   Framework Application to Generative & Agentic AI
    *   Essential AI Assurance Artifacts
*   **Main Content Area:**
    *   Will display content dynamically based on sidebar selection.
    *   Sections will be clearly titled using `st.header` and `st.subheader`.
    *   `st.columns` will be used where side-by-side content or comparative analysis is required (e.g., for interactive mapping).

### Input Widgets and Controls

*   **Interactive Framework Comparator (`st.radio` / `st.selectbox`):**
    *   Within the "Framework Comparison & Interactive Mapping" section, users will find a selection widget (e.g., `st.radio` or `st.selectbox`) presenting key SR 11-7 elements:
        *   Model Definition
        *   Risk Amplification
        *   Effective Challenge
        *   Model Risk Governance
        *   Model Lifecycle Management (represented by Development/Implementation, Validation, Ongoing Monitoring pillars).
    *   **"Clicking" on an SR 11-7 element (via selection) must trigger automatic highlighting of corresponding functions and attributes within the NIST AI RMF section.** This will be implemented by dynamically updating the display in the adjacent column or below the selection, highlighting relevant rows in mapping tables and relevant trustworthiness attribute definitions.

### Visualization Components

*   **Structured Text:** All introductory, explanatory, and conceptual content will be rendered using `st.markdown`, maintaining the original markdown formatting from the Jupyter Notebook.
*   **Tables:** All tabular data (e.g., SR 11-7 pillars, framework comparisons, mapping tables, example Model Card/Data Card/Risk Register fields) will be displayed using `st.dataframe` or `st.table` for clear, readable presentation.
*   **Text-based AI Risk Taxonomy:** The "Five Key Dimensions of AI Risk" will be presented as a structured list within `st.markdown`.
*   **Interactive Highlighting:** For the comparative section, specific rows or cells within `st.dataframe` or `st.markdown` blocks will be visually emphasized (e.g., with bold text, different background color using custom CSS embedded via `st.markdown` with `unsafe_allow_html=True`, or `st.info` blocks) based on user selections in the SR 11-7 component.
*   **Performance and Fairness Metrics:** Mathematical formulas for metrics like Accuracy, F1-Score, Demographic Parity, and Equalized Odds will be displayed using `st.markdown` with appropriate LaTeX formatting.

## 3. Additional Requirements

*   **Annotation and Tooltip Specifications:**
    *   For definitions and explanations of key concepts (e.g., emergent AI risks, trustworthiness attributes), `st.expander` widgets will be used. When a user clicks on a concept, an expander will reveal its detailed definition or explanation.
    *   For shorter definitions or quick clarifications, `st.info` boxes can be employed adjacent to the concept.
*   **State Management:** `st.session_state` will be utilized to preserve the selections made by the user in input widgets (e.g., the chosen SR 11-7 pillar in the interactive comparator) across application reruns, ensuring changes are not lost and maintaining a consistent user experience.

## 4. Notebook Content and Code Requirements

All textual content from the Jupyter Notebook's markdown cells will be directly incorporated into the Streamlit application using `st.markdown`. Python functions designed to generate pandas DataFrames will be called and displayed using `st.dataframe`.

### Extracted Code Stubs and Usage

1.  **Introduction and Overview:**
    *   Markdown content for "AI Framework Comparator: SR 11-7 vs. NIST AI RMF", "Introduction", "Module Overview and Learning Objectives" will be rendered directly via `st.markdown`.
    *   No specific code stubs for this section other than `st.markdown`.

2.  **The Imperative of AI Risk Management & AI Risk Taxonomy:**
    *   Markdown content for "The Imperative of AI Risk Management", "Emergent AI Risks", "Five Key Dimensions of AI Risk".
    *   **Code Stub:**
        ```python
        def create_ai_risk_taxonomy_diagram_text():
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
    *   **Streamlit Usage:** `st.markdown(create_ai_risk_taxonomy_diagram_text())`

3.  **Foundations of Model Risk Management (SR 11-7):**
    *   Markdown content for "Foundations of Model Risk Management (SR 11-7)", "Core Principles and Pillars of SR 11-7".
    *   **Code Stub:**
        ```python
        def create_sr117_pillars_table():
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
    *   **Streamlit Usage:**
        `st.subheader("SR 11-7 Model Risk Management (MRM) Pillars")`
        `st.dataframe(create_sr117_pillars_table())`

4.  **Broadening Model Definition & Risk Tiering:**
    *   Markdown content for "Broadening Model Definition & Risk Tiering".
    *   **Code Stub:**
        ```python
        def create_sr117_modern_frameworks_comparison_table():
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
    *   **Streamlit Usage:**
        `st.subheader("SR 11-7 vs. Modern AI Frameworks: A Comparative View")`
        `st.dataframe(create_sr117_modern_frameworks_comparison_table())`

5.  **AI Risk Taxonomy: Deep Dive (Data, Model, System, Human, Organizational Risks):**
    *   Markdown content for "AI Risk Taxonomy: Deep Dive", "Data Risks: Quality, Provenance, and Privacy", "Model Risks: Bias, Accuracy, and Robustness", "AI Risk Taxonomy: System, Human, and Organizational Risks", "System Risks: Integration, Architecture, and Supply Chain", "Human-Centric AI Risks: Misuse, Over-Reliance, and Oversight", "Organizational AI Risk: Governance, Policy, and Culture", "Interconnected AI Risks & Emerging Threats".
    *   **Conceptual Metrics (via `st.markdown` with LaTeX):**
        *   Demographic Parity: `$P(\hat{Y}=1 | A=a) = P(\hat{Y}=1 | A=b)$`
        *   Equalized Odds: `$P(\hat{Y}=1 | Y=y, A=a) = P(\hat{Y}=1 | Y=y, A=b)$`
        *   Accuracy (display equation): `$$Accuracy = \frac{\text{True Positives} + \text{True Negatives}}{\text{Total Samples}}$$`
        *   F1-Score (display equation): `$$F1-Score = 2 \times \frac{Precision \times Recall}{Precision + Recall}$$`
    *   No specific DataFrame generation for this section beyond the general markdown display of definitions and formulas.

6.  **Introduction to NIST AI Risk Management Framework (AI RMF 1.0) & Trustworthy AI Attributes:**
    *   Markdown content for "Introduction to NIST AI Risk Management Framework (AI RMF 1.0)", "Core Objectives of AI RMF", "Trustworthy AI Attributes: Validity, Reliability, Safety", "Trustworthy AI Attributes: Security, Transparency, Fairness", "Trustworthy AI Attributes: Accountability & Privacy-Preserving".
    *   **Code Stubs:**
        ```python
        def create_nist_ai_rmf_validity_reliability_safety_attributes_table():
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

        def create_nist_ai_rmf_security_transparency_fairness_attributes_table():
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

        def create_nist_ai_rmf_accountability_privacy_attributes_table():
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
    *   **Streamlit Usage:**
        `st.subheader("Key Trustworthy AI Attributes (Part 1)")`
        `st.dataframe(create_nist_ai_rmf_validity_reliability_safety_attributes_table())`
        `st.subheader("Key Trustworthy AI Attributes (Part 2)")`
        `st.dataframe(create_nist_ai_rmf_security_transparency_fairness_attributes_table())`
        `st.subheader("Key Trustworthy AI Attributes (Part 3)")`
        `st.dataframe(create_nist_ai_rmf_accountability_privacy_attributes_table())`

7.  **Complementary Frameworks: SR 11-7 & NIST AI RMF (Comparative Section):**
    *   Markdown content for "Complementary Frameworks: SR 11-7 & NIST AI RMF", "Distinct Scopes", "Shared Objectives", "Integration Benefits".
    *   **Code Stub:**
        ```python
        def create_sr117_nist_comparison_summary_table():
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
    *   **Streamlit Usage:**
        `st.subheader("SR 11-7 vs. NIST AI RMF: Summary Comparison")`
        `st.dataframe(create_sr117_nist_comparison_summary_table())`

8.  **Mapping SR 11-7 MRM to NIST AI RMF (Interactive Mapping):**
    *   Markdown content for "Mapping SR 11-7 MRM to NIST AI RMF: The 'Govern' Function", "Mapping SR 11-7 MRM to NIST AI RMF: The 'Map' & 'Measure' Functions", "Mapping SR 11-7 MRM to NIST AI RMF: The 'Manage' Function".
    *   **Code Stubs:**
        ```python
        def create_sr117_to_nist_govern_mapping_table():
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

        def create_sr117_to_nist_map_measure_mapping_table():
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

        def create_sr117_to_nist_manage_mapping_table():
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
    *   **Streamlit Usage (Interactive Component):**
        *   An `st.radio` or `st.selectbox` will list SR 11-7 pillars/principles.
        *   Based on the selection, a dynamic display will be rendered. This involves:
            *   Conditionally displaying and highlighting rows in the `create_sr117_to_nist_govern_mapping_table()`, `create_sr117_to_nist_map_measure_mapping_table()`, and `create_sr117_to_nist_manage_mapping_table()` results. For instance, if "Model Governance" is selected, the corresponding row in `create_sr117_to_nist_govern_mapping_table()` will be formatted (e.g., `st.dataframe(df.style.apply(highlight_row, axis=1))`).
            *   Displaying definitions for relevant NIST AI RMF trustworthiness attributes using `st.expander` or `st.info` blocks, dynamically chosen based on the selected SR 11-7 element.
            *   `st.markdown("### Mapping SR 11-7 MRM Pillars to NIST AI RMF: Govern Function")`
            *   `st.dataframe(create_sr117_to_nist_govern_mapping_table())` (with highlighting logic)
            *   Similar for Map & Measure, and Manage functions.

9.  **Framework Application to Generative & Agentic AI:**
    *   Markdown content for "Framework Application to Generative & Agentic AI", "Heightened Model Risk", "Specific Risks of Agentic AI", "Tailored Mitigation and Oversight".
    *   No specific code stubs for this section.

10. **Essential AI Assurance Artifacts:**
    *   Markdown content for "Essential AI Assurance Artifacts", "Introduction to AI Assurance Documentation", "Model Cards: AI Model Information Summary", "Essential AI Assurance Artifacts: Data Cards", "Essential AI Assurance Artifacts: Risk Registers".
    *   **Code Stubs:**
        ```python
        def create_model_card_example_fields_table():
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

        def create_data_card_example_fields_table():
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

        def create_risk_register_example_fields_table():
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
    *   **Streamlit Usage:**
        `st.subheader("Example Model Card Structure")`
        `st.dataframe(create_model_card_example_fields_table())`
        `st.subheader("Example Data Card Structure")`
        `st.dataframe(create_data_card_example_fields_table())`
        `st.subheader("Example AI Risk Register Structure")`
        `st.dataframe(create_risk_register_example_fields_table())`

The application will consolidate all markdown content and DataFrame generation from the Jupyter Notebook into a cohesive, interactive Streamlit experience, ensuring adherence to all specified formatting and functional requirements.