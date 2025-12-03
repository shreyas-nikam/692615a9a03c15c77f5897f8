
import streamlit as st
import pandas as pd

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

def main():
    st.header("Introduction to NIST AI Risk Management Framework (AI RMF 1.0)")
    st.markdown("""
    The National Institute of Standards and Technology (NIST) AI Risk Management Framework (AI RMF 1.0), released in January 2023,
    provides a comprehensive, voluntary framework for managing risks associated with the design, development, deployment, and use of AI systems.
    It is designed to be sector-agnostic and applicable across the entire AI lifecycle.
    """)

    st.subheader("Core Objectives of AI RMF")
    st.markdown("""
    The NIST AI RMF is built around four core functions: **Govern, Map, Measure, and Manage**.
    These functions are continuous and iterative, designed to foster trustworthy AI systems.

    *   **Govern:** Establish a culture of AI risk management, define roles and responsibilities, and ensure accountability.
    *   **Map:** Identify and characterize AI risks, potential impacts, and vulnerabilities throughout the AI lifecycle.
    *   **Measure:** Evaluate, analyze, and track AI risks and the effectiveness of mitigation strategies.
    *   **Manage:** Prioritize, implement, and communicate AI risk mitigation strategies.
    """)

    st.subheader("Trustworthy AI Attributes")
    st.markdown("""
    Central to the NIST AI RMF are the concept of "Trustworthy AI," defined by a set of characteristics or attributes that promote responsible and beneficial AI systems.
    """)

    st.markdown("### Trustworthy AI Attributes: Validity, Reliability, Safety")
    st.dataframe(create_nist_ai_rmf_validity_reliability_safety_attributes_table())

    st.markdown("### Trustworthy AI Attributes: Security, Transparency, Fairness")
    st.dataframe(create_nist_ai_rmf_security_transparency_fairness_attributes_table())

    st.markdown("### Trustworthy AI Attributes: Accountability & Privacy-Preserving")
    st.dataframe(create_nist_ai_rmf_accountability_privacy_attributes_table())

    st.markdown("""
    These attributes provide a holistic view of what makes an AI system trustworthy, extending beyond mere performance metrics to encompass ethical, societal, and operational considerations.
    The AI RMF encourages organizations to integrate these attributes throughout their AI risk management processes.
    """)
