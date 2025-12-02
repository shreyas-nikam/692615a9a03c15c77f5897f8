import streamlit as st
import pandas as pd
import matplotlib.pyplot as plt
import seaborn as sns
import numpy as np

def plot_risk_matrix_comparison(baseline_df, mitigated_df, title):
    fig, ax = plt.subplots(figsize=(14, 9))
    
    # Define color palette for qualitative impact
    impact_colors = {'Critical': 'darkred', 'High': 'red', 'Medium': 'orange', 'Low': 'lightgreen'}
    
    # Prepare data for plotting
    # Ensure monetary impact is positive for log scale
    baseline_df['baseline_impact_monetary_log'] = np.log1p(baseline_df['baseline_impact_monetary'])
    mitigated_df['mitigated_impact_monetary_log'] = np.log1p(mitigated_df['mitigated_impact_monetary'])

    # Merge for easier plotting of transitions
    comparison_df = pd.merge(
        baseline_df[['risk_name', 'baseline_likelihood', 'baseline_impact_monetary_log', 'baseline_cost_of_failure', 'baseline_impact_qualitative']],
        mitigated_df[['risk_name', 'mitigated_likelihood', 'mitigated_impact_monetary_log', 'mitigated_cost_of_failure', 'mitigated_impact_qualitative']],
        on='risk_name',
        how='inner'
    )

    # Plot baseline risks
    for i, row in comparison_df.iterrows():
        ax.scatter(
            x=row['baseline_impact_monetary_log'],
            y=row['baseline_likelihood'],
            s=row['baseline_cost_of_failure'] / 10000, 
            color=impact_colors.get(row['baseline_impact_qualitative'], 'grey'),
            marker='o',
            alpha=0.6,
            edgecolors='black',
            linewidth=0.5,
            label='Baseline' if i == 0 else "" # Label once for legend
        )
        ax.text(
            row['baseline_impact_monetary_log'] + 0.1, 
            row['baseline_likelihood'], 
            f"{row['risk_name']} (B)", 
            fontsize=8, 
            color=impact_colors.get(row['baseline_impact_qualitative'], 'grey')
        )

    # Plot mitigated risks and arrows
    for i, row in comparison_df.iterrows():
        ax.scatter(
            x=row['mitigated_impact_monetary_log'],
            y=row['mitigated_likelihood'],
            s=row['mitigated_cost_of_failure'] / 10000, 
            color=impact_colors.get(row['mitigated_impact_qualitative'], 'grey'),
            marker='X',
            alpha=0.8,
            edgecolors='black',
            linewidth=0.5,
            label='Mitigated' if i == 0 else "" # Label once for legend
        )
        ax.text(
            row['mitigated_impact_monetary_log'] + 0.1, 
            row['mitigated_likelihood'], 
            f"{row['risk_name']} (M)", 
            fontsize=8, 
            color=impact_colors.get(row['mitigated_impact_qualitative'], 'grey')
        )

        # Draw arrow from baseline to mitigated
        ax.annotate('', 
            xy=(row['mitigated_impact_monetary_log'], row['mitigated_likelihood']), 
            xytext=(row['baseline_impact_monetary_log'], row['baseline_likelihood']), 
            arrowprops=dict(facecolor='blue', shrink=0.05, width=0.5, headwidth=5), 
            alpha=0.5
        )

    ax.set_title(title, fontsize=16)
    ax.set_xlabel("Monetary Impact (Log Scale)", fontsize=12)
    ax.set_ylabel("Likelihood (0-1)", fontsize=12)
    ax.set_ylim(-0.05, 1.05) # Extend y-axis slightly
    ax.grid(True, linestyle='--', alpha=0.6)

    # Custom legend for markers (Baseline and Mitigated)
    legend_elements_markers = [
        plt.Line2D([0], [0], marker='o', color='w', label='Baseline Risk', markerfacecolor='grey', markersize=10, markeredgecolor='black'),
        plt.Line2D([0], [0], marker='X', color='w', label='Mitigated Risk', markerfacecolor='grey', markersize=10, markeredgecolor='black'),
        plt.Line2D([0], [0], color='blue', lw=2, label='Shift with Mitigation', linestyle='-')
    ]

    # Custom legend for qualitative impact
    legend_elements_qualitative = [
        plt.Line2D([0], [0], marker='o', color='w', label=label, markerfacecolor=color, markersize=10, markeredgecolor='black')
        for label, color in impact_colors.items()
    ]

    # Combine legends
    first_legend = ax.legend(handles=legend_elements_markers, title="Risk State", loc='upper left', bbox_to_anchor=(1.05, 1))
    ax.add_artist(first_legend)
    ax.legend(handles=legend_elements_qualitative, title="Qualitative Impact", loc='lower left', bbox_to_anchor=(1.05, 0))

    # Formatting x-axis ticks for monetary values
    ax.set_xscale('linear') 
    # Use a lambda function for formatting to get around the log1p transform, showing original values
    current_xticks = ax.get_xticks()
    x_ticks_labels = []
    for tick_val in current_xticks:
        if tick_val >= 0:
            original_value = np.expm1(tick_val)
            if original_value >= 1_000_000: # Millions
                x_ticks_labels.append(f"${original_value/1_000_000:.0f}M")
            elif original_value >= 1_000: # Thousands
                x_ticks_labels.append(f"${original_value/1_000:.0f}K")
            else:
                x_ticks_labels.append(f"${original_value:.0f}")
        else:
            x_ticks_labels.append("") # Handle negative or zero log values gracefully
    ax.set_xticklabels(x_ticks_labels)

    plt.tight_layout()
    return fig

def main():
    st.markdown("""
    ## <h2 style="color:#0A2647;">10. Updated Risk Matrix: Seeing the Shift</h2>

    To provide a comprehensive view of the impact of your mitigation strategies, this section displays a comparative risk matrix. This specialized scatter plot shows both the baseline and mitigated positions of each risk.

    Key features of this visualization include:

    *   **Baseline Risks:** Represented by 'o' markers.
    *   **Mitigated Risks:** Represented by 'X' markers.
    *   **Arrows:** Drawn from each baseline risk point to its corresponding mitigated risk point, visually demonstrating the shift in likelihood and monetary impact due to the applied mitigations.
    *   **Qualitative Impact:** Colors indicate the qualitative impact, which is dynamically updated for mitigated risks based on their new monetary thresholds.
    *   **Size of points:** Still corresponds to the Cost of Failure (baseline and mitigated respectively).

    This matrix is invaluable for understanding how effectively strategies are reducing both the likelihood and potential financial consequences of AI risks, and identifying any residual risks that remain at a high level.
    """)

    if "baseline_risks_df" not in st.session_state or st.session_state.baseline_risks_df.empty:
        st.info("Please go to the '5. Identifying Baseline Risks' page to assess and load baseline risks first.")
        return
    
    if "mitigated_risks_df" not in st.session_state or st.session_state.mitigated_risks_df.empty:
        st.info("Please go to the '8. Simulating Mitigation Outcomes' page and click 'Simulate Mitigations' to generate mitigated risk data.")
        return

    st.subheader("Comparative Risk Matrix")

    if st.button("Plot Risk Matrix Comparison", help="Generate a scatter plot showing the shift from baseline to mitigated risks."):
        with st.spinner("Generating comparative risk matrix..."):
            fig = plot_risk_matrix_comparison(
                st.session_state.baseline_risks_df.copy(), 
                st.session_state.mitigated_risks_df.copy(), 
                f"AI Risk Matrix Comparison: {st.session_state.selected_scenario_id}"
            )
            st.pyplot(fig)
            st.success("Comparative risk matrix generated.")
    else:
        st.info("Click the button above to visualize the shift in risks.")
