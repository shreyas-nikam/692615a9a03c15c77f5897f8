import streamlit as st
import pandas as pd

def calculate_cost_of_failure(likelihood, monetary_impact):
    return likelihood * monetary_impact

def display_baseline_risk_details(scenario_data):
    if scenario_data and "risks" in scenario_data:
        risks_df = pd.DataFrame(scenario_data["risks"])
        risks_df["baseline_cost_of_failure"] = risks_df.apply(
            lambda row: calculate_cost_of_failure(row["baseline_likelihood"], row["baseline_impact_monetary"]),
            axis=1
        )
        # Reorder columns for better readability
        risks_df = risks_df[[
            "risk_name",
            "baseline_likelihood",
            "baseline_impact_qualitative",
            "baseline_impact_monetary",
            "baseline_cost_of_failure"
        ]]
        return risks_df
    return pd.DataFrame()

def main():
    st.markdown("""
    ## <h2 style="color:#0A2647;">5. Identifying and Assessing Baseline Risks</h2>

    Once a scenario is selected, the next critical step is to identify and assess the baseline risks associated with it. This involves understanding the inherent likelihood and potential impact of various risk events before any mitigation strategies are applied.

    In this section, we will display the predefined risks for the chosen scenario, including their estimated likelihood, qualitative impact, monetary impact, and the calculated **Cost of Failure**.

    The **Cost of Failure ($C_F$)** is calculated as:
    $$C_F = P(Risk) \times Impact_{Monetary}$$

    This metric helps in quantifying the expected financial loss if a risk materializes, providing a basis for prioritizing risks.
    """)

    if "selected_scenario_data" in st.session_state and st.session_state.selected_scenario_data:
        st.subheader(f"Baseline Risks for Scenario: {st.session_state.selected_scenario_data['scenario_id']}")

        baseline_risks_df = display_baseline_risk_details(st.session_state.selected_scenario_data)

        if not baseline_risks_df.empty:
            st.dataframe(baseline_risks_df, use_container_width=True, hide_index=True)
            st.session_state.baseline_risks_df = baseline_risks_df
            st.success("Baseline risks loaded and calculated. You can now proceed to visualize them.")
        else:
            st.warning("No baseline risks found for the selected scenario.")
            st.session_state.baseline_risks_df = pd.DataFrame() # Ensure it's an empty DataFrame
    else:
        st.info("Please select a scenario in the '4. Scenario Selection' page to view baseline risks.")