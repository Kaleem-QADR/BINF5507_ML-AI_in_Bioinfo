# Heart Disease Prediction using Machine Learning

This project explores **heart disease prediction** using **ElasticNet Regression, Logistic Regression, and k-NN Classification**.

## 📂 Repository Structure
```
Assignment_2/
├── README.md # Project documentation
├── Scripts/ # Code files
  │ ├── main.ipynb # Jupyter Notebook for full analysis
├── Data/ # Dataset & Model performance plots
  │ ├── heart_disease_uci.csv # UCI Heart Disease dataset (if needed)
├── Plots #output plot images for reference
  │ ├── Logistic_Regression_AUROC.png
  │ ├── Logistic_Regression_Precision_Recall_Curve.png
  │ ├── k-NN_Classifier_AUROC.png
  │ ├── k-NN_Classifier_Precision_Recall_Curve.png
```


## 📝 **Project Overview**
This project involves:
- **Data Preprocessing** (handling missing values, encoding, scaling)
- **Regression Model** (ElasticNet for `chol`)
- **Classification Models** (Logistic Regression & k-NN for `num`)
- **Model Evaluation** (AUROC, AUPRC, and performance plots)

## 📊 **Results**
| Model                  | AUROC  | AUPRC  |
|------------------------|--------|--------|
| Logistic Regression    | 0.9007 | 0.9190 |
| k-NN Classifier       | 0.8662 | 0.8813 |

## 🚀 **How to Run**
1. Clone this repository:
```bash
git clone https://github.com/Kaleem-QADR/BINF5507_ML-AI_in_Bioinfo.git
2. Navigate to the project directory:
```
cd BINF5507_ML-AI_in_Bioinfo/Assignment_2

```
3. Install dependencies:
```
pip install -r requirements.txt
```
4. Run main.ipynb in Jupyter Notebook:
```
jupyter notebook main.ipynb
```

🔹 Data Preprocessing
```
# Convert 'num' into a binary classification target
df["num"] = df["num"].apply(lambda x: 1 if x > 0 else 0)
```
🔹 Train Logistic Regression
```
log_reg = GridSearchCV(LogisticRegression(), {"penalty": ["l2"], "solver": ["lbfgs"]}, scoring="roc_auc", cv=5)
log_reg.fit(X_train_clf, y_train_clf)
y_prob_lr = log_reg.best_estimator_.predict_proba(X_test_clf)[:, 1]
```
🔹 Plot AUROC Curve
```
def plot_auroc(y_true, y_prob, model_name):
    fpr, tpr, _ = roc_curve(y_true, y_prob)
    plt.plot(fpr, tpr, color='blue', label=f"AUC: {roc_auc_score(y_true, y_prob):.2f}")
    plt.xlabel("False Positive Rate")
    plt.ylabel("True Positive Rate")
    plt.title(f"{model_name} - ROC Curve")
    plt.legend()
    plt.show()
```
