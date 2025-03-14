# Assignment 4: Survival Analysis

## Overview
This assignment focuses on applying survival analysis techniques to a clinical dataset of head and neck cancer patients. The objective is to analyze survival patterns and compare different modeling approaches.

## Dataset
- **RADCURE Clinical Dataset** (provided as `Data/RADCURE_Clinical_v04_20241219.csv`)
- Includes survival time, event indicators, and clinical covariates (e.g., age, treatment type, tumor stage)

## Methods Implemented
### 1. **Kaplan-Meier (KM) Survival Analysis**
   - Generates survival curves for different patient groups
   - Performs log-rank tests to compare survival differences

### 2. **Cox Proportional Hazards Regression**
   - Evaluates survival impact based on multiple covariates
   - Checks proportional hazards assumption

### 3. **Random Survival Forests (RSF)**
   - Predicts survival using an ensemble-based approach
   - Performs variable importance analysis

## Project Structure
```bash
BINF5507_ML-AI_in_Bioinfo/
├── Assignment_4/
│   ├── README.md
│   ├── Scripts/         # Python files
│   │   ├── main.ipynb   # Jupyter notebook with analysis
│   ├── Data/            # RADCURE dataset
│   │   ├── RADCURE_Clinical_v04_20241219.csv
|   ├── Plots            # All plots generated
```


## **🛠️ Steps in the Analysis**
### **1️⃣ Data Preprocessing**
- Cleaned missing values.
- Standardized numerical features.
- Encoded categorical variables.

### **2️⃣ Kaplan-Meier Survival Analysis**
- Estimated survival probabilities for **Stage_Grouped** and **Age_Binned**.
- Conducted **Log-Rank Tests** to compare survival curves.

### **3️⃣ Cox Proportional Hazards Model**
- Fit **Standard Cox Model**, **Lasso (L1) Regularized Cox**, and **Ridge (L2) Regularized Cox**.
- Checked **Proportional Hazards Assumption** and adjusted for violations.
- Compared **C-Index values** across models.

### **4️⃣ Random Survival Forests (RSF)**
- Trained an RSF model for **survival prediction**.
- **Computed feature importance** using permutation importance.
- Compared **C-Index with Cox models**.

---

## **📊 Model Comparison**
| **Model**                         | **C-Index** |
|-----------------------------------|------------|
| **Standard Cox Model (λ=0)**       | `0.6650`   |
| **Lasso Cox Model (λ=0.01)**       | `0.6646`   |
| **Ridge Cox Model (λ=1.0)**        | `0.6495`   |
| **Random Survival Forests (RSF)**  | `0.7642`   |

- **Log-Rank Test Results:**
  - **Stage_Grouped p-value:** `5.0966e-06`
  - **Age_Binned p-value:** `2.1650e-31`

- **Conclusion:** RSF had the highest predictive accuracy (`C-Index = 0.7642`), while **Cox models provided interpretable hazard ratios**.

---

## **📊 Top Predictive Features (RSF Importance Ranking)**
| **Feature**         | **Importance Score** |
|---------------------|------------------|
| **Age**            | `0.0909` |
| **Stage**          | `0.0785` |
| **Smoking Status** | `0.0669` |
| **Tx Modality**    | `0.0463` |
| **Age_Binned**     | `0.0178` |

---

# Installation & Execution
Clone the repository:
```bash
git clone https://github.com/Kaleem-QADR/BINF5507_ML-AI_in_Bioinfo.git

```
## Navigate to the assignment folder:
```bash
cd BINF5507_ML-AI_in_Bioinfo/Assignment_4/Scripts
```
## Install dependencies:
```bash
pip install -r requirements.txt
```
# Run the Jupyter Notebook:
```bash
jupyter notebook main.ipynb
```
## Deliverables
GitHub Repository: Contains all scripts, data, and documentation.

## Conclusion
This analysis compares traditional statistical survival models (Kaplan-Meier, Cox) with machine learning-based survival prediction (RSF). The results highlight:

Stage and Age are significant survival predictors.
RSF provides flexible survival predictions but requires tuning.
Cox regression offers a balance between interpretability and predictive accuracy.

## Author
Kaleem Uddin Mohammed
Contact: Dr.KaleemCCRP@Gmail.com

## License
This project is for educational purposes only.
