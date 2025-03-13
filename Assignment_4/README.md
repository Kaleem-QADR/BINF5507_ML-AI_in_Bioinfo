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
```
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

## Author
Kaleem Uddin Mohammed
Contact: Dr.KaleemCCRP@Gmail.com
## License
This project is for educational purposes only.
