import streamlit as st
import pandas as pd
import numpy as np
import plotly.express as px
import plotly.graph_objects as go
import matplotlib.pyplot as plt
from sklearn.model_selection import train_test_split
from sklearn.tree import DecisionTreeClassifier, plot_tree
from sklearn.metrics import accuracy_score, confusion_matrix

# --- UI Configuration ---
st.set_page_config(page_title="Decision Tree Classifier", layout="wide")

st.title("🌳 AI Decision Tree")
st.markdown("### Supervised Learning: Non-Linear Classification")
st.markdown("""
> **The Logic:** Unlike Regression, a Decision Tree splits data into branches. 
> It asks a sequence of "Yes/No" questions to categorize data. 
> This is great for capturing complex, non-linear patterns.
""")

# --- Sidebar: Controls ---
st.sidebar.header("⚙️ Model Tuning")
st.sidebar.write("Adjust parameters to control Overfitting vs. Underfitting.")

# Hyperparameters (Tuning)
max_depth = st.sidebar.slider("Max Tree Depth", 1, 10, 3,
                              help="How deep the tree can grow. Deeper = More complex (risk of overfitting).")
min_samples = st.sidebar.slider("Min Samples to Split", 2, 20, 5,
                                help="Minimum data points required to create a new branch.")
criterion = st.sidebar.selectbox("Split Criterion", ["gini", "entropy"],
                                 help="The math used to measure the quality of a split.")

st.sidebar.divider()
st.sidebar.header("📝 Simulation Data")
dataset_size = st.sidebar.slider("Dataset Size", 20, 200, 100)
noise_level = st.sidebar.slider("Data Noise (Overlap)", 0.0, 1.0, 0.2)

# --- Step 1: Data Generation ---
# We simulate a relationship: High Study Hours + High Prev Score = PASS
np.random.seed(42)

# Feature 1: Study Hours (0 to 12)
study_hours = np.random.uniform(0, 12, dataset_size)
# Feature 2: Previous Exam Score (30 to 100)
prev_scores = np.random.uniform(30, 100, dataset_size)

# Logic: Pass if (Study > 6) OR (Study > 4 AND Score > 70)
# We add noise to make it realistic (some people pass with less work, some fail with more)
base_logic = (study_hours > 6) | ((study_hours > 4) & (prev_scores > 70))
labels = [1 if (x and np.random.rand() > noise_level) else 0 for x in base_logic]
# Fix random flips to ensure at least some noise logic holds
labels = np.array(labels)

df = pd.DataFrame({
    'StudyHours': study_hours,
    'PrevExamScore': prev_scores,
    'Pass': labels
})

# --- Step 2: Training ---
X = df[['StudyHours', 'PrevExamScore']]
y = df['Pass']

X_train, X_test, y_train, y_test = train_test_split(X, y, test_size=0.2, random_state=42)

model = DecisionTreeClassifier(max_depth=max_depth, min_samples_split=min_samples, criterion=criterion)
model.fit(X_train, y_train)

# Predictions
y_pred = model.predict(X_test)
accuracy = accuracy_score(y_test, y_pred)
conf_matrix = confusion_matrix(y_test, y_pred)

# --- Step 3: The Dashboard ---

# Tab 1: Performance & Boundary
# Tab 2: The Tree Structure (Visualizing the brain)
tab1, tab2 = st.tabs(["📊 Decision Boundary & Metrics", "🌳 Tree Structure Visualization"])

with tab1:
    col1, col2, col3 = st.columns(3)
    col1.metric("Model Accuracy", f"{accuracy:.1%}")
    col2.metric("Tree Depth", model.get_depth())
    col3.metric("Leaf Nodes", model.get_n_leaves())

    st.subheader("Decision Boundary Visualization")
    st.write("The background color shows how the AI carves the map into 'Pass' (Blue) and 'Fail' (Red) regions.")

    # Create a meshgrid to visualize the "Decision Surface"
    x_min, x_max = X['StudyHours'].min() - 1, X['StudyHours'].max() + 1
    y_min, y_max = X['PrevExamScore'].min() - 5, X['PrevExamScore'].max() + 5
    xx, yy = np.meshgrid(np.arange(x_min, x_max, 0.1), np.arange(y_min, y_max, 1))

    # Predict across the entire grid
    Z = model.predict(np.c_[xx.ravel(), yy.ravel()])
    Z = Z.reshape(xx.shape)

    # Plotly Contour Plot for Decision Boundary
    fig = go.Figure()

    # 1. The Decision Regions (Background)
    fig.add_trace(go.Contour(
        x=np.arange(x_min, x_max, 0.1),
        y=np.arange(y_min, y_max, 1),
        z=Z,
        showscale=False,
        colorscale=['#ffcccc', '#cceeff'],  # Light Red (Fail), Light Blue (Pass)
        opacity=0.4,
        hoverinfo='skip',
        name='Decision Region'
    ))

    # 2. The Actual Data Points
    fig.add_trace(go.Scatter(
        x=df['StudyHours'],
        y=df['PrevExamScore'],
        mode='markers',
        marker=dict(
            size=10,
            color=df['Pass'],
            colorscale=['#ff0000', '#0000ff'],  # Red (Fail), Blue (Pass)
            line=dict(width=1, color='black')
        ),
        text=['PASS' if p == 1 else 'FAIL' for p in df['Pass']],
        name='Student Data'
    ))

    fig.update_layout(
        xaxis_title="Study Hours",
        yaxis_title="Previous Exam Score",
        height=600,
        title="Study Hours vs. Exam Score"
    )
    st.plotly_chart(fig, use_container_width=True)

with tab2:
    st.subheader("Visualizing the Logic")
    st.write("This diagram shows the exact questions the model asks to reach a decision.")

    # We use Matplotlib for the tree structure as it's the standard for sklearn
    fig_tree, ax = plt.subplots(figsize=(20, 10))
    plot_tree(model,
              filled=True,
              feature_names=['Study Hours', 'Prev Score'],
              class_names=['Fail', 'Pass'],
              rounded=True,
              ax=ax,
              fontsize=10)
    st.pyplot(fig_tree)

# --- Step 4: Live Tester ---
st.divider()
st.subheader("🎯 Test the Model")
col_input1, col_input2, col_btn = st.columns([1, 1, 1])

with col_input1:
    in_hours = st.number_input("Study Hours", 0.0, 12.0, 5.0)
with col_input2:
    in_score = st.number_input("Previous Score", 0, 100, 70)

if col_btn.button("Predict Outcome"):
    prediction = model.predict([[in_hours, in_score]])[0]
    result = "PASS" if prediction == 1 else "FAIL"
    color = "green" if result == "PASS" else "red"
    st.markdown(f"### Prediction: <span style='color:{color}'>{result}</span>", unsafe_allow_html=True)