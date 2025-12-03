
import streamlit as st
import pandas as pd

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

def main():
    st.header("Foundations of Model Risk Management (SR 11-7)")
    st.markdown("""
    SR 11-7, officially titled "Guidance on Model Risk Management," was issued by the Federal Reserve and the Office of the Comptroller of the Currency (OCC) in 2011.
    While primarily aimed at banking organizations to manage the risks associated with financial models, its principles provide a foundational understanding for managing risks in any sophisticated analytical system, including AI.
    """)

    st.subheader("Core Principles and Pillars of SR 11-7")
    st.markdown("""
    SR 11-7 outlines three core pillars for effective model risk management:

    1.  **Governance:** Strong oversight by senior management and the board of directors, clear policies, and defined roles and responsibilities.
    2.  **Validation:** Independent and robust validation of models to assess their conceptual soundness, implementation, and ongoing performance.
    3.  **Model Development and Use:** Sound practices for model design, implementation, and use, coupled with comprehensive documentation.

    These pillars are often broken down into specific operational areas:
    """)
    st.dataframe(create_sr117_pillars_table())

    st.subheader("Broadening Model Definition & Risk Tiering")
    st.markdown("""
    While SR 11-7 focused on quantitative models, the spirit of its guidance can be extended to AI. However, the definition of "model" and the approach to risk tiering need to evolve.
    """)

    st.markdown("### SR 11-7 vs. Modern AI Frameworks: A Comparative View")
    st.dataframe(create_sr117_modern_frameworks_comparison_table())

    st.markdown("""
    In essence, while SR 11-7 provides a robust foundation, AI