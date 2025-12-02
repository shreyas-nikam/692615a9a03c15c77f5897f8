import streamlit as st

def main():
    st.markdown(r"""
    ## <h2 style="color:#0A2647;">3. Defining Key Risk Metrics</h2>

    To effectively manage AI risks, it is crucial to define and quantify them using a consistent set of metrics. This allows for objective assessment, comparison, and tracking of risk mitigation efforts.

    ### 3.1 Probability of Risk ($P(Risk)$)

    The probability of risk, often referred to as likelihood, represents the chance or frequency of a specific AI risk event occurring. It is typically expressed as a value between 0 and 1, where:

    *   $P(Risk) = 0$: The event is impossible or extremely unlikely to occur.
    *   $P(Risk) = 1$: The event is certain to occur.

    For practical purposes, we often use qualitative descriptions alongside quantitative estimates, such as:

    *   **Very Low:** $< 0.1$
    *   **Low:** $0.1 - 0.3$
    *   **Medium:** $0.3 - 0.6$
    *   **High:** $0.6 - 0.9$
    *   **Very High:** $> 0.9$

    ### 3.2 Impact ($Impact$)

    Impact quantifies the severity of a risk event if it occurs. We consider two forms of impact:

    #### 3.2.1 Qualitative Impact

    This provides a categorical assessment of the severity based on predefined criteria, often related to reputational damage, regulatory fines, operational disruption, or harm to individuals. Common categories include:

    *   **Critical:** Catastrophic consequences, severe reputational damage, major regulatory fines, significant operational disruption, severe harm.
    *   **High:** Serious consequences, notable reputational damage, substantial regulatory fines, moderate operational disruption, moderate harm.
    *   **Medium:** Moderate consequences, minor reputational damage, small regulatory fines, limited operational disruption, minor harm.
    *   **Low:** Minimal consequences, negligible impact.

    #### 3.2.2 Monetary Impact ($Impact_{Monetary}$)

    This is a quantifiable financial estimation of the loss or cost incurred if a risk event materializes. This can include direct costs (e.g., fines, legal fees, repair costs) and indirect costs (e.g., lost revenue, brand devaluation). Monetary impact is expressed in a currency (e.g., USD).

    ### 3.3 Cost of Failure ($C_F$)

    The Cost of Failure is a crucial metric that combines the probability of a risk event with its potential monetary impact, providing an expected financial loss. It helps in prioritizing risks and allocating resources for mitigation.

    The formula for the Cost of Failure is:
    $$C_F = P(Risk) \times Impact_{Monetary}$$

    Where:
    *   $C_F$: Cost of Failure (e.g., in USD)
    *   $P(Risk)$: Probability of the risk occurring (0-1)
    *   $Impact_{Monetary}$: Monetary impact if the risk occurs (e.g., in USD)

    ### 3.4 Probability Modification for Mitigations ($P_{mitigated}(Risk)$)

    Mitigation strategies are designed to reduce the likelihood of a risk event. The mitigated probability is calculated by applying a `likelihood_reduction_factor` to the baseline probability.

    The formula is:
    $$P_{mitigated}(Risk) = P_{baseline}(Risk) \times (1 - Reduction\_Factor_{Likelihood})$$

    Where:
    *   $P_{mitigated}(Risk)$: The probability of the risk after applying mitigations.
    *   $P_{baseline}(Risk)$: The initial probability of the risk before mitigations.
    *   $Reduction\_Factor_{Likelihood}$: A factor (0-1) representing the percentage reduction in likelihood due to the mitigation. For example, a factor of 0.2 means a 20% reduction.

    ### 3.5 Impact Modification for Mitigations ($Impact_{mitigated}(Monetary)$)

    Mitigation strategies can also reduce the monetary impact if a risk event still occurs. The mitigated monetary impact is calculated by applying an `impact_reduction_factor` to the baseline monetary impact.

    The formula is:
    $$Impact_{mitigated}(Monetary) = Impact_{baseline}(Monetary) \times (1 - Reduction\_Factor_{Impact})$$

    Where:
    *   $Impact_{mitigated}(Monetary)$: The monetary impact after applying mitigations.
    *   $Impact_{baseline}(Monetary)$: The initial monetary impact before mitigations.
    *   $Reduction\_Factor_{Impact}$: A factor (0-1) representing the percentage reduction in monetary impact due to the mitigation. For example, a factor of 0.15 means a 15% reduction.
    """))