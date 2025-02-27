# Assignment 3: Clustering Algorithm Self-Study

## 📌 Overview
This project focuses on implementing and analyzing three clustering algorithms:
- **k-Means**
- **Hierarchical Clustering**
- **DBSCAN**

We compare their performance using three datasets:
1. **Moons Dataset** - Best for DBSCAN due to non-spherical clusters.
2. **Blobs Dataset** - Works well with k-Means and Hierarchical Clustering.
3. **Circles Dataset** - DBSCAN performs best due to its density-based approach.

## 📂 Folder Structure
'''
Assignment_3/ │── scripts/ │ ├── main.ipynb # Jupyter Notebook with clustering implementation │ │── plots/ │ ├── moons_clustering.png # Output visualization for moons dataset │ ├── blobs_clustering.png # Output visualization for blobs dataset │ ├── circles_clustering.png # Output visualization for circles dataset │ │── README.md # Project description and instructions │── report.docx # Final report document
'''

## 🚀 How to Run
1. Open the `scripts/main.ipynb` file in Jupyter Notebook.
2. Run all cells to generate clustering results.
3. All plots will be saved in the `plots/` folder.

## 📊 Results Summary
| Dataset | Best Algorithm | Reason |
|---------|---------------|--------|
| Moons | **DBSCAN** | Best for non-spherical clusters |
| Blobs | **k-Means & Hierarchical** | Works well for well-separated blobs |
| Circles | **DBSCAN** | Detects circular clusters correctly |

## 🔗 Resources
- [DBSCAN Documentation](https://scikit-learn.org/stable/modules/generated/sklearn.cluster.DBSCAN.html)
- [k-Means Documentation](https://scikit-learn.org/stable/modules/generated/sklearn.cluster.KMeans.html)
- [Hierarchical Clustering](https://scikit-learn.org/stable/modules/generated/sklearn.cluster.AgglomerativeClustering.html)

'''
