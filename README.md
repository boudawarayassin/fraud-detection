# Fraud Detection System

An end-to-end Machine Learning project for detecting fraudulent financial transactions using the PaySim dataset and XGBoost.

## Project Overview

This project develops a complete fraud detection system, from exploratory data analysis and preprocessing to model training, explainability, model deployment, and web-based prediction.

The final system exposes the trained Machine Learning model through a FastAPI REST API and provides a web interface for transaction analysis.

## Objectives

- Analyze fraudulent and normal transactions
- Handle severe class imbalance
- Build a robust preprocessing pipeline
- Compare several Machine Learning models
- Optimize the fraud detection model
- Select an appropriate classification threshold
- Explain predictions using SHAP
- Deploy the model through FastAPI
- Provide a web interface for real-time predictions

## Dataset

The project uses the PaySim dataset.

Main features:

- `step`
- `type`
- `amount`
- `oldbalanceOrg`
- `newbalanceOrig`
- `oldbalanceDest`
- `newbalanceDest`

Target:

- `isFraud`

The dataset contains more than 6 million transactions and is highly imbalanced.

## Machine Learning Workflow

The project follows this workflow:

1. Exploratory Data Analysis
2. Data cleaning
3. Feature selection
4. Train/Test split
5. Categorical encoding
6. Numerical feature scaling
7. Pipeline construction
8. Cross-validation
9. Class imbalance analysis
10. Model comparison
11. Hyperparameter tuning
12. Threshold optimization
13. SHAP explainability
14. Model serialization
15. FastAPI deployment
16. Web interface

## Models Tested

The following models were investigated:

- Logistic Regression
- Decision Tree
- Random Forest
- XGBoost

XGBoost was selected for the final application because it provided strong fraud detection performance in the experiments.

## Final Model

The final model uses:

- XGBoost
- OneHotEncoder for transaction type
- StandardScaler for numerical features
- Pipeline for preprocessing and prediction
- Optimized classification threshold

The selected threshold is:

`0.33956692`

Instead of relying exclusively on the default 0.5 threshold, the threshold was selected using out-of-fold predictions on the training set.

## Evaluation

Using the selected threshold, the model achieved approximately:

| Metric | Fraud class |
|---|---:|
| Precision | 0.933 |
| Recall | 0.868 |
| F1-score | 0.899 |

The dataset is highly imbalanced, therefore accuracy alone is not considered an appropriate primary metric.

## Explainability

SHAP was used to understand how the XGBoost model makes predictions.

The analysis was performed at two levels:

### Global explanation

Identifies features that have the largest influence on model predictions across many transactions.

### Local explanation

Explains why an individual transaction was classified as fraudulent or normal.

Important features observed during the analysis included:

- `newbalanceOrig`
- `oldbalanceOrg`
- `amount`
- `type_CASH_OUT`
- `type_TRANSFER`
- `newbalanceDest`

SHAP values describe the model's behavior and should not be interpreted as causal relationships.

## API

The application uses FastAPI.

Start the API with:

```bash
uvicorn src.app:app --reload