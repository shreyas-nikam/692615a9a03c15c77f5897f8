import streamlit as st
import pandas as pd

def calculate_cost_of_failure(likelihood, monetary_impact):
    return likelihood * monetary_impact

def apply_selected_mitigations(baseline_risk_data_df, selected_mitigations_details):
    mitigated_risks_df = baseline_risk_data_df.copy()
    mitigated_risks_df["mitigated_likelihood"] = mitigated_risks_df["baseline_likelihood"]
    mitigated_risks_df["mitigated_impact_monetary"] = mitigated_risks_df["baseline_impact_monetary"]

    for index, risk in mitigated_risks_df.iterrows():
        risk_name = risk["risk_name"]
        
        # Initialize effective survival factors to 1 (meaning no reduction initially)
        effective_likelihood_survival_factor = 1.0
        effective_impact_survival_factor = 1.0

        for mitigation in selected_mitigations_details:
            if risk_name in mitigation["applies_to_risks"]:
                # Multiplicatively apply reduction factors
                effective_likelihood_survival_factor *= (1 - mitigation["likelihood_reduction_factor"])
                effective_impact_survival_factor *= (1 - mitigation["impact_reduction_factor"])
        
        # Calculate mitigated values
        mitigated_likelihood = risk["baseline_likelihood"] * effective_likelihood_survival_factor
        mitigated_impact_monetary = risk["baseline_impact_monetary"] * effective_impact_survival_factor
        
        # Ensure likelihood doesn't go below 0 or above 1
        mitigated_risks_df.loc[index, "mitigated_likelihood"] = max(0.0, min(1.0, mitigated_likelihood))
        # Ensure monetary impact is not negative
        mitigated_risks_df.loc[index, "mitigated_impact_monetary"] = max(0.0, mitigated_impact_monetary)

    mitigated_risks_df["mitigated_cost_of_failure"] = mitigated_risks_df.apply(
        lambda row: calculate_cost_of_failure(row["mitigated_likelihood"], row["mitigated_impact_monetary"]),
        axis=1
    )

    # Determine mitigated qualitative impact based on new monetary thresholds
    # >= $2M Critical, >= $1M High, >= $0.5M Medium, else Low
    def get_mitigated_qualitative_impact(monetary_impact):
        if monetary_impact >= 2000000:
            return "Critical"
        elif monetary_impact >= 1000000:
            return "High"
        elif monetary_impact >= 500000:
            return "Medium"
        else:
            return "Low"
    
    mitigated_risks_df["mitigated_impact_qualitative"] = mitigated_risks_df["mitigated_impact_monetary"].apply(get_mitigated_qualitative_impact)

    # Select and reorder columns for display and comparison
    mitigated_risks_df = mitigated_risks_df[[
        "risk_name",
        "baseline_likelihood",
        "mitigated_likelihood",
        "baseline_impact_qualitative",
        "mitigated_impact_qualitative",
        "baseline_impact_monetary",
        "mitigated_impact_monetary",
        "baseline_cost_of_failure",
        "mitigated_cost_of_failure"
    ]]
    
    return mitigated_risks_df

def main():
    st.markdown("""
    ## <h2 style="color:#0A2647;">8. Simulating Mitigation Outcomes: Reduced Risk</h2>

    With selected mitigation strategies, we can now simulate their effects on the baseline risks. This simulation will provide a "mitigated" risk profile, showing how the likelihood, monetary impact, and consequently, the **Cost of Failure** are expected to change.

    The calculations for mitigated likelihood and monetary impact involve applying the respective `reduction_factor` for each selected mitigation. If multiple mitigations apply to the same risk, their reduction factors are combined multiplicatively. The new qualitative impact is also re-evaluated based on updated monetary thresholds:

    *   Monetary Impact $\ge \$2M$: **Critical**
    *   Monetary Impact $\ge \$1M$: **High**
    *   Monetary Impact $\ge \$0.5M$: **Medium**
    *   Else: **Low**

    Click the "Simulate Mitigations" button below to see the adjusted risk details.
    """)

    if "baseline_risks_df" not in st.session_state or st.session_state.baseline_risks_df.empty:
        st.info("Please go to the '5. Identifying Baseline Risks' page to assess and load baseline risks first.")
        return

    if "user_selected_mitigations_details" not in st.session_state or not st.session_state.user_selected_mitigations_details:
        st.info("Please select mitigation strategies in the '7. Proposing Mitigation Strategies' page before simulating.")
        return

    st.subheader(f"Simulating Mitigations for Scenario: {st.session_state.selected_scenario_id}")

    if st.button("Simulate Mitigations", help="Calculate the effects of selected mitigation strategies."):
        with st.spinner("Simulating mitigation outcomes..."):
            mitigated_risks_df = apply_selected_mitigations(
                st.session_state.baseline_risks_df,
                st.session_state.user_selected_mitigations_details
            )
            st.session_state.mitigated_risks_df = mitigated_risks_df
            st.success("Mitigation simulation complete! See the mitigated risk details below.")
    
    if "mitigated_risks_df" in st.session_state and not st.session_state.mitigated_risks_df.empty:
        st.subheader("Mitigated Risk Details")
        st.dataframe(st.session_state.mitigated_risks_df, use_container_width=True, hide_index=True)
    else:
        st.info("No mitigated risk data available yet. Click 'Simulate Mitigations' to generate results.")
