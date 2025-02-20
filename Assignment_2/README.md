# Assignment 2: Regression and Classification Models

## Overview
This project implements machine learning models for **regression and classification** using the **Heart Disease Dataset** from the UCI Machine Learning Repository. The primary objectives are:
- Training and evaluating regression models to predict cholesterol levels.
- Training and evaluating classification models to predict the presence of heart disease.
- Analyzing hyperparameter effects and visualizing performance metrics.

## Repository Structure
```
YourClassRepositoryName/YourAssignmentFolderName
├── README.md              # Project documentation
├── Scripts/
│   ├── main.ipynb         # Jupyter Notebook for training & evaluation
│   ├── regression.py      # Python script for regression models
│   ├── classification.py  # Python script for classification models
│   ├── utils.py           # Helper functions for data preprocessing & visualization
├── Data/
│   ├── heart_disease_uci.csv  # Dataset file
```

## Dataset
The dataset used in this assignment is the **Heart Disease Dataset** from the UCI Machine Learning Repository.

- **Features:** Age, sex, chest pain type, resting blood pressure, cholesterol, fasting blood sugar, etc.
- **Target Variables:**
  - **Regression Task:** Predict cholesterol levels (`chol` column).
  - **Classification Task:** Predict heart disease presence (`num` column).

### Data Source:
[UCI Machine Learning Repository - Heart Disease](https://archive.ics.uci.edu/dataset/45/heart+disease)

## Setup Instructions
1. **Clone the repository**:
   ```sh
   git clone https://github.com/YourUsername/YourClassRepositoryName.git
   cd YourClassRepositoryName/YourAssignmentFolderName
   ```

2. **Install dependencies**:
   ```sh
   pip install -r requirements.txt
   ```

3. **Download Dataset** (if not included):
   ```python
   from sklearn.datasets import fetch_openml
   data = fetch_openml(name="heart-disease", as_frame=True)
   ```

4. **Run the Jupyter Notebook**:
   ```sh
   jupyter notebook Scripts/main.ipynb
   ```

## Model Implementation
### 1. Regression Models (Predicting Cholesterol Levels)
- Implement **ElasticNet Regression**.
- Tune **alpha** and **l1_ratio** hyperparameters.
- Evaluate models using:
  - **R² Score**
  - **Root Mean Squared Error (RMSE)**
- Generate a **heatmap** of R² and RMSE scores.

### 2. Classification Models (Predicting Heart Disease)
- Implement:
  - **Logistic Regression**
  - **k-Nearest Neighbors (k-NN)**
- Hyperparameter tuning:
  - Logistic Regression: **penalty, solver**
  - k-NN: **n_neighbors** (e.g., {1, 5, 10})
- Evaluation Metrics:
  - **Accuracy, F1 Score, AUROC, AUPRC**
- Visualizations:
  - **AUROC and AUPRC curves** for best models.


## Contact
For questions, contact DrKaleemCCRP@Gmail.com or open an issue on GitHub.
