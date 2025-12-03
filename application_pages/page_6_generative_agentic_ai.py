
import streamlit as st

def main():
    st.header("Framework Application to Generative & Agentic AI")
    st.markdown("""
    The advent of Generative AI (e.g., Large Language Models - LLMs) and Agentic AI systems introduces a new frontier in AI risk management.
    While SR 11-7 and NIST AI RMF provide foundational principles, these advanced AI paradigms necessitate tailored considerations and mitigation strategies.
    """)

    st.subheader("Heightened Model Risk with Generative AI")
    st.markdown("""
    Generative AI models, due to their emergent capabilities and less predictable outputs, introduce heightened model risks:

    *   **Hallucinations & Factual Inaccuracy:** LLMs can generate plausible-sounding but incorrect or fabricated information.
    *   **Misinformation & Disinformation:** Potential for generating and spreading harmful or deceptive content at scale.
    *   **Intellectual Property (IP) Infringement:** Generative models trained on vast datasets may reproduce copyrighted material.
    *   **Bias Propagation:** Can perpetuate and amplify societal biases present in their training data, leading to unfair outputs.
    *   **Data Leakage/Privacy Concerns:** Risk of inadvertently revealing sensitive information from training data.
    *   **Adversarial Prompting/Prompt Injection:** Malicious inputs designed to manipulate the model's behavior or extract sensitive information.
    """)

    st.subheader("Specific Risks of Agentic AI")
    st.markdown("""
    Agentic AI systems, capable of autonomous decision-making and action, introduce further complexities:

    *   **Loss of Control:** Difficulty in establishing clear boundaries and ensuring human oversight over autonomous actions.
    *   **Emergent Behaviors:** Unpredictable and unintended behaviors arising from complex interactions within the environment.
    *   **Ethical Dilemmas:** Agents making decisions in ethically ambiguous situations without human intervention.
    *   **Safety Criticality:** High stakes when agents operate in physical environments or make irreversible decisions.
    *   **Dependency Risks:** Over-reliance on agents can lead to critical failures if the agent malfunctions or is compromised.
    """)

    st.subheader("Tailored Mitigation and Oversight")
    st.markdown("""
    Managing risks in Generative and Agentic AI requires a combination of traditional MRM principles and new, AI-specific approaches:

    *   **Enhanced Prompt Engineering & Guardrails:** Developing robust prompt engineering techniques and implementing explicit content filters and guardrails to control model outputs.
    *   **Human-in-the-Loop & Human-on-the-Loop:** Designing systems where humans retain ultimate control, either by actively reviewing outputs (in-the-loop) or monitoring performance with intervention capabilities (on-the-loop).
    *   **Rigorous Red Teaming:** Proactively testing AI systems for vulnerabilities, biases, and unintended behaviors using adversarial techniques.
    *   **Transparency & Explainability:** Investing in methods to understand model reasoning and output generation, even for complex generative models.
    *   **Continuous Monitoring & Drift Detection:** Implementing sophisticated monitoring for changes in output quality, factual accuracy, and alignment with intended behavior.
    *   **AI Bill of Materials (AI-BOM) & Supply Chain Security:** Documenting all components of an AI system, including third-party models and datasets, and managing supply chain risks.
    *   **Clear Accountability Frameworks:** Establishing who is responsible for AI actions and outcomes, especially for autonomous agents.
    *   **Ethical AI Review Boards:** Incorporating independent ethical review during the design and deployment phases.

    By adapting and extending the principles of SR 11-7 and NIST AI RMF, organizations can build a more resilient and responsible approach to managing the risks of advanced AI systems.
    """)
