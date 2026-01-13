import streamlit as st

st.set_page_config(
    page_title="ML Workbench",
    page_icon="🧠",
    layout="wide"
)

st.title("🧠 The Machine Learning Workbench")
st.markdown("### v2.0 - Enterprise Edition")

st.markdown(
    """
    > **System Status:** Online 🟢

    Welcome to the centralized portfolio for Machine Learning algorithms. 
    This platform demonstrates the mathematical foundations of AI, built from scratch.

    ---

    ### 📂 Available Modules

    #### 1. [Linear Regression (Real Estate)](/Linear_Regression)
    * **Core Concept:** Prediction of continuous values.
    * **The "What":** Predicting house prices based on square footage.
    * **Key Metric:** $R^2$ (Accuracy) & MSE (Error).

    #### 2. [Logistic Regression (Student Success)](/Logistic_Regression)
    * **Core Concept:** Binary Classification (Probability).
    * **The "What":** Predicting if a student passes based on study hours.
    * **Key Metric:** Confusion Matrix & Sigmoid Probability.

    ---

    *Architecture: Streamlit Multipage App | Stack: Python, Scikit-Learn, Plotly*
    """
)