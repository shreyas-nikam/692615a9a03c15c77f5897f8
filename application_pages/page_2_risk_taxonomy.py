import streamlit as st

def main():
    st.markdown("""
    ## <h2 style=\"color:#0A2647;\">2. AI Risk Taxonomy: Understanding the Dimensions</h2>

    AI risks are multifaceted and can manifest across various stages of the AI lifecycle and operational deployment. A structured taxonomy helps in systematically identifying, assessing, and managing these risks.

    We categorize AI risks into the following primary dimensions:

    ### 2.1 Data-Centric Risks
    These risks originate from the data used to train, validate, and operate AI models.

    *   **Data Quality Issues:**
        *   **Bias:** Systematic errors in the data that lead to unfair or discriminatory outcomes (e.g., historical biases in training data reflecting societal inequalities).
        *   **Noise/Errors:** Inaccuracies, inconsistencies, or outliers in the data that can degrade model performance and reliability.
        *   **Incompleteness:** Missing data points that can lead to biased or ineffective models.
    *   **Data Privacy & Security:**
        *   **Sensitive Data Exposure:** Accidental or malicious leakage of personal identifiable information (PII) or confidential data.
        *   **Inference Attacks:** Techniques to deduce sensitive training data from model outputs.
    *   **Data Drift/Shift:**
        *   **Concept Drift:** The statistical properties of the target variable, which the model is trying to predict, change over time.
        *   **Covariate Shift:** The distribution of the input variables changes between the training and production environments.

    ### 2.2 Model-Centric Risks
    These risks are inherent to the AI model itself, its design, training, and operational characteristics.

    *   **Performance & Reliability:**
        *   **Inaccuracy:** Model making incorrect predictions or classifications.
        *   **Robustness Issues:** Model's susceptibility to small perturbations in input data (e.g., adversarial attacks).
        *   **Scalability:** Model's inability to handle increased data volume or user load efficiently.
    *   **Explainability & Interpretability:**
        *   **Black Box Nature:** Inability to understand why a model made a particular decision, hindering auditing and accountability.
    *   **Hallucinations (Generative AI Specific):**
        *   **Factual Inaccuracy:** Generative models producing content that is factually incorrect or nonsensical, presented as truth.
        *   **Confabulation:** Creating believable but false information.

    ### 2.3 System-Centric Risks
    These risks arise from the integration of AI models into broader technical systems and infrastructure.

    *   **Integration Failures:**
        *   **Compatibility Issues:** Problems arising from AI models not seamlessly integrating with existing IT infrastructure.
        *   **Dependency Risks:** Vulnerabilities introduced by relying on external libraries, APIs, or data sources.
    *   **Scalability & Latency:**
        *   **System Overload:** Inability of the entire system to handle demand, leading to service degradation or failure.
    *   **Security Vulnerabilities:**
        *   **Model Poisoning:** Malicious alteration of training data to compromise model integrity.
        *   **Adversarial Attacks:** Specially crafted inputs designed to trick a model into making errors.

    ### 2.4 Human-Centric Risks
    These risks relate to how humans interact with, understand, and are affected by AI systems.

    *   **Misuse & Malicious Use:**
        *   **Intentional Harm:** Using AI for harmful purposes (e.g., autonomous weapons, deepfakes for misinformation).
        *   **Unintended Consequences:** AI systems leading to unexpected negative outcomes due to unforeseen human interaction patterns.
    *   **Loss of Human Oversight/Control (Agentic AI Specific):**
        *   **Autonomy Creep:** AI systems gradually gaining more control or making decisions without adequate human review.
        *   **Goal Mis-specification:** AI pursuing objectives that, while technically aligned with its programming, lead to undesirable real-world outcomes from a human perspective.
        *   **Error Propagation:** Small errors or misinterpretations by an agentic AI cascading into significant system failures due to autonomous actions.
    *   **Bias & Fairness:**
        *   **Algorithmic Discrimination:** AI systems perpetuating or amplifying societal biases, leading to unfair treatment of certain groups.

    ### 2.5 Organizational Risks
    These risks pertain to the organizational structures, processes, and governance surrounding AI development and deployment.

    *   **Regulatory & Compliance Risks:**
        *   **Non-compliance:** Failure to adhere to relevant laws, regulations, and ethical guidelines (e.g., GDPR, AI Act).
        *   **Reputational Damage:** Negative public perception or loss of trust due to AI failures or ethical breaches.
    *   **Governance & Accountability:**
        *   **Lack of Clear Roles:** Ambiguity in who is responsible for AI system performance, errors, or ethical implications.
        *   **Insufficient Audit Trails:** Inability to trace AI decisions and actions for accountability purposes.
    *   **Economic & Societal Impact:**
        *   **Job Displacement:** AI automation leading to significant changes in employment landscapes.
        *   **Market Manipulation:** AI systems being used to unfairly influence markets.
    """))