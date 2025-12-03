
import streamlit as st

def main():
    st.header("AI Framework Comparator: SR 11-7 vs. NIST AI RMF")
    st.markdown("""
    In this lab, we will clarify the relationship and complementary nature of SR 11-7 and the NIST AI Risk Management Framework (AI RMF 1.0).
    It aims to provide Risk Managers with a deeper understanding of the evolution from traditional model risk management to comprehensive AI assurance,
    highlighting key differences, shared objectives, and practical integration points for robust AI governance.
    """)

    st.subheader("Module Overview and Learning Objectives")
    st.markdown("""
    *   To understand AI risk and assurance in the context of large-scale AI systems, including Large Language Models (LLMs) and agentic architectures.
    *   To review and comprehend Model Risk Management (MRM) principles as outlined in SR 11-7.
    *   To categorize AI risks systematically using a multidimensional taxonomy (Data, Model, System, Human, Organizational).
    *   To explore and understand the NIST AI Risk Management Framework (AI RMF 1.0) and its core objectives and trustworthiness attributes.
    *   To apply SR 11-7 and NIST AI RMF principles to generative and agentic AI systems, including identifying life cycle risks and tailored mitigation strategies.
    *   To develop and understand essential AI assurance artifacts (Model Cards, Data Cards, Risk Registers).
    *   To trace the evolution of assurance practices from traditional MRM to comprehensive AI assurance.
    """)
