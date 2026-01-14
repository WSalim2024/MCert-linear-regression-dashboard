import streamlit as st
import pandas as pd
import numpy as np
import plotly.graph_objects as go
from sklearn.model_selection import train_test_split
from sklearn.linear_model import LogisticRegression
from sklearn.tree import DecisionTreeClassifier
from sklearn.metrics import accuracy_score, precision_score, recall_score, confusion_matrix

# --- UI Configuration ---
st.set_page_config(page_title="Model Showdown", layout="wide")

st.title("⚔️ Model Showdown: Logistic vs. Decision Tree")
st.markdown("### The Ultimate Test: Linear vs. Non-Linear")
st.markdown("""
> **The Challenge:** We will train both models on the **exact same dataset** (Study Hours + Previous Score).
> * **Logistic Regression** tries to draw a straight line to separate Pass/Fail.
> * **Decision Tree** tries to draw boxes around the Pass/Fail regions.
""")

# --- Sidebar: Simulation Controls ---
st.sidebar.header("⚙️ Data Lab")
dataset_size = st.sidebar.slider("Dataset Size", 50, 500, 200)
noise_level = st.sidebar.slider("Data Noise (Complexity)", 0.0, 1.0, 0.3,
                                help="Higher noise makes the groups harder to separate.")

# --- Step 1: Data Generation (2 Features) ---
np.random.seed(42)

# Feature 1: Study Hours (0-12)
study_hours = np.random.uniform(0, 12, dataset_size)
# Feature 2: Previous Exam Score (30-100)
prev_scores = np.random.uniform(30, 100, dataset_size)

# The "Truth" Logic: Pass if (Hours > 6) OR (Hours > 3 AND Score > 75)
# This creates a "Step" shape that is hard for a straight line to fit perfectly
base_logic = (study_hours > 6) | ((study_hours > 3) & (prev_scores > 75))
# Add noise flip
labels = [1 if (x and np.random.rand() > noise_level) else 0 for x in base_logic]
# Ensure valid labels even with high noise
labels = np.array([0 if l < 0 else (1 if l > 1 else l) for l in labels])

df = pd.DataFrame({
    'StudyHours': study_hours,
    'PrevExamScore': prev_scores,
    'Pass': labels
})

# Split Data
X = df[['StudyHours', 'PrevExamScore']]
y = df['Pass']
X_train, X_test, y_train, y_test = train_test_split(X, y, test_size=0.2, random_state=42)

# --- Step 2: Model Training ---
# Model A: Logistic Regression (The Linear Thinker)
log_model = LogisticRegression()
log_model.fit(X_train, y_train)
log_pred = log_model.predict(X_test)

# Model B: Decision Tree (The Non-Linear Thinker)
# We limit depth to 4 to prevent it from "cheating" (overfitting) too easily
tree_model = DecisionTreeClassifier(max_depth=4, random_state=42)
tree_model.fit(X_train, y_train)
tree_pred = tree_model.predict(X_test)

# --- Step 3: Comparative Metrics ---
st.divider()
st.subheader("1. The Scoreboard (Performance Comparison)")

metrics_data = {
    "Metric": ["Accuracy", "Precision (Pass)", "Recall (Pass)", "True Negatives", "False Positives"],
    "Logistic Regression": [
        f"{accuracy_score(y_test, log_pred):.1%}",
        f"{precision_score(y_test, log_pred, zero_division=0):.2f}",
        f"{recall_score(y_test, log_pred, zero_division=0):.2f}",
        confusion_matrix(y_test, log_pred)[0][0],
        confusion_matrix(y_test, log_pred)[0][1]
    ],
    "Decision Tree": [
        f"{accuracy_score(y_test, tree_pred):.1%}",
        f"{precision_score(y_test, tree_pred, zero_division=0):.2f}",
        f"{recall_score(y_test, tree_pred, zero_division=0):.2f}",
        confusion_matrix(y_test, tree_pred)[0][0],
        confusion_matrix(y_test, tree_pred)[0][1]
    ]
}
metrics_df = pd.DataFrame(metrics_data)
st.table(metrics_df)

# --- Step 4: Visualizing the Decision Boundaries ---
st.subheader("2. Visualizing the 'Brain' Differences")
st.write("Notice how the Linear model cuts straight, while the Tree carves out specific regions.")

# Create Meshgrid for plotting
x_min, x_max = X['StudyHours'].min() - 0.5, X['StudyHours'].max() + 0.5
y_min, y_max = X['PrevExamScore'].min() - 5, X['PrevExamScore'].max() + 5
xx, yy = np.meshgrid(np.arange(x_min, x_max, 0.1), np.arange(y_min, y_max, 1))


# Helper function to plot
def plot_boundary(model, title):
    Z = model.predict(np.c_[xx.ravel(), yy.ravel()])
    Z = Z.reshape(xx.shape)

    fig = go.Figure()
    # Decision Surface
    fig.add_trace(go.Contour(
        x=np.arange(x_min, x_max, 0.1), y=np.arange(y_min, y_max, 1), z=Z,
        showscale=False, colorscale=['#ffcccc', '#cceeff'], opacity=0.4, hoverinfo='skip'
    ))
    # Actual Data
    fig.add_trace(go.Scatter(
        x=df['StudyHours'], y=df['PrevExamScore'], mode='markers',
        marker=dict(size=8, color=df['Pass'], colorscale=['#ff0000', '#0000ff'], line=dict(width=1, color='black')),
        name='Student Data'
    ))
    fig.update_layout(title=title, xaxis_title="Study Hours", yaxis_title="Prev Score", height=500,
                      margin=dict(l=20, r=20, t=40, b=20))
    return fig


col1, col2 = st.columns(2)

with col1:
    st.markdown("#### 🤖 Logistic Regression")
    st.plotly_chart(plot_boundary(log_model, "Linear Boundary"), use_container_width=True)
    st.info("Observation: It draws a single straight line. It struggles if the 'Pass' group is L-shaped or clustered.")

with col2:
    st.markdown("#### 🌳 Decision Tree")
    st.plotly_chart(plot_boundary(tree_model, "Non-Linear Boundary"), use_container_width=True)
    st.success(
        "Observation: It draws rectangular 'steps'. It can capture the logic: 'Low hours are okay IF score is high'.")