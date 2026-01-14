import streamlit as st
import pandas as pd
import numpy as np
import plotly.express as px
from sklearn.model_selection import GridSearchCV, train_test_split
from sklearn.tree import DecisionTreeClassifier
from sklearn.metrics import accuracy_score

# --- UI Configuration ---
st.set_page_config(page_title="Grid Search Lab", layout="wide")

st.title("🔍 Automated Tuning (Grid Search)")
st.markdown("### Stop Guessing. Let the AI tune itself.")
st.markdown("""
> **The Problem:** Manually adjusting 'Max Depth' or 'Min Samples' is slow and imprecise.
> **The Solution:** **GridSearchCV**. We define a 'Grid' of settings, and the computer tests *every single combination*.
> **The Result:** The mathematically optimal configuration for your model.
""")

# --- Sidebar: Configuration ---
st.sidebar.header("⚙️ Data & Grid Config")
dataset_size = st.sidebar.slider("Dataset Size", 50, 500, 200)
noise_level = st.sidebar.slider("Data Noise", 0.0, 1.0, 0.3)

st.sidebar.divider()
st.sidebar.subheader("Define the Search Grid")
st.sidebar.info("Select the range of parameters to test.")

# The "Grid" inputs
depth_min, depth_max = st.sidebar.slider("Test Max Depths (Range)", 1, 10, (2, 6))
split_options = st.sidebar.multiselect("Test Criteria", ["gini", "entropy"], default=["gini", "entropy"])
min_samples_options = st.sidebar.multiselect("Test Min Samples Leaf", [1, 2, 5, 10], default=[1, 5])

# --- Step 1: Generate Data ---
np.random.seed(42)
study_hours = np.random.uniform(0, 12, dataset_size)
prev_scores = np.random.uniform(30, 100, dataset_size)
# Complex logic: Pass if (Hours > 6) OR (Hours > 3 AND Score > 75)
base_logic = (study_hours > 6) | ((study_hours > 3) & (prev_scores > 75))
labels = [1 if (x and np.random.rand() > noise_level) else 0 for x in base_logic]

df = pd.DataFrame({'StudyHours': study_hours, 'PrevExamScore': prev_scores, 'Target': labels})
X = df[['StudyHours', 'PrevExamScore']]
y = df['Target']

X_train, X_test, y_train, y_test = train_test_split(X, y, test_size=0.2, random_state=42)

# --- Step 2: The Grid Search Engine ---
st.divider()

if st.button("🚀 Run Grid Search Auto-Tuning", type="primary"):
    if not split_options or not min_samples_options:
        st.error("Please select at least one Criterion and one Min Sample option.")
    else:
        # 1. Define the Parameter Grid
        param_grid = {
            'max_depth': range(depth_min, depth_max + 1),
            'criterion': split_options,
            'min_samples_leaf': min_samples_options
        }

        # 2. Initialize Logic
        tree = DecisionTreeClassifier(random_state=42)
        grid_search = GridSearchCV(tree, param_grid, cv=5, scoring='accuracy', n_jobs=-1)

        with st.spinner(
                f"Testing {len(param_grid['max_depth']) * len(split_options) * len(min_samples_options)} combinations..."):
            # 3. Fit (Train)
            grid_search.fit(X_train, y_train)

        # --- Step 3: Analysis Dashboard ---
        best_model = grid_search.best_estimator_
        test_acc = best_model.score(X_test, y_test)

        # Top Metrics Row
        col1, col2, col3 = st.columns(3)
        col1.metric("🏆 Best Accuracy (CV)", f"{grid_search.best_score_:.1%}")
        col2.metric("🧪 Test Set Accuracy", f"{test_acc:.1%}")
        col3.success(f"Best Params: {grid_search.best_params_}")

        # Visualizing Results
        results_df = pd.DataFrame(grid_search.cv_results_)

        # Filter relevant columns for display
        clean_results = results_df[
            ['param_max_depth', 'param_criterion', 'param_min_samples_leaf', 'mean_test_score', 'rank_test_score']]
        clean_results.columns = ['Depth', 'Criterion', 'Min Samples', 'Accuracy', 'Rank']

        st.subheader("📊 Performance Landscape")

        tab1, tab2 = st.tabs(["Heatmap Visualization", "Detailed Results Table"])

        with tab1:
            st.write("Darker Blue = Better Performance. Find the 'Sweet Spot'.")
            # Pivot data for heatmap: Depth vs Min Samples (averaged over criterion)
            heatmap_data = clean_results.pivot_table(index='Depth', columns='Min Samples', values='Accuracy',
                                                     aggfunc='mean')

            fig = px.imshow(
                heatmap_data,
                text_auto='.1%',
                aspect="auto",
                color_continuous_scale="Blues",
                labels=dict(x="Min Samples Leaf", y="Tree Depth", color="Accuracy"),
                title="Hyperparameter Heatmap: Depth vs. Min Samples"
            )
            st.plotly_chart(fig, use_container_width=True)

        with tab2:
            st.dataframe(clean_results.sort_values(by='Rank').style.format({'Accuracy': '{:.2%}'}))

else:
    st.info("👈 Configure your grid on the left, then click 'Run Grid Search' to find the best AI settings.")