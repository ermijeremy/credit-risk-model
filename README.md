# 💳 Credit Risk Modeling – Week 5 Project

## 📌 Project Overview

In this project, we act as data scientists at a financial institution working to assess the **creditworthiness** of customers who **lack a direct "default" label**. The goal is to build an **interpretable, regulator-compliant model** that estimates credit risk using behavioral data, while aligning with standards such as the **Basel II Accord**.

We create a **proxy target**, conduct EDA, engineer features, train models, and explain them using interpretable techniques like **Weight of Evidence (WoE)** and **SHAP values**.

---

## 🎯 Project Objectives

- Understand the **business and regulatory context** of credit scoring.
- Design a **proxy variable** to represent default risk.
- Conduct **exploratory data analysis** (EDA) to identify meaningful patterns.
- Engineer features including **RFM scores**, WoE bins, and BIV analysis.
- Build **interpretable models** (Logistic Regression with WoE).
- Benchmark with **complex models** (e.g., XGBoost) and use **SHAP** for explainability.
- Provide actionable **recommendations** based on risk segmentation.

---

## 🧩 Tasks Overview

| Task | Description |
|------|-------------|
| **Task 1** | Understand the business context, Basel II implications, and need for interpretability |
| **Task 2** | Perform EDA: customer profiles, RFM analysis, churn/disengagement patterns |
| **Task 3** | Feature Engineering: RFM features, WoE transformation, BIV, missing data |
| **Task 4** | Create a proxy variable to simulate default (e.g., low frequency, low monetary scores) |
| **Task 5** | Train and evaluate models: logistic regression, XGBoost, SHAP interpretation |
| **Task 6** | Create an actionable report: segment customers by risk, recommend policies |

---

## 🔐 Credit Scoring Business Understanding

### 1. Basel II and Model Transparency

Basel II requires that models used to measure credit risk be transparent, explainable, and reproducible. This makes **interpretable models** like Logistic Regression (with WoE features) suitable for compliance, as they allow both internal stakeholders and regulators to understand how credit decisions are made.  
The Basel II Accord mandates that banks accurately measure and manage credit risk to determine capital adequacy. This requires models that are interpretable and well-documented, enabling regulators and stakeholders to understand the risk assessment process and ensure compliance with regulatory standards.

---

### 2. Using a Proxy Variable for Default

Because our dataset lacks a direct "default" label, we build a **proxy target** from behavioral indicators (like RFM scores). This allows us to train supervised models, but introduces a risk of **label noise**—so we must validate the model carefully to avoid bias or overfitting.  
a proxy variable is also essential to define a target for model training, such as categorizing customers as high or low risk. However, this proxy may not perfectly align with actual default behavior, risking misclassification that could lead to financial losses or incorrect loan decisions.

---

### 3. Interpretable vs Complex Models

Simple models like Logistic Regression with Weight of Evidence (WoE) are transparent and regulator-friendly but may miss complex data patterns. Complex models like Gradient Boosting offer higher predictive accuracy but are less interpretable, posing challenges in regulated environments where explainability is critical.

| Metric                     | Logistic Regression | XGBoost |
|---------------------------|---------------------|---------|
| Interpretability          | ✅ Very high         | ❌ Low (black box) |
| Performance               | ✅ Good              | ✅ Often better |
| Auditability              | ✅ Easy              | ⚠️ Needs SHAP/LIME |
| Risk of Overfitting       | ✅ Low               | ❌ Higher |
| Regulatory Alignment      | ✅ Strong            | ⚠️ Extra documentation needed |

---

## 📊 Key Features Used

- **RFM** (Recency, Frequency, Monetary)
- **WoE Binning**
- **BIV (Bi-Variate Information Value)**
- **Missing value flags**
- **Behavioral time-based features**

---

## 📦 Repository Structure  

credit-risk-model/   
├── data/  
│ ├── raw/  
│ └── processed/  
├── notebooks/  
│ ├── 1.0-eda.ipynb  
│ ├── 2.0-feature-eng.ipynb  
│ ├── 3.0-modeling.ipynb  
│ ├── 4.0-shap-analysis.ipynb  
├── src/  
│ ├── api/  
| | ├── main.py  
│ | └── pydantic_models.py  
│ ├── __init__.py 
│ ├── data_processing.py  
│ ├── predict.py  
│ └── train.py  
├── tests/  
├── Dockerfile  
├── docker-compose.yml  
├── .gitignore  
├── requirements.txt  
└── README.md  