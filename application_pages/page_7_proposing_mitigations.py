import streamlit as st
import pandas as pd

def display_available_mitigations_for_scenario(scenario_data):
    if scenario_data and "mitigations" in scenario_data:
        mitigations_df = pd.DataFrame(scenario_data["mitigations"])
        # Reorder columns for better readability
        mitigations_df = mitigations_df[[
            "mitigation_name",
            "applies_to_risks",
            "likelihood_reduction_factor",
            "impact_reduction_factor"
        ]]
        return mitigations_df
    return pd.DataFrame()

def main():
    st.markdown("""
    ## <h2 style="color:#0A2647;">7. Proposing Mitigation Strategies</h2>

    After understanding the baseline risk profile, the next step is to propose and select appropriate mitigation strategies. Mitigation strategies are actions or controls designed to reduce the likelihood of a risk event occurring or to lessen its impact if it does occur.

    In this section, you will be presented with a list of available mitigation strategies for the chosen scenario. Each strategy comes with an estimated `likelihood_reduction_factor` and `impact_reduction_factor`, representing the percentage reduction it can achieve on the respective risk dimensions.

    You can select one or more mitigation strategies using the multi-select widget below. Once selected, these strategies will be applied to the baseline risks to simulate a "mitigated" risk profile.

    **Important Considerations:**
    *   Multiple mitigations applying to the same risk will have their reduction factors combined multiplicatively (e.g., if two mitigations offer 20% and 30% likelihood reduction, the combined reduction is not 50%, but $1 - (1-0.2) \times (1-0.3) = 1 - 0.8 \times 0.7 = 1 - 0.56 = 0.44$, or 44%).
    *   Some mitigations might apply to multiple risks, reflecting their broad applicability.
    """)

    if "selected_scenario_data" in st.session_state and st.session_state.selected_scenario_data:
        st.subheader(f"Available Mitigation Strategies for Scenario: {st.session_state.selected_scenario_data['scenario_id']}")

        available_mitigations_df = display_available_mitigations_for_scenario(st.session_state.selected_scenario_data)

        if not available_mitigations_df.empty:
            st.dataframe(available_mitigations_df, use_container_width=True, hide_index=True)
            st.session_state.available_mitigations_df = available_mitigations_df

            mitigation_options = available_mitigations_df["mitigation_name"].tolist()

            # Initialize or update user_selected_mitigation_names in session state
            if "user_selected_mitigation_names" not in st.session_state:
                st.session_state.user_selected_mitigation_names = []

            selected_mitigation_names = st.multiselect(
                label="Select Mitigation Strategies to Apply",
                options=mitigation_options,
                default=st.session_state.user_selected_mitigation_names,
                key="mitigation_selector",
                help="Choose one or more strategies to reduce risks. Their effects will be simulated."
            )

            # Update session state with currently selected mitigations
            st.session_state.user_selected_mitigation_names = selected_mitigation_names

            if selected_mitigation_names:
                st.session_state.user_selected_mitigations_details = available_mitigations_df[
                    available_mitigations_df["mitigation_name"].isin(selected_mitigation_names)
                ].to_dict(orient="records")
                st.success(f"Selected {len(selected_mitigation_names)} mitigation(s). Click 'Simulate Mitigations' on the next page to see their impact.")
            else:
                st.session_state.user_selected_mitigations_details = []
                st.info("No mitigations selected yet. Select some to proceed with simulation.")

        else:
            st.warning("No mitigation strategies found for the selected scenario.")
            st.session_state.available_mitigations_df = pd.DataFrame()
            st.session_state.user_selected_mitigation_names = []
            st.session_state.user_selected_mitigations_details = []

    else:
        st.info("Please select a scenario in the '4. Scenario Selection' page to view and select mitigation strategies.")
