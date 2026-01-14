import streamlit as st

st.set_page_config(
    page_title="ML Workbench",
    page_icon="🧠",
    layout="wide"
)

st.title("🧠 The Machine Learning Workbench")
st.markdown("### v3.1 - Comparison Update")
st.markdown("""
> **System Status:** Online 🟢

Welcome to the centralized portfolio for Machine Learning algorithms.

---

### 📂 Learning Modules

#### 1. [Linear Regression](/Linear_Regression) (Real Estate)
* Prediction of continuous values ($y=mx+b$).

#### 2. [Logistic Regression](/Logistic_Regression) (Probability)
* Binary classification using probabilities (S-Curve).

#### 3. [Decision Tree](/Decision_Tree) (Rules)
* Non-linear classification using decision rules.

### ⚔️ Analysis Modules

#### 4. [Model Showdown](/Model_Comparison) (New!)
* **The Arena:** Compare Logistic Regression vs. Decision Trees side-by-side.
* **The Goal:** Visualize how different algorithms "see" the same data differently.
""")