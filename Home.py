import streamlit as st

st.set_page_config(
    page_title="ML Workbench",
    page_icon="🧠",
    layout="wide"
)

st.title("🧠 The Machine Learning Workbench")
st.markdown("### v3.0 - Enterprise Edition")

st.markdown(
    """
    > **System Status:** Online 🟢

    Welcome to the centralized portfolio for Machine Learning algorithms. 
    This platform demonstrates the mathematical foundations of AI, built from scratch.

    ---

    ### 📂 Available Modules

    #### 1. [Linear Regression (Real Estate)](/Linear_Regression)
    * **Type:** Regression (Continuous)
    * **Use Case:** Predicting house prices.
    * **Core Math:** $y = mx + b$

    #### 2. [Logistic Regression (Student Success)](/Logistic_Regression)
    * **Type:** Classification (Binary)
    * **Use Case:** Pass/Fail Probability.
    * **Core Math:** Sigmoid Function (S-Curve).

    #### 3. [Decision Tree (Exam Classifier)](/Decision_Tree)
    * **Type:** Non-Linear Classification
    * **Use Case:** Complex decision rules.
    * **Core Math:** Gini Impurity & Entropy (Tree Splitting).

    ---

    *Architecture: Streamlit Multipage App | Stack: Python, Scikit-Learn, Plotly*
    """
)