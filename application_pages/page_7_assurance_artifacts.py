
import streamlit as st
import pandas as pd

def create_model_card_example_fields_table():
    data = {
        "Model Card Field": [
            "Model Name/ID", "Version", "Owner", "Date Developed",
            "Intended Use Cases", "Out-of-Scope Uses",
            "Training Data Description", "Evaluation Metrics (Overall)",
            "Fairness Metrics/Subgroup Performance", "Known Limitations",
            "Ethical Considerations", "Deployment/Monitoring Guidelines"
        ],
        "Example Content/Purpose": [
            "Financial Fraud Detection Model v1.2", "1.2", "Risk Management Dept.", "2023-10-26",
            "Detecting suspicious credit card transactions.", "Loan application scoring, customer service chatbots.",
            "Synthetic transaction data, anonymized customer profiles (2020-2023).", "Accuracy: 95%, F1-Score: 0.88",
            "Equal Opportunity (False Negative Rate for different demographics).", "May struggle with novel fraud patterns.",
            "Potential for false positives impacting legitimate users; need clear appeal process.", "Continuous monitoring for drift, quarterly re-evaluation."
        ]
    }
    df = pd.DataFrame(data)
    return df

def create_data_card_example_fields_table():
    data = {
        "Data Card Field": [
            "Dataset Name/ID", "Version", "Source(s)", "Collection Method",
            "Date Collected/Created", "Last Updated",
            "Data Description", "Number of Samples/Features",
            "Annotation/Labeling Process", "Known Biases/Limitations",
            "Privacy Considerations", "Data Retention Policy"
        ],
        "Example Content/Purpose": [
            "Customer Transaction History", "1.0", "Internal CRM, Third-Party Payment Processor", "Automated API pull, Manual entry",
            "2018-01-01 to 2023-09-30", "2023-10-15",
            "Anonymized transaction details for credit card usage.", "10M rows, 50 features",
            "Fraudulent transactions labeled by human experts.", "Geographical bias towards urban areas; potential underrepresentation of certain demographics.",
            "All PII anonymized; GDPR compliant.", "Data retained for 7 years as per regulatory requirements."
        ]
    }
    df = pd.DataFrame(data)
    return df

def create_risk_register_example_fields_table():
    data = {
        "Risk Register Field": [
            "Risk ID", "Risk Category", "Risk Description",
            "Potential Impact (Severity)", "Likelihood", "Risk Score (Impact x Likelihood)",
            "Mitigation Controls", "Response Plan", "Owner", "Status", "Date Identified", "Last Review Date"
        ],
        "Example Content/Purpose": [
            "AI-001", "Model (Bias)", "Algorithmic bias leading to discriminatory loan decisions.",
            "High (Reputational, Legal, Financial)", "Medium", "High (3x2 = 6)",
            "Fairness audit; re-weighting training data; human-in-the-loop review for high-risk applications.", "Alert risk team; pause model deployment; initiate remediation plan; notify affected parties.", "Chief Risk Officer", "In Progress", "2023-08-01", "2023-10-20"
        ]
    }
    df = pd.DataFrame(data)
    return df

def main():
    st.header("Essential AI Assurance Artifacts")
    st.markdown("""
    Effective AI risk management and assurance rely heavily on robust documentation. Just as financial models require detailed records, AI systems demand specialized artifacts to ensure transparency, accountability, and ongoing trustworthiness.
    These artifacts serve as critical communication tools for developers, risk managers, auditors, and regulators.
    """)

    st.subheader("Introduction to AI Assurance Documentation")
    st.markdown("""
    Beyond traditional software documentation, AI assurance artifacts focus specifically on the unique characteristics and risks of AI systems. Key examples include:

    *   **Model Cards:** Summarize key information about an AI model.
    *   **Data Cards:** Detail the characteristics and provenance of datasets used to train AI.
    *   **Risk Registers:** Document identified risks, their assessment, and mitigation strategies.
    """)

    st.subheader("Model Cards: AI Model Information Summary")
    st.markdown("""
    Inspired by product labels, Model Cards provide a structured summary of an AI model's characteristics, intended uses, performance, and ethical considerations. They are crucial for transparency and responsible deployment.
    """)
    st.dataframe(create_model_card_example_fields_table())

    st.subheader("Essential AI Assurance Artifacts: Data Cards")
    st.markdown("""
    Data Cards complement Model Cards by providing detailed information about the datasets used to train and evaluate AI models. Understanding the data is fundamental to understanding potential biases and limitations of the AI system.
    """)
    st.dataframe(create_data_card_example_fields_table())

    st.subheader("Essential AI Assurance Artifacts: Risk Registers")
    st.markdown("""
    An AI Risk Register is a critical tool for systematically identifying, assessing, tracking, and mitigating risks throughout the AI lifecycle. It provides a living document for ongoing risk management.
    """)
    st.dataframe(create_risk_register_example_fields_table())

    st.markdown("""
    These assurance artifacts are not static documents but should be continuously updated throughout the AI lifecycle, reflecting changes in the model, data, or operating environment. They are foundational for auditing, regulatory compliance, and building trust in AI systems.
    """)
