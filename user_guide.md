id: 692615a9a03c15c77f5897f8_user_guide
summary: Lab 1: Principles of AI Risk and Assurance User Guide
feedback link: https://docs.google.com/forms/d/e/1FAIpQLSfWkOK-in_bMMoHSZfcIvAeO58PAH9wrDqcxnJABHaxiDqhSA/viewform?usp=sf_link
environments: Web
status: Published
# QuLab: AI Risk and Assurance Lab User Guide

## 1. Welcome to QuLab: Understanding AI Risk and Assurance
Duration: 00:05

<aside class="positive">
This introductory step provides essential context for the lab, highlighting its importance and what you will learn.
</aside>

Welcome to **QuLab: AI Risk and Assurance Lab**! In today's rapidly evolving technological landscape, Artificial Intelligence (AI) systems, especially Generative AI and Agentic AI, introduce novel and complex risks. Understanding, quantifying, and mitigating these risks is paramount for responsible AI deployment. This interactive sandbox is specifically designed for Risk Managers and anyone interested in gaining practical experience with AI risk management.

Through this lab, you will not only identify different categories of AI risks but also learn how to quantify their potential impact, experiment with various mitigation strategies, and visualize the effectiveness of your decisions. You will also become familiar with key AI risk concepts like `hallucinations` (where an AI invents facts), `goal mis-specification` (when an AI's objective leads to unintended outcomes), `autonomy creep` (AI systems gaining more control than intended), and `human-in-the-loop` (the necessity of human oversight).

This guide will walk you through each section of the QuLab application, helping you leverage its functionalities to explore the multifaceted world of AI risks.

To begin, ensure you are on the "1. Introduction" page in the application's sidebar. This page provides an overview of the lab's key learning objectives, which mirror the concepts we will cover together.

## 2. Exploring the AI Risk Taxonomy
Duration: 00:07

<aside class="positive">
A structured understanding of AI risk categories is fundamental to effective risk management. This step breaks down where different types of risks originate.
</aside>

Before we can manage AI risks, we need to understand what they are and where they come from. AI risks are diverse and can emerge at various points in an AI system's lifecycle. The QuLab application provides a clear taxonomy to help you categorize these risks systematically.

Navigate to the "2. AI Risk Taxonomy" page using the sidebar. Here, you will find a detailed breakdown of AI risks across five primary dimensions:

*   **Data-Centric Risks:** These risks stem from the data used by AI. Think about `Bias` in training data, which can lead to unfair outcomes, or `Data Privacy & Security` issues, where sensitive information might be exposed. `Data Drift/Shift` refers to changes in data patterns over time, which can make a once-accurate model less reliable.
*   **Model-Centric Risks:** These are risks inherent to the AI model itself. This includes `Inaccuracy` (the model making wrong predictions) or `Robustness Issues` (the model being easily fooled). For Generative AI, a key risk is `Hallucinations`, where the model generates factually incorrect but convincing information.
*   **System-Centric Risks:** These risks arise from how the AI model integrates into a larger technical system. This could involve `Integration Failures` with existing infrastructure or `Security Vulnerabilities` like model poisoning.
*   **Human-Centric Risks:** These focus on the interaction between humans and AI. Concepts like `Autonomy Creep` (an AI system gradually taking more decisions without human intervention) and `Goal Mis-specification` (the AI achieving its programmed goal but with undesirable real-world consequences) are crucial for Agentic AI. `Error Propagation` can occur when a small error by an autonomous agent cascades into a larger system failure.
*   **Organizational Risks:** These relate to the broader governance, compliance, and societal impacts. `Regulatory & Compliance Risks` (e.g., failure to meet legal standards) and `Reputational Damage` are significant concerns for any organization deploying AI.

Familiarize yourself with these categories, as they form the basis for identifying specific risks in our scenarios.

## 3. Defining Key Metrics for AI Risk Quantification
Duration: 00:08

<aside class="positive">
Quantifying risks allows for objective assessment and prioritization. This step introduces the mathematical concepts behind how we measure risk in this lab.
</aside>

To move beyond qualitative descriptions, we need to quantify AI risks. This allows for objective comparisons, prioritization of efforts, and tracking of improvements. The QuLab uses a set of standard risk metrics.

Go to the "3. Defining Key Risk Metrics" page in the sidebar. Here, the application explains the core metrics:

*   **Probability of Risk ($P(Risk)$):** This is the likelihood of a risk event occurring, expressed as a value between 0 (impossible) and 1 (certain). The application often maps these to qualitative terms like "Very Low" to "Very High."
*   **Impact ($Impact$):** This measures the severity if a risk occurs.
    *   **Qualitative Impact:** A categorical assessment (e.g., Critical, High, Medium, Low) based on factors like reputational damage, regulatory fines, or harm to individuals.
    *   **Monetary Impact ($Impact_{Monetary}$):** A financial estimate of the loss in a specific currency (e.g., USD) if the risk materializes.
*   **Cost of Failure ($C_F$):** This is perhaps the most important metric for prioritization. It calculates the expected financial loss by combining the probability and monetary impact.
    $$C_F = P(Risk) \times Impact_{Monetary}$$
    A higher Cost of Failure indicates a more critical risk in financial terms.
*   **Probability Modification for Mitigations ($P_{mitigated}(Risk)$):** When you apply mitigation strategies, they reduce the likelihood of a risk. The new probability is calculated by applying a `likelihood_reduction_factor` to the baseline probability.
    $$P_{mitigated}(Risk) = P_{baseline}(Risk) \times (1 - Reduction\_Factor_{Likelihood})$$
*   **Impact Modification for Mitigations ($Impact_{mitigated}(Monetary)$):** Similarly, mitigations can also reduce the financial impact if a risk still occurs, using an `impact_reduction_factor`.
    $$Impact_{mitigated}(Monetary) = Impact_{baseline}(Monetary) \times (1 - Reduction\_Factor_{Impact})$$

Understanding these metrics is crucial for interpreting the simulation results later in the lab.

## 4. Selecting an AI Risk Scenario
Duration: 00:03

<aside class="positive">
This is your first interactive step! Choosing a scenario sets the foundation for your AI risk analysis.
</aside>

Now that we understand the types of risks and how to quantify them, it's time to put that knowledge into practice by selecting a real-world (simulated) scenario.

Navigate to the "4. Scenario Selection" page.

You will see a table outlining several predefined AI risk scenarios. Each scenario describes a situation involving either Generative AI (like an LLM providing financial advice) or Agentic AI (like an autonomous supply chain agent). These scenarios come with a set of baseline risks and potential mitigation strategies.

1.  **Review the Scenarios:** Look at the `scenario_description` and `ai_type` for each available scenario.
2.  **Select a Scenario:** Use the `Select an AI Risk Scenario` dropdown menu to choose the scenario you wish to analyze. For instance, you could start with "LLM_001: A financial advisory LLM provides incorrect investment advice..."
3.  Once selected, the application will confirm your choice with a success message. This action loads the specific risks and mitigations associated with that scenario into the application's memory for subsequent steps.

<aside class="negative">
If you change the scenario later, all your previous selections and calculations will be reset to ensure a clean analysis for the new scenario.
</aside>

## 5. Identifying and Assessing Baseline Risks
Duration: 00:05

<aside class="positive">
This step reveals the initial risk landscape for your chosen scenario, providing a clear picture of potential threats before any intervention.
</aside>

With a scenario chosen, the next logical step is to understand the risks inherent to that scenario **before** we try to manage them. These are called "baseline risks."

Navigate to the "5. Identifying Baseline Risks" page.

On this page, the application will display a table detailing all the baseline risks associated with your selected scenario. For each risk, you will see:

*   `risk_name`: A descriptive name for the risk (e.g., "Hallucination (Financial Advice)").
*   `baseline_likelihood`: The initial probability of the risk occurring.
*   `baseline_impact_qualitative`: The initial severity described in categories (e.g., Critical, High).
*   `baseline_impact_monetary`: The initial financial cost if the risk materializes.
*   `baseline_cost_of_failure`: The calculated expected financial loss ($C_F$) for that risk, using the formula $C_F = P(Risk) \times Impact_{Monetary}$.

Review this table carefully. The `baseline_cost_of_failure` column is particularly important as it helps you identify which risks are financially most significant *before* any mitigations. These are the risks that typically require the most urgent attention.

## 6. Visualizing the Baseline Risk Profile
Duration: 00:05

<aside class="positive">
Visualizations transform complex data into easily understandable insights, making risk identification and prioritization more intuitive.
</aside>

Tables provide detailed data, but a visual representation can often convey the overall risk profile much more effectively.

Navigate to the "6. Visualizing Baseline Risk Profile" page.

Here, the application generates a **Baseline AI Risk Matrix**. This is a powerful scatter plot that visualizes all the baseline risks simultaneously:

*   **X-axis (Monetary Impact):** Shows the potential financial loss, presented on a logarithmic scale to better display risks with a wide range of monetary impacts.
*   **Y-axis (Likelihood):** Shows the probability of the risk occurring, from 0 to 1.
*   **Color of Points:** Each risk point is colored according to its `qualitative_impact` (e.g., dark red for Critical, light green for Low).
*   **Size of Points:** The size of each point is scaled by its `baseline_cost_of_failure`. Larger points indicate risks with higher expected financial losses.

This matrix allows you to quickly identify "high-risk" areas – risks that are high on the Y-axis, far to the right on the X-axis, and represented by large, dark-colored points. These are the risks demanding the most attention for mitigation.

## 7. Proposing Mitigation Strategies
Duration: 00:07

<aside class="positive">
This is where you become the risk manager! Selecting strategies to reduce risks is a core part of effective AI governance.
</aside>

Once you understand your baseline risks, the next step is to choose how you will address them. This involves selecting appropriate **mitigation strategies**.

Navigate to the "7. Proposing Mitigation Strategies" page.

You will find a table listing all the available mitigation strategies for your selected scenario. For each mitigation, you'll see:

*   `mitigation_name`: The name of the strategy (e.g., "Fact-Checking RAG Integration").
*   `applies_to_risks`: Which specific baseline risks this mitigation is designed to address.
*   `likelihood_reduction_factor`: The estimated percentage reduction in the likelihood of the risk(s) it applies to (e.g., 0.6 means a 60% reduction).
*   `impact_reduction_factor`: The estimated percentage reduction in the monetary impact of the risk(s) it applies to (e.g., 0.3 means a 30% reduction).

Below the table, use the `Select Mitigation Strategies to Apply` multi-select dropdown. Here, you can choose one or more mitigation strategies. As you select them:

*   The application will store your choices.
*   Remember that multiple mitigations applying to the same risk will have their reduction factors combined multiplicatively. For example, if two mitigations both reduce likelihood by 20%, the combined effect is $1 - (1-0.2) \times (1-0.2) = 1 - 0.8 \times 0.8 = 1 - 0.64 = 0.36$, or a 36% reduction, not 40%. This reflects a more realistic compounding effect.

Choose the mitigations you believe will be most effective in reducing the risks identified in the previous steps.

## 8. Simulating Mitigation Outcomes
Duration: 00:05

<aside class="positive">
See the tangible impact of your chosen mitigation strategies. This step quantifies the "after" picture of your risk profile.
</aside>

After selecting your mitigation strategies, it's time to see their theoretical impact on your risk profile. This simulation will show you the "mitigated" risk values.

Navigate to the "8. Simulating Mitigation Outcomes" page.

You will see a button labeled "Simulate Mitigations." Click this button.

The application will then apply your selected mitigation strategies to the baseline risks. For each risk, it will calculate:

*   `mitigated_likelihood`: The new probability of the risk occurring after mitigations.
*   `mitigated_impact_monetary`: The new monetary impact if the risk occurs after mitigations.
*   `mitigated_impact_qualitative`: The new qualitative impact, which is re-evaluated based on the new `mitigated_impact_monetary` using the following thresholds:
    *   Monetary Impact $\ge \$2M$: **Critical**
    *   Monetary Impact $\ge \$1M$: **High**
    *   Monetary Impact $\ge \$0.5M$: **Medium**
    *   Else: **Low**
*   `mitigated_cost_of_failure`: The new expected financial loss ($C_F$) after mitigations.

A table displaying these mitigated risk details will appear. Compare these values with the baseline risks you saw earlier to understand the effectiveness of your chosen strategies. You should observe a reduction in likelihood, monetary impact, and especially the cost of failure for the risks targeted by your mitigations.

## 9. Comparative Risk Visualization
Duration: 00:05

<aside class="positive">
Visual comparisons help instantly grasp the effectiveness of your mitigation efforts across different risk dimensions.
</aside>

While tables show precise numbers, visual charts can highlight the changes brought about by your mitigations more intuitively.

Navigate to the "9. Comparative Risk Visualization" page.

You will find a button labeled "Plot Comparative Risks." Click this button.

The application will generate two side-by-side bar charts:

1.  **Likelihood Comparison:** This chart compares the `baseline_likelihood` and `mitigated_likelihood` for each risk. You should see a noticeable drop in the height of the mitigated bars compared to the baseline bars, indicating successful likelihood reduction.
2.  **Cost of Failure Comparison:** This chart compares the `baseline_cost_of_failure` and `mitigated_cost_of_failure`. Since the Cost of Failure combines both likelihood and monetary impact, a significant reduction here signifies effective overall risk management.

These visualizations provide an immediate assessment of how well your chosen strategies have performed in reducing the expected impact and probability of each risk.

## 10. Understanding the Updated Risk Matrix
Duration: 00:06

<aside class="positive">
This advanced visualization allows you to see the "journey" of each risk from its baseline state to its mitigated state, offering a holistic view of your risk landscape.
</aside>

Beyond simple comparisons, it's highly beneficial to see the shift in the entire risk profile on a single, comprehensive visualization.

Navigate to the "10. Updated Risk Matrix" page.

You will see a button labeled "Plot Risk Matrix Comparison." Click this button.

The application will generate an updated risk matrix, which is a specialized scatter plot showing both the original and the mitigated positions of each risk:

*   **Baseline Risks:** These are marked with 'o' (circles), representing the initial state.
*   **Mitigated Risks:** These are marked with 'X', representing the state after applying your chosen mitigations.
*   **Arrows:** Crucially, an arrow connects each baseline risk point to its corresponding mitigated risk point. These arrows visually demonstrate the "shift" or reduction achieved in both likelihood (Y-axis) and monetary impact (X-axis).
*   **Color and Size:** The color still represents qualitative impact, dynamically updated for mitigated risks, and the size still indicates the Cost of Failure (baseline for 'o', mitigated for 'X').

This visualization is incredibly powerful for understanding the overall transformation of your risk landscape. You can clearly see which risks have moved from high-likelihood, high-impact areas towards lower-risk zones, and which might still remain problematic.

## 11. Identifying Remaining Risks and New Challenges
Duration: 00:04

<aside class="positive">
Risk management is an ongoing process. This step helps you identify what still needs attention and anticipates future considerations.
</aside>

Even with the best mitigation strategies, it's rare to eliminate all risks. Some will remain as "residual risks," and new challenges might even be introduced by the mitigation efforts themselves.

Navigate to the "11. Remaining Risks & New Challenges" page.

You will find a button labeled "Summarize Remaining Risks." Click this button.

The application will generate a textual summary, focusing on:

*   **Residual Risks with High or Critical Impact:** This section will highlight any risks that, even after your chosen mitigations, still have a `High` or `Critical` qualitative impact, along with their mitigated likelihood, monetary impact, and cost of failure. These are the risks that may require further attention or alternative strategies.
*   **Overall Risk Reduction:** A quantitative summary of the total expected Cost of Failure across all risks before and after mitigations, showing the percentage reduction achieved. This provides a high-level measure of your success.
*   **Potential New Challenges/Considerations:** This section offers illustrative points about broader aspects of risk management, such as the `Implementation Cost` of mitigations, the possibility of `New Risks Introduced` by complex solutions, and the need for `Monitoring & Review` to ensure ongoing effectiveness.

This summary is vital for understanding that risk management is not a one-time activity but a continuous cycle of assessment, mitigation, and monitoring.

## 12. Resetting the Scenario
Duration: 00:02

<aside class="positive">
This utility step allows you to easily restart your analysis, facilitating experimentation with different scenarios or mitigation approaches.
</aside>

To encourage experimentation and allow you to explore different scenarios or mitigation strategies, the QuLab provides a simple way to reset the application state.

Navigate to the "12. Reset Scenario" page.

You will see a button labeled "Reset Scenario." Click this button.

Confirm your action, and the application will clear all your previous selections (scenario, chosen mitigations) and calculated results. The application will then return to an initial state, effectively restarting the entire process.

This feature is particularly useful if you want to:

*   Select a different AI risk scenario from the beginning.
*   Experiment with a completely different set of mitigation strategies for the same scenario.
*   Simply start over with a clean slate.

You can now return to "4. Scenario Selection" and begin a new AI risk analysis journey!
