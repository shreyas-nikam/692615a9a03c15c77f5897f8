id: 692615a9a03c15c77f5897f8_documentation
summary: Lab 1: Principles of AI Risk and Assurance Documentation
feedback link: https://docs.google.com/forms/d/e/1FAIpQLSfWkOK-in_bMMoHSZfcIvAeO58PAH9wrDqcxnJABHaxiDqhSA/viewform?usp=sf_link
environments: Web
status: Published
# QuLab: AI Risk and Assurance Codelab

## 1. Introduction to AI Risk Management with QuLab
Duration: 0:05:00

In today's rapidly evolving technological landscape, Artificial Intelligence (AI), particularly Generative AI and Agentic AI systems, presents both unprecedented opportunities and significant risks. Managing these risks effectively is crucial for ensuring responsible and reliable AI deployment. This codelab introduces **QuLab: AI Risk and Assurance Lab**, an interactive sandbox designed for risk managers, developers, and AI practitioners to explore, quantify, and mitigate AI-related risks.

### Why is AI Risk Management Important?
AI systems, especially sophisticated ones like Large Language Models (LLMs) and autonomous agents, can fail in complex and unexpected ways. These failures can lead to severe consequences, including financial losses, reputational damage, regulatory penalties, and even harm to individuals. Proactive risk management is essential to:
*   **Ensure Trust and Safety**: Build confidence in AI systems among users and stakeholders.
*   **Maintain Compliance**: Adhere to emerging AI regulations and ethical guidelines (e.g., EU AI Act).
*   **Protect Business Value**: Safeguard against financial losses and brand erosion.
*   **Promote Responsible Innovation**: Foster the development of beneficial AI technologies.

### QuLab's Purpose and Learning Objectives
QuLab provides a practical environment to:
*   **Understand AI Risk Categories**: Delve into various risk dimensions, including data, model, system, human-centric, and organizational risks.
*   **Quantify Risk**: Learn to quantify risk likelihood, qualitative and monetary impact, and the financial cost of potential failures.
*   **Experiment with Mitigations**: Propose and simulate the effects of different mitigation strategies on risk reduction.
*   **Visualize Impact**: Observe the reduction of risk both before and after applying mitigations through interactive plots.
*   **Identify Residual Risks**: Understand how to identify remaining risks and anticipate new challenges introduced by mitigation efforts.
*   **Grasp Key Concepts**: Gain practical insights into critical AI risk concepts such as `hallucinations`, `goal mis-specification`, `autonomy creep`, `error propagation`, `human-in-the-loop`, and `oversight mechanisms`.

### Application Architecture and Flow
The QuLab application is built using Streamlit, a Python library for creating interactive web applications. It follows a modular architecture, with a main `app.py` file orchestrating navigation between different functional pages located in the `application_pages/` directory.

<figure>
  <img src="https://i.imgur.com/example_architecture.png" alt="QuLab Application Architecture Diagram">
  <figcaption>Figure 1: High-level Architecture of the QuLab Streamlit Application.</figcaption>
</figure>

The typical flow through the application involves:
1.  **Selection of a Scenario**: Choose a predefined AI system and its associated risks.
2.  **Baseline Risk Assessment**: View the inherent risks, their likelihood, impact, and initial Cost of Failure.
3.  **Mitigation Strategy Proposal**: Select potential strategies to reduce identified risks.
4.  **Simulation & Visualization**: Observe the calculated reduction in risks and their visual representation in updated risk matrices and comparative charts.
5.  **Residual Risk Analysis**: Understand what risks remain and potential new challenges.

This codelab will walk you through each step, explaining the underlying code and the concepts it demonstrates.

## 2. Setting Up the QuLab Application
Duration: 0:03:00

To get started with QuLab, you'll need to set up your Python environment and run the Streamlit application.

### Prerequisites
Ensure you have Python 3.8+ installed.

### Dependencies
The application relies on several Python libraries:
*   `streamlit`
*   `pandas`
*   `matplotlib`
*   `seaborn`
*   `numpy`

### Installation
First, save the provided `app.py` and the contents of the `application_pages` directory in your local machine.
Make sure your directory structure looks like this:

```
your-project-folder/
├── app.py
└── application_pages/
    ├── __init__.py
    ├── page_1_introduction.py
    ├── page_2_risk_taxonomy.py
    ├── page_3_risk_metrics.py
    ├── page_4_scenario_selection.py
    ├── page_5_baseline_risks.py
    ├── page_6_visualizing_baseline.py
    ├── page_7_proposing_mitigations.py
    ├── page_8_simulating_outcomes.py
    ├── page_9_comparative_visualization.py
    ├── page_10_updated_risk_matrix.py
    ├── page_11_remaining_risks.py
    └── page_12_reset_scenario.py
```

Next, install the required libraries:

```console
pip install streamlit pandas matplotlib seaborn numpy
```

### Running the Application
Navigate to your project folder in the terminal and run the Streamlit application:

```console
streamlit run app.py
```

This command will open the QuLab application in your default web browser. You should see the main page with a sidebar navigation.

<aside class="positive">
  <b>Tip:</b> If the application doesn't open automatically, look for a URL in your terminal (usually `http://localhost:8501`) and open it manually in your browser.
</aside>

### Application Structure (`app.py`)
The `app.py` file is the entry point and orchestrator for the QuLab application. It sets up the Streamlit page configuration, displays the main title, and manages navigation between different pages.

```python
import streamlit as st

st.set_page_config(page_title="QuLab", layout="wide")
st.sidebar.image("https://www.quantuniversity.com/assets/img/logo5.jpg")
st.sidebar.divider()
st.title("QuLab: AI Risk and Assurance Lab")
st.divider()

# ... (Introduction markdown content) ...

page = st.sidebar.selectbox(
    label="Navigation",
    options=[
        "1. Introduction",
        "2. AI Risk Taxonomy",
        # ... (other pages) ...
    ]
)

if page == "1. Introduction":
    from application_pages.page_1_introduction import main
    main()
elif page == "2. AI Risk Taxonomy":
    from application_pages.page_2_risk_taxonomy import main
    main()
# ... (rest of the page routing) ...
```

Each page in the `application_pages` directory has a `main()` function that Streamlit calls when that page is selected in the sidebar. This modular approach keeps the codebase organized and easier to manage.

## 3. Understanding AI Risk Taxonomy
Duration: 0:07:00

Before diving into quantifying risks, it's essential to understand the different categories and types of AI risks. QuLab categorizes AI risks into five primary dimensions, aligning with common industry practices and regulatory considerations. This step explores the content of `application_pages/page_2_risk_taxonomy.py`.

Navigate to "2. AI Risk Taxonomy" in the sidebar.

```python
# application_pages/page_2_risk_taxonomy.py
import streamlit as st

def main():
    st.markdown("""
    ## <h2 style=\"color:#0A2647;\">2. AI Risk Taxonomy: Understanding the Dimensions</h2>

    AI risks are multifaceted and can manifest across various stages of the AI lifecycle and operational deployment. A structured taxonomy helps in systematically identifying, assessing, and managing these risks.

    We categorize AI risks into the following primary dimensions:

    ### 2.1 Data-Centric Risks
    These risks originate from the data used to train, validate, and operate AI models.
    *   **Data Quality Issues:** Bias, Noise/Errors, Incompleteness.
    *   **Data Privacy & Security:** Sensitive Data Exposure, Inference Attacks.
    *   **Data Drift/Shift:** Concept Drift, Covariate Shift.

    ### 2.2 Model-Centric Risks
    These risks are inherent to the AI model itself, its design, training, and operational characteristics.
    *   **Performance & Reliability:** Inaccuracy, Robustness Issues, Scalability.
    *   **Explainability & Interpretability:** Black Box Nature.
    *   **Hallucinations (Generative AI Specific):** Factual Inaccuracy, Confabulation.

    ### 2.3 System-Centric Risks
    These risks arise from the integration of AI models into broader technical systems and infrastructure.
    *   **Integration Failures:** Compatibility Issues, Dependency Risks.
    *   **Scalability & Latency:** System Overload.
    *   **Security Vulnerabilities:** Model Poisoning, Adversarial Attacks.

    ### 2.4 Human-Centric Risks
    These risks relate to how humans interact with, understand, and are affected by AI systems.
    *   **Misuse & Malicious Use:** Intentional Harm, Unintended Consequences.
    *   **Loss of Human Oversight/Control (Agentic AI Specific):** Autonomy Creep, Goal Mis-specification, Error Propagation.
    *   **Bias & Fairness:** Algorithmic Discrimination.

    ### 2.5 Organizational Risks
    These risks pertain to the organizational structures, processes, and governance surrounding AI development and deployment.
    *   **Regulatory & Compliance Risks:** Non-compliance, Reputational Damage.
    *   **Governance & Accountability:** Lack of Clear Roles, Insufficient Audit Trails.
    *   **Economic & Societal Impact:** Job Displacement, Market Manipulation.
    """))
```

<aside class="positive">
  <b>Key Takeaway:</b> Understanding this taxonomy is fundamental. When evaluating an AI system, a risk manager should systematically consider potential failures across all these dimensions to ensure comprehensive coverage. The distinctions between generative AI specific risks (like hallucinations) and agentic AI specific risks (like autonomy creep) are particularly important in modern AI systems.
</aside>

## 4. Defining Key Risk Metrics
Duration: 0:05:00

To move beyond qualitative descriptions, risks need to be quantified. This section, covered by `application_pages/page_3_risk_metrics.py`, defines the key metrics used throughout QuLab for assessing and comparing AI risks.

Navigate to "3. Defining Key Risk Metrics" in the sidebar.

```python
# application_pages/page_3_risk_metrics.py
import streamlit as st

def main():
    st.markdown(r"""
    ## <h2 style="color:#0A2647;">3. Defining Key Risk Metrics</h2>

    To effectively manage AI risks, it is crucial to define and quantify them using a consistent set of metrics. This allows for objective assessment, comparison, and tracking of risk mitigation efforts.

    ### 3.1 Probability of Risk ($P(Risk)$)
    The probability of risk, often referred to as likelihood, represents the chance or frequency of a specific AI risk event occurring. It is typically expressed as a value between 0 and 1.

    ### 3.2 Impact ($Impact$)
    Impact quantifies the severity of a risk event if it occurs. We consider two forms of impact:
    #### 3.2.1 Qualitative Impact
    Categorical assessment (Critical, High, Medium, Low) based on predefined criteria.
    #### 3.2.2 Monetary Impact ($Impact_{Monetary}$)
    A quantifiable financial estimation of the loss or cost incurred if a risk event materializes, expressed in currency.

    ### 3.3 Cost of Failure ($C_F$)
    The Cost of Failure is a crucial metric that combines the probability of a risk event with its potential monetary impact, providing an expected financial loss.
    The formula for the Cost of Failure is:
    $$C_F = P(Risk) \times Impact_{Monetary}$$

    ### 3.4 Probability Modification for Mitigations ($P_{mitigated}(Risk)$)
    Mitigation strategies reduce the likelihood.
    $$P_{mitigated}(Risk) = P_{baseline}(Risk) \times (1 - Reduction\_Factor_{Likelihood})$$

    ### 3.5 Impact Modification for Mitigations ($Impact_{mitigated}(Monetary)$)
    Mitigation strategies can also reduce the monetary impact.
    $$Impact_{mitigated}(Monetary) = Impact_{baseline}(Monetary) \times (1 - Reduction\_Factor_{Impact})$$
    """))
```

These formulas are the backbone of the risk quantification in QuLab. The $C_F$ metric is particularly important as it allows for an objective, comparable measure of overall risk exposure. The `Reduction_Factor` concepts are key to simulating the effectiveness of mitigation strategies.

## 5. Scenario Selection: Setting the Stage
Duration: 0:04:00

This step, managed by `application_pages/page_4_scenario_selection.py`, is where you select a specific AI risk scenario to analyze. Each scenario simulates a real-world application of Generative AI or Agentic AI, complete with predefined baseline risks and potential mitigation strategies.

Navigate to "4. Scenario Selection" in the sidebar.

```python
# application_pages/page_4_scenario_selection.py
import streamlit as st
import pandas as pd
import numpy as np

@st.cache_data(ttl="2h")
def generate_synthetic_scenarios():
    # ... (scenario data definition) ...
    scenarios = [
        {
            "scenario_id": "LLM_001",
            "scenario_description": "A financial advisory LLM provides incorrect investment advice due to hallucinations...",
            "ai_type": "Generative AI (LLM)",
            "risks": [
                {"risk_name": "Hallucination (Financial Advice)", "baseline_likelihood": 0.5, "baseline_impact_qualitative": "Critical", "baseline_impact_monetary": 5000000},
                # ...
            ],
            "mitigations": [
                {"mitigation_name": "Fact-Checking RAG Integration", "applies_to_risks": ["Hallucination (Financial Advice)"], "likelihood_reduction_factor": 0.6, "impact_reduction_factor": 0.3},
                # ...
            ]
        },
        # ... (other scenarios) ...
    ]
    return scenarios

def main():
    st.markdown("""
    ## <h2 style="color:#0A2647;">4. Scenario Selection: Setting the Stage</h2>
    ...
    """)

    if "scenarios_data" not in st.session_state:
        st.session_state.scenarios_data = generate_synthetic_scenarios()

    scenarios_df = pd.DataFrame([ ... ]) # Prepares scenarios for display

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
            # Clear other session states when scenario changes to ensure a fresh start
            st.session_state.pop("baseline_risks_df", None)
            st.session_state.pop("available_mitigations_df", None)
            st.session_state.pop("user_selected_mitigation_names", None)
            st.session_state.pop("user_selected_mitigations_details", None)
            st.session_state.pop("mitigated_risks_df", None)

        st.session_state.selected_scenario_data = select_scenario_data(
            st.session_state.selected_scenario_id,
            st.session_state.scenarios_data
        )
        st.success(f"Scenario \"{st.session_state.selected_scenario_id}\" selected.")
    # ...
```

<aside class="positive">
  <b>`@st.cache_data` and `st.session_state` Explanation:</b>
  The `generate_synthetic_scenarios` function uses `@st.cache_data`. This decorator tells Streamlit to cache the function's output, meaning it will only run once and store the result. Subsequent calls within a specified `ttl` (time-to-live) will retrieve the cached data, speeding up the application.
  The `st.session_state` is crucial for maintaining the state of the application across user interactions and page navigations. When a scenario is selected, its data (`selected_scenario_data`) is stored in `st.session_state`. If the user changes the scenario, other related session states (like selected mitigations or calculated risks) are explicitly cleared to ensure a clean slate for the new scenario.
</aside>

Select one of the scenarios, for example, `LLM_001`. You'll receive a success message confirming your selection.

## 6. Identifying and Assessing Baseline Risks
Duration: 0:03:00

With a scenario selected, this step (`application_pages/page_5_baseline_risks.py`) focuses on identifying and assessing the inherent risks before any mitigation efforts. It calculates the `baseline_cost_of_failure` for each risk.

Navigate to "5. Identifying Baseline Risks" in the sidebar.

```python
# application_pages/page_5_baseline_risks.py
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
            "risk_name", "baseline_likelihood", "baseline_impact_qualitative",
            "baseline_impact_monetary", "baseline_cost_of_failure"
        ]]
        return risks_df
    return pd.DataFrame()

def main():
    st.markdown("""
    ## <h2 style="color:#0A2647;">5. Identifying and Assessing Baseline Risks</h2>
    ...
    The **Cost of Failure ($C_F$)** is calculated as:
    $$C_F = P(Risk) \times Impact_{Monetary}$$
    """)

    if "selected_scenario_data" in st.session_state and st.session_state.selected_scenario_data:
        st.subheader(f"Baseline Risks for Scenario: {st.session_state.selected_scenario_data['scenario_id']}")
        baseline_risks_df = display_baseline_risk_details(st.session_state.selected_scenario_data)

        if not baseline_risks_df.empty:
            st.dataframe(baseline_risks_df, use_container_width=True, hide_index=True)
            st.session_state.baseline_risks_df = baseline_risks_df
            st.success("Baseline risks loaded and calculated. You can now proceed to visualize them.")
        # ...
    else:
        st.info("Please select a scenario in the '4. Scenario Selection' page to view baseline risks.")
```

The application will display a table of baseline risks, their likelihood, qualitative and monetary impacts, and the calculated Cost of Failure. This table provides a quantitative snapshot of the risks before any interventions.

## 7. Visualizing Baseline Risk Profile
Duration: 0:04:00

Visualizations are powerful tools for understanding complex data. This step, handled by `application_pages/page_6_visualizing_baseline.py`, generates a **Baseline Risk Matrix** to visually represent the initial risk profile.

Navigate to "6. Visualizing Baseline Risk Profile" in the sidebar.

```python
# application_pages/page_6_visualizing_baseline.py
import streamlit as st
import pandas as pd
import matplotlib.pyplot as plt
import seaborn as sns
import numpy as np

def plot_risk_matrix(risk_data_df, title):
    fig, ax = plt.subplots(figsize=(12, 8))
    
    impact_colors = {'Critical': 'darkred', 'High': 'red', 'Medium': 'orange', 'Low': 'lightgreen'}
    risk_data_df['color'] = risk_data_df['baseline_impact_qualitative'].map(impact_colors)
    risk_data_df['baseline_impact_monetary_log'] = np.log1p(risk_data_df['baseline_impact_monetary'])

    scatter = ax.scatter(
        x=risk_data_df['baseline_impact_monetary_log'],
        y=risk_data_df['baseline_likelihood'],
        s=risk_data_df['baseline_cost_of_failure'] / 10000, # Scale size
        c=risk_data_df['color'],
        alpha=0.7,
        edgecolors='w',
        linewidth=0.5
    )

    # Annotate risk names
    for i, row in risk_data_df.iterrows():
        ax.text(row['baseline_impact_monetary_log'] + 0.1, row['baseline_likelihood'], row['risk_name'], fontsize=9)

    ax.set_title(title, fontsize=16)
    ax.set_xlabel("Monetary Impact (Log Scale)", fontsize=12)
    ax.set_ylabel("Likelihood (0-1)", fontsize=12)
    ax.set_ylim(-0.05, 1.05)
    ax.grid(True, linestyle='--', alpha=0.6)

    legend_elements = [ ... ] # Legend for qualitative impact
    ax.legend(handles=legend_elements, title="Qualitative Impact", bbox_to_anchor=(1.05, 1), loc='upper left')
    
    plt.tight_layout()
    return fig

def main():
    st.markdown("""
    ## <h2 style="color:#0A2647;">6. Visualizing Baseline Risk Profile</h2>
    ...
    """)

    if "baseline_risks_df" in st.session_state and not st.session_state.baseline_risks_df.empty:
        st.subheader("Baseline Risk Matrix")
        fig = plot_risk_matrix(st.session_state.baseline_risks_df.copy(), "Baseline AI Risk Matrix")
        st.pyplot(fig)
        st.success("Baseline risk matrix visualized. You can now propose mitigation strategies.")
    else:
        st.info("Please go to the '5. Identifying Baseline Risks' page to assess and load baseline risks first.")
```

The risk matrix uses:
*   **X-axis:** Monetary Impact (transformed to a logarithmic scale using `np.log1p` for better visualization of wide ranges).
*   **Y-axis:** Likelihood (0-1).
*   **Color of points:** Represents the qualitative impact (Critical, High, Medium, Low).
*   **Size of points:** Corresponds to the calculated **Cost of Failure**. Larger points indicate risks with higher expected financial losses.

This plot immediately highlights which risks are most critical based on their combined likelihood, impact, and overall cost of failure.

## 8. Proposing Mitigation Strategies
Duration: 0:04:00

Once you understand the baseline risks, the next step is to propose and select mitigation strategies. This is done in `application_pages/page_7_proposing_mitigations.py`.

Navigate to "7. Proposing Mitigation Strategies" in the sidebar.

```python
# application_pages/page_7_proposing_mitigations.py
import streamlit as st
import pandas as pd

def display_available_mitigations_for_scenario(scenario_data):
    if scenario_data and "mitigations" in scenario_data:
        mitigations_df = pd.DataFrame(scenario_data["mitigations"])
        mitigations_df = mitigations_df[[
            "mitigation_name", "applies_to_risks",
            "likelihood_reduction_factor", "impact_reduction_factor"
        ]]
        return mitigations_df
    return pd.DataFrame()

def main():
    st.markdown("""
    ## <h2 style="color:#0A2647;">7. Proposing Mitigation Strategies</h2>
    ...
    """)

    if "selected_scenario_data" in st.session_state and st.session_state.selected_scenario_data:
        st.subheader(f"Available Mitigation Strategies for Scenario: {st.session_state.selected_scenario_data['scenario_id']}")
        available_mitigations_df = display_available_mitigations_for_scenario(st.session_state.selected_scenario_data)

        if not available_mitigations_df.empty:
            st.dataframe(available_mitigations_df, use_container_width=True, hide_index=True)
            st.session_state.available_mitigations_df = available_mitigations_df

            mitigation_options = available_mitigations_df["mitigation_name"].tolist()
            if "user_selected_mitigation_names" not in st.session_state:
                st.session_state.user_selected_mitigation_names = []

            selected_mitigation_names = st.multiselect(
                label="Select Mitigation Strategies to Apply",
                options=mitigation_options,
                default=st.session_state.user_selected_mitigation_names,
                key="mitigation_selector",
                help="Choose one or more strategies to reduce risks. Their effects will be simulated."
            )

            st.session_state.user_selected_mitigation_names = selected_mitigation_names

            if selected_mitigation_names:
                st.session_state.user_selected_mitigations_details = available_mitigations_df[
                    available_mitigations_df["mitigation_name"].isin(selected_mitigation_names)
                ].to_dict(orient="records")
                st.success(f"Selected {len(selected_mitigation_names)} mitigation(s).")
            # ...
        # ...
    # ...
```

The page displays a table of available mitigation strategies for your selected scenario. Each mitigation is described by its name, the risks it applies to, and its estimated `likelihood_reduction_factor` and `impact_reduction_factor`.

Use the multi-select widget to choose one or more mitigation strategies. The `likelihood_reduction_factor` and `impact_reduction_factor` are percentages (0-1) representing how much a mitigation is expected to reduce the likelihood and monetary impact of a risk.

<aside class="negative">
  <b>Important Note on Combined Reductions:</b>
  If multiple selected mitigations apply to the same risk, their reduction factors are combined multiplicatively, not additively. For example, if Mitigation A reduces likelihood by 20% (factor 0.2) and Mitigation B reduces likelihood by 30% (factor 0.3) for the same risk, the total reduction is not 50%. Instead, the likelihood is reduced by $1 - (1 - 0.2) \times (1 - 0.3) = 1 - 0.8 \times 0.7 = 1 - 0.56 = 0.44$, or 44%. This reflects a more realistic scenario where reductions become less effective as the risk approaches zero.
</aside>

Select a few mitigations that you think will significantly reduce the risks in your chosen scenario.

## 9. Simulating Mitigation Outcomes: Reduced Risk
Duration: 0:04:00

After selecting mitigation strategies, this step (`application_pages/page_8_simulating_outcomes.py`) simulates their combined effects on the baseline risks to produce a "mitigated" risk profile.

Navigate to "8. Simulating Mitigation Outcomes" in the sidebar.

```python
# application_pages/page_8_simulating_outcomes.py
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
        effective_likelihood_survival_factor = 1.0 # (1 - total_likelihood_reduction)
        effective_impact_survival_factor = 1.0     # (1 - total_impact_reduction)

        for mitigation in selected_mitigations_details:
            if risk_name in mitigation["applies_to_risks"]:
                effective_likelihood_survival_factor *= (1 - mitigation["likelihood_reduction_factor"])
                effective_impact_survival_factor *= (1 - mitigation["impact_reduction_factor"])
        
        mitigated_likelihood = risk["baseline_likelihood"] * effective_likelihood_survival_factor
        mitigated_impact_monetary = risk["baseline_impact_monetary"] * effective_impact_survival_factor
        
        mitigated_risks_df.loc[index, "mitigated_likelihood"] = max(0.0, min(1.0, mitigated_likelihood))
        mitigated_risks_df.loc[index, "mitigated_impact_monetary"] = max(0.0, mitigated_impact_monetary)

    mitigated_risks_df["mitigated_cost_of_failure"] = mitigated_risks_df.apply(
        lambda row: calculate_cost_of_failure(row["mitigated_likelihood"], row["mitigated_impact_monetary"]),
        axis=1
    )
    
    # Re-evaluate qualitative impact based on new monetary thresholds
    def get_mitigated_qualitative_impact(monetary_impact):
        if monetary_impact >= 2000000: return "Critical"
        elif monetary_impact >= 1000000: return "High"
        elif monetary_impact >= 500000: return "Medium"
        else: return "Low"
    mitigated_risks_df["mitigated_impact_qualitative"] = mitigated_risks_df["mitigated_impact_monetary"].apply(get_mitigated_qualitative_impact)

    return mitigated_risks_df[[
        "risk_name", "baseline_likelihood", "mitigated_likelihood",
        "baseline_impact_qualitative", "mitigated_impact_qualitative",
        "baseline_impact_monetary", "mitigated_impact_monetary",
        "baseline_cost_of_failure", "mitigated_cost_of_failure"
    ]]

def main():
    st.markdown("""
    ## <h2 style="color:#0A2647;">8. Simulating Mitigation Outcomes: Reduced Risk</h2>
    ...
    """)

    if st.button("Simulate Mitigations", help="Calculate the effects of selected mitigation strategies."):
        with st.spinner("Simulating mitigation outcomes..."):
            mitigated_risks_df = apply_selected_mitigations(
                st.session_state.baseline_risks_df,
                st.session_state.user_selected_mitigations_details
            )
            st.session_state.mitigated_risks_df = mitigated_risks_df
            st.success("Mitigation simulation complete!")
    
    if "mitigated_risks_df" in st.session_state and not st.session_state.mitigated_risks_df.empty:
        st.subheader("Mitigated Risk Details")
        st.dataframe(st.session_state.mitigated_risks_df, use_container_width=True, hide_index=True)
    # ...
```

Click the "Simulate Mitigations" button. The application will compute the new `mitigated_likelihood`, `mitigated_impact_monetary`, and `mitigated_cost_of_failure` for each risk, taking into account all selected mitigations and their multiplicative effects. The qualitative impact is also re-evaluated based on adjusted monetary thresholds.

The resulting table provides a side-by-side comparison of baseline and mitigated values, allowing you to see the direct impact of your chosen strategies.

## 10. Comparative Risk Visualization: Before and After Mitigations
Duration: 0:04:00

To get an intuitive understanding of the mitigation's effectiveness, this step (`application_pages/page_9_comparative_visualization.py`) generates comparative bar charts illustrating the reduction in likelihood and cost of failure.

Navigate to "9. Comparative Risk Visualization" in the sidebar.

```python
# application_pages/page_9_comparative_visualization.py
import streamlit as st
import pandas as pd
import matplotlib.pyplot as plt
import seaborn as sns

def plot_comparative_risk(baseline_df, mitigated_df):
    comparison_df = pd.merge(
        baseline_df[['risk_name', 'baseline_likelihood', 'baseline_cost_of_failure']],
        mitigated_df[['risk_name', 'mitigated_likelihood', 'mitigated_cost_of_failure']],
        on='risk_name',
        how='inner'
    )

    fig, axes = plt.subplots(1, 2, figsize=(18, 7))
    plt.style.use('seaborn-v0_8-darkgrid')

    # Likelihood Comparison Bar Chart
    likelihood_melted = comparison_df.melt(
        id_vars='risk_name', value_vars=['baseline_likelihood', 'mitigated_likelihood'],
        var_name='Risk Type', value_name='Likelihood'
    )
    sns.barplot(ax=axes[0], x='risk_name', y='Likelihood', hue='Risk Type', data=likelihood_melted,
                palette={"baseline_likelihood": "skyblue", "mitigated_likelihood": "lightcoral"})
    axes[0].set_title('Likelihood Comparison: Baseline vs. Mitigated')
    axes[0].tick_params(axis='x', rotation=45, ha='right')
    axes[0].set_ylim(0, 1.0)

    # Cost of Failure Comparison Bar Chart
    cost_melted = comparison_df.melt(
        id_vars='risk_name', value_vars=['baseline_cost_of_failure', 'mitigated_cost_of_failure'],
        var_name='Cost Type', value_name='Cost of Failure'
    )
    sns.barplot(ax=axes[1], x='risk_name', y='Cost of Failure', hue='Cost Type', data=cost_melted,
                palette={"baseline_cost_of_failure": "mediumseagreen", "mitigated_cost_of_failure": "gold"})
    axes[1].set_title('Cost of Failure Comparison: Baseline vs. Mitigated')
    axes[1].tick_params(axis='x', rotation=45, ha='right')
    axes[1].yaxis.set_major_formatter(plt.FuncFormatter(lambda x, p: f"${x:,.0f}"))

    plt.tight_layout()
    return fig

def main():
    st.markdown("""
    ## <h2 style="color:#0A2647;">9. Comparative Risk Visualization: Before and After Mitigations</h2>
    ...
    """)

    if st.button("Plot Comparative Risks", help="Generate bar charts comparing baseline and mitigated risks."):
        with st.spinner("Generating comparative risk charts..."):
            fig = plot_comparative_risk(st.session_state.baseline_risks_df, st.session_state.mitigated_risks_df)
            st.pyplot(fig)
            st.success("Comparative risk charts generated.")
    # ...
```

Click the "Plot Comparative Risks" button. You will see two bar charts:
*   **Likelihood Comparison:** Shows the `baseline_likelihood` vs. `mitigated_likelihood` for each risk.
*   **Cost of Failure Comparison:** Shows the `baseline_cost_of_failure` vs. `mitigated_cost_of_failure`.

These charts clearly illustrate the quantitative reduction achieved by your selected mitigation strategies. A noticeable drop in the mitigated bars compared to the baseline bars signifies effective risk reduction.

## 11. Updated Risk Matrix: Seeing the Shift
Duration: 0:05:00

While bar charts show aggregated reductions, a comparative risk matrix provides a granular view of how each individual risk has shifted. This step (`application_pages/page_10_updated_risk_matrix.py`) generates a specialized scatter plot.

Navigate to "10. Updated Risk Matrix" in the sidebar.

```python
# application_pages/page_10_updated_risk_matrix.py
import streamlit as st
import pandas as pd
import matplotlib.pyplot as plt
import seaborn as sns
import numpy as np

def plot_risk_matrix_comparison(baseline_df, mitigated_df, title):
    fig, ax = plt.subplots(figsize=(14, 9))
    
    impact_colors = {'Critical': 'darkred', 'High': 'red', 'Medium': 'orange', 'Low': 'lightgreen'}
    
    baseline_df['baseline_impact_monetary_log'] = np.log1p(baseline_df['baseline_impact_monetary'])
    mitigated_df['mitigated_impact_monetary_log'] = np.log1p(mitigated_df['mitigated_impact_monetary'])

    comparison_df = pd.merge( # Merge baseline and mitigated data
        baseline_df[['risk_name', 'baseline_likelihood', 'baseline_impact_monetary_log', 'baseline_cost_of_failure', 'baseline_impact_qualitative']],
        mitigated_df[['risk_name', 'mitigated_likelihood', 'mitigated_impact_monetary_log', 'mitigated_cost_of_failure', 'mitigated_impact_qualitative']],
        on='risk_name',
        how='inner'
    )

    # Plot baseline risks (circles) and mitigated risks (X markers)
    for i, row in comparison_df.iterrows():
        ax.scatter( # Baseline
            x=row['baseline_impact_monetary_log'], y=row['baseline_likelihood'],
            s=row['baseline_cost_of_failure'] / 10000, color=impact_colors.get(row['baseline_impact_qualitative'], 'grey'),
            marker='o', alpha=0.6, edgecolors='black', linewidth=0.5, label='Baseline' if i == 0 else ""
        )
        ax.text(row['baseline_impact_monetary_log'] + 0.1, row['baseline_likelihood'], f"{row['risk_name']} (B)", fontsize=8, color=impact_colors.get(row['baseline_impact_qualitative'], 'grey'))

        ax.scatter( # Mitigated
            x=row['mitigated_impact_monetary_log'], y=row['mitigated_likelihood'],
            s=row['mitigated_cost_of_failure'] / 10000, color=impact_colors.get(row['mitigated_impact_qualitative'], 'grey'),
            marker='X', alpha=0.8, edgecolors='black', linewidth=0.5, label='Mitigated' if i == 0 else ""
        )
        ax.text(row['mitigated_impact_monetary_log'] + 0.1, row['mitigated_likelihood'], f"{row['risk_name']} (M)", fontsize=8, color=impact_colors.get(row['mitigated_impact_qualitative'], 'grey'))

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
    ax.set_ylim(-0.05, 1.05)
    ax.grid(True, linestyle='--', alpha=0.6)

    # Custom legends for markers and qualitative impact
    legend_elements_markers = [ ... ]
    legend_elements_qualitative = [ ... ]
    first_legend = ax.legend(handles=legend_elements_markers, title="Risk State", loc='upper left', bbox_to_anchor=(1.05, 1))
    ax.add_artist(first_legend)
    ax.legend(handles=legend_elements_qualitative, title="Qualitative Impact", loc='lower left', bbox_to_anchor=(1.05, 0))

    # Formatting x-axis ticks for monetary values
    current_xticks = ax.get_xticks()
    x_ticks_labels = []
    for tick_val in current_xticks:
        if tick_val >= 0:
            original_value = np.expm1(tick_val) # Inverse of log1p
            if original_value >= 1_000_000: x_ticks_labels.append(f"${original_value/1_000_000:.0f}M")
            elif original_value >= 1_000: x_ticks_labels.append(f"${original_value/1_000:.0f}K")
            else: x_ticks_labels.append(f"${original_value:.0f}")
        else: x_ticks_labels.append("")
    ax.set_xticklabels(x_ticks_labels)

    plt.tight_layout()
    return fig

def main():
    st.markdown("""
    ## <h2 style="color:#0A2647;">10. Updated Risk Matrix: Seeing the Shift</h2>
    ...
    """)

    if st.button("Plot Risk Matrix Comparison", help="Generate a scatter plot showing the shift from baseline to mitigated risks."):
        with st.spinner("Generating comparative risk matrix..."):
            fig = plot_risk_matrix_comparison(
                st.session_state.baseline_risks_df.copy(),
                st.session_state.mitigated_risks_df.copy(),
                f"AI Risk Matrix Comparison: {st.session_state.selected_scenario_id}"
            )
            st.pyplot(fig)
            st.success("Comparative risk matrix generated.")
    # ...
```

Click the "Plot Risk Matrix Comparison" button. This visualization is key to understanding the full impact of your mitigation strategies:
*   **Circles (`o`):** Represent the baseline position of each risk.
*   **Crosses (`X`):** Represent the mitigated position of each risk.
*   **Arrows:** Connect each baseline risk to its mitigated counterpart, clearly showing the direction and magnitude of the shift.
*   **Color and Size:** Still reflect the qualitative impact and Cost of Failure, but now for both baseline and mitigated states.

This matrix allows you to immediately identify risks that have significantly moved towards a lower likelihood and impact, as well as those that remain in high-risk zones, even after mitigations.

## 12. Remaining Risks & New Challenges
Duration: 0:03:00

Even with effective mitigation strategies, some risks may persist, and new challenges can emerge. This final analytical step (`application_pages/page_11_remaining_risks.py`) provides a summary of the residual risks and prompts reflection on further considerations.

Navigate to "11. Remaining Risks & New Challenges" in the sidebar.

```python
# application_pages/page_11_remaining_risks.py
import streamlit as st
import pandas as pd

def summarize_post_mitigation_risks(mitigated_risk_data_df):
    summary_text = []

    if mitigated_risk_data_df.empty: return "No mitigated risks to summarize."

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

    total_baseline_cost = mitigated_risk_data_df["baseline_cost_of_failure"].sum()
    total_mitigated_cost = mitigated_risk_data_df["mitigated_cost_of_failure"].sum()

    if total_baseline_cost > 0:
        reduction_percentage = ((total_baseline_cost - total_mitigated_cost) / total_baseline_cost) * 100
        summary_text.append(f"\n### Overall Risk Reduction:")
        summary_text.append(f"The total expected Cost of Failure across all risks has been reduced from `${total_baseline_cost:,d}` to `${total_mitigated_cost:,d}`, representing a **{reduction_percentage:.2f}% reduction**.")

    summary_text.append("\n### Potential New Challenges/Considerations:")
    summary_text.append("- **Implementation Cost:** What are the financial and operational costs associated with implementing the chosen mitigations?")
    summary_text.append("- **New Risks Introduced:** Could any of the implemented mitigations introduce new, unforeseen risks?")
    summary_text.append("- **Monitoring & Review:** Continuous monitoring is required to ensure mitigations remain effective and new risks are identified.")
    
    return "\n".join(summary_text)

def main():
    st.markdown("""
    ## <h2 style="color:#0A2647;">11. Remaining Risks & New Challenges</h2>
    ...
    """)

    if st.button("Summarize Remaining Risks", help="Provide a textual summary of risks after mitigation."):
        with st.spinner("Generating summary..."):
            summary = summarize_post_mitigation_risks(st.session_state.mitigated_risks_df)
            st.markdown(summary)
            st.success("Summary generated.")
    # ...
```

Click the "Summarize Remaining Risks" button. The application will generate a textual summary that includes:
*   **Residual Risks:** Lists any risks that still have a "High" or "Critical" qualitative impact, even after mitigations. This highlights areas requiring further attention or acceptance.
*   **Overall Risk Reduction:** Provides the total percentage reduction in the expected Cost of Failure across all risks.
*   **Potential New Challenges/Considerations:** Prompts you to think about broader implications, such as the actual cost of implementing mitigations, the possibility of new risks being introduced, and the necessity of ongoing monitoring.

<aside class="positive">
  <b>Important Principle:</b> Risk management is an iterative process. It's rarely about eliminating all risks but rather reducing them to an acceptable level and continuously monitoring for new threats or changes in existing ones.
</aside>

## 13. Reset Scenario for Re-experimentation
Duration: 0:02:00

To facilitate further experimentation or to start a new analysis from scratch, QuLab provides a "Reset Scenario" functionality, implemented in `application_pages/page_12_reset_scenario.py`.

Navigate to "12. Reset Scenario" in the sidebar.

```python
# application_pages/page_12_reset_scenario.py
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
    
    st.success("Scenario state has been reset! You can now select a new scenario and restart the analysis.")
    st.rerun() # Rerun the app to reflect the cleared state

def main():
    st.markdown("""
    ## <h2 style="color:#0A2647;">12. Reset Scenario for Re-experimentation</h2>
    ...
    """)

    st.subheader("Reset Application State")
    if st.button("Reset Scenario", help="Clear all scenario data and selections to start fresh."):
        reset_current_scenario_state()
```

Click the "Reset Scenario" button. This action will clear all relevant variables stored in Streamlit's `st.session_state`, effectively resetting the application to its initial state. You will be redirected to the "1. Introduction" page, allowing you to select a new scenario and begin the risk analysis process anew.

This functionality is invaluable for developers and risk managers who want to:
*   Experiment with different mitigation strategies for the same scenario.
*   Analyze different AI risk scenarios.
*   Ensure that no previous selections interfere with a new analysis.

Congratulations! You have successfully navigated and explored the functionalities of QuLab, gaining practical insights into AI risk assessment, quantification, and mitigation using an interactive Streamlit application. This foundation will empower you to approach AI risk management with greater confidence and analytical rigor.
