import streamlit as st
import pandas as pd
import numpy as np
import plotly.graph_objects as go
from sklearn.model_selection import train_test_split
from sklearn.linear_model import LinearRegression
from sklearn.metrics import mean_squared_error, r2_score

st.set_page_config(page_title="Linear Regression", layout="wide")

st.title("🏡 AI Real Estate Estimator")
st.markdown("### Supervised Learning: Regression")

# --- Sidebar ---
st.sidebar.header("⚙️ Simulation Controls")
data_points = st.sidebar.slider("Number of Houses", 10, 200, 50)
noise_level = st.sidebar.slider("Market Volatility (Noise)", 0, 50000, 15000)

# --- Logic ---
np.random.seed(42)
sq_ft = np.random.randint(1000, 5000, size=data_points)
price = (sq_ft * 150) + np.random.normal(0, noise_level, size=data_points) + 50000
df = pd.DataFrame({'SquareFootage': sq_ft, 'Price': price})

X = df[['SquareFootage']]
y = df['Price']
X_train, X_test, y_train, y_test = train_test_split(X, y, test_size=0.2, random_state=42)

model = LinearRegression()
model.fit(X_train, y_train)

# --- Visualization ---
x_range = np.linspace(df['SquareFootage'].min(), df['SquareFootage'].max(), 100).reshape(-1, 1)
y_range_pred = model.predict(x_range)

# Metrics
y_pred_test = model.predict(X_test)
mse = mean_squared_error(y_test, y_pred_test)
r2 = r2_score(y_test, y_pred_test)

col1, col2, col3 = st.columns(3)
col1.metric("Model Slope", f"${model.coef_[0]:.2f}/sqft")
col2.metric("R² Accuracy", f"{r2:.2f}")
col3.metric("MSE", f"{mse:,.0f}")

fig = go.Figure()
fig.add_trace(go.Scatter(x=df['SquareFootage'], y=df['Price'], mode='markers', name='Actual Sales'))
fig.add_trace(go.Scatter(x=x_range.flatten(), y=y_range_pred, mode='lines', name='AI Model', line=dict(color='red')))
fig.update_layout(title="Price vs. SqFt", xaxis_title="Square Footage", yaxis_title="Price")
st.plotly_chart(fig, use_container_width=True)

# --- Tester ---
st.divider()
user_input = st.number_input("Predict Price for SqFt:", 500, 10000, 2000)
if st.button("Calculate"):
    pred = model.predict([[user_input]])[0]
    st.success(f"Estimated Price: **${pred:,.2f}**")