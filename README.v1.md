<p align="center">
  <img src="https://img.shields.io/badge/Python-3.8+-3776AB?style=for-the-badge&logo=python&logoColor=white" alt="Python"/>
  <img src="https://img.shields.io/badge/Streamlit-FF4B4B?style=for-the-badge&logo=streamlit&logoColor=white" alt="Streamlit"/>
  <img src="https://img.shields.io/badge/scikit--learn-F7931E?style=for-the-badge&logo=scikit-learn&logoColor=white" alt="Scikit-learn"/>
  <img src="https://img.shields.io/badge/License-MIT-green?style=for-the-badge" alt="License"/>
</p>

<h1 align="center">🏡 AI Real Estate Estimator</h1>
<h3 align="center">Interactive Linear Regression Dashboard</h3>

<p align="center">
  <em>Transform raw data science concepts into actionable business intelligence</em>
</p>

---

[![GitHub](https://img.shields.io/badge/GitHub-WSalim2024-181717?style=flat-square&logo=github)](https://github.com/WSalim2024)
[![LinkedIn](https://img.shields.io/badge/LinkedIn-Connect-0A66C2?style=flat-square&logo=linkedin)](https://linkedin.com)

---

## 📋 Table of Contents

- [Overview](#-overview)
- [Key Features](#-key-features)
- [How It Works](#-how-it-works)
- [Technical Architecture](#-technical-architecture)
- [Tech Stack](#-tech-stack)
- [Installation](#-installation)
- [Usage Guide](#-usage-guide)
- [Limitations](#-limitations)
- [Disclaimer](#-disclaimer)
- [Author](#-author)

---

## 🎯 Overview

The **AI Real Estate Estimator** is an interactive machine learning dashboard designed to demonstrate the fundamental principles of predictive modeling. By leveraging Linear Regression, this tool analyzes the relationship between property square footage and market price, delivering real-time visualizations and price estimations based on user-defined parameters.

This project serves as a bridge between raw data science concepts and actionable business intelligence. It transforms a static Python script into a user-facing web application, demonstrating how Agentic AI tools can provide transparency into algorithmic decision-making.

---

## ✨ Key Features

| Feature | Description |
|:--------|:------------|
| **🎲 Dynamic Data Generation** | Control dataset size and market volatility to simulate different economic environments |
| **⚡ Real-Time Training** | Model retrains instantly as data parameters change |
| **📊 Interactive Visualization** | Powered by Plotly—zoom, pan, and hover over data points to inspect individual sales |
| **📈 Live Metrics** | Instant calculation of Model Slope, Mean Squared Error (MSE), and R² accuracy scores |
| **🔮 Prediction Interface** | Input specific square footage and receive immediate price estimates |

---

## ⚙️ How It Works

The application generates a synthetic housing market dataset, trains a supervised machine learning model on that data, and presents the findings in an interactive dashboard. It predicts house prices based solely on size, visually plotting the "Line of Best Fit" that minimizes prediction error.

### Workflow Pipeline

```
┌─────────────────┐     ┌─────────────────┐     ┌─────────────────┐     ┌─────────────────┐
│   📥 INGEST     │ ──▶ │   ✂️ SPLIT      │ ──▶ │   🎯 FIT        │ ──▶ │   🔮 PREDICT    │
│                 │     │                 │     │                 │     │                 │
│ Generate data   │     │ Train: 80%      │     │ Calculate       │     │ Apply formula   │
│ based on user   │     │ Test:  20%      │     │ optimal line    │     │ to new inputs   │
│ parameters      │     │                 │     │                 │     │                 │
└─────────────────┘     └─────────────────┘     └─────────────────┘     └─────────────────┘
```

### Core Logic: Simple Linear Regression

The model uses **Ordinary Least Squares (OLS) Linear Regression** to find the linear equation that best predicts the target value.

**Equation:**

$$y = mx + b$$

| Symbol | Meaning |
|:------:|:--------|
| $y$ | Predicted Price |
| $x$ | Square Footage |
| $m$ | Slope (Price per sq/ft) |
| $b$ | Intercept (Base price) |

**Optimization Strategy:** Minimizing the Mean Squared Error (MSE)

---

## 🏗️ Technical Architecture

The application follows a monolithic script architecture optimized for data prototyping:

```
┌────────────────────────────────────────────────────────┐
│                    🖥️ FRONTEND                         │
│                    Streamlit UI                        │
├────────────────────────────────────────────────────────┤
│                 📊 VISUALIZATION                       │
│                  Plotly Express                        │
├────────────────────────────────────────────────────────┤
│                  🧠 BACKEND LOGIC                      │
│            Python + Scikit-Learn                       │
├────────────────────────────────────────────────────────┤
│                 📦 DATA PROCESSING                     │
│                 NumPy + Pandas                         │
└────────────────────────────────────────────────────────┘
```

---

## 🛠️ Tech Stack

| Component | Technology | Purpose |
|:----------|:-----------|:--------|
| **Language** | Python 3.x | Core application logic |
| **ML Library** | Scikit-Learn | Model training and metrics |
| **Data Manipulation** | Pandas | DataFrame management |
| **Math Operations** | NumPy | Array handling and generation |
| **UI Framework** | Streamlit | Interactive dashboard interface |
| **Plotting** | Plotly | Interactive visualizations |

---

## 📦 Installation

### Requirements

- **OS:** Windows, macOS, or Linux
- **Python:** Version 3.8 or higher
- **Browser:** Chrome, Firefox, or Edge

### Setup Instructions

**1. Clone the Repository**

```bash
git clone https://github.com/WSalim2024/linear-regression-dashboard.git
```

**2. Navigate to the Project Directory**

```bash
cd linear-regression-dashboard
```

**3. Create a Virtual Environment** *(Recommended)*

```bash
python -m venv venv

# Activate on macOS/Linux:
source venv/bin/activate

# Activate on Windows:
venv\Scripts\activate
```

**4. Install Dependencies**

```bash
pip install -r requirements.txt
```

**5. Launch the Application**

```bash
streamlit run app.py
```

The dashboard will automatically open in your default browser at `http://localhost:8501`

---

## 📖 Usage Guide

### Step-by-Step Instructions

1. **Adjust Parameters**  
   Use the sidebar sliders to control the **Number of Houses** and **Market Volatility (Noise)**.

2. **Analyze Metrics**  
   Monitor the top three key performance indicators:
   - **Slope** — Price increase per square foot
   - **R² Score** — Model accuracy (closer to 1.0 is better)
   - **MSE** — Average prediction error

3. **Explore the Visualization**  
   - 🔵 **Blue dots** — Actual data points
   - 🔴 **Red line** — Model's prediction line
   - Hover over elements for detailed information

4. **Make Predictions**  
   Enter a square footage value (e.g., `2500`) in the prediction panel and click **"Predict Price"** to see the AI's estimation.

---

## ⚠️ Limitations

| Limitation | Description |
|:-----------|:------------|
| **Single Feature** | The model considers only square footage. Real estate prices are influenced by location, age, condition, and many other factors. |
| **Linearity Assumption** | The model assumes a straight-line relationship and cannot capture complex, non-linear market trends. |
| **Synthetic Data** | The current version uses generated data rather than real historical records. |

---

## 📜 Disclaimer

> **⚠️ Educational Use Only**
>
> This tool is designed for educational and demonstrative purposes only. It should **not** be used for actual real estate financial planning or investment decisions. The "Market Volatility" simulation is a mathematical approximation and does not reflect real-world economic factors.

---

## 👨‍💻 Author

<p align="center">
  <a href="https://github.com/WSalim2024">
    <img src="https://img.shields.io/badge/GitHub-WSalim2024-181717?style=for-the-badge&logo=github" alt="GitHub"/>
  </a>
  <a href="https://linkedin.com">
    <img src="https://img.shields.io/badge/LinkedIn-Connect-0A66C2?style=for-the-badge&logo=linkedin" alt="LinkedIn"/>
  </a>
</p>

---

<p align="center">
  <em>⭐ If you find this project useful, please consider giving it a star!</em>
</p>

<p align="center">
  Made with ❤️ and Python
</p>
