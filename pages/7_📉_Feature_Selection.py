import streamlit as st
import pandas as pd
import numpy as np
import statsmodels.api as sm
from sklearn.linear_model import LinearRegression, Lasso
from sklearn.metrics import r2_score
import plotly.graph_objects as go

# --- UI Configuration ---
st.set_page_config(page_title="Feature Selection Lab", layout="wide")

st.title("📉 Feature Selection Suite")
st.markdown("### Three Strategies. One Goal.")
st.markdown("""
> **The Goal:** Find the 'Signal' (useful data) and ignore the 'Noise' (useless data).
> * **Strategy A (Backward):** Start with EVERYTHING. Delete the trash. (Uses P-Values)
> * **Strategy B (Forward):** Start with NOTHING. Add the gems. (Uses R-Squared)
> * **Strategy C (LASSO):** Penalize complexity. Shrink coefficients to Zero. (Uses L1 Regularization)
""")

# --- Sidebar: Data Generator ---
st.sidebar.header("⚙️ Data Lab")
n_samples = st.sidebar.slider("Dataset Size", 50, 500, 200)
st.sidebar.info("Target = 5 * StudyHours + 0.5 * PrevScore + Error")
noise_features = st.sidebar.multiselect(
    "Add 'Garbage' Features (Noise)",
    ["Shoe Size", "Jersey Number", "Twitter Followers", "Height (cm)", "Random ID"],
    default=["Shoe Size", "Twitter Followers", "Jersey Number"]
)

# --- Step 1: Generate Data ---
np.random.seed(42)

# Real Signals
study_hours = np.random.uniform(1, 10, n_samples)
prev_score = np.random.uniform(40, 100, n_samples)
# Target (Pass/Fail) depends ONLY on Study & Score
y_continuous = 5 * study_hours + 0.5 * prev_score + np.random.normal(0, 5, n_samples)

# Create DataFrame
data = {
    'Study Hours': study_hours,
    'Prev Exam Score': prev_score,
    'Target': y_continuous
}

# Add Garbage Noise
for feature in noise_features:
    data[feature] = np.random.uniform(0, 100, n_samples)

df = pd.DataFrame(data)

# Show Raw Data
st.subheader("1. The Dataset")
st.dataframe(df.head(5), use_container_width=True)

# --- Define Algorithms ---
X = df.drop(columns=['Target'])
y = df['Target']

tab1, tab2, tab3 = st.tabs(["🔙 Backward Elimination", "🔜 Forward Selection", "🎯 LASSO (L1)"])

# --- TAB 1: BACKWARD ELIMINATION ---
with tab1:
    st.markdown("#### The 'Garbage Collector' Approach")
    st.write("Starts with all features. Removes the one with the highest P-Value (>0.05).")

    if st.button("🚀 Run Backward Elimination"):
        iteration = 1
        features_remaining = list(X.columns)

        while len(features_remaining) > 0:
            # Fit Model
            X_current = X[features_remaining]
            X_with_const = sm.add_constant(X_current)
            model = sm.OLS(y, X_with_const).fit()

            # Get Worst Feature
            p_values = model.pvalues.drop('const')
            max_p = p_values.max()
            worst_feature = p_values.idxmax()

            # Decision
            col_a, col_b = st.columns([3, 1])
            if max_p > 0.05:
                col_a.markdown(f"**Round {iteration}:** `{worst_feature}` has P-Value **{max_p:.4f}**.")
                col_b.error(f"🗑️ DROPPED {worst_feature}")
                features_remaining.remove(worst_feature)
            else:
                col_a.markdown(f"**Round {iteration}:** All P-Values are < 0.05.")
                col_b.success("✅ STOPPING")
                break
            iteration += 1

        st.success(f"**Final Survivors:** {', '.join(features_remaining)}")

# --- TAB 2: FORWARD SELECTION ---
with tab2:
    st.markdown("#### The 'Talent Scout' Approach")
    st.write("Starts with zero features. Adds the one that improves R² score the most.")

    if st.button("🚀 Run Forward Selection"):
        selected_features = []
        remaining_candidates = list(X.columns)
        current_score = 0.0
        iteration = 1

        # Loop until no candidates left
        while len(remaining_candidates) > 0:
            scores_with_candidates = []

            # Test every candidate
            for candidate in remaining_candidates:
                temp_features = selected_features + [candidate]
                X_temp = X[temp_features]

                model = LinearRegression()
                model.fit(X_temp, y)
                score = r2_score(y, model.predict(X_temp))
                scores_with_candidates.append((score, candidate))

            # Find the winner of this round
            scores_with_candidates.sort(reverse=True)  # Highest score first
            best_new_score, best_candidate = scores_with_candidates[0]

            col_a, col_b = st.columns([3, 1])

            # Decision Logic: Did it improve the model?
            if best_new_score > current_score + 0.001:
                col_a.markdown(
                    f"**Round {iteration}:** Adding `{best_candidate}` improves R² to **{best_new_score:.4f}**.")
                col_b.success(f"➕ ADDED {best_candidate}")

                selected_features.append(best_candidate)
                remaining_candidates.remove(best_candidate)
                current_score = best_new_score
            else:
                col_a.markdown(
                    f"**Round {iteration}:** Adding `{best_candidate}` (R²={best_new_score:.4f}) shows no significant improvement.")
                col_b.warning("🛑 STOPPING")
                break

            iteration += 1

        st.success(f"**Final Selection:** {', '.join(selected_features)}")

# --- TAB 3: LASSO (L1 Regularization) ---
with tab3:
    st.markdown("#### The 'Penalty' Approach (LASSO)")
    st.write("Does not remove features step-by-step. Instead, it squeezes weak coefficients to Zero.")

    # User Input for Alpha
    alpha_val = st.slider("Select Regularization Strength (Alpha)", 0.01, 10.0, 1.0, step=0.1,
                          help="Higher Alpha = More features removed (Coefficients -> 0).")

    if st.button("🚀 Run LASSO Regression"):
        # 1. Initialize & Fit
        lasso_model = Lasso(alpha=alpha_val)
        lasso_model.fit(X, y)
        y_pred = lasso_model.predict(X)

        # 2. Analyze Coefficients
        coeffs = pd.Series(lasso_model.coef_, index=X.columns)
        r2 = r2_score(y, y_pred)

        st.metric("Model R² Score", f"{r2:.3f}")

        # 3. Visualization
        col_res1, col_res2 = st.columns(2)

        with col_res1:
            st.write("##### Feature Coefficients")
            st.write("Notice how 'Noise' features shrink to 0.0 as Alpha increases.")

            # Color logic: Red if 0 (Eliminated), Blue if kept
            colors = ['red' if c == 0 else 'blue' for c in coeffs.values]

            fig = go.Figure(go.Bar(
                x=coeffs.index,
                y=coeffs.values,
                marker_color=colors,
                text=[f"{v:.2f}" for v in coeffs.values],
                textposition='auto'
            ))
            fig.update_layout(title=f"LASSO Coefficients (Alpha={alpha_val})", yaxis_title="Coefficient Value")
            st.plotly_chart(fig, use_container_width=True)

        with col_res2:
            st.write("##### Selection Status")
            survivors = coeffs[coeffs != 0].index.tolist()
            eliminated = coeffs[coeffs == 0].index.tolist()

            if survivors:
                st.success(f"✅ **Kept:** {', '.join(survivors)}")
            if eliminated:
                st.error(f"🗑️ **Eliminated (Coef=0):** {', '.join(eliminated)}")
            else:
                st.info("No features eliminated yet. Try increasing Alpha!")