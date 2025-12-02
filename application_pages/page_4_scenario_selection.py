import streamlit as st
import pandas as pd
import numpy as np

# Helper function to generate synthetic scenarios
@st.cache_data(ttl="2h")
def generate_synthetic_scenarios():
    scenarios = [
        {
            "scenario_id": "LLM_001",
            "scenario_description": "A financial advisory LLM provides incorrect investment advice due to hallucinations, leading to client losses.",
            "ai_type": "Generative AI (LLM)",
            "risks": [
                {"risk_name": "Hallucination (Financial Advice)", "baseline_likelihood": 0.5, "baseline_impact_qualitative": "Critical", "baseline_impact_monetary": 5000000},
                {"risk_name": "Data Privacy Breach (Client Info)", "baseline_likelihood": 0.2, "baseline_impact_qualitative": "High", "baseline_impact_monetary": 2000000},
                {"risk_name": "Bias in Investment Recommendations", "baseline_likelihood": 0.4, "baseline_impact_qualitative": "High", "baseline_impact_monetary": 1500000},
                {"risk_name": "Regulatory Non-Compliance", "baseline_likelihood": 0.3, "baseline_impact_qualitative": "Critical", "baseline_impact_monetary": 3000000},
                {"risk_name": "Reputational Damage", "baseline_likelihood": 0.6, "baseline_impact_qualitative": "Critical", "baseline_impact_monetary": 4000000},
            ],
            "mitigations": [
                {"mitigation_name": "Fact-Checking RAG Integration", "applies_to_risks": ["Hallucination (Financial Advice)"], "likelihood_reduction_factor": 0.6, "impact_reduction_factor": 0.3},
                {"mitigation_name": "Enhanced Data Anonymization", "applies_to_risks": ["Data Privacy Breach (Client Info)"], "likelihood_reduction_factor": 0.4, "impact_reduction_factor": 0.2},
                {"mitigation_name": "Bias Detection & Correction Algorithms", "applies_to_risks": ["Bias in Investment Recommendations"], "likelihood_reduction_factor": 0.5, "impact_reduction_factor": 0.25},
                {"mitigation_name": "Human-in-the-Loop Review (Critical Advice)", "applies_to_risks": ["Hallucination (Financial Advice)", "Bias in Investment Recommendations"], "likelihood_reduction_factor": 0.7, "impact_reduction_factor": 0.4},
                {"mitigation_name": "Regular Compliance Audits", "applies_to_risks": ["Regulatory Non-Compliance"], "likelihood_reduction_factor": 0.3, "impact_reduction_factor": 0.15},
                {"mitigation_name": "Public Relations Crisis Plan", "applies_to_risks": ["Reputational Damage"], "likelihood_reduction_factor": 0.1, "impact_reduction_factor": 0.5},
            ]
        },
        {
            "scenario_id": "AGENTIC_002",
            "scenario_description": "An autonomous supply chain optimization agent misinterprets demand signals, leading to significant overstocking and financial loss.",
            "ai_type": "Agentic AI",
            "risks": [
                {"risk_name": "Goal Mis-specification (Overstocking)", "baseline_likelihood": 0.6, "baseline_impact_qualitative": "Critical", "baseline_impact_monetary": 7000000},
                {"risk_name": "Error Propagation (Supply Chain)", "baseline_likelihood": 0.4, "baseline_impact_qualitative": "High", "baseline_impact_monetary": 3000000},
                {"risk_name": "Autonomy Creep (Unintended Actions)", "baseline_likelihood": 0.3, "baseline_impact_qualitative": "High", "baseline_impact_monetary": 2500000},
                {"risk_name": "System Integration Failure", "baseline_likelihood": 0.2, "baseline_impact_qualitative": "Medium", "baseline_impact_monetary": 1000000},
                {"risk_name": "Vendor Lock-in Risk", "baseline_likelihood": 0.1, "baseline_impact_qualitative": "Low", "baseline_impact_monetary": 500000},
            ],
            "mitigations": [
                {"mitigation_name": "Formal Verification of Agent Goals", "applies_to_risks": ["Goal Mis-specification (Overstocking)"], "likelihood_reduction_factor": 0.5, "impact_reduction_factor": 0.2},
                {"mitigation_name": "Hierarchical Control with Human Oversight", "applies_to_risks": ["Error Propagation (Supply Chain)", "Autonomy Creep (Unintended Actions)"], "likelihood_reduction_factor": 0.6, "impact_reduction_factor": 0.3},
                {"mitigation_name": "Rollback & Recovery Protocols", "applies_to_risks": ["Error Propagation (Supply Chain)"], "likelihood_reduction_factor": 0.4, "impact_reduction_factor": 0.4},
                {"mitigation_name": "Interoperability Standards Adherence", "applies_to_risks": ["System Integration Failure"], "likelihood_reduction_factor": 0.3, "impact_reduction_factor": 0.1},
                {"mitigation_name": "Multi-vendor Strategy", "applies_to_risks": ["Vendor Lock-in Risk"], "likelihood_reduction_factor": 0.2, "impact_reduction_factor": 0.15},
            ]
        },
        {
            "scenario_id": "LLM_003",
            "scenario_description": "A medical diagnostic LLM generates incorrect differential diagnoses due to outdated training data, leading to misdiagnosis.",
            "ai_type": "Generative AI (LLM)",
            "risks": [
                {"risk_name": "Outdated Information/Hallucination", "baseline_likelihood": 0.7, "baseline_impact_qualitative": "Critical", "baseline_impact_monetary": 10000000},
                {"risk_name": "Data Bias (Underrepresented Groups)", "baseline_likelihood": 0.4, "baseline_impact_qualitative": "High", "baseline_impact_monetary": 4000000},
                {"risk_name": "Lack of Explainability (Medical Diagnosis)", "baseline_likelihood": 0.5, "baseline_impact_qualitative": "High", "baseline_impact_monetary": 3000000},
                {"risk_name": "Regulatory Fines (Medical Device)", "baseline_likelihood": 0.6, "baseline_impact_qualitative": "Critical", "baseline_impact_monetary": 8000000},
            ],
            "mitigations": [
                {"mitigation_name": "Continuous Model Retraining/Updating", "applies_to_risks": ["Outdated Information/Hallucination"], "likelihood_reduction_factor": 0.6, "impact_reduction_factor": 0.3},
                {"mitigation_name": "Diverse Data Sourcing & Augmentation", "applies_to_risks": ["Data Bias (Underrepresented Groups)"], "likelihood_reduction_factor": 0.5, "impact_reduction_factor": 0.2},
                {"mitigation_name": "XAI (Explainable AI) Integration", "applies_to_risks": ["Lack of Explainability (Medical Diagnosis)"], "likelihood_reduction_factor": 0.3, "impact_reduction_factor": 0.15},
                {"mitigation_name": "Clinical Review by Physicians", "applies_to_risks": ["Outdated Information/Hallucination", "Data Bias (Underrepresented Groups)"], "likelihood_reduction_factor": 0.8, "impact_reduction_factor": 0.5},
                {"mitigation_name": "Compliance Framework for Medical AI", "applies_to_risks": ["Regulatory Fines (Medical Device)"], "likelihood_reduction_factor": 0.4, "impact_reduction_factor": 0.25},
            ]
        }
    ]
    return scenarios

def select_scenario_data(scenario_id, scenarios_list):
    for scenario in scenarios_list:
        if scenario["scenario_id"] == scenario_id:
            return scenario
    return None

def main():
    st.markdown("""
    ## <h2 style="color:#0A2647;">4. Scenario Selection: Setting the Stage</h2>

    The first step in our AI risk management sandbox is to select a specific AI risk scenario to analyze. Each scenario presents a unique set of challenges and potential risks associated with either Generative AI or Agentic AI systems.

    By choosing a scenario, you will load its predefined baseline risks and a set of available mitigation strategies, allowing you to experiment with risk assessment and reduction in a practical context.

    Below is a table outlining the available scenarios. Please select one to proceed with the lab.
    """)

    if "scenarios_data" not in st.session_state:
        st.session_state.scenarios_data = generate_synthetic_scenarios()

    # Prepare data for display
    scenarios_df = pd.DataFrame([
        {
            "scenario_id": s["scenario_id"],
            "scenario_description": s["scenario_description"],
            "ai_type": s["ai_type"]
        }
        for s in st.session_state.scenarios_data
    ])

    st.subheader("Available AI Risk Scenarios")
    st.dataframe(scenarios_df, use_container_width=True, hide_index=True)

    scenario_options = scenarios_df["scenario_id"].tolist()

    # Set default if not already selected
    if "selected_scenario_id" not in st.session_state or st.session_state.selected_scenario_id not in scenario_options:
        st.session_state.selected_scenario_id = scenario_options[0] if scenario_options else None

    selected_scenario_id = st.selectbox(
        label="Select an AI Risk Scenario",
        options=scenario_options,
        index=scenario_options.index(st.session_state.selected_scenario_id) if st.session_state.selected_scenario_id else 0,
        key="scenario_selector",
        help="Choose a scenario to load its baseline risks and available mitigations."
    )

    if selected_scenario_id:
        if st.session_state.selected_scenario_id != selected_scenario_id:
            st.session_state.selected_scenario_id = selected_scenario_id
            # Clear other session states when scenario changes to ensure a fresh start for the new scenario
            st.session_state.pop("baseline_risks_df", None)
            st.session_state.pop("available_mitigations_df", None)
            st.session_state.pop("user_selected_mitigation_names", None)
            st.session_state.pop("user_selected_mitigations_details", None)
            st.session_state.pop("mitigated_risks_df", None)

        st.session_state.selected_scenario_data = select_scenario_data(
            st.session_state.selected_scenario_id, 
            st.session_state.scenarios_data
        )

        st.success(f"Scenario \"{st.session_state.selected_scenario_id}\" selected. Proceed to the next sections to identify baseline risks and propose mitigations.")
    else:
        st.warning("Please select a scenario to continue.")
