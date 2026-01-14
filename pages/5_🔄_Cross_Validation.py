import streamlit as st
import pandas as pd
import numpy as np
import plotly.express as px
import plotly.graph_objects as go
from sklearn.model_selection import train_test_split, cross_val_score, cross_validate, KFold
from sklearn.linear_model import LogisticRegression, LinearRegression
from sklearn.metrics import accuracy_score, precision_score, recall_score, f1_score, r2_score, mean_squared_error

# --- UI Configuration ---
st.set_page_config(page_title="Cross-Validation Lab", layout="wide")

st.title("🔄 Cross-Validation Lab")
st.markdown("### Reliability Engineering: Is your model just 'Lucky'?")
st.markdown("""
> **The Problem:** A single Train/Test split might be biased (too easy or too hard).
> **The Solution:** **K-Fold Cross-Validation**. We split the data into K parts (Folds) and train K times.
> **The Benefit:** A reliable "Average Score" that reflects true real-world performance.
""")

# --- Sidebar ---
st.sidebar.header("⚙️ CV Configuration")
cv_folds = st.sidebar.slider("Number of Folds (K)", 2, 10, 5, help="How many times to split and retrain.")
dataset_size = st.sidebar.slider("Dataset Size", 50, 500, 100)
noise_level = st.sidebar.slider("Data Noise", 0.0, 1.0, 0.2)

# --- Task Selection ---
task_type = st.radio("Select Task Type:", ["Classification (Pass/Fail)", "Regression (Predict Price)"], horizontal=True)

# --- Data Generation & Processing ---
np.random.seed(42)

if "Classification" in task_type:
    # 1. Classification Data
    study_hours = np.random.uniform(0, 12, dataset_size)
    prev_scores = np.random.uniform(30, 100, dataset_size)
    base_logic = (study_hours > 5) & (prev_scores > 60)
    labels = [1 if (x and np.random.rand() > noise_level) else 0 for x in base_logic]

    df = pd.DataFrame({'StudyHours': study_hours, 'PrevExamScore': prev_scores, 'Target': labels})
    X = df[['StudyHours', 'PrevExamScore']]
    y = df['Target']
    model = LogisticRegression()
    scoring_metrics = ['accuracy', 'precision', 'recall', 'f1']
    main_metric_name = "Accuracy"

else:
    # 2. Regression Data
    sq_ft = np.random.uniform(500, 5000, dataset_size)
    # Price = 300 * SqFt + 50000 + Noise
    price = (300 * sq_ft) + 50000 + np.random.normal(0, 50000 * (noise_level + 0.1), dataset_size)

    df = pd.DataFrame({'SqFt': sq_ft, 'Price': price})
    X = df[['SqFt']]  # 2D array
    y = df['Price']
    model = LinearRegression()
    # Note: Scikit-Learn uses negative MSE for optimization, so we flip it back later
    scoring_metrics = ['r2', 'neg_mean_squared_error', 'neg_mean_absolute_error']
    main_metric_name = "R² Score"

# --- Analysis Section ---
col1, col2 = st.columns(2)

# --- 1. The Single Split Approach (The "Old Way") ---
with col1:
    st.subheader("1. The Single Split (Risky)")
    st.write("Training once on 80% of data. If this 80% is easy, score is misleading.")

    X_train, X_test, y_train, y_test = train_test_split(X, y, test_size=0.2, random_state=42)
    model.fit(X_train, y_train)
    y_pred = model.predict(X_test)

    if "Classification" in task_type:
        single_score = accuracy_score(y_test, y_pred)
        st.metric(label="Single Test Accuracy", value=f"{single_score:.1%}")

        # Missing Requirement: Display F1 Score
        st.dataframe({
            "Metric": ["Accuracy", "Precision", "Recall", "F1-Score"],
            "Score": [
                f"{single_score:.2f}",
                f"{precision_score(y_test, y_pred, zero_division=0):.2f}",
                f"{recall_score(y_test, y_pred, zero_division=0):.2f}",
                f"{f1_score(y_test, y_pred, zero_division=0):.2f}"
            ]
        })
    else:
        single_score = r2_score(y_test, y_pred)
        st.metric(label="Single R² Score", value=f"{single_score:.3f}")
        st.write(f"MSE: {mean_squared_error(y_test, y_pred):,.0f}")

# --- 2. The Cross-Validation Approach (The "Pro Way") ---
with col2:
    st.subheader(f"2. {cv_folds}-Fold Cross-Validation (Robust)")
    st.write(f"Training {cv_folds} times on different splits. Averaging the results.")

    # Run CV
    cv_results = cross_validate(model, X, y, cv=cv_folds, scoring=scoring_metrics)

    # Extract Scores
    if "Classification" in task_type:
        mean_score = cv_results['test_accuracy'].mean()
        std_dev = cv_results['test_accuracy'].std()

        st.metric(label=f"Average {main_metric_name}", value=f"{mean_score:.1%}", delta=f"±{std_dev:.1%}")

        # Comparative Table
        cv_df = pd.DataFrame({
            "Fold #": range(1, cv_folds + 1),
            "Accuracy": cv_results['test_accuracy'],
            "Precision": cv_results['test_precision'],
            "Recall": cv_results['test_recall'],
            "F1-Score": cv_results['test_f1']
        })
        st.dataframe(cv_df.style.format("{:.2f}"))

    else:
        mean_score = cv_results['test_r2'].mean()
        std_dev = cv_results['test_r2'].std()

        st.metric(label=f"Average {main_metric_name}", value=f"{mean_score:.3f}", delta=f"±{std_dev:.3f}")

        cv_df = pd.DataFrame({
            "Fold #": range(1, cv_folds + 1),
            "R² Score": cv_results['test_r2'],
            "MSE (Negative)": cv_results['test_neg_mean_squared_error']
        })
        st.dataframe(cv_df.style.format({"R² Score": "{:.3f}", "MSE (Negative)": "{:,.0f}"}))

# --- 3. Visualization ---
st.divider()
st.subheader("📊 Visualizing the Variability")
st.write("Does the model performance jump around? If bars are uneven, your model is unstable.")

# Bar Chart of scores per fold
fold_indices = list(range(1, cv_folds + 1))
if "Classification" in task_type:
    scores = cv_results['test_accuracy']
    title_text = "Accuracy per Fold"
else:
    scores = cv_results['test_r2']
    title_text = "R² Score per Fold"

fig = px.bar(x=fold_indices, y=scores, labels={'x': 'Fold Number', 'y': 'Score'}, title=title_text)
# Add a line for the Single Split result to compare
fig.add_hline(y=single_score, line_dash="dot", annotation_text="Single Split Score", annotation_position="top right",
              line_color="red")
fig.add_hline(y=mean_score, line_dash="dash", annotation_text="CV Average Score", annotation_position="bottom right",
              line_color="green")

st.plotly_chart(fig, use_container_width=True)