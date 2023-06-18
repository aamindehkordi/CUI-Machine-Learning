# Clustering Directory

The Clustering directory contains several Python scripts related to the K-Means Clustering algorithm. Below is a brief description of each script:

- `2020_Fall_AliAmin_K-MeansClustering.py`: This script is a K-Means Clustering algorithm implementation. It includes functions for calculating Euclidean distance, finding the closest centroid, initializing empty clusters, assigning items to the closest cluster, choosing random centroids, calculating centroid location, plotting clusters in 2D, and creating K-Means clusters. The script also includes a dictionary of student grades used as data for the K-Means Clustering algorithm.

- `KElbow.py`: This script is a simple implementation of the Elbow Method used in K-Means Clustering. The script includes a function named `kElbow` that calculates the Within-Cluster-Sum of Squared Errors (WSSE) for a range of possible K-values. The function takes a list of data points and the maximum number of clusters as inputs.

- `cluster.py`: This script is a comprehensive implementation of the K-Means Clustering algorithm. It includes functions for cleaning data, converting data to the proper format, and running the K-Means algorithm. The script also includes error checking for command-line parameters and data cleaning. The main part of the script loads raw CSV data, cleans the data, converts it to the proper format, and runs the K-Means algorithm. If the data is 2-dimensional, it plots the clusters.

- `kmeans.py`: This script is a simple implementation of the K-Means Clustering algorithm. It includes functions for initializing centroids, assigning points to clusters, updating centroids, and calculating the sum of squared errors. The script also includes a function named `kmeans` that runs the K-Means algorithm on a given set of data points and a specified number of clusters.

- `kplot2d.py`: This script is a module for plotting 2-dimensional clusters using matplotlib. It includes two main functions: `plot_clusters` and `plot_neighbor`. The `plot_clusters` function plots all samples using a unique color that distinguishes each cluster from all the others, with centroids drawn as a black plus sign (+). The `plot_neighbor` function plots all samples using a unique color that distinguishes each label from all the others, with test results shown as a darker colored 'x' over a lighter colored square. If the 'x' and the square are the same color, the prediction was correct.
