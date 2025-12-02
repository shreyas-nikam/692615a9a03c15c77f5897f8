import streamlit as st
import pandas as pd
import matplotlib.pyplot as plt
import seaborn as sns

def plot_comparative_risk(baseline_df, mitigated_df):
    # Ensure risk names are consistent for merging
    comparison_df = pd.merge(
        baseline_df[['risk_name', 'baseline_likelihood', 'baseline_cost_of_failure']],
        mitigated_df[['risk_name', 'mitigated_likelihood', 'mitigated_cost_of_failure']],
        on='risk_name',
        how='inner'
    )

    fig, axes = plt.subplots(1, 2, figsize=(18, 7))
    plt.style.use('seaborn-v0_8-darkgrid')

    # Bar chart for Likelihood Comparison
    likelihood_melted = comparison_df.melt(
        id_vars='risk_name',
        value_vars=['baseline_likelihood', 'mitigated_likelihood'],
        var_name='Risk Type',
        value_name='Likelihood'
    )
    sns.barplot(
        ax=axes[0],
        x='risk_name',
        y='Likelihood',
        hue='Risk Type',
        data=likelihood_melted,
        palette={"baseline_likelihood": "skyblue", "mitigated_likelihood": "lightcoral"}
    )
    axes[0].set_title('Likelihood Comparison: Baseline vs. Mitigated', fontsize=14)
    axes[0].set_xlabel('Risk Name', fontsize=12)
    axes[0].set_ylabel('Likelihood', fontsize=12)
    axes[0].tick_params(axis='x', rotation=45, ha='right')
    axes[0].set_ylim(0, 1.0)
    axes[0].grid(axis='y', linestyle='--', alpha=0.7)

    # Bar chart for Cost of Failure Comparison
    cost_melted = comparison_df.melt(
        id_vars='risk_name',
        value_vars=['baseline_cost_of_failure', 'mitigated_cost_of_failure'],
        var_name='Cost Type',
        value_name='Cost of Failure'
    )
    sns.barplot(
        ax=axes[1],
        x='risk_name',
        y='Cost of Failure',
        hue='Cost Type',
        data=cost_melted,
        palette={"baseline_cost_of_failure": "mediumseagreen", "mitigated_cost_of_failure": "gold"}
    )
    axes[1].set_title('Cost of Failure Comparison: Baseline vs. Mitigated', fontsize=14)
    axes[1].set_xlabel('Risk Name', fontsize=12)
    axes[1].set_ylabel('Cost of Failure', fontsize=12)
    axes[1].tick_params(axis='x', rotation=45, ha='right')
    axes[1].yaxis.set_major_formatter(plt.FuncFormatter(lambda x, p: f"${x:,.0f}"))
    axes[1].grid(axis='y', linestyle='--', alpha=0.7)

    plt.tight_layout()
    return fig

def main():
    st.markdown("""
    ## <h2 style="color:#0A2647;">9. Comparative Risk Visualization: Before and After Mitigations</h2>

    After simulating the effects of mitigation strategies, it is essential to visualize the changes in the risk profile. This section provides a comparative view of the baseline risks versus the mitigated risks, highlighting the effectiveness of the chosen strategies.

    We will present two side-by-side bar charts:

    1.  **Likelihood Comparison:** This chart compares the `baseline_likelihood` with the `mitigated_likelihood` for each risk. A significant drop in the mitigated bar indicates effective likelihood reduction.
    2.  **Cost of Failure Comparison:** This chart compares the `baseline_cost_of_failure` with the `mitigated_cost_of_failure`. As the `Cost of Failure` is a product of likelihood and monetary impact, a reduction here signifies a positive outcome from the mitigation efforts.

    These visualizations help in intuitively understanding the quantitative impact of your proposed risk management actions.
    """)

    if "baseline_risks_df" not in st.session_state or st.session_state.baseline_risks_df.empty:
        st.info("Please go to the '5. Identifying Baseline Risks' page and '8. Simulating Mitigation Outcomes' page to assess baseline risks and simulate mitigations first.")
        return
    
    if "mitigated_risks_df" not in st.session_state or st.session_state.mitigated_risks_df.empty:
        st.info("Please go to the '8. Simulating Mitigation Outcomes' page and click 'Simulate Mitigations' to generate mitigated risk data.")
        return

    st.subheader("Comparative Risk Bar Charts")
    
    if st.button("Plot Comparative Risks", help="Generate bar charts comparing baseline and mitigated risks."):
        with st.spinner("Generating comparative risk charts..."):
            fig = plot_comparative_risk(st.session_state.baseline_risks_df, st.session_state.mitigated_risks_df)
            st.pyplot(fig)
            st.success("Comparative risk charts generated.")
    else:
        st.info("Click the button above to visualize the comparative risks.")
