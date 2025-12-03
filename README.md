# AI Framework Comparator: SR 11-7 vs. NIST AI RMF

## Project Title and Description

**AI Framework Comparator: SR 11-7 vs. NIST AI RMF**

This Streamlit application serves as an interactive lab project designed to clarify the intricate relationship and complementary nature of the Federal Reserve's SR 11-7 "Guidance on Model Risk Management" and the NIST AI Risk Management Framework (AI RMF 1.0).

The primary objective is to equip Risk Managers and AI practitioners with a deeper understanding of the evolution from traditional model risk management (MRM) practices to comprehensive AI assurance. It highlights the key differences, shared objectives, and practical integration points necessary for establishing robust AI governance in today's rapidly evolving technological landscape, particularly with the advent of large-scale AI systems like Large Language Models (LLMs) and agentic architectures.

## Features

This application provides a structured, interactive learning experience covering critical aspects of AI risk management and governance:

*   **Introduction to AI Assurance:** Overview of the lab's purpose, scope, and key learning objectives.
*   **The Imperative of AI Risk Management:** Exploration of emergent AI risks, a detailed 5-dimensional AI risk taxonomy (Data, Model, System, Human, Organizational), and conceptual metrics.
*   **Foundations of SR 11-7:** A deep dive into the core principles, pillars (Governance, Validation, Development & Use), and how its model definition and risk tiering can be extended to AI contexts.
*   **Introduction to NIST AI RMF 1.0:** Comprehensive explanation of the NIST AI RMF, its four core functions (Govern, Map, Measure, Manage), and the seven key Trustworthy AI attributes (Validity, Reliability, Safety, Security, Transparency, Fairness, Accountability, Privacy-Preserving).
*   **Framework Comparison & Interactive Mapping:** A detailed comparison of SR 11-7 and NIST AI RMF, highlighting their distinct scopes, shared objectives, and integration benefits. Includes an interactive tool to map SR 11-7 principles to NIST AI RMF functions and trustworthiness attributes.
*   **Application to Generative & Agentic AI:** Discussion of the heightened and specific risks introduced by Generative AI (e.g., LLM hallucinations, IP infringement) and Agentic AI (e.g., loss of control, emergent behaviors), along with tailored mitigation and oversight strategies.
*   **Essential AI Assurance Artifacts:** Introduction and examples of critical documentation tools such as Model Cards, Data Cards, and AI Risk Registers, which are vital for transparency, accountability, and compliance.

## Getting Started

Follow these instructions to set up and run the Streamlit application on your local machine.

### Prerequisites

Ensure you have the following installed:

*   **Python 3.8+**
*   **pip** (Python package installer, usually comes with Python)

### Installation

1.  **Clone the repository:**

    ```bash
    git clone https://github.com/yourusername/AI-Framework-Comparator.git # Replace with actual repo URL
    cd AI-Framework-Comparator
    ```

2.  **Create a virtual environment (recommended):**

    ```bash
    python -m venv venv
    # On Windows
    .\venv\Scripts\activate
    # On macOS/Linux
    source venv/bin/activate
    ```

3.  **Install the required dependencies:**

    Create a `requirements.txt` file in the root directory of your project with the following content:

    ```
    streamlit>=1.0.0
    pandas>=1.0.0
    ```

    Then install them:

    ```bash
    pip install -r requirements.txt
    ```

## Usage

Once the dependencies are installed, you can run the Streamlit application:

```bash
streamlit run app.py
```

This command will open the application in your default web browser, typically at `http://localhost:8501`. You can then navigate through the different sections of the lab using the sidebar.

## Project Structure

The project is organized to clearly separate the main application logic from individual lab pages.

```
AI-Framework-Comparator/
├── app.py                            # Main Streamlit application entry point and navigation.
├── application_pages/                # Directory containing individual lab pages.
│   ├── page_1_introduction.py        # Introduction to the lab and learning objectives.
│   ├── page_2_ai_risk_management.py  # Details on AI risk taxonomy and emergent risks.
│   ├── page_3_foundations_sr117.py   # Core principles of SR 11-7.
│   ├── page_4_nist_ai_rmf.py         # Introduction to NIST AI RMF and trustworthy AI attributes.
│   ├── page_5_framework_comparison_mapping.py # Compares SR 11-7 and NIST AI RMF with interactive mapping.
│   ├── page_6_generative_agentic_ai.py# Applies frameworks to Generative and Agentic AI risks.
│   └── page_7_assurance_artifacts.py # Explains essential AI assurance documentation.
├── requirements.txt                  # Lists Python dependencies.
└── README.md                         # This README file.
```

## Technology Stack

*   **Python 3.8+**: The core programming language.
*   **Streamlit**: The framework used for building the interactive web application.
*   **Pandas**: Utilized for data manipulation and displaying tabular data within the Streamlit app.

## Contributing

This project is a lab exercise. While direct contributions might not be the primary focus, suggestions for improvements, bug reports, or feature requests are welcome. Please open an issue in the GitHub repository.

## License

This project is open-source and available under the [MIT License](LICENSE).

## Contact

For any questions or inquiries, please reach out to:

*   **QuantUniversity**
*   **Website:** [quantuniversity.com](https://www.quantuniversity.com/)
*   **GitHub Repository:** [Link to your GitHub repository if applicable]