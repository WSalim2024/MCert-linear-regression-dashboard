<div align="center">

# 🧠 The Machine Learning Workbench

### **Version 3.6 — The Complete Selection Suite**

*The Definitive ML Educational Platform: Three Philosophies of Feature Selection*

---

![Python](https://img.shields.io/badge/Python-3.10+-3776AB?style=for-the-badge&logo=python&logoColor=white)
![Streamlit](https://img.shields.io/badge/Streamlit-1.28+-FF4B4B?style=for-the-badge&logo=streamlit&logoColor=white)
![Scikit-Learn](https://img.shields.io/badge/Scikit--Learn-1.3+-F7931E?style=for-the-badge&logo=scikit-learn&logoColor=white)
![Statsmodels](https://img.shields.io/badge/Statsmodels-0.14+-4051B5?style=for-the-badge&logo=python&logoColor=white)
![Plotly](https://img.shields.io/badge/Plotly-5.18+-3F4F75?style=for-the-badge&logo=plotly&logoColor=white)
![Version](https://img.shields.io/badge/Version-3.6-blueviolet?style=for-the-badge)
![Modules](https://img.shields.io/badge/Modules-7-orange?style=for-the-badge)
![Selection Methods](https://img.shields.io/badge/Selection_Methods-3-success?style=for-the-badge)
![License](https://img.shields.io/badge/License-MIT-green?style=for-the-badge)

<br>

[**Features**](#-key-features) · [**Modules**](#-module-overview) · [**Installation**](#-installation) · [**User Guide**](#-user-guide)

<br>

```
╔═══════════════════════════════════════════════════════════════════════════════╗
║                                                                               ║
║   "Three paths to feature selection: Statistical elimination, performance    ║
║    recruitment, or mathematical shrinkage. All roads lead to simplicity."    ║
║                                                                               ║
╚═══════════════════════════════════════════════════════════════════════════════╝
```

</div>

---

## 📋 Table of Contents

- [Overview](#-overview)
- [What's New in v3.6](#-whats-new-in-v36)
- [Key Features](#-key-features)
- [Module Overview](#-module-overview)
- [Module G: Feature Selection Suite (Complete)](#-module-g-feature-selection-suite-complete)
- [Tech Stack](#-tech-stack)
- [Installation](#-installation)
- [User Guide](#-user-guide)
- [Disclaimer](#-disclaimer)
- [Author](#-author)

---

## 🚀 Overview

**The Machine Learning Workbench v3.6** delivers the **complete ML educational platform** — a comprehensive learning environment spanning from fundamental algorithms to advanced feature engineering with three distinct selection methodologies.

This release completes the Feature Selection Suite by adding **LASSO (L1 Regularization)**, offering users a third powerful approach to identifying the features that truly matter.

<div align="center">

```
┌─────────────────────────────────────────────────────────────────────────────────┐
│                   THREE PHILOSOPHIES OF FEATURE SELECTION                       │
├─────────────────────────────────────────────────────────────────────────────────┤
│                                                                                 │
│    🔙 BACKWARD              🔜 FORWARD               🎯 LASSO                   │
│    ELIMINATION              SELECTION               REGULARIZATION              │
│    ─────────────            ─────────────           ─────────────               │
│                                                                                 │
│    "The Garbage             "The Talent             "The Shrink                 │
│     Collector"               Scout"                  Ray"                       │
│                                                                                 │
│    Start: ALL               Start: ZERO             Start: ALL                  │
│    Action: REMOVE           Action: ADD             Action: SHRINK              │
│    Metric: P-Value          Metric: R²              Metric: Coefficient         │
│    Tool: Statsmodels        Tool: Sklearn           Tool: Sklearn.Lasso         │
│                                                                                 │
│    ┌───────────┐            ┌───────────┐           ┌───────────┐               │
│    │██ ██ ██ ██│            │           │           │██ ██ ██ ██│               │
│    │██ ██ ██   │            │        ██ │           │██ ▪▪ ▪▪ ██│               │
│    │██ ██      │ ───►       │     ██ ██ │ ───►      │██    ·  ██│ ───►          │
│    │██         │            │  ██ ██ ██ │           │██       ██│               │
│    └───────────┘            └───────────┘           └───────────┘               │
│     Subtractive              Additive               Shrinkage                   │
│                                                     (to zero)                   │
│                                                                                 │
│    SAME DESTINATION: The optimal, minimal feature set                           │
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
| 🎯 **Feature Selection** | Three methods: Backward, Forward, **LASSO** | G |

---

## ✨ What's New in v3.6

### 🎯 LASSO Regularization — "The Shrink Ray"

The Feature Selection Suite is now **complete** with three distinct methodologies:

<div align="center">

| Tab | Method | Metaphor | Mechanism | Library |
|:---:|:-------|:---------|:----------|:--------|
| 🔙 **Tab 1** | Backward Elimination | The Garbage Collector | Remove by P-Value | Statsmodels |
| 🔜 **Tab 2** | Forward Selection | The Talent Scout | Add by R² gain | Scikit-Learn |
| 🎯 **Tab 3** | **LASSO (L1)** | **The Shrink Ray** | **Shrink to Zero** | **Scikit-Learn** |

</div>

### What Makes LASSO Different?

```
┌─────────────────────────────────────────────────────────────────────────────────┐
│                         LASSO: THE MATHEMATICAL APPROACH                        │
├─────────────────────────────────────────────────────────────────────────────────┤
│                                                                                 │
│  BACKWARD & FORWARD:                    LASSO:                                  │
│  Binary decisions                       Continuous shrinkage                    │
│  ─────────────────────                  ───────────────────────                 │
│                                                                                 │
│  Feature is either:                     Feature coefficients:                   │
│    ✅ IN the model                        📊 Gradually shrink                   │
│    ❌ OUT of the model                    📉 Until they hit ZERO                │
│                                           🎯 Then effectively removed           │
│                                                                                 │
│  ┌─────────────────────────────────────────────────────────────────────────┐    │
│  │                                                                         │    │
│  │   THE SHRINKAGE EFFECT (as Alpha increases):                           │    │
│  │                                                                         │    │
│  │   Alpha = 0.01        Alpha = 0.10        Alpha = 1.00                  │    │
│  │   ────────────        ────────────        ────────────                  │    │
│  │                                                                         │    │
│  │   Study_Hours: 8.72   Study_Hours: 8.45   Study_Hours: 7.89            │    │
│  │   Shoe_Size:   0.23   Shoe_Size:   0.08   Shoe_Size:   0.00 ← GONE!    │    │
│  │   Jersey_Num: -0.12   Jersey_Num:  0.00   Jersey_Num:  0.00 ← GONE!    │    │
│  │   Fav_Color:   0.15   Fav_Color:   0.02   Fav_Color:   0.00 ← GONE!    │    │
│  │                                                                         │    │
│  │   Noise coefficients PHYSICALLY SHRINK TO ZERO                          │    │
│  │                                                                         │    │
│  └─────────────────────────────────────────────────────────────────────────┘    │
│                                                                                 │
└─────────────────────────────────────────────────────────────────────────────────┘
```

### The Alpha Slider

LASSO introduces an interactive **Alpha (α) slider** that controls regularization strength:

| Alpha Value | Effect | Interpretation |
|-------------|--------|----------------|
| **α → 0** | Minimal penalty | Behaves like standard regression |
| **α = 0.1** | Moderate penalty | Weak features start shrinking |
| **α = 1.0** | Strong penalty | Only strongest features survive |
| **α → ∞** | Maximum penalty | All coefficients → 0 |

---

## 🎯 Key Features

<table>
<tr>
<td width="50%">

### 📈 Core Algorithms
- **Linear Regression** — Continuous prediction
- **Logistic Regression** — Binary classification
- **Decision Trees** — Non-linear boundaries
- **Real-time Training** — Instant visual feedback

</td>
<td width="50%">

### 🔬 Validation & Reliability
- **K-Fold Cross-Validation** — Multi-split testing
- **Variance Analysis** — Stability metrics
- **Per-Fold Breakdown** — Granular insights

</td>
</tr>
<tr>
<td width="50%">

### 🔍 Automation & Tuning
- **Grid Search** — Exhaustive parameter sweep
- **Heatmap Visualization** — Parameter landscapes
- **Best Config Discovery** — Automatic optimization

</td>
<td width="50%">

### 🎯 Feature Selection Suite (COMPLETE)
- 🔙 **Backward Elimination** — P-Value pruning
- 🔜 **Forward Selection** — R² recruitment
- 🎯 **LASSO (L1)** — Coefficient shrinkage
- **Interactive Alpha Control** — Real-time regularization

</td>
</tr>
</table>

---

## 📦 Module Overview

The Workbench contains **7 distinct learning modules** with a now-complete Feature Selection Suite:

<div align="center">

| Module | Name | Icon | Focus Area | Key Concept |
|:------:|:-----|:----:|:-----------|:------------|
| **A** | Linear Regression | 📈 | Continuous Prediction | OLS, Best-Fit Line |
| **B** | Logistic Regression | 📊 | Binary Classification | Sigmoid, Probability |
| **C** | Decision Tree | 🌳 | Non-linear Boundaries | Gini Impurity, Splits |
| **D** | Model Showdown | ⚔️ | Algorithm Comparison | Linear vs Non-linear |
| **E** | Cross-Validation Lab | 🔬 | Reliability Testing | K-Fold, Variance |
| **F** | Grid Search Lab | 🔍 | Hyperparameter Tuning | Exhaustive Search |
| **G** | **Feature Selection Suite** | 🎯 | **Feature Engineering** | **3 Methods Complete** |

</div>

### Module G: Three Selection Strategies

```
┌─────────────────────────────────────────────────────────────────────────────────┐
│                    MODULE G: FEATURE SELECTION SUITE                            │
├─────────────────────────────────────────────────────────────────────────────────┤
│                                                                                 │
│   ┌───────────────────┬───────────────────┬───────────────────┐                 │
│   │ 🔙 Tab 1          │ 🔜 Tab 2          │ 🎯 Tab 3          │                 │
│   │ BACKWARD          │ FORWARD           │ LASSO             │                 │
│   │ ELIMINATION       │ SELECTION         │ (L1 Regularization)│                │
│   ├───────────────────┼───────────────────┼───────────────────┤                 │
│   │                   │                   │                   │                 │
│   │ P-Value Based     │ R² Based          │ Penalty Based     │                 │
│   │ Statsmodels       │ Scikit-Learn      │ Scikit-Learn      │                 │
│   │ Discrete removal  │ Discrete addition │ Continuous shrink │                 │
│   │                   │                   │                   │                 │
│   └───────────────────┴───────────────────┴───────────────────┘                 │
│                                                                                 │
└─────────────────────────────────────────────────────────────────────────────────┘
```

---

## 🎯 Module G: Feature Selection Suite (Complete)

<div align="center">

### **Three Tabs. Three Philosophies. One Goal.**

*The complete toolkit for identifying features that matter*

</div>

---

### 🔙 Tab 1: Backward Elimination — "The Garbage Collector"

**Philosophy:** Start with everything, remove the statistically insignificant.

| Aspect | Detail |
|--------|--------|
| **Starting Point** | All features included |
| **Metric** | P-Value (statistical significance) |
| **Threshold** | P > 0.05 → Remove |
| **Library** | `statsmodels.OLS` |
| **Output** | Elimination Log + P-Value Chart |

```python
import statsmodels.api as sm

# Iteratively remove features with P > 0.05
model = sm.OLS(y, sm.add_constant(X)).fit()
p_values = model.pvalues
```

---

### 🔜 Tab 2: Forward Selection — "The Talent Scout"

**Philosophy:** Start with nothing, recruit only features that improve performance.

| Aspect | Detail |
|--------|--------|
| **Starting Point** | Zero features (empty model) |
| **Metric** | R² (variance explained) |
| **Criterion** | Add feature with max R² improvement |
| **Library** | `sklearn.linear_model.LinearRegression` |
| **Output** | R² Growth Chart |

```python
from sklearn.linear_model import LinearRegression
from sklearn.metrics import r2_score

# Iteratively add features that maximize R²
model = LinearRegression().fit(X[selected], y)
r2 = r2_score(y, model.predict(X[selected]))
```

---

### 🎯 Tab 3: LASSO (L1 Regularization) — "The Shrink Ray" (NEW!)

**Philosophy:** Let mathematics naturally shrink useless coefficients to exactly zero.

<div align="center">

```
┌─────────────────────────────────────────────────────────────────────────────────┐
│                        🎯 LASSO REGULARIZATION                                  │
│                        "The Shrink Ray"                                         │
├─────────────────────────────────────────────────────────────────────────────────┤
│                                                                                 │
│  THE CONCEPT:                                                                   │
│  ════════════                                                                   │
│  LASSO adds a PENALTY term to the loss function that punishes large            │
│  coefficients. Noise features, which have weak relationships with the          │
│  target, cannot "afford" the penalty and shrink to EXACTLY ZERO.               │
│                                                                                 │
│  LOSS FUNCTION:                                                                 │
│  ┌─────────────────────────────────────────────────────────────────────────┐    │
│  │                                                                         │    │
│  │   Standard OLS:   minimize  Σ(yᵢ - ŷᵢ)²                                 │    │
│  │                                                                         │    │
│  │   LASSO (L1):     minimize  Σ(yᵢ - ŷᵢ)²  +  α × Σ|βⱼ|                   │    │
│  │                             ─────────────    ──────────                 │    │
│  │                              Prediction       L1 Penalty                │    │
│  │                                Error          (shrinkage)               │    │
│  │                                                                         │    │
│  └─────────────────────────────────────────────────────────────────────────┘    │
│                                                                                 │
│  THE ALPHA (α) SLIDER:                                                          │
│  ═════════════════════                                                          │
│                                                                                 │
│   ┌─────────────────────────────────────────────────────────────────────┐       │
│   │  Alpha:  [0.01]────────────────●───────────────────────────[10.0]  │       │
│   │                            ▲                                        │       │
│   │                       Current: 0.50                                 │       │
│   └─────────────────────────────────────────────────────────────────────┘       │
│                                                                                 │
│   α → 0:    Minimal penalty → All features kept (like OLS)                      │
│   α ↑:      Increasing penalty → Weak features start shrinking                  │
│   α → ∞:    Maximum penalty → All coefficients → 0                              │
│                                                                                 │
└─────────────────────────────────────────────────────────────────────────────────┘
```

</div>

#### How LASSO Shrinks Coefficients

As you increase the Alpha slider, watch what happens to the coefficients:

```
┌─────────────────────────────────────────────────────────────────────────────────┐
│                    COEFFICIENT EVOLUTION AS ALPHA INCREASES                     │
├─────────────────────────────────────────────────────────────────────────────────┤
│                                                                                 │
│  Feature          │ α=0.01  │ α=0.05  │ α=0.10  │ α=0.50  │ α=1.00  │ Status   │
│  ─────────────────┼─────────┼─────────┼─────────┼─────────┼─────────┼──────────│
│  Study_Hours      │  8.723  │  8.698  │  8.651  │  8.234  │  7.891  │ ✅ KEPT  │
│  Shoe_Size        │  0.234  │  0.156  │  0.087  │  0.012  │  0.000  │ ❌ GONE  │
│  Jersey_Number    │ -0.123  │ -0.067  │ -0.021  │  0.000  │  0.000  │ ❌ GONE  │
│  Favorite_Color   │  0.156  │  0.098  │  0.034  │  0.000  │  0.000  │ ❌ GONE  │
│                                                                                 │
│  ════════════════════════════════════════════════════════════════════════════   │
│                                                                                 │
│  INTERPRETATION:                                                                │
│  • Study_Hours maintains a strong coefficient → REAL SIGNAL                     │
│  • Noise features progressively shrink → eventually hit EXACTLY 0.000           │
│  • Zero coefficient = Feature mathematically removed from equation              │
│                                                                                 │
└─────────────────────────────────────────────────────────────────────────────────┘
```

#### The Coefficient Bar Chart

The LASSO tab features a powerful **Coefficient Bar Chart** visualization:

```
┌─────────────────────────────────────────────────────────────────────────────────┐
│                      📊 COEFFICIENT BAR CHART                                   │
│                      (Alpha = 0.50)                                             │
├─────────────────────────────────────────────────────────────────────────────────┤
│                                                                                 │
│  Coefficient                                                                    │
│  Value                                                                          │
│    │                                                                            │
│    │                                                                            │
│  8 ┤   ┌───────┐                                                                │
│    │   │███████│                                                                │
│    │   │███████│                                                                │
│  6 ┤   │███████│                                                                │
│    │   │███████│ ← GREEN: Strong positive coefficient                          │
│    │   │███████│          (Study_Hours = 8.23)                                  │
│  4 ┤   │███████│                                                                │
│    │   │███████│                                                                │
│    │   │███████│                                                                │
│  2 ┤   │███████│                                                                │
│    │   │███████│                                                                │
│    │   │███████│                                                                │
│  0 ┼───┴───────┴────┬────────────┬────────────┬────────────┬────────────────    │
│    │                │            │            │            │                    │
│    │               ┌┴┐          ┌┴┐          ┌┴┐                                │
│    │               │▓│          │▓│          │▓│                                │
│    │               └─┘          └─┘          └─┘                                │
│    │                                                                            │
│    │             ← RED: Coefficient = 0.00 (ELIMINATED)                         │
│    │                                                                            │
│       Study      Shoe        Jersey      Favorite                               │
│       Hours      Size        Number       Color                                 │
│                                                                                 │
│  ═══════════════════════════════════════════════════════════════════════════    │
│                                                                                 │
│  LEGEND:                                                                        │
│  ┌──────────────────────────────────────────────────────────────────────────┐   │
│  │  🟩 GREEN BAR  = Active feature (coefficient ≠ 0)                        │   │
│  │  🟥 RED BAR    = Eliminated feature (coefficient = 0.00)                 │   │
│  │  BAR HEIGHT   = Magnitude of coefficient                                 │   │
│  └──────────────────────────────────────────────────────────────────────────┘   │
│                                                                                 │
└─────────────────────────────────────────────────────────────────────────────────┘
```

#### LASSO Implementation

```python
from sklearn.linear_model import Lasso

def lasso_selection(X, y, alpha=1.0):
    """
    Perform LASSO feature selection via L1 regularization.
    
    Parameters:
    -----------
    X : DataFrame
        Feature matrix
    y : Series
        Target variable
    alpha : float
        Regularization strength (higher = more shrinkage)
    
    Returns:
    --------
    dict : Feature coefficients (zeros indicate elimination)
    """
    # Fit LASSO model
    lasso = Lasso(alpha=alpha, random_state=42)
    lasso.fit(X, y)
    
    # Extract coefficients
    coefficients = dict(zip(X.columns, lasso.coef_))
    
    # Identify eliminated features (coefficient = 0)
    eliminated = [f for f, c in coefficients.items() if c == 0]
    selected = [f for f, c in coefficients.items() if c != 0]
    
    return {
        'coefficients': coefficients,
        'selected': selected,
        'eliminated': eliminated
    }

# Example usage
result = lasso_selection(X, y, alpha=0.5)
print(f"Selected: {result['selected']}")
print(f"Eliminated: {result['eliminated']}")
```

---

### 🔄 Three Methods Compared

<div align="center">

```
┌─────────────────────────────────────────────────────────────────────────────────┐
│                    COMPLETE COMPARISON: ALL THREE METHODS                       │
├─────────────────────────────┬─────────────────────────┬─────────────────────────┤
│                             │                         │                         │
│  🔙 BACKWARD ELIMINATION    │  🔜 FORWARD SELECTION   │  🎯 LASSO (L1)          │
│                             │                         │                         │
├─────────────────────────────┼─────────────────────────┼─────────────────────────┤
│                             │                         │                         │
│  Metaphor:                  │  Metaphor:              │  Metaphor:              │
│  "The Garbage Collector"    │  "The Talent Scout"     │  "The Shrink Ray"       │
│                             │                         │                         │
├─────────────────────────────┼─────────────────────────┼─────────────────────────┤
│                             │                         │                         │
│  Starting Point:            │  Starting Point:        │  Starting Point:        │
│  ALL features               │  ZERO features          │  ALL features           │
│                             │                         │                         │
├─────────────────────────────┼─────────────────────────┼─────────────────────────┤
│                             │                         │                         │
│  Action:                    │  Action:                │  Action:                │
│  REMOVE worst               │  ADD best               │  SHRINK to zero         │
│                             │                         │                         │
├─────────────────────────────┼─────────────────────────┼─────────────────────────┤
│                             │                         │                         │
│  Selection Type:            │  Selection Type:        │  Selection Type:        │
│  Discrete (in/out)          │  Discrete (in/out)      │  Continuous (shrinkage) │
│                             │                         │                         │
├─────────────────────────────┼─────────────────────────┼─────────────────────────┤
│                             │                         │                         │
│  Metric:                    │  Metric:                │  Metric:                │
│  P-Value                    │  R² Score               │  Coefficient magnitude  │
│                             │                         │                         │
├─────────────────────────────┼─────────────────────────┼─────────────────────────┤
│                             │                         │                         │
│  Threshold:                 │  Threshold:             │  Control:               │
│  P > 0.05                   │  ΔR² < threshold        │  Alpha (α) slider       │
│                             │                         │                         │
├─────────────────────────────┼─────────────────────────┼─────────────────────────┤
│                             │                         │                         │
│  Library:                   │  Library:               │  Library:               │
│  statsmodels.OLS            │  sklearn.LinearReg      │  sklearn.Lasso          │
│                             │                         │                         │
├─────────────────────────────┼─────────────────────────┼─────────────────────────┤
│                             │                         │                         │
│  Output:                    │  Output:                │  Output:                │
│  • Elimination Log          │  • R² Growth Chart      │  • Coefficient Bar Chart│
│  • P-Value Chart            │  • Feature Rankings     │  • Zero = Eliminated    │
│                             │                         │  • Red bars = removed   │
│                             │                         │                         │
├─────────────────────────────┼─────────────────────────┼─────────────────────────┤
│                             │                         │                         │
│  Best When:                 │  Best When:             │  Best When:             │
│  • Need inference           │  • Need interpretable   │  • Many features        │
│  • Small feature sets       │    performance gains    │  • Want automatic       │
│  • Statistical rigor        │  • Most features        │    selection            │
│    required                 │    likely useless       │  • Continuous control   │
│                             │                         │    desired              │
│                             │                         │                         │
└─────────────────────────────┴─────────────────────────┴─────────────────────────┘
```

</div>

### When to Use Each Method

| Scenario | Recommended Method | Reason |
|----------|-------------------|--------|
| Need statistical significance | 🔙 Backward | P-Values provide inference |
| Building from scratch | 🔜 Forward | See incremental gains |
| Many features, want automation | 🎯 LASSO | Handles high dimensionality |
| Want to explore regularization | 🎯 LASSO | Interactive Alpha control |
| Need to explain removals | 🔙 Backward | Clear statistical justification |
| Want performance-focused selection | 🔜 Forward | R² directly measures improvement |

---

## 🛠️ Tech Stack

<div align="center">

| Layer | Technology | Version | Purpose |
|:-----:|:----------:|:-------:|:--------|
| **🖥️ Frontend** | Streamlit | 1.28+ | Interactive web interface |
| **🐍 Runtime** | Python | 3.10+ | Core programming language |
| **📊 Data** | Pandas | 2.0+ | DataFrames & manipulation |
| **🔢 Numerical** | NumPy | 1.24+ | Array operations |
| **🤖 ML Engine** | Scikit-Learn | 1.3+ | Models, CV, Grid Search, **Lasso** |
| **📈 Statistics** | Statsmodels | 0.14+ | OLS, P-Values |
| **📉 Visualization** | Plotly | 5.18+ | Interactive charts |

</div>

### Triple-Library Feature Selection

```
┌─────────────────────────────────────────────────────────────────────────────────┐
│                    FEATURE SELECTION: COMPLETE TOOLKIT                          │
├─────────────────────────────────────────────────────────────────────────────────┤
│                                                                                 │
│                         ┌─────────────────────────┐                             │
│                         │   FEATURE SELECTION     │                             │
│                         │        SUITE            │                             │
│                         └───────────┬─────────────┘                             │
│                                     │                                           │
│              ┌──────────────────────┼──────────────────────┐                    │
│              │                      │                      │                    │
│              ▼                      ▼                      ▼                    │
│    ┌─────────────────┐    ┌─────────────────┐    ┌─────────────────┐            │
│    │  🔙 BACKWARD    │    │  🔜 FORWARD     │    │  🎯 LASSO       │            │
│    │  ELIMINATION    │    │  SELECTION      │    │  (L1)           │            │
│    └────────┬────────┘    └────────┬────────┘    └────────┬────────┘            │
│             │                      │                      │                     │
│             ▼                      ▼                      ▼                     │
│    ┌─────────────────┐    ┌─────────────────┐    ┌─────────────────┐            │
│    │  STATSMODELS    │    │  SCIKIT-LEARN   │    │  SCIKIT-LEARN   │            │
│    │                 │    │                 │    │                 │            │
│    │  sm.OLS()       │    │  LinearReg()    │    │  Lasso()        │            │
│    │  .pvalues       │    │  r2_score()     │    │  .coef_         │            │
│    └─────────────────┘    └─────────────────┘    └─────────────────┘            │
│                                                                                 │
│    ═══════════════════════════════════════════════════════════════════════      │
│                                                                                 │
│    THREE LIBRARIES, THREE APPROACHES, ONE GOAL:                                 │
│    Identify the minimal set of features that explain the data.                  │
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

### requirements.txt (v3.6)

```
streamlit>=1.28.0
scikit-learn>=1.3.0       # LinearRegression, Lasso, CV, GridSearch
statsmodels>=0.14.0       # OLS with P-Values
pandas>=2.0.0
numpy>=1.24.0
plotly>=5.18.0
matplotlib>=3.7.0
```

### Step 4: Verify Installation

```bash
python -c "
import streamlit
import sklearn
from sklearn.linear_model import Lasso
import statsmodels
import plotly

print('✅ All dependencies installed!')
print(f'   Scikit-Learn: {sklearn.__version__}')
print(f'   - Lasso: Available ✓')
print(f'   Statsmodels: {statsmodels.__version__}')
"
```

### Step 5: Launch the Application

```bash
streamlit run Home.py
```

Navigate to `http://localhost:8501` in your browser.

---

## 📖 User Guide

### Using the Complete Feature Selection Suite

#### 🔙 Tab 1: Backward Elimination

1. Click **🔙 Backward Elimination** tab
2. Observe the synthetic dataset with mixed features
3. Click **"Run Backward Elimination"**
4. Watch the Elimination Log as features are removed
5. Review the P-Value chart for surviving features

#### 🔜 Tab 2: Forward Selection

1. Click **🔜 Forward Selection** tab
2. Click **"Run Forward Selection"**
3. Watch the R² Growth Chart build step-by-step
4. Identify steep jumps (real signals) vs flat lines (noise)

#### 🎯 Tab 3: LASSO (NEW!)

1. Click **🎯 LASSO** tab
2. **Adjust the Alpha slider** (start low, increase gradually)
3. **Watch the Coefficient Bar Chart update in real-time**
4. Observe noise features turn **RED** as they hit **0.00**
5. Note which features maintain their coefficients (real signals)

### Interpreting LASSO Results

| Visual Cue | Meaning |
|------------|---------|
| 🟩 **Green bar** | Active feature (coefficient ≠ 0) |
| 🟥 **Red bar** | Eliminated feature (coefficient = 0.00) |
| **Tall bar** | Strong influence on prediction |
| **Short bar** | Weak influence (may shrink to 0 at higher α) |

### Recommended Workflow

```
┌─────────────────────────────────────────────────────────────────────────────────┐
│                         RECOMMENDED WORKFLOW                                    │
├─────────────────────────────────────────────────────────────────────────────────┤
│                                                                                 │
│  1. START with LASSO (Tab 3)                                                    │
│     • Quick overview of feature importance                                      │
│     • Slide Alpha to see shrinkage behavior                                     │
│                                                                                 │
│  2. VALIDATE with BACKWARD (Tab 1)                                              │
│     • Get statistical significance (P-Values)                                   │
│     • Confirm LASSO eliminations are statistically justified                    │
│                                                                                 │
│  3. VERIFY with FORWARD (Tab 2)                                                 │
│     • See incremental R² contributions                                          │
│     • Confirm selected features actually improve model                          │
│                                                                                 │
│  4. COMPARE all three results                                                   │
│     • Agreement = High confidence in selection                                  │
│     • Disagreement = Investigate edge-case features                             │
│                                                                                 │
└─────────────────────────────────────────────────────────────────────────────────┘
```

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
| v3.4 | Feature Engineering | 7 | Backward Elimination |
| v3.5 | Selection Suite | 7 | + Forward Selection |
| **v3.6** | **Complete Suite** | **7** | **+ LASSO (L1)** |

---

**Built with 🔙 elimination, 🔜 selection, 🎯 regularization, and ☕ persistence**

*The Machine Learning Workbench v3.6 — Three Paths to Feature Enlightenment*

---

```
╔═══════════════════════════════════════════════════════════════════════════════╗
║                                                                               ║
║   "Remove the garbage. Recruit the talent. Shrink the noise.                  ║
║    Three philosophies, one truth: Simplicity is the ultimate sophistication." ║
║                                                                               ║
╚═══════════════════════════════════════════════════════════════════════════════╝
```

![Footer](https://capsule-render.vercel.app/api?type=waving&color=gradient&customColorList=12,9,5,2&height=100&section=footer)

</div>
