import streamlit as st
import pandas as pd
import numpy as np
import plotly.graph_objects as go
from sklearn.linear_model import LogisticRegression

st.set_page_config(page_title="Logistic Regression", layout="wide")

st.title("🎓 AI Student Success Predictor")
st.markdown("### Supervised Learning: Classification")

# --- Sidebar ---
st.sidebar.header("⚙️ Simulation Lab")
hours_studied = st.sidebar.slider("Your Study Hours", 0.0, 12.0, 5.5, step=0.5)
dataset_size = st.sidebar.slider("Dataset Size", 10, 100, 30)

# --- Logic ---
np.random.seed(42)
study_hours = np.random.uniform(1, 10, dataset_size)
probabilities = 1 / (1 + np.exp(-(study_hours - 5.5) * 2))
pass_fail = [1 if np.random.rand() < p else 0 for p in probabilities]
df = pd.DataFrame({'StudyHours': study_hours, 'Pass': pass_fail})

model = LogisticRegression()
model.fit(df[['StudyHours']], df['Pass'])

# --- Visualization ---
x_range = np.linspace(0, 12, 100).reshape(-1, 1)
y_range_prob = model.predict_proba(x_range)[:, 1]
user_prob = model.predict_proba([[hours_studied]])[0][1]
user_outcome = "PASS" if user_prob > 0.5 else "FAIL"

col1, col2, col3 = st.columns(3)
col1.metric("Input Hours", f"{hours_studied} hrs")
col2.metric("Prediction", user_outcome)
col3.metric("Probability", f"{user_prob:.1%}")

fig = go.Figure()
fig.add_trace(go.Scatter(x=df['StudyHours'], y=df['Pass'], mode='markers', name='Student Data', marker=dict(color=df['Pass'], colorscale='RdYlGn')))
fig.add_trace(go.Scatter(x=x_range.flatten(), y=y_range_prob, mode='lines', name='Sigmoid Curve', line=dict(color='blue')))
fig.add_trace(go.Scatter(x=[hours_studied], y=[user_prob], mode='markers', name='You', marker=dict(size=15, color='orange', symbol='star')))

fig.update_layout(title="Probability of Passing vs. Study Hours", xaxis_title="Hours", yaxis_title="Probability")
st.plotly_chart(fig, use_container_width=True)

with st.expander("Show Model Coefficients"):
    st.write(f"Slope (Coefficient): {model.coef_[0][0]:.4f}")
    st.write(f"Intercept: {model.intercept_[0]:.4f}")