<div align="center">

# 🧠 The Machine Learning Workbench

### **Version 3.4 — The Feature Engineering Update**

*A Comprehensive ML Educational Suite: From Basic Regression to Automated Feature Selection*

---

![Python](https://img.shields.io/badge/Python-3.10+-3776AB?style=for-the-badge&logo=python&logoColor=white)
![Streamlit](https://img.shields.io/badge/Streamlit-1.28+-FF4B4B?style=for-the-badge&logo=streamlit&logoColor=white)
![Scikit-Learn](https://img.shields.io/badge/Scikit--Learn-1.3+-F7931E?style=for-the-badge&logo=scikit-learn&logoColor=white)
![Statsmodels](https://img.shields.io/badge/Statsmodels-0.14+-4051B5?style=for-the-badge&logo=python&logoColor=white)
![Version](https://img.shields.io/badge/Version-3.4-blueviolet?style=for-the-badge)
![Modules](https://img.shields.io/badge/Modules-7-orange?style=for-the-badge)
![License](https://img.shields.io/badge/License-MIT-green?style=for-the-badge)

<br>

[**Features**](#-key-features) · [**Modules**](#-module-overview) · [**Installation**](#-installation) · [**User Guide**](#-user-guide)

<br>

```
╔═══════════════════════════════════════════════════════════════════════════════╗
║                                                                               ║
║    "Not all features are created equal — let statistics prove which ones     ║
║     matter and which ones are just noise."                                    ║
║                                                                               ║
╚═══════════════════════════════════════════════════════════════════════════════╝
```

</div>

---

## 📋 Table of Contents

- [Overview](#-overview)
- [What's New in v3.4](#-whats-new-in-v34)
- [Key Features](#-key-features)
- [Module Overview](#-module-overview)
- [Module G: Feature Selection Lab](#-module-g-feature-selection-lab-new)
- [How It Works: Backward Elimination](#-how-it-works-backward-elimination)
- [Tech Stack](#-tech-stack)
- [Installation](#-installation)
- [User Guide](#-user-guide)
- [Disclaimer](#-disclaimer)
- [Author](#-author)

---

## 🚀 Overview

**The Machine Learning Workbench v3.4** has evolved into a **comprehensive ML educational suite** — a complete learning platform that takes users from fundamental concepts to advanced feature engineering techniques.

This release introduces **statistical feature selection**, answering one of the most critical questions in machine learning: *"Which features actually matter?"*

<div align="center">

```
┌─────────────────────────────────────────────────────────────────────────────────┐
│                         THE COMPLETE LEARNING JOURNEY                           │
├─────────────────────────────────────────────────────────────────────────────────┤
│                                                                                 │
│   FUNDAMENTALS          VALIDATION           AUTOMATION         ENGINEERING    │
│       │                     │                    │                   │         │
│       ▼                     ▼                    ▼                   ▼         │
│   ┌───────┐            ┌───────┐            ┌───────┐           ┌───────┐      │
│   │ Learn │     →      │ Trust │     →      │ Tune  │     →     │ Clean │      │
│   │Models │            │Models │            │Models │           │  Data │      │
│   └───────┘            └───────┘            └───────┘           └───────┘      │
│                                                                                 │
│   Modules              Module E              Module F            Module G       │
│    A-D                 Cross-Val             Grid Search         Feature        │
│                                                                  Selection      │
│                                                                                 │
│                    ◄─────────── v3.4 COMPLETE SUITE ───────────►               │
│                                                                                 │
└─────────────────────────────────────────────────────────────────────────────────┘
```

</div>

### Platform Capabilities

| Capability | Description | Module |
|------------|-------------|--------|
| 📈 **Visualization** | See algorithms think in real-time | A, B, C |
| ⚔️ **Comparison** | Pit algorithms against each other | D |
| 🔬 **Validation** | Test reliability with K-Fold CV | E |
| 🔍 **Optimization** | Auto-tune hyperparameters | F |
| 🗑️ **Feature Selection** | Eliminate useless variables | G |

---

## ✨ What's New in v3.4

### 🗑️ Feature Selection Lab — "The Garbage Collector"

The flagship addition that uses **statistical hypothesis testing** to mathematically prove which features contribute to predictions and which ones are just noise.

| Feature | Description |
|---------|-------------|
| 📊 **Backward Elimination** | Iteratively removes statistically insignificant features |
| 📉 **P-Value Analysis** | Uses statsmodels OLS for significance testing |
| 🎭 **Noise Injection** | Mixes real predictors with garbage features |
| 📋 **Elimination Log** | Watch features get dropped round-by-round |
| ✅ **Final Significance Check** | Verify surviving features are truly significant |

### 🆕 New Dependency: Statsmodels

```diff
+ statsmodels>=0.14.0    # NEW: OLS regression with P-Value calculation
```

**Why Statsmodels?**

Scikit-Learn is optimized for prediction, not inference. For statistical significance testing (P-Values, confidence intervals), we need `statsmodels`:

```python
# Scikit-Learn: Prediction-focused
from sklearn.linear_model import LinearRegression
model.fit(X, y)
predictions = model.predict(X_new)  # ✅ Great for this

# Statsmodels: Inference-focused
import statsmodels.api as sm
model = sm.OLS(y, X).fit()
p_values = model.pvalues  # ✅ Great for this
```

---

## 🎯 Key Features

<table>
<tr>
<td width="50%">

### 📈 Core Algorithms
- **Linear Regression** — Continuous value prediction
- **Logistic Regression** — Binary classification
- **Decision Trees** — Non-linear boundaries
- **Real-time Training** — Instant visual feedback

</td>
<td width="50%">

### 🔬 Validation & Reliability
- **K-Fold Cross-Validation** — Test across multiple splits
- **Variance Analysis** — Measure model stability
- **Per-Fold Breakdown** — Granular performance view

</td>
</tr>
<tr>
<td width="50%">

### 🔍 Automation & Tuning
- **Grid Search** — Exhaustive parameter optimization
- **Heatmap Visualization** — Parameter landscape mapping
- **Best Config Discovery** — Automatic optimal settings

</td>
<td width="50%">

### 🗑️ Feature Engineering (NEW)
- **Backward Elimination** — Statistical feature pruning
- **P-Value Calculation** — Significance testing
- **Noise Detection** — Identify garbage features
- **Elimination Logging** — Step-by-step removal tracking

</td>
</tr>
</table>

---

## 📦 Module Overview

The Workbench now contains **7 distinct learning modules**, each building on the previous:

<div align="center">

| Module | Name | Icon | Focus Area | Key Concept |
|:------:|:-----|:----:|:-----------|:------------|
| **A** | Linear Regression | 📈 | Continuous Prediction | OLS, Best-Fit Line |
| **B** | Logistic Regression | 📊 | Binary Classification | Sigmoid, Probability |
| **C** | Decision Tree | 🌳 | Non-linear Boundaries | Gini Impurity, Splits |
| **D** | Model Showdown | ⚔️ | Algorithm Comparison | Linear vs Non-linear |
| **E** | Cross-Validation Lab | 🔬 | Reliability Testing | K-Fold, Variance |
| **F** | Grid Search Lab | 🔍 | Hyperparameter Tuning | Exhaustive Search |
| **G** | Feature Selection Lab | 🗑️ | **Feature Engineering** | **Backward Elimination** |

</div>

### Module Progression Path

```
┌─────────────────────────────────────────────────────────────────────────────────┐
│                           LEARNING PROGRESSION                                  │
├─────────────────────────────────────────────────────────────────────────────────┤
│                                                                                 │
│   BEGINNER                 INTERMEDIATE                 ADVANCED                │
│                                                                                 │
│   ┌─────┐ ┌─────┐ ┌─────┐     ┌─────┐ ┌─────┐          ┌─────┐ ┌─────┐         │
│   │  A  │→│  B  │→│  C  │ ──► │  D  │→│  E  │ ──────►  │  F  │→│  G  │         │
│   └─────┘ └─────┘ └─────┘     └─────┘ └─────┘          └─────┘ └─────┘         │
│                                                                                 │
│   "How do        "Which       "Is my         "What's the   "Which features     │
│    models         model is     model          best           actually           │
│    work?"         better?"     reliable?"     config?"       matter?"           │
│                                                                                 │
└─────────────────────────────────────────────────────────────────────────────────┘
```

---

## 🗑️ Module G: Feature Selection Lab (NEW!)

<div align="center">

### **"The Garbage Collector"**

*Mathematically proving which features matter and which are just noise*

</div>

### The Problem: Feature Pollution

In real-world datasets, not all columns contribute to predictions. Some features are:

```
┌─────────────────────────────────────────────────────────────────────────────────┐
│                        FEATURE POLLUTION PROBLEM                                │
├─────────────────────────────────────────────────────────────────────────────────┤
│                                                                                 │
│   PREDICTING: Student Exam Scores                                               │
│                                                                                 │
│   USEFUL FEATURES:                    GARBAGE FEATURES:                         │
│   ─────────────────                   ─────────────────                         │
│   ✅ Study Hours (correlation!)       ❌ Shoe Size (random noise)               │
│   ✅ Attendance Rate (predictive!)    ❌ Jersey Number (meaningless)            │
│   ✅ Previous GPA (strong signal!)    ❌ Favorite Color Code (irrelevant)       │
│                                       ❌ Birth Month (no relationship)          │
│                                                                                 │
│   THE QUESTION: How do we PROVE which features are garbage?                     │
│   THE ANSWER: Statistical significance testing (P-Values)                       │
│                                                                                 │
└─────────────────────────────────────────────────────────────────────────────────┘
```

### The Solution: Backward Elimination

The Feature Selection Lab uses **Backward Elimination** — a systematic process that:

1. Starts with ALL features (useful + garbage)
2. Fits an OLS regression model
3. Calculates P-Values for each feature
4. Removes the feature with the **highest P-Value** (if P > 0.05)
5. Repeats until all remaining features are statistically significant

### P-Value Interpretation

| P-Value | Meaning | Action |
|---------|---------|--------|
| **P < 0.01** | Highly significant | ✅ Definitely keep |
| **P < 0.05** | Statistically significant | ✅ Keep |
| **P ≥ 0.05** | Not significant | ❌ **ELIMINATE** |
| **P > 0.50** | Likely random noise | ❌ Garbage feature |

### The Lab Interface

```
┌─────────────────────────────────────────────────────────────────────────────────┐
│                       🗑️ FEATURE SELECTION LAB                                  │
├─────────────────────────────────────────────────────────────────────────────────┤
│                                                                                 │
│  📊 DATASET CONFIGURATION                                                       │
│  ┌───────────────────────────────────────────────────────────────────────────┐  │
│  │  Real Feature: Study_Hours (TRUE predictor of exam scores)               │  │
│  │                                                                           │  │
│  │  Noise Features Injected:                                                 │  │
│  │    • Shoe_Size (random integers 6-12)                                     │  │
│  │    • Jersey_Number (random integers 1-99)                                 │  │
│  │    • Favorite_Color_Code (random integers 1-10)                           │  │
│  │    • Birth_Month (random integers 1-12)                                   │  │
│  │                                                                           │  │
│  │  Target: Exam_Score = f(Study_Hours) + ε                                  │  │
│  └───────────────────────────────────────────────────────────────────────────┘  │
│                                                                                 │
│  🔄 BACKWARD ELIMINATION IN PROGRESS...                                         │
│                                                                                 │
└─────────────────────────────────────────────────────────────────────────────────┘
```

---

### 📋 The Elimination Log

Watch the algorithm systematically identify and remove garbage features round-by-round:

```
┌─────────────────────────────────────────────────────────────────────────────────┐
│                          📋 ELIMINATION LOG                                     │
├─────────────────────────────────────────────────────────────────────────────────┤
│                                                                                 │
│  ╔═══════════════════════════════════════════════════════════════════════════╗  │
│  ║ ROUND 1                                                                   ║  │
│  ╠═══════════════════════════════════════════════════════════════════════════╣  │
│  ║ Feature             │ Coefficient │ P-Value  │ Status                     ║  │
│  ╠═════════════════════╪═════════════╪══════════╪════════════════════════════╣  │
│  ║ const               │   12.453    │  0.0001  │ ✅ Significant             ║  │
│  ║ Study_Hours         │    8.721    │  0.0000  │ ✅ Significant             ║  │
│  ║ Shoe_Size           │    0.234    │  0.7823  │ ⚠️  Candidate              ║  │
│  ║ Jersey_Number       │   -0.012    │  0.9156  │ 🗑️  WORST (removing...)   ║  │
│  ║ Favorite_Color_Code │    0.156    │  0.6234  │ ⚠️  Candidate              ║  │
│  ║ Birth_Month         │   -0.089    │  0.8901  │ ⚠️  Candidate              ║  │
│  ╚═══════════════════════════════════════════════════════════════════════════╝  │
│                                                                                 │
│  🗑️ DROPPED: Jersey_Number (P-Value: 0.9156 > 0.05)                             │
│                                                                                 │
│  ══════════════════════════════════════════════════════════════════════════════ │
│                                                                                 │
│  ╔═══════════════════════════════════════════════════════════════════════════╗  │
│  ║ ROUND 2                                                                   ║  │
│  ╠═══════════════════════════════════════════════════════════════════════════╣  │
│  ║ Feature             │ Coefficient │ P-Value  │ Status                     ║  │
│  ╠═════════════════════╪═════════════╪══════════╪════════════════════════════╣  │
│  ║ const               │   12.501    │  0.0001  │ ✅ Significant             ║  │
│  ║ Study_Hours         │    8.698    │  0.0000  │ ✅ Significant             ║  │
│  ║ Shoe_Size           │    0.198    │  0.8012  │ ⚠️  Candidate              ║  │
│  ║ Favorite_Color_Code │    0.167    │  0.5987  │ ⚠️  Candidate              ║  │
│  ║ Birth_Month         │   -0.102    │  0.8734  │ 🗑️  WORST (removing...)   ║  │
│  ╚═══════════════════════════════════════════════════════════════════════════╝  │
│                                                                                 │
│  🗑️ DROPPED: Birth_Month (P-Value: 0.8734 > 0.05)                               │
│                                                                                 │
│  ══════════════════════════════════════════════════════════════════════════════ │
│                                                                                 │
│  ╔═══════════════════════════════════════════════════════════════════════════╗  │
│  ║ ROUND 3                                                                   ║  │
│  ╠═══════════════════════════════════════════════════════════════════════════╣  │
│  ║ Feature             │ Coefficient │ P-Value  │ Status                     ║  │
│  ╠═════════════════════╪═════════════╪══════════╪════════════════════════════╣  │
│  ║ const               │   12.534    │  0.0000  │ ✅ Significant             ║  │
│  ║ Study_Hours         │    8.712    │  0.0000  │ ✅ Significant             ║  │
│  ║ Shoe_Size           │    0.187    │  0.8123  │ 🗑️  WORST (removing...)   ║  │
│  ║ Favorite_Color_Code │    0.145    │  0.6456  │ ⚠️  Candidate              ║  │
│  ╚═══════════════════════════════════════════════════════════════════════════╝  │
│                                                                                 │
│  🗑️ DROPPED: Shoe_Size (P-Value: 0.8123 > 0.05)                                 │
│                                                                                 │
│  ══════════════════════════════════════════════════════════════════════════════ │
│                                                                                 │
│  ╔═══════════════════════════════════════════════════════════════════════════╗  │
│  ║ ROUND 4                                                                   ║  │
│  ╠═══════════════════════════════════════════════════════════════════════════╣  │
│  ║ Feature             │ Coefficient │ P-Value  │ Status                     ║  │
│  ╠═════════════════════╪═════════════╪══════════╪════════════════════════════╣  │
│  ║ const               │   12.567    │  0.0000  │ ✅ Significant             ║  │
│  ║ Study_Hours         │    8.723    │  0.0000  │ ✅ Significant             ║  │
│  ║ Favorite_Color_Code │    0.134    │  0.6789  │ 🗑️  WORST (removing...)   ║  │
│  ╚═══════════════════════════════════════════════════════════════════════════╝  │
│                                                                                 │
│  🗑️ DROPPED: Favorite_Color_Code (P-Value: 0.6789 > 0.05)                       │
│                                                                                 │
└─────────────────────────────────────────────────────────────────────────────────┘
```

---

### ✅ Final Significance Check

After elimination completes, a bar chart displays the P-Values of surviving features:

```
┌─────────────────────────────────────────────────────────────────────────────────┐
│                      ✅ FINAL SIGNIFICANCE CHECK                                │
├─────────────────────────────────────────────────────────────────────────────────┤
│                                                                                 │
│  P-Value (log scale)                                                            │
│    │                                                                            │
│    │                                                                            │
│ .05├ ─ ─ ─ ─ ─ ─ ─ ─ ─ ─ ─ ─ ─ ─ SIGNIFICANCE THRESHOLD ─ ─ ─ ─ ─ ─ ─ ─ ─     │
│    │                                                                            │
│    │                                                                            │
│    │                                                                            │
│    │                                                                            │
│.001│                                                                            │
│    │                                                                            │
│    │                                                                            │
│    │  ▓▓                                                                        │
│    │  ▓▓                                                                        │
│.000│  ▓▓  ← P-Value so small it's barely visible!                               │
│    │  ▓▓                                                                        │
│    └──┬────────────────────────────────────────────────────────────────────     │
│       │                                                                         │
│    Study_Hours                                                                  │
│                                                                                 │
│  ═══════════════════════════════════════════════════════════════════════════    │
│                                                                                 │
│  📊 FINAL MODEL SUMMARY                                                         │
│  ┌───────────────────────────────────────────────────────────────────────────┐  │
│  │                                                                           │  │
│  │  Surviving Features: 1 (Study_Hours)                                      │  │
│  │  Eliminated Features: 4 (Shoe_Size, Jersey_Number, Favorite_Color_Code,   │  │
│  │                          Birth_Month)                                     │  │
│  │                                                                           │  │
│  │  Study_Hours:                                                             │  │
│  │    • Coefficient: 8.723                                                   │  │
│  │    • P-Value: 0.0000000012 (highly significant!)                          │  │
│  │    • Interpretation: Each additional study hour increases                 │  │
│  │                      exam score by ~8.7 points                            │  │
│  │                                                                           │  │
│  │  R-Squared: 0.847 (84.7% of variance explained by Study_Hours alone)      │  │
│  │                                                                           │  │
│  └───────────────────────────────────────────────────────────────────────────┘  │
│                                                                                 │
│  🎯 CONCLUSION: The algorithm correctly identified Study_Hours as the ONLY     │
│     statistically significant predictor, eliminating all 4 noise features.     │
│                                                                                 │
└─────────────────────────────────────────────────────────────────────────────────┘
```

**Why is the bar barely visible?**

When a feature is truly predictive, its P-Value is astronomically small (e.g., 0.0000000012). On a chart where the threshold is 0.05, such tiny values appear as almost invisible bars — which is exactly what we want to see!

---

## ⚙️ How It Works: Backward Elimination

The Feature Selection Lab implements a systematic **Backward Elimination** workflow:

```
┌─────────────────────────────────────────────────────────────────────────────────┐
│                     🔄 BACKWARD ELIMINATION WORKFLOW                            │
├─────────────────────────────────────────────────────────────────────────────────┤
│                                                                                 │
│                              ┌─────────────┐                                    │
│                              │   START     │                                    │
│                              │ All Features│                                    │
│                              └──────┬──────┘                                    │
│                                     │                                           │
│                                     ▼                                           │
│                         ┌───────────────────────┐                               │
│                         │   FIT OLS MODEL       │                               │
│                         │   (statsmodels.OLS)   │                               │
│                         └───────────┬───────────┘                               │
│                                     │                                           │
│                                     ▼                                           │
│                         ┌───────────────────────┐                               │
│                         │   GET P-VALUES        │                               │
│                         │   for all features    │                               │
│                         └───────────┬───────────┘                               │
│                                     │                                           │
│                                     ▼                                           │
│                         ┌───────────────────────┐                               │
│                         │   MAX P-VALUE > 0.05? │                               │
│                         └───────────┬───────────┘                               │
│                                     │                                           │
│                        ┌────────────┴────────────┐                              │
│                        │                         │                              │
│                       YES                        NO                             │
│                        │                         │                              │
│                        ▼                         ▼                              │
│              ┌─────────────────┐       ┌─────────────────┐                      │
│              │  DROP FEATURE   │       │      DONE       │                      │
│              │  with highest   │       │                 │                      │
│              │    P-Value      │       │  All remaining  │                      │
│              └────────┬────────┘       │  features are   │                      │
│                       │                │   significant   │                      │
│                       │                └─────────────────┘                      │
│                       │                                                         │
│                       └──────────────────┐                                      │
│                                          │                                      │
│                                          ▼                                      │
│                              (Return to FIT step)                               │
│                                                                                 │
└─────────────────────────────────────────────────────────────────────────────────┘
```

### Implementation Code

```python
import statsmodels.api as sm
import numpy as np

def backward_elimination(X, y, significance_level=0.05):
    """
    Perform backward elimination for feature selection.
    
    Parameters:
    -----------
    X : DataFrame
        Feature matrix with column names
    y : Series
        Target variable
    significance_level : float
        P-value threshold (default: 0.05)
    
    Returns:
    --------
    list : Names of selected features
    """
    features = list(X.columns)
    elimination_log = []
    
    while len(features) > 0:
        # Step 1: Fit OLS model with current features
        X_with_const = sm.add_constant(X[features])
        model = sm.OLS(y, X_with_const).fit()
        
        # Step 2: Get P-Values (exclude constant)
        p_values = model.pvalues[1:]  # Skip 'const'
        
        # Step 3: Find maximum P-Value
        max_p_value = p_values.max()
        
        # Step 4: Check if worst feature exceeds threshold
        if max_p_value > significance_level:
            # Identify and drop the worst feature
            worst_feature = p_values.idxmax()
            features.remove(worst_feature)
            
            # Log the elimination
            elimination_log.append({
                'round': len(elimination_log) + 1,
                'dropped': worst_feature,
                'p_value': max_p_value
            })
        else:
            # All remaining features are significant
            break
    
    return features, elimination_log
```

### Why Statsmodels for P-Values?

```
┌─────────────────────────────────────────────────────────────────────────────────┐
│                    SCIKIT-LEARN vs STATSMODELS                                  │
├─────────────────────────────────────────────────────────────────────────────────┤
│                                                                                 │
│  SCIKIT-LEARN (Prediction-Focused)        STATSMODELS (Inference-Focused)       │
│  ──────────────────────────────────        ─────────────────────────────────    │
│                                                                                 │
│  ✅ Fast model training                   ✅ P-Values for each coefficient      │
│  ✅ Easy prediction pipeline              ✅ Confidence intervals                │
│  ✅ Cross-validation built-in             ✅ Hypothesis testing                  │
│  ❌ No native P-Value calculation         ✅ R-squared, Adj R-squared            │
│  ❌ No significance testing               ✅ F-statistic                         │
│                                                                                 │
│  USE CASE: Production ML                  USE CASE: Statistical Analysis        │
│                                                                                 │
│  THE WORKBENCH USES BOTH:                                                       │
│  • Scikit-Learn for Grid Search, CV, Tree models                                │
│  • Statsmodels for Feature Selection (P-Value calculation)                      │
│                                                                                 │
└─────────────────────────────────────────────────────────────────────────────────┘
```

---

## 🛠️ Tech Stack

<div align="center">

| Layer | Technology | Version | Purpose |
|:-----:|:----------:|:-------:|:--------|
| **🖥️ Frontend** | Streamlit | 1.28+ | Interactive web interface |
| **🐍 Runtime** | Python | 3.10+ | Core programming language |
| **📊 Data** | Pandas | 2.0+ | DataFrames & manipulation |
| **🔢 Numerical** | NumPy | 1.24+ | Array operations |
| **🤖 ML Engine** | Scikit-Learn | 1.3+ | Models, CV, Grid Search |
| **📈 Statistics** | **Statsmodels** | **0.14+** | **OLS, P-Values (NEW)** |
| **📉 Visualization** | Plotly | 5.18+ | Interactive charts |

</div>

### Dependency Graph

```
┌─────────────────────────────────────────────────────────────────────────────────┐
│                          TECHNOLOGY INTEGRATION                                 │
├─────────────────────────────────────────────────────────────────────────────────┤
│                                                                                 │
│                              ┌──────────────┐                                   │
│                              │  STREAMLIT   │                                   │
│                              │   (UI/UX)    │                                   │
│                              └──────┬───────┘                                   │
│                                     │                                           │
│                    ┌────────────────┼────────────────┐                          │
│                    │                │                │                          │
│                    ▼                ▼                ▼                          │
│            ┌─────────────┐  ┌─────────────┐  ┌─────────────┐                    │
│            │SCIKIT-LEARN │  │ STATSMODELS │  │   PLOTLY    │                    │
│            │             │  │    (NEW)    │  │             │                    │
│            │ • Models    │  │ • OLS       │  │ • Charts    │                    │
│            │ • CV        │  │ • P-Values  │  │ • Heatmaps  │                    │
│            │ • GridSearch│  │ • Inference │  │ • Interact  │                    │
│            └──────┬──────┘  └──────┬──────┘  └─────────────┘                    │
│                   │                │                                            │
│                   └────────┬───────┘                                            │
│                            │                                                    │
│                            ▼                                                    │
│                    ┌─────────────┐                                              │
│                    │   PANDAS    │                                              │
│                    │   NUMPY     │                                              │
│                    │  (Data I/O) │                                              │
│                    └─────────────┘                                              │
│                                                                                 │
└─────────────────────────────────────────────────────────────────────────────────┘
```

---

## 📥 Installation

### Prerequisites

- Python 3.8 or higher
- pip package manager
- Git (for cloning)

### Step 1: Clone the Repository

```bash
git clone https://github.com/yourusername/ml-workbench.git
cd ml-workbench
```

### Step 2: Create Virtual Environment

```bash
# Create environment
python -m venv venv

# Activate (Linux/macOS)
source venv/bin/activate

# Activate (Windows)
.\venv\Scripts\activate
```

### Step 3: Install Dependencies

```bash
pip install --upgrade pip
pip install -r requirements.txt
```

### requirements.txt (v3.4)

```
streamlit>=1.28.0
scikit-learn>=1.3.0
pandas>=2.0.0
numpy>=1.24.0
plotly>=5.18.0
matplotlib>=3.7.0
statsmodels>=0.14.0    # NEW: Required for Feature Selection Lab
```

### Step 4: Verify Installation

```bash
python -c "
import streamlit
import sklearn
import statsmodels
import plotly

print('✅ All dependencies installed!')
print(f'   Statsmodels: {statsmodels.__version__}')  # Verify new dependency
"
```

### Step 5: Launch the Application

```bash
streamlit run Home.py
```

Navigate to `http://localhost:8501` in your browser.

---

## 📖 User Guide

### Using the Feature Selection Lab

1. **Navigate** to **🗑️ Feature Selection Lab** in the sidebar
2. **Observe** the synthetic dataset with mixed features
3. **Click** "Run Backward Elimination"
4. **Watch** the Elimination Log update round-by-round
5. **Review** the Final Significance Check graph

### Interpreting Results

| Result | Meaning | Insight |
|--------|---------|---------|
| **Feature Dropped** | P-Value > 0.05 | No statistical relationship with target |
| **Feature Kept** | P-Value < 0.05 | Significant predictor |
| **Tiny P-Value Bar** | P-Value << 0.001 | Extremely strong predictor |
| **Multiple Survivors** | Several P < 0.05 | Multi-factor model appropriate |

---

## ⚠️ Disclaimer

<div align="center">

---

**📚 EDUCATIONAL USE ONLY**

---

</div>

This application is developed **exclusively for educational and demonstration purposes**.

- **Not for Production**: Results should not guide real-world decisions
- **Synthetic Data Only**: All datasets are algorithmically generated
- **No Warranty**: Software provided "as is"
- **Learning Tool**: Designed to build intuition, not replace professional analysis

---

## 👨‍💻 Author

<div align="center">

### **Waqar Salim**

*Master's Student & IT Professional*

---

[![LinkedIn](https://img.shields.io/badge/LinkedIn-Connect-0A66C2?style=for-the-badge&logo=linkedin)](https://linkedin.com/in/yourprofile)
[![GitHub](https://img.shields.io/badge/GitHub-Follow-181717?style=for-the-badge&logo=github)](https://github.com/yourusername)

---

### Version History

| Version | Codename | Modules | Key Addition |
|---------|----------|:-------:|--------------|
| v3.1 | Visual Basics | 4 | Core algorithms |
| v3.2 | Reliability Engineering | 5 | Cross-Validation |
| v3.3 | Automation Update | 6 | Grid Search |
| **v3.4** | **Feature Engineering** | **7** | **Backward Elimination** |

---

**Built with 🧠 statistics, 🗑️ garbage collection, and ☕ persistence**

*The Machine Learning Workbench v3.4 — Separating Signal from Noise*

---

```
╔═══════════════════════════════════════════════════════════════════════════════╗
║                                                                               ║
║   "In God we trust. All others must bring data... and significant P-Values." ║
║                                                                               ║
╚═══════════════════════════════════════════════════════════════════════════════╝
```

![Footer](https://capsule-render.vercel.app/api?type=waving&color=gradient&customColorList=12,9,5&height=100&section=footer)

</div>
