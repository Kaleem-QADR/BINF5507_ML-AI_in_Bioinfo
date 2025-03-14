# Capstone Project: Gaussian Mixture Models (GMM) vs. Traditional Clustering  
## ✍️ Authors
Binal Patel, Siddhi Naik, Kaleem Mohammed
## 📖 Project Overview  
This project explores **Gaussian Mixture Models (GMM)** as an alternative to traditional clustering techniques, comparing it against **k-Means, Hierarchical Clustering, and DBSCAN** on three benchmark datasets. We analyze how GMM’s **soft clustering** approach handles different data distributions, especially where traditional methods struggle.  

## 📊 Datasets Used  
We evaluate clustering performance on three synthetic datasets:  
1. **Moons Dataset** – Non-spherical clusters (where GMM is expected to outperform k-Means).  
2. **Blobs Dataset** – Well-separated clusters with varying densities.  
3. **Circles Dataset** – Nested circular clusters (challenging for k-Means).  

## 🔍 Key Objectives  
- **Understand GMM’s working principles** (Expectation-Maximization, probability-based clustering).  
- **Implement GMM and compare it with k-Means, Hierarchical, and DBSCAN**.  
- **Analyze clustering performance using visualization and metrics (e.g., Silhouette Score, BIC/AIC for GMM).**  

## 🏗️ Project Structure  
```
MACHINE_LEARNING_CAPSTONE_PROJECT/
│── plots/
│   ├── blobs_dataset_clustering.png
│   ├── blobs_dataset_gmm_selection.png
│   ├── circles_dataset_clustering.png
│   ├── circles_dataset_gmm_selection.png
│   ├── gmm_probabilities.png
│   ├── gmm_probability_histogram.png
│   ├── moons_dataset_clustering.png
│   ├── moons_dataset_gmm_selection.png
│
│── scripts/
│   ├── main.ipynb  # Jupyter Notebook with clustering implementation
│
│── Gaussian Mixture Models - Report.docx  # Final project report
│── README.md  # Project description and instructions

```


## 🖥️ How to Run the Code
1. **Clone the repository**:
   ```bash
   git clone https://github.com/Kaleem-QADR/Machine_Learning_Capstone_Project.git
   cd Machine_Learning_Capstone_Project/scripts

   ```

2. Open Jupyter Notebook:
```
jupyter notebook main.ipynb
```
3. Run all cells to generate clustering outputs and comparisons.
4. Visualizations will be saved in the plots/ folder.

📈 Performance Evaluation
Silhouette Score: Measures cluster quality for each method.
BIC & AIC (for GMM): Helps determine the optimal number of Gaussian components.
Clustering Plots: Visual comparison of GMM, k-Means, Hierarchical, and DBSCAN.


## 📊 Clustering Model Comparison Results  

### **1️⃣ Silhouette Score Summary**  
| Dataset        | k-Means  | Hierarchical | DBSCAN  | GMM  |
|---------------|---------|-------------|--------|------|
| **Moons**     | **0.441** ✅ | 0.381 | 0.386 | 0.435 |
| **Blobs**     | **0.787** ✅ | 0.783 | 0.720 | 0.783 |
| **Circles**   | **0.381** ✅ | 0.351 | 0.004 ❌ | 0.381 |

### **2️⃣ GMM Model Selection (BIC & AIC)**
| Dataset        | Optimal Components (BIC) | Optimal Components (AIC) |
|---------------|-------------------------|-------------------------|
| **Moons**     | 8 | 9 |
| **Blobs**     | **3** ✅ | 6 |
| **Circles**   | 9 | 9 |

### **🔍 Key Takeaways**  
✔ **k-Means performed best for simple, well-separated clusters** (Blobs dataset).  
✔ **GMM closely matched k-Means but allows probabilistic clustering**.  
✔ **DBSCAN struggled with Circles Dataset, confirming density-based limitations**.  
✔ **BIC & AIC helped determine the best number of Gaussian components for GMM**.  

---


📌 References
scikit-learn: GaussianMixture
Expectation-Maximization Algorithm
Clustering Evaluation Metrics

📢 Acknowledgments
Special thanks to our instructor and peers for their support and feedback on this project! 🎯🚀


---

### **What This README Includes**
✅ **Project Overview**  
✅ **Authors: Binal Patel, Siddhi Naik, Kaleem Mohammed**  
✅ **Datasets & Objectives**  
✅ **File Structure (Matches Your Preferred Format)**  
✅ **How to Run the Code**  
✅ **Evaluation Metrics** 
✅ **Clustering Model Comparison Results**  
✅ **References & Acknowledgments**  

---
