
import streamlit as st
import pandas as pd

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

def main():
    st.header("The Imperative of AI Risk Management")
    st.markdown("""
    The rapid adoption of Artificial Intelligence (AI) across industries presents unprecedented opportunities but also introduces novel and complex risks.
    Traditional risk management frameworks, while foundational, often fall short in addressing the unique challenges posed by AI systems,
    especially large-scale generative models and autonomous agents.
    This section delves into the critical need for specialized AI risk management and introduces a comprehensive taxonomy to categorize these emergent risks.
    """)

    st.subheader("Emergent AI Risks")
    st.markdown("""
    As AI systems become more sophisticated and integrated into critical applications, new categories of risks emerge:

    *   **Bias Amplification:** AI models can learn and even amplify biases present in training data, leading to unfair or discriminatory outcomes.
    *   **Lack of Explainability (Opacity):** The "black box" nature of complex AI models makes it difficult to understand their decision-making process, hindering auditing and accountability.
    *   **Adversarial Attacks:** Malicious actors can manipulate AI inputs to force erroneous or harmful outputs, compromising system integrity.
    *   **Systemic Risks:** Widespread deployment of similar AI models can lead to correlated failures with broad societal and economic impacts.
    *   **Loss of Human Oversight:** Over-reliance on autonomous AI systems can diminish human judgment and control, leading to unintended consequences.
    """)

    st.subheader("Five Key Dimensions of AI Risk")
    st.markdown("Understanding AI risks requires a systematic approach. We categorize AI risks across five key dimensions:")
    st.markdown(create_ai_risk_taxonomy_diagram_text())

    st.subheader("AI Risk Taxonomy: Deep Dive")

    st.markdown("### Data Risks: Quality, Provenance, and Privacy")
    st.markdown("""
    Data is the lifeblood of AI, and its characteristics directly influence model performance and fairness. Key data risks include:

    *   **Data Quality:** Inaccurate, incomplete, or noisy data can lead to erroneous model outputs.
    *   **Data Provenance:** Lack of transparency regarding data origin and collection methods can obscure embedded biases or legal/ethical concerns.
    *   **Data Privacy:** AI systems often process sensitive personal information, raising concerns about data breaches and misuse.
    *   **Data Bias:** Skewed or unrepresentative datasets can lead to models that perform poorly or unfairly for certain demographic groups.
    """)

    st.markdown("### Model Risks: Bias, Accuracy, and Robustness")
    st.markdown("""
    Model risks stem from the design, training, and inherent properties of the AI algorithm itself:

    *   **Algorithmic Bias:** Beyond data bias, inherent algorithmic choices or optimization objectives can introduce or amplify unfairness.
    *   **Inaccuracy:** Models that fail to meet performance benchmarks or make incorrect predictions can lead to operational failures.
    *   **Lack of Robustness:** Models sensitive to minor input perturbations (e.g., adversarial examples) are unreliable in real-world conditions.
    *   **Lack of Interpretability/Explainability:** Difficulty in understanding why a model makes certain predictions complicates auditing, debugging, and user trust.
    *   **Concept Drift/Model Decay:** Over time, the relationship between inputs and outputs can change, degrading model performance if not continuously monitored.
    """)

    st.markdown("### AI Risk Taxonomy: System, Human, and Organizational Risks")

    st.markdown("### System Risks: Integration, Architecture, and Supply Chain")
    st.markdown("""
    AI systems do not operate in isolation. They are part of larger technical ecosystems, introducing system-level risks:

    *   **Integration Risks:** Challenges in integrating AI components with existing IT infrastructure, leading to compatibility issues or unexpected behaviors.
    *   **Architectural Vulnerabilities:** Flaws in system design that create security gaps or performance bottlenecks.
    *   **Supply Chain Risks:** Dependencies on third-party AI models, data providers, or infrastructure can introduce vulnerabilities (e.g., unvetted components, data poisoning).
    *   **Cybersecurity Risks:** AI systems can be targets for or enablers of advanced cyber attacks.
    """)

    st.markdown("### Human-Centric AI Risks: Misuse, Over-Reliance, and Oversight")
    st.markdown("""
    The human element is crucial throughout the AI lifecycle. Risks arise from how humans interact with and manage AI:

    *   **Misuse/Malicious Use:** Intentional deployment of AI for harmful purposes (e.g., surveillance, misinformation).
    *   **Over-Reliance/Automation Bias:** Humans over-trusting or over-relying on AI outputs, potentially ignoring contradictory evidence or their own judgment.
    *   **Loss of Oversight/Control:** Lack of effective human monitoring or intervention mechanisms, especially in autonomous AI systems.
    *   **Misinterpretation of AI Outputs:** Users misunderstanding AI predictions or explanations, leading to incorrect decisions.
    """)

    st.markdown("### Organizational AI Risk: Governance, Policy, and Culture")
    st.markdown("""
    Effective AI risk management requires robust organizational structures, policies, and a supportive culture:

    *   **Lack of Governance:** Absence of clear policies, roles, and responsibilities for AI development, deployment, and oversight.
    *   **Policy Gaps:** Inadequate internal policies or external regulations to address emergent AI risks.
    *   **Cultural Resistance:** Organizational culture that resists responsible AI practices, transparency, or ethical considerations.
    *   **Accountability Deficits:** Unclear lines of accountability for AI system failures or harmful outcomes.
    *   **Resource Constraints:** Insufficient investment in skilled personnel, tools, or processes for AI risk management.
    """)

    st.markdown("### Interconnected AI Risks & Emerging Threats")
    st.markdown("""
    It's critical to recognize that these risk dimensions are not isolated but often interconnected. A data bias, for example, can lead to model bias, which then contributes to human misuse, ultimately posing an organizational risk.
    Furthermore, the rapid evolution of AI, particularly with large language models (LLMs) and agentic AI, introduces emerging threats:

    *   **Generative AI Risks:** Hallucinations, misinformation generation, intellectual property infringement, deepfakes.
    *   **Agentic AI Risks:** Unintended autonomous actions, loss of control, emergent behaviors, ethical dilemmas in decision-making.

    Effective AI risk management necessitates a holistic and adaptive approach to address this complex and evolving landscape.
    """)

    st.subheader("Conceptual Metrics for AI Risk")

    st.markdown(r"Demographic Parity: $P(\hat{Y}=1 | A=a) = P(\hat{Y}=1 | A=b)$")
    st.markdown(r"Equalized Odds: $P(\hat{Y}=1 | Y=y, A=a) = P(\hat{Y}=1 | Y=y, A=b)$")
    st.markdown(r"$$Accuracy = \frac{\text{True Positives} + \text{True Negatives}}{\text{Total Samples}}$$")
    st.markdown(r"$$F1-Score = 2 \times \frac{Precision \times Recall}{Precision + Recall}$$")
