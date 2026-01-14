import streamlit as st

st.set_page_config(
    page_title="ML Workbench",
    page_icon="🧠",
    layout="wide"
)

st.title("🧠 The Machine Learning Workbench")
st.markdown("### v3.2 - Reliability Update")
st.markdown("""
> **System Status:** Online 🟢

Welcome to the centralized portfolio for Machine Learning algorithms.

---

### 📂 Learning Modules

#### 1. [Linear Regression](/Linear_Regression)
* Prediction of continuous values.

#### 2. [Logistic Regression](/Logistic_Regression)
* Binary classification (Probability).

#### 3. [Decision Tree](/Decision_Tree)
* Non-linear classification (Rules).

### ⚔️ Analysis Modules

#### 4. [Model Showdown](/Model_Comparison)
* **Compare:** Linear vs. Non-Linear boundaries side-by-side.

#### 5. [Cross-Validation Lab](/Cross_Validation) (New!)
* **Audit:** Test model reliability using K-Fold Cross-Validation.
* **Metrics:** F1-Score, R² Averaging, and Stability Testing.

---
*Created by [Your Name]*
""")