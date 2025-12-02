import streamlit as st
import pandas as pd

def reset_current_scenario_state():
    # Clear relevant session state variables to reset the application flow
    for key in [
        "selected_scenario_id",
        "selected_scenario_data",
        "baseline_risks_df",
        "available_mitigations_df",
        "user_selected_mitigation_names",
        "user_selected_mitigations_details",
        "mitigated_risks_df"
    ]:
        if key in st.session_state:
            del st.session_state[key]
    
    # Re-initialize scenarios_data if it was cleared for some reason, though @st.cache_data should handle it.
    # if "scenarios_data" not in st.session_state:
    #     from application_pages.page_4_scenario_selection import generate_synthetic_scenarios
    #     st.session_state.scenarios_data = generate_synthetic_scenarios()

    st.success("Scenario state has been reset! You can now select a new scenario and restart the analysis.")
    st.rerun()

def main():
    st.markdown("""
    ## <h2 style="color:#0A2647;">12. Reset Scenario for Re-experimentation</h2>

    This section allows you to reset the entire scenario state, clearing all selections and computed results. This is useful if you wish to:

    *   Start fresh with a new scenario.
    *   Experiment with different mitigation strategies for the same scenario from the beginning.
    *   Undo previous selections and calculations.

    Clicking the "Reset Scenario" button will clear all `st.session_state` variables related to the current scenario's selection and analysis, returning the application to its initial state (scenario selection).

    This ensures a clean slate for new experiments and analyses within the sandbox.
    """)

    st.subheader("Reset Application State")
    if st.button("Reset Scenario", help="Clear all scenario data and selections to start fresh."):
        reset_current_scenario_state()
