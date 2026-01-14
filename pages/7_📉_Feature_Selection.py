import streamlit as st
import pandas as pd
import numpy as np
import statsmodels.api as sm
import plotly.graph_objects as go

# --- UI Configuration ---
st.set_page_config(page_title="Feature Selection Lab", layout="wide")

st.title("📉 Feature Selection: Backward Elimination")
st.markdown("### The 'Garbage Collector' for AI Models")
st.markdown("""
> **The Concept:** A model with too much data gets confused (Overfitting).
> **The Strategy:** Start with ALL features, calculate their 'Significance' (P-Value), and delete the worst one.
> **The Goal:** Keep only features with $P < 0.05$ (Statistically Significant).
""")

# --- Sidebar: Data Generator ---
st.sidebar.header("⚙️ Data Lab")
n_samples = st.sidebar.slider("Dataset Size", 50, 500, 200)
st.sidebar.info("We will generate a dataset where 'Target' depends ONLY on Study Hours & Prev Score.")
noise_features = st.sidebar.multiselect(
    "Add 'Garbage' Features (Noise)",
    ["Shoe Size", "Jersey Number", "Twitter Followers", "Height (cm)", "Random ID"],
    default=["Shoe Size", "Twitter Followers"]
)

# --- Step 1: Generate Data ---
np.random.seed(42)

# Real Signals
study_hours = np.random.uniform(1, 10, n_samples)
prev_score = np.random.uniform(40, 100, n_samples)
# Target (Pass/Fail) depends ONLY on Study & Score
# y = 5*Hours + 0.5*Score + Error
y_continuous = 5 * study_hours + 0.5 * prev_score + np.random.normal(0, 5, n_samples)

# Create DataFrame
data = {
    'Study Hours': study_hours,
    'Prev Exam Score': prev_score,
    'Target (Score)': y_continuous
}

# Add Garbage Noise (Totally random numbers)
for feature in noise_features:
    data[feature] = np.random.uniform(0, 100, n_samples)

df = pd.DataFrame(data)

# --- Analysis Section ---
col1, col2 = st.columns([1, 2])

with col1:
    st.subheader("1. The Raw Data")
    st.write("Notice the 'Garbage' columns mixed with real data.")
    st.dataframe(df.head(8), use_container_width=True)

    start_btn = st.button("🚀 Run Backward Elimination", type="primary")

# --- Step 2: The Algorithm ---
if start_btn:
    with col2:
        st.subheader("2. Elimination Log")

        # Prepare Data for Statsmodels
        # We must manually add a "Constant" (Intercept) column for OLS to work
        X = df.drop(columns=['Target (Score)'])
        y = df['Target (Score)']

        iteration = 1
        features_remaining = list(X.columns)

        # Log container
        log_container = st.container()

        while len(features_remaining) > 0:
            # 1. Fit Model with current features
            X_current = X[features_remaining]
            X_with_const = sm.add_constant(X_current)  # Add intercept
            model = sm.OLS(y, X_with_const).fit()  # Fit Ordinary Least Squares

            # 2. Get P-Values (Skip 'const')
            p_values = model.pvalues.drop('const')
            max_p_value = p_values.max()
            worst_feature = p_values.idxmax()

            # 3. Visualization Logic
            with log_container:
                col_log1, col_log2 = st.columns([3, 1])
                if max_p_value > 0.05:
                    col_log1.markdown(
                        f"**Round {iteration}:** Worst offender is `{worst_feature}` (P={max_p_value:.4f}).")
                    col_log2.error("ELIMINATED ❌")
                    features_remaining.remove(worst_feature)  # Remove least significant feature
                else:
                    col_log1.markdown(f"**Round {iteration}:** All remaining features are significant (P < 0.05).")
                    col_log2.success("STOPPING ✅")
                    break

            iteration += 1

    # --- Step 3: Visualization ---
    st.divider()
    st.subheader("3. Final Result Analysis")

    fin_col1, fin_col2 = st.columns(2)

    with fin_col1:
        st.success(f"✅ **Survivors:** {', '.join(features_remaining)}")
        st.caption("The algorithm correctly identified the real signals.")

    with fin_col2:
        removed = [f for f in df.columns if f not in features_remaining and f != 'Target (Score)']
        st.error(f"🗑️ **Eliminated:** {', '.join(removed)}")
        st.caption("The algorithm correctly identified the noise.")

    # P-Value Bar Chart
    st.write("### 📊 Final Significance Check (Lower is Better)")
    final_p_values = model.pvalues.drop('const')

    fig = go.Figure(go.Bar(
        x=final_p_values.index,
        y=final_p_values.values,
        marker_color=['green' if p < 0.05 else 'red' for p in final_p_values.values]
    ))
    # Add threshold line at 0.05
    fig.add_hline(y=0.05, line_dash="dash", line_color="red", annotation_text="Significance Threshold (0.05)")
    fig.update_layout(title="Final P-Values (Target: < 0.05)", yaxis_title="P-Value")
    st.plotly_chart(fig, use_container_width=True)

else:
    with col2:
        st.info("👈 Click the button to start the elimination process.")