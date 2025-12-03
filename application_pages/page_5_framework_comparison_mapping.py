
import streamlit as st
import pandas as pd

def create_sr117_nist_comparison_summary_table():
    data = {
        "Aspect": ["Scope", "Primary Focus", "Regulatory Nature", "Key Objective"],
        "SR 11-7": [
            "Banking sector (financial models)",
            "Model Risk Management (MRM)",
            "Mandatory (for regulated financial institutions)",
            "Minimize adverse outcomes from model use"
        ],
        "NIST AI RMF": [
            "All AI systems across industries",
            "Trustworthy AI (risk management for AI)",
            "Voluntary (but rapidly becoming industry best practice)",
            "Foster development and use of trustworthy AI"
        ]
    }
    df = pd.DataFrame(data)
    return df

def create_sr117_to_nist_govern_mapping_table():
    data = {
        "SR 11-7 MRM Pillar": [
            "Model Governance",
            "Development/Implementation",
            "Validation",
            "Ongoing Monitoring"
        ],
        "NIST AI RMF Govern Function": [
            "Govern",
            "Govern",
            "Govern",
            "Govern"
        ],
        "Key Aspects & Best Practices": [
            "Establishing clear roles, policies, and a culture for AI risk oversight, including board-level governance. Ensuring AI risk stays within organizational tolerance and designing governance for human-in-the-loop oversight.",
            "Defining responsibilities for secure AI development and deployment and ensuring ethical considerations are embedded from the outset.",
            "Overseeing the objective review and effective challenge processes for AI models to ensure their accuracy, reliability, and fairness.",
            "Establishing robust procedures for continuous oversight, performance monitoring, and accountability throughout the AI lifecycle."
        ]
    }
    df = pd.DataFrame(data)
    return df

def create_sr117_to_nist_map_measure_mapping_table():
    data = {
        "SR 11-7 MRM Pillar": [
            "Development/Implementation",
            "Validation",
            "Ongoing Monitoring"
        ],
        "NIST AI RMF Function": [
            "Map",
            "Measure",
            "Measure"
        ],
        "Key Aspects & Best Practices": [
            "Identifying AI lifecycle risks (data quality, model bias, system integration flaws, human misuse). Creating risk taxonomies, model cards, and data cards to document purpose, training data, and limitations.",
            "Quantifying risks through rigorous testing and validation (benchmark, scenario-based, backtesting). Developing performance metrics (e.g., Accuracy, F1-Score) and assessing trustworthiness attributes (e.g., fairness metrics).",
            "Establishing continuous validation processes, ongoing performance checks, and user feedback. Integrating identified risks and controls into a risk register."
        ]
    }
    df = pd.DataFrame(data)
    return df

def create_sr117_to_nist_manage_mapping_table():
    data = {
        "SR 11-7 MRM Pillar": [
            "Ongoing Monitoring",
            "Validation",
            "Development/Implementation"
        ],
        "NIST AI RMF Function": [
            "Manage",
            "Manage",
            "Manage"
        ],
        "Key Aspects & Best Practices": [
            "Implementing continuous validation processes, drift detection, and performance monitoring. Establishing incident reporting and response mechanisms, integrating findings into a risk register, and ensuring accountability and human-in-the-loop oversight.",
            "Utilizing insights from rigorous testing (e.g., adversarial testing, red-teaming) to inform and update mitigation strategies and control measures, including input sanitization and detecting prompt injection.",
            "Integrating risk controls and security measures early in the AI lifecycle, including model supply chain security, access governance, and maintaining an AI Bill of Materials (AI-BOM)."
        ]
    }
    df = pd.DataFrame(data)
    return df

def get_nist_attribute_info(attribute):
    attributes = {
        "Validity": "Ensuring the AI system accurately performs its intended function and produces correct outputs.",
        "Reliability": "Guarantees consistent and stable performance of the AI system over time and across operational conditions.",
        "Safety": "Minimizing the potential for the AI system to cause harm to individuals, society, or the environment.",
        "Security": "Protecting AI systems from adversarial attacks and ensuring data integrity and access governance.",
        "Transparency": "Understanding how AI systems arrive at outputs through interpretability methods and counterfactuals.",
        "Fairness": "Identifying and mitigating biases in AI to ensure equitable and just outcomes for all.",
        "Accountability": "Establishing clear roles, policies, and governance for AI risk oversight to ensure responsibility for AI outcomes.",
        "Privacy-Preserving": "Implementing strategies to address data sensitivity and integrating privacy by design throughout the AI lifecycle."
    }
    return attributes.get(attribute, "No detailed information available for this attribute.")

def highlight_row(row, selected_pillar):
    if row["SR 11-7 MRM Pillar"] == selected_pillar:
        return ['background-color: yellow'] * len(row)
    return [''] * len(row)

def main():
    st.header("Complementary Frameworks: SR 11-7 & NIST AI RMF")
    st.markdown("""
    While SR 11-7 and NIST AI RMF originate from different regulatory landscapes and address distinct scopes, they are not mutually exclusive.
    Instead, they offer complementary perspectives that, when integrated, can form a more robust approach to AI risk management.
    """)

    st.subheader("Distinct Scopes")
    st.markdown("""
    *   **SR 11-7:** Primarily focused on financial models within the banking sector, emphasizing quantitative model risk.
    *   **NIST AI RMF:** Broadly applicable to all types of AI systems across various industries, with a strong emphasis on trustworthy AI attributes and societal impacts.
    """)

    st.subheader("Shared Objectives")
    st.markdown("""
    Despite their differences, both frameworks share fundamental objectives:

    *   **Risk Mitigation:** Both aim to identify, assess, and mitigate risks associated with the use of advanced analytical systems.
    *   **Governance & Oversight:** Both emphasize the importance of strong governance, clear accountability, and senior management involvement.
    *   **Continuous Monitoring:** Both advocate for ongoing assessment and adaptation to ensure models/AI systems remain fit for purpose.
    """)

    st.subheader("Integration Benefits")
    st.markdown("""
    Integrating principles from both frameworks can provide a comprehensive strategy:

    *   SR 11-7's rigor in financial model validation can inform the technical assurance of AI.
    *   NIST AI RMF's focus on trustworthiness attributes (fairness, transparency, privacy) can broaden SR 11-7's scope to address ethical and societal AI risks.
    *   SR 11-7's established governance structures can be extended to cover the broader AI lifecycle as defined by NIST.
    """)

    st.subheader("SR 11-7 vs. NIST AI RMF: Summary Comparison")
    st.dataframe(create_sr117_nist_comparison_summary_table())

    st.markdown("---")

    st.subheader("Mapping SR 11-7 MRM to NIST AI RMF: Interactive Mapping")
    st.markdown("""
    This section illustrates how the core pillars and principles of SR 11-7 align with and contribute to the functions of the NIST AI RMF.
    Select an SR 11-7 element to see its corresponding aspects within the NIST AI RMF.
    """)

    sr117_options = [
        "Model Definition",
        "Risk Amplification",
        "Effective Challenge",
        "Model Risk Governance",
        "Model Development & Implementation",
        "Model Validation",
        "Ongoing Monitoring"
    ]

    if "selected_sr117_pillar" not in st.session_state:
        st.session_state.selected_sr117_pillar = sr117_options[0]

    selected_pillar = st.radio(
        label="Select an SR 11-7 Element",
        options=sr117_options,
        index=sr117_options.index(st.session_state.selected_sr117_pillar),
        key="sr117_selector"
    )

    st.session_state.selected_sr117_pillar = selected_pillar

    st.markdown(f"### Exploring: {selected_pillar}")

    if selected_pillar == "Model Definition":
        st.markdown("""
        **SR 11-7 View:** Focuses on quantitative methods, systems, and approaches that apply quantitative methods to process input data and, on the basis of quantitative assumptions, judgments, or theories, generate quantitative outputs.
        
        **NIST AI RMF Connection:** In AI RMF, the "model definition" extends to all AI/ML systems, their outputs, and even decision-making processes, emphasizing the need to "Map" the AI system's capabilities, limitations, and intended uses. This aligns with defining the scope of what is being governed and managed under the AI RMF.
        """)
    elif selected_pillar == "Risk Amplification":
        st.markdown("""
        **SR 11-7 View:** Recognizes that models can introduce and amplify risks, requiring careful management.
        
        **NIST AI RMF Connection:** This concept is central to the "Map" function of AI RMF, where potential negative impacts (risks) are identified and characterized across the AI lifecycle, including emergent risks unique to AI (e.g., algorithmic bias, adversarial attacks, ethical concerns). Trustworthiness attributes like **Safety**, **Fairness**, and **Security** directly address these amplified risks.
        """)
        with st.expander("Trustworthiness Attributes Related to Risk Amplification"):
            st.info(f"**Safety:** {get_nist_attribute_info('Safety')}")
            st.info(f"**Fairness:** {get_nist_attribute_info('Fairness')}")
            st.info(f"**Security:** {get_nist_attribute_info('Security')}")
    elif selected_pillar == "Effective Challenge":
        st.markdown("""
        **SR 11-7 View:** Requires independent validation and critical assessment by qualified personnel who are not involved in the model's development. This ensures objectivity and identifies potential flaws.
        
        **NIST AI RMF Connection:** This maps strongly to the "Measure" and "Govern" functions. "Measure" involves evaluating AI systems against trustworthiness attributes through rigorous testing and validation, akin to independent challenge. "Govern" ensures that processes for objective review and effective challenge are established and overseen within the organizational culture. Attributes like **Transparency** and **Accountability** are crucial for effective challenge.
        """)
        with st.expander("Trustworthiness Attributes Related to Effective Challenge"):
            st.info(f"**Transparency:** {get_nist_attribute_info('Transparency')}")
            st.info(f"**Accountability:** {get_nist_attribute_info('Accountability')}")
    elif selected_pillar == "Model Risk Governance":
        st.markdown("""
        **SR 11-7 View:** Emphasizes strong oversight by the board and senior management, clear policies, and defined roles and responsibilities for model risk management.
        
        **NIST AI RMF Connection:** This directly aligns with the "Govern" function, which focuses on establishing a culture of AI risk management, defining roles and responsibilities, and ensuring accountability. The **Accountability** attribute is foundational here.
        """)
        with st.expander("Trustworthiness Attributes Related to Model Risk Governance"):
            st.info(f"**Accountability:** {get_nist_attribute_info('Accountability')}")

        st.markdown("### Mapping SR 11-7 MRM Pillars to NIST AI RMF: Govern Function")
        df_govern = create_sr117_to_nist_govern_mapping_table()
        st.dataframe(df_govern.style.apply(highlight_row, selected_pillar=selected_pillar, axis=1), use_container_width=True)

    elif selected_pillar == "Model Development & Implementation":
        st.markdown("""
        **SR 11-7 View:** Focuses on sound practices for model design, data quality, and implementation controls.
        
        **NIST AI RMF Connection:** This maps to both "Map" and "Manage" functions. In "Map," risks associated with data quality and model design are identified. In "Manage," controls are implemented early in the lifecycle, including security measures and an AI Bill of Materials (AI-BOM). Trustworthiness attributes like **Validity**, **Reliability**, and **Security** are key during this phase.
        """)
        with st.expander("Trustworthiness Attributes Related to Model Development & Implementation"):
            st.info(f"**Validity:** {get_nist_attribute_info('Validity')}")
            st.info(f"**Reliability:** {get_nist_attribute_info('Reliability')}")
            st.info(f"**Security:** {get_nist_attribute_info('Security')}")

        st.markdown("### Mapping SR 11-7 MRM Pillars to NIST AI RMF: Map & Manage Functions")
        df_map_manage = create_sr117_to_nist_map_measure_mapping_table()
        st.dataframe(df_map_manage.style.apply(highlight_row, selected_pillar=selected_pillar, axis=1), use_container_width=True)

        df_manage = create_sr117_to_nist_manage_mapping_table()
        st.dataframe(df_manage.style.apply(highlight_row, selected_pillar=selected_pillar, axis=1), use_container_width=True)

    elif selected_pillar == "Model Validation":
        st.markdown("""
        **SR 11-7 View:** Emphasizes independent assessment of model logic, data, and performance, including outcomes analysis and backtesting.
        
        **NIST AI RMF Connection:** This strongly aligns with the "Measure" function, which involves quantifying risks through rigorous testing, validation, and assessing trustworthiness attributes. It also contributes to "Manage" by providing insights for mitigation. Attributes like **Validity**, **Reliability**, **Fairness**, and **Transparency** are critical for robust validation.
        """)
        with st.expander("Trustworthiness Attributes Related to Model Validation"):
            st.info(f"**Validity:** {get_nist_attribute_info('Validity')}")
            st.info(f"**Reliability:** {get_nist_attribute_info('Reliability')}")
            st.info(f"**Fairness:** {get_nist_attribute_info('Fairness')}")
            st.info(f"**Transparency:** {get_nist_attribute_info('Transparency')}")

        st.markdown("### Mapping SR 11-7 MRM Pillars to NIST AI RMF: Measure & Manage Functions")
        df_map_measure = create_sr117_to_nist_map_measure_mapping_table()
        st.dataframe(df_map_measure.style.apply(highlight_row, selected_pillar=selected_pillar, axis=1), use_container_width=True)

        df_manage = create_sr117_to_nist_manage_mapping_table()
        st.dataframe(df_manage.style.apply(highlight_row, selected_pillar=selected_pillar, axis=1), use_container_width=True)

    elif selected_pillar == "Ongoing Monitoring":
        st.markdown("""
        **SR 11-7 View:** Requires continuous monitoring of model performance, data characteristics, and model limitations to ensure ongoing accuracy and reliability.
        
        **NIST AI RMF Connection:** This directly translates to the "Measure" and "Manage" functions. "Measure" involves continuous validation, performance checks, and user feedback. "Manage" focuses on implementing continuous validation processes, drift detection, and incident response. Attributes like **Reliability**, **Safety**, and **Accountability** are crucial for ongoing monitoring.
        """)
        with st.expander("Trustworthiness Attributes Related to Ongoing Monitoring"):
            st.info(f"**Reliability:** {get_nist_attribute_info('Reliability')}")
            st.info(f"**Safety:** {get_nist_attribute_info('Safety')}")
            st.info(f"**Accountability:** {get_nist_attribute_info('Accountability')}")

        st.markdown("### Mapping SR 11-7 MRM Pillars to NIST AI RMF: Measure & Manage Functions")
        df_map_measure = create_sr117_to_nist_map_measure_mapping_table()
        st.dataframe(df_map_measure.style.apply(highlight_row, selected_pillar=selected_pillar, axis=1), use_container_width=True)

        df_manage = create_sr117_to_nist_manage_mapping_table()
        st.dataframe(df_manage.style.apply(highlight_row, selected_pillar=selected_pillar, axis=1), use_container_width=True)
