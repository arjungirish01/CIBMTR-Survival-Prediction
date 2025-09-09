# CIBMTR Survival Prediction

This project predicts **patient survival outcomes** using the [CIBMTR dataset](https://www.cibmtr.org/).  
It applies **machine learning and survival analysis** to identify key clinical features that influence outcomes.

---

## Problem Statement
Hematopoietic stem cell transplantation (HSCT) is a complex treatment, and predicting patient survival helps improve decision-making.  
This project explores **machine learning models** and **survival analysis** for outcome prediction.

---

## Methods
- **Data preprocessing**: Handling missing values, categorical encoding, feature scaling  
- **Models**:
  - Logistic Regression
  - Random Forest
  - XGBoost
  - Survival models (Kaplan-Meier, CoxPH via `lifelines`)  
- **Evaluation metrics**:
  - Accuracy, ROC-AUC, Log-loss
  - Concordance index (for survival analysis)

---

## Results
- Random Forest & XGBoost performed best in classification.
- Cox Proportional Hazards model provided interpretable survival insights.
- Feature importance highlighted key clinical predictors.

---

## Project Structure

CIBMTR-Survival-Prediction/
├── data/                # Raw data (ignored in Git)
├── notebooks/           # Jupyter notebooks for analysis
│   └── cibmtr-survival-prediction.ipynb
├── src/                 # Source code
│   ├── preprocessing.py # Data preprocessing functions
│   ├── modeling.py      # Model training functions
│   └── evaluation.py    # Evaluation metrics and plots
├── models/              # Saved models (ignored in Git)
├── requirements.txt     # Project dependencies
├── README.md            # Project overview
├── LICENSE              # Project license
└── .gitignore           # Git ignore file


## 🚀 Getting Started
1. Clone repo  
   ```bash
   git clone https://github.com/<your-username>/cibmtr-survival-prediction.git
   cd CIBTR-SURVIVAL-PREDICTION

2. Install Dependencies
   ```bash
   pip install -r requirements.txt

3. Run Notebook
  ```bash
  jupyter notebook notebooks/cibmtr-survival-prediction.ipynb

  
