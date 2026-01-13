import streamlit as st
import pandas as pd
import numpy as np
import plotly.express as px
import plotly.graph_objects as go
from sklearn.model_selection import train_test_split
from sklearn.linear_model import LinearRegression
from sklearn.metrics import mean_squared_error, r2_score

# --- UI Configuration ---
st.set_page_config(page_title="Linear Regression Lab", layout="wide")

st.title("🏡 AI Real Estate Estimator")
st.markdown("""
> **Leadership Note:** Transparency builds trust. This dashboard visualizes 
> how our machine learning model makes decisions based on square footage.
""")

st.divider()

# --- Sidebar: The Control Room ---
st.sidebar.header("⚙️ Simulation Controls")
st.sidebar.write("Tweak the dataset parameters to see how the model adapts.")

# Interactive: Let user choose dataset size and "Noise" (randomness)
data_points = st.sidebar.slider("Number of Houses", min_value=10, max_value=200, value=50)
noise_level = st.sidebar.slider("Market Volatility (Noise)", min_value=0, max_value=50000, value=15000)

# --- Step 1: Data Generation ---
# We create synthetic data based on the user's slider inputs
np.random.seed(42)
sq_ft = np.random.randint(1000, 5000, size=data_points)
# Base price calculation + random noise/volatility
price = (sq_ft * 150) + np.random.normal(0, noise_level, size=data_points) + 50000

df = pd.DataFrame({'SquareFootage': sq_ft, 'Price': price})

# --- Step 2: Modeling ---
X = df[['SquareFootage']]
y = df['Price']

X_train, X_test, y_train, y_test = train_test_split(X, y, test_size=0.2, random_state=42)

model = LinearRegression()
model.fit(X_train, y_train)

# Predictions for the line of best fit across the whole range
x_range = np.linspace(df['SquareFootage'].min(), df['SquareFootage'].max(), 100).reshape(-1, 1)
y_range_pred = model.predict(x_range)

# --- Step 3: Metrics & Evaluation ---
# We calculate metrics on the Test set only
y_pred_test = model.predict(X_test)
mse = mean_squared_error(y_test, y_pred_test)
r2 = r2_score(y_test, y_pred_test)

# Display Metrics in Columns
col1, col2, col3 = st.columns(3)
col1.metric("Model Slope (Price per SqFt)", f"${model.coef_[0]:.2f}")
col2.metric("Prediction Accuracy (R²)", f"{r2:.2f}")
col3.metric("Mean Squared Error", f"{mse:,.0f}")

# --- Step 4: Visualization ---
st.subheader("Interactive Regression Analysis")

# Using Plotly for interactive tooltips and zooming
fig = go.Figure()

# Add Actual Data Points
fig.add_trace(go.Scatter(
    x=df['SquareFootage'],
    y=df['Price'],
    mode='markers',
    name='Actual Sales',
    marker=dict(color='#3b82f6', opacity=0.6, size=8)
))

# Add Regression Line
fig.add_trace(go.Scatter(
    x=x_range.flatten(),
    y=y_range_pred,
    mode='lines',
    name='AI Prediction Model',
    line=dict(color='#ef4444', width=3)
))

fig.update_layout(
    title="Price vs. Square Footage",
    xaxis_title="Square Footage",
    yaxis_title="Price ($)",
    template="plotly_white",
    height=500
)

st.plotly_chart(fig, use_container_width=True)

# --- Step 5: Tester ---
st.divider()
st.subheader("🎯 Test the Model")
user_input = st.number_input("Enter Square Footage to Predict Price:", min_value=500, max_value=10000, value=2000)

if st.button("Predict Price"):
    prediction = model.predict([[user_input]])[0]
    st.success(f"The estimated price for a **{user_input} sqft** house is **${prediction:,.2f}**")