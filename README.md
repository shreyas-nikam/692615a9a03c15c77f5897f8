# QuLab: AI Risk and Assurance Lab

<p align="center">
  <img src="https://www.quantuniversity.com/assets/img/logo5.jpg" alt="QuLab Logo" width="150"/>
</p>

## Project Description

**QuLab: AI Risk and Assurance Lab** is an interactive Streamlit application designed as a comprehensive sandbox for Risk Managers to explore, quantify, mitigate, and visualize AI risks, with a particular focus on Generative AI (e.g., LLMs) and Agentic AI systems. This lab project provides a practical framework for understanding the multifaceted world of AI risks and developing effective assurance strategies.

Through guided scenarios, users can delve into various risk dimensions, learn to quantify risk likelihood and monetary impact, simulate the effects of mitigation strategies, and observe the reduction of risk profiles before and after interventions. The application also aims to solidify understanding of critical AI risk concepts through hands-on experimentation.

## ✨ Features

QuLab offers a structured, step-by-step approach to AI risk management:

*   **Introduction to AI Risk:** Comprehensive overview of AI risk principles and learning objectives.
*   **AI Risk Taxonomy:** Detailed exploration of various AI risk categories, including data-centric, model-centric, system-centric, human-centric, and organizational risks.
*   **Defining Key Risk Metrics:** Understand and quantify risk using metrics like Probability of Risk ($P(Risk)$), Qualitative Impact, Monetary Impact ($Impact_{Monetary}$), and Cost of Failure ($C_F$).
*   **Scenario Selection:** Choose from predefined AI risk scenarios involving Generative AI or Agentic AI to begin analysis.
*   **Identifying Baseline Risks:** Load and review the inherent risks associated with the selected scenario, including their initial likelihood and potential impact.
*   **Visualizing Baseline Risk Profile:** Generate an interactive scatter plot (Risk Matrix) to visualize the baseline risk posture based on likelihood, monetary impact, qualitative impact, and Cost of Failure.
*   **Proposing Mitigation Strategies:** Browse and select from a list of available mitigation strategies, each with estimated reduction factors for likelihood and impact.
*   **Simulating Mitigation Outcomes:** Apply selected mitigations to calculate their effect on baseline risks, resulting in a "mitigated" risk profile.
*   **Comparative Risk Visualization:** View side-by-side bar charts comparing baseline vs. mitigated likelihood and Cost of Failure for each risk, demonstrating the effectiveness of strategies.
*   **Updated Risk Matrix:** Visualize the shift in risk profiles on a combined risk matrix, showing both baseline and mitigated positions, connected by arrows to illustrate the reduction.
*   **Remaining Risks & New Challenges:** Summarize residual risks that still pose significant threats post-mitigation and discuss potential new challenges or considerations.
*   **Reset Scenario:** Clear all session data to restart the analysis with a new scenario or fresh mitigation choices.

## 🚀 Getting Started

Follow these instructions to get a copy of the project up and running on your local machine.

### Prerequisites

Ensure you have the following installed:

*   **Python 3.8+**: Download from [python.org](https://www.python.org/downloads/)
*   **pip**: Python's package installer (usually comes with Python)
*   **git**: For cloning the repository

### Installation

1.  **Clone the repository:**

    ```bash
    git clone https://github.com/YourGitHubUsername/QuLab-AI-Risk-Lab.git
    cd QuLab-AI-Risk-Lab
    ```

    *(Note: Replace `YourGitHubUsername` with the actual GitHub username if this project is hosted.)*

2.  **Create a virtual environment (recommended):**

    ```bash
    python -m venv venv
    ```

3.  **Activate the virtual environment:**

    *   **On macOS/Linux:**
        ```bash
        source venv/bin/activate
        ```
    *   **On Windows:**
        ```bash
        .\venv\Scripts\activate
        ```

4.  **Install the required dependencies:**

    Create a `requirements.txt` file in the root directory with the following content:

    ```
    streamlit>=1.30.0
    pandas>=2.0.0
    numpy>=1.20.0
    matplotlib>=3.5.0
    seaborn>=0.11.0
    ```

    Then, install them:

    ```bash
    pip install -r requirements.txt
    ```

## 🏃 Usage

1.  **Run the Streamlit application:**

    Make sure your virtual environment is activated and you are in the project's root directory.
    ```bash
    streamlit run app.py
    ```

2.  **Access the application:**

    Your web browser will automatically open to `http://localhost:8501` (or another port if 8501 is in use).

3.  **Navigate and Experiment:**

    *   Use the sidebar on the left to navigate through the different sections of the lab.
    *   Start by selecting a scenario in "4. Scenario Selection".
    *   Follow the guided steps, assessing baseline risks, proposing mitigations, and visualizing their impact.
    *   Use the "12. Reset Scenario" page to start a new experiment or change your selections.

## 📂 Project Structure

The project is organized into the following directories and files:

```
QuLab-AI-Risk-Lab/
├── app.py                      # Main Streamlit application entry point
├── requirements.txt            # List of Python dependencies
└── application_pages/          # Directory containing individual lab pages
    ├── __init__.py             # Makes application_pages a Python package
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

## 🛠️ Technology Stack

*   **Python**: The core programming language.
*   **Streamlit**: For building the interactive web application and user interface.
*   **Pandas**: For data manipulation and analysis, especially for risk dataframes.
*   **NumPy**: For numerical operations, particularly in risk calculations and transformations.
*   **Matplotlib**: For creating static, interactive, and animated visualizations.
*   **Seaborn**: Built on Matplotlib, for creating attractive and informative statistical graphics.

## 🤝 Contributing

Contributions are welcome! If you have suggestions for improvements, new features, or bug fixes, please follow these steps:

1.  Fork the repository.
2.  Create a new branch (`git checkout -b feature/your-feature-name`).
3.  Make your changes.
4.  Commit your changes (`git commit -m 'Add new feature'`).
5.  Push to the branch (`git push origin feature/your-feature-name`).
6.  Open a Pull Request.

Please ensure your code adheres to good practices and that any new dependencies are added to `requirements.txt`.

## 📄 License

This project is licensed under the MIT License - see the [LICENSE](LICENSE) file for details.

## ✉️ Contact

For questions or feedback, please contact:

*   **QuantUniversity**
*   **Website:** [https://www.quantuniversity.com/](https://www.quantuniversity.com/)
*   **Email:** info@quantuniversity.com

---
*(This README was generated for a lab project and aims to be comprehensive for educational purposes.)*

## License

## QuantUniversity License

© QuantUniversity 2025  
This notebook was created for **educational purposes only** and is **not intended for commercial use**.  

- You **may not copy, share, or redistribute** this notebook **without explicit permission** from QuantUniversity.  
- You **may not delete or modify this license cell** without authorization.  
- This notebook was generated using **QuCreate**, an AI-powered assistant.  
- Content generated by AI may contain **hallucinated or incorrect information**. Please **verify before using**.  

All rights reserved. For permissions or commercial licensing, contact: [info@qusandbox.com](mailto:info@qusandbox.com)
