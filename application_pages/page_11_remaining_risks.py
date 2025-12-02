import streamlit as st
import pandas as pd

def summarize_post_mitigation_risks(mitigated_risk_data_df):
    summary_text = []

    if mitigated_risk_data_df.empty:
        return "No mitigated risks to summarize."

    # Identify critical/high residual risks
    critical_high_risks = mitigated_risk_data_df[
        (mitigated_risk_data_df["mitigated_impact_qualitative"] == "Critical") |
        (mitigated_risk_data_df["mitigated_impact_qualitative"] == "High")
    ].copy()

    if not critical_high_risks.empty:
        summary_text.append("### Residual Risks with High or Critical Impact:")
        for _, row in critical_high_risks.iterrows():
            summary_text.append(f"- **{row['risk_name']}** still has a mitigated likelihood of `{row['mitigated_likelihood']:.2f}` and a mitigated monetary impact of `${row['mitigated_impact_monetary']:,d}` ({row['mitigated_impact_qualitative']}). The mitigated cost of failure is `${row['mitigated_cost_of_failure']:,d}`.")
    else:
        summary_text.append("### No residual risks with High or Critical impact identified after mitigation!")

    # General summary of risk reduction
    total_baseline_cost = mitigated_risk_data_df["baseline_cost_of_failure"].sum()
    total_mitigated_cost = mitigated_risk_data_df["mitigated_cost_of_failure"].sum()

    if total_baseline_cost > 0:
        reduction_percentage = ((total_baseline_cost - total_mitigated_cost) / total_baseline_cost) * 100
        summary_text.append(f"\n### Overall Risk Reduction:")
        summary_text.append(f"The total expected Cost of Failure across all risks has been reduced from `${total_baseline_cost:,d}` to `${total_mitigated_cost:,d}`, representing a **{reduction_percentage:.2f}% reduction**.")
    else:
        summary_text.append(f"\n### Overall Risk Reduction:")
        summary_text.append(f"The total expected Cost of Failure across all risks is `${total_mitigated_cost:,d}`.")

    # Potential new challenges (illustrative - could be expanded)
    summary_text.append("\n### Potential New Challenges/Considerations:")
    summary_text.append("- **Implementation Cost:** What are the financial and operational costs associated with implementing the chosen mitigations? (Not quantified in this simulation, but crucial in real-world scenarios).")
    summary_text.append("- **New Risks Introduced:** Could any of the implemented mitigations introduce new, unforeseen risks? (e.g., increased complexity, dependency on new systems, human-in-the-loop bottlenecks).")
    summary_text.append("- **Monitoring & Review:** Continuous monitoring is required to ensure mitigations remain effective and new risks are identified.")
    
    return "\n".join(summary_text)

def main():
    st.markdown("""
    ## <h2 style="color:#0A2647;">11. Remaining Risks & New Challenges</h2>

    Even after implementing robust mitigation strategies, some risks may persist, or new challenges might emerge. This section helps you to identify and understand the **residual risks** and to consider potential new issues introduced by the mitigation process.

    The summary below will highlight:

    *   **Residual Risks:** Any risks that still possess a `High` or `Critical` qualitative impact even after mitigations.
    *   **Overall Reduction:** A quantitative summary of the total `Cost of Failure` reduction achieved.
    *   **New Challenges:** Illustrative considerations for additional risks or complexities that might arise from implementing the chosen mitigations (e.g., implementation costs, new dependencies).

    It is crucial for risk managers to acknowledge that risk management is an ongoing process, and complete elimination of all risks is rarely feasible, especially in complex AI systems.
    """)

    if "mitigated_risks_df" not in st.session_state or st.session_state.mitigated_risks_df.empty:
        st.info("Please go to the '8. Simulating Mitigation Outcomes' page and click 'Simulate Mitigations' to generate mitigated risk data before summarizing.")
        return

    st.subheader(f"Summary of Post-Mitigation Risks for Scenario: {st.session_state.selected_scenario_id}")

    if st.button("Summarize Remaining Risks", help="Provide a textual summary of risks after mitigation."):
        with st.spinner("Generating summary..."):
            summary = summarize_post_mitigation_risks(st.session_state.mitigated_risks_df)
            st.markdown(summary)
            st.success("Summary generated.")
    else:
        st.info("Click the button above to get a summary of remaining risks and new challenges.")
