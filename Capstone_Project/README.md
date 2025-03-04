# Capstone Project: Gaussian Mixture Models (GMM) vs. Traditional Clustering  

✍️ Authors
Binal Patel,
Siddhi Naik,
Kaleem Mohammed
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
Capstone_Project/
│── scripts/
│ ├── main.ipynb # Jupyter Notebook with GMM implementation and comparisons
│── plots/ # Clustering output visualizations
│ ├── moons_clustering.png # GMM vs. traditional clustering on Moons Dataset
│ ├── blobs_clustering.png # GMM vs. traditional clustering on Blobs Dataset
│ ├── circles_clustering.png # GMM vs. traditional clustering on Circles Dataset
│── README.md # Project description and instructions
│── report.docx # Final written report
```

## 🖥️ How to Run the Code  
1. **Clone the repository:**  
   ```bash
   git clone https://github.com/Kaleem-QADR/BINF5507_ML-AI_in_Bioinfo/tree/main/Capstone_Project
   cd Capstone_Project/scripts
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


📌 References
scikit-learn: GaussianMixture
Expectation-Maximization Algorithm
Clustering Evaluation Metrics

📢 Acknowledgments
Special thanks to our instructor and peers for their support and feedback on this project! 🎯🚀


---

### **What This README Includes**
✅ **Project Overview**  
✅ **Datasets & Objectives**  
✅ **File Structure (Matches Your Preferred Format)**  
✅ **How to Run the Code**  
✅ **Evaluation Metrics**  
✅ **Authors: Binal Patel, Siddhi Naik, Kaleem Mohammed**  
✅ **References & Acknowledgments**  

---
