import streamlit as st
import pandas as pd
import matplotlib.pyplot as plt
import seaborn as sns
import numpy as np

def plot_risk_matrix(risk_data_df, title):
    fig, ax = plt.subplots(figsize=(12, 8))
    
    # Define color palette for qualitative impact
    impact_colors = {'Critical': 'darkred', 'High': 'red', 'Medium': 'orange', 'Low': 'lightgreen'}
    risk_data_df['color'] = risk_data_df['baseline_impact_qualitative'].map(impact_colors)

    # Ensure monetary impact is positive for log scale
    risk_data_df['baseline_impact_monetary_log'] = np.log1p(risk_data_df['baseline_impact_monetary'])

    scatter = ax.scatter(
        x=risk_data_df['baseline_impact_monetary_log'],
        y=risk_data_df['baseline_likelihood'],
        s=risk_data_df['baseline_cost_of_failure'] / 10000, # Scale size for better visualization
        c=risk_data_df['color'],
        alpha=0.7,
        edgecolors='w',
        linewidth=0.5
    )

    # Annotate risk names
    for i, row in risk_data_df.iterrows():
        ax.text(
            row['baseline_impact_monetary_log'] + 0.1, 
            row['baseline_likelihood'], 
            row['risk_name'], 
            fontsize=9
        )

    ax.set_xscale('linear') # Keep linear for log1p transformed data
    x_ticks_labels = [f"${int(np.expm1(tick)):,d}" for tick in ax.get_xticks() if tick >= 0]
    ax.set_xticklabels(x_ticks_labels)

    ax.set_title(title, fontsize=16)
    ax.set_xlabel("Monetary Impact (Log Scale)", fontsize=12)
    ax.set_ylabel("Likelihood (0-1)", fontsize=12)
    ax.set_ylim(-0.05, 1.05) # Extend y-axis slightly
    ax.grid(True, linestyle='--', alpha=0.6)

    # Create a legend for qualitative impact
    legend_elements = [
        plt.Line2D([0], [0], marker='o', color='w', label=label, markerfacecolor=color, markersize=10)
        for label, color in impact_colors.items()
    ]
    ax.legend(handles=legend_elements, title="Qualitative Impact", bbox_to_anchor=(1.05, 1), loc='upper left')
    
    plt.tight_layout()
    return fig

def main():
    st.markdown("""
    ## <h2 style="color:#0A2647;">6. Visualizing Baseline Risk Profile</h2>

    Visualizing risks is crucial for quickly understanding the overall risk posture and identifying the most critical threats. In this section, we present a **Baseline Risk Matrix** that plots each identified risk based on its likelihood and monetary impact.

    The matrix provides a clear overview of:

    *   **X-axis:** Monetary Impact (on a logarithmic scale to accommodate wide ranges).
    *   **Y-axis:** Likelihood (ranging from 0 to 1).
    *   **Color of points:** Represents the qualitative impact (Critical, High, Medium, Low).
    *   **Size of points:** Corresponds to the calculated **Cost of Failure**, highlighting risks with higher expected financial losses.

    This visualization helps in pinpointing high-impact, high-likelihood risks that warrant immediate attention.
    """)

    if "baseline_risks_df" in st.session_state and not st.session_state.baseline_risks_df.empty:
        st.subheader("Baseline Risk Matrix")
        fig = plot_risk_matrix(st.session_state.baseline_risks_df.copy(), "Baseline AI Risk Matrix")
        st.pyplot(fig)
        st.success("Baseline risk matrix visualized. You can now propose mitigation strategies.")
    else:
        st.info("Please go to the '5. Identifying Baseline Risks' page to assess and load baseline risks first.")
