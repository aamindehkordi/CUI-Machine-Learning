
################################################################################
# 2D Machine Learning Plotting Module                                          #
#   Plots 2-dimensional clusters using matplotlib. Centroids input is a list   #
#   of tuples (one tuple per centroid) and cluster input is a list of lists of #
#   of tuples (one list per cluster, one tuple per datapoint). Works well with #
#   data from kmeans.py                                                        #
#                                                                              #
#   file:   kplot2d.py                                                         #
#   author: prof-tallman                                                       #
################################################################################



################################################################################
#                                   IMPORTS                                    #
################################################################################

import matplotlib.pyplot as plt
import numpy as np
import math



################################################################################
#                                  GLOBALS                                     #
################################################################################

_colors = ( "tab:blue", "tab:orange", "tab:green", "tab:red", "tab:purple",
            "tab:brown", "tab:pink", "tab:gray", "tab:olive", "tab:cyan" )



################################################################################
#                                   MODULE                                     #
################################################################################

def plot_clusters(centroids, clusters,
                  title=None, x_label=None, y_label=None, inches=6):

    """ Plots all samples using a unique color that distinguishes each cluster
        from all the others. Centroids are drawn as a black plus sign (+).
        There should be a 1-to-1 parallel relationship between each of the
        centroids and each of the clusters. If the data contains anomalies,
        they must be placed in an iterable object at the end of the clusters
        and without a centroid. Outliers are shown in grey. Only 10 clusters
        can be plotted, not counting the outliers.

        Each sample is a tuple containing the x- and y-coordinates.

        Ex:  centroids = [(9.0, 9.0),
                          (1.0, 1.0)]
             clusters  = [[(10, 10), (8, 10), (8, 8), (10, 8)],
                          [(2, 2), (0, 2), (2, 0), (0, 0)]]
    """

    centroid_count = len(centroids)
    cluster_count = len(clusters)
    color_count = len(_colors)

    # Cannot have more centroids/clusters than we have colors. Also, cluster
    # list must have exactly the same number of elements as centroid list (or
    # one one more holding outlier data points that are to be drawn in gray)

    if centroid_count > color_count:
        raise ValueError("Error: maximum of {} clusters allowed".format(color_count))

    if cluster_count != centroid_count and cluster_count != centroid_count + 1:
        raise ValueError("Error: mismatch between number of clusters ({}) and centroids ({})".format(cluster_count, centroid_count))

    # Create a color list for this plot using a subset of the master colors
    # Silver is the color for outliers, if outliers exist in this data
    colors = list(_colors[:centroid_count])
    if cluster_count > centroid_count:
        colors.append("silver")

    # Initialize the plot
    plt.figure(figsize=(inches, inches))
    plt.title(title, fontsize=16, pad=15)
    plt.xlabel(x_label, fontsize=12, labelpad=5)
    plt.ylabel(y_label, fontsize=12, labelpad=5)
    plt.tight_layout()

    # Plot the cluster points, identifying each cluster by its color
    data_x = [sample[0] for clus in clusters for sample in clus]
    data_y = [sample[1] for clus in clusters for sample in clus]
    data_c = [colors[i] for i, clus in enumerate(clusters) for sample in clus]
    plt.scatter(data_x, data_y, c=data_c)

    # Plot the centroids with a plus sign using the same color as the clusters
    centroids_x = [cent[0] for cent in centroids]
    centroids_y = [cent[1] for cent in centroids]
    centroids_c = colors[:centroid_count]
    plt.scatter(centroids_x, centroids_y, c='black', marker='+')

    plt.show()
    return



def plot_neighbors(train_data, test_data, test_results,
                   title=None, x_label=None, y_label=None, inches=6):

    """ Plots all samples using a unique color that distinguishes each label
        from all the others. Test results are shown as a darker colored 'x'
        over a lighter colored square. If the 'x' and the square are the same
        color, the prediction was correct. Only 10 unique labels can be plotted
        because that's all the colors we know.

        Each sample should be a 3-dimensional tuple. The first two dimensions
        store the x- and y-coordinates and the last dimension holds the label.

        Ex:  train_data   = [(7, 68, 1), (5, 54, 1), (1, 193, 0), (0, 157, 0)...
             test_data    = [(6, 151, 0), (5, 122, 0), (6, 17, 1), (8, 31, 0)...
             test_results = [(6, 151, 0), (5, 122, 0), (6, 17, 1), (8, 31, 1)...
    """

    # Initialize the plot
    plt.figure(figsize=(inches, inches))
    plt.title(title, fontsize=16, pad=15)
    plt.xlabel(x_label, fontsize=12, labelpad=5)
    plt.ylabel(y_label, fontsize=12, labelpad=5)
    plt.tight_layout()

    # Each color represents a different label
    label_count = len(set([sample[-1] for sample in train_data]))
    color_count = len(_colors)
    if label_count > color_count:
        raise ValueError("Error: maximum of {} labels allowed".format(color_count))
    colors = list(_colors[:label_count])

    # Plot training data (it is properly labeled)
    x_values = [sample[0] for sample in train_data]
    y_values = [sample[1] for sample in train_data]
    c_values = [colors[sample[-1]] for sample in train_data]
    plt.scatter(x_values, y_values, c=c_values, marker='s', alpha=0.7)

    # Plot test data (it is properly labeled)
    x_values = [sample[0] for sample in test_data]
    y_values = [sample[1] for sample in test_data]
    c_values = [colors[sample[-1]] for sample in test_data]
    plt.scatter(x_values, y_values, c=c_values, marker='s', alpha=0.7)

    # Plot test results over top the test data; errors will be different colors
    x_values = [sample[0] for sample in test_results]
    y_values = [sample[1] for sample in test_results]
    c_values = [colors[sample[-1]] for sample in test_results]
    plt.scatter(x_values, y_values, c=c_values, marker='x')

    plt.show()
    return



################################################################################
#                                  TESTING                                     #
################################################################################

if __name__ == "__main__":

    test_centroids = [(9.0, 9.0), (1.0, 1.0)]
    test_clusters = [[(10, 10), (8, 10), (8, 8), (10, 8)], [(2, 2), (0, 2), (2, 0), (0, 0)]]
    print()
    print("Running KMeans System Test: Check Results")
    print("Centroids: {}".format(test_centroids))
    print("Clusters:  {}".format(test_clusters))
    plot_clusters(test_centroids, test_clusters, "System Test",
                  x_label="X Position", y_label="Y Position", inches=3)

    training_data = [(7, 68, 1), (5, 54, 1), (1, 193, 0), (0, 157, 0), (3, 45, 1), (3, 37, 1), (3, 141, 0), (15, 43, 1), (18, 110, 0), (26, 242, 0), (56, 244, 0), (4, 35, 1), (38, 218, 0), (16, 229, 0), (18, 48, 1), (2, 243, 0), (16, 226, 0), (22, 44, 1), (6, 196, 0), (3, 40, 1), (75, 238, 0), (5, 173, 0), (46, 202, 0), (96, 129, 1), (41, 67, 1), (7, 33, 1), (5, 42, 1), (8, 136, 0)]
    testing_data  = [(6, 151, 0), (5, 122, 0), (6, 17, 1), (8, 31, 0), (17, 133, 0), (11, 32, 1), (65, 84, 1), (14, 28, 1), (9, 36, 1), (5, 16, 1), (21, 29, 1), (8, 23, 1), (50, 66, 1)]
    test_results =  [(6, 151, 0), (5, 122, 0), (6, 17, 1), (8, 31, 1), (17, 133, 0), (11, 32, 1), (65, 84, 1), (14, 28, 1), (9, 36, 1), (5, 16, 1), (21, 29, 1), (8, 23, 1), (50, 66, 1)]
    print()
    print("Running KNN System Test: Check Results")
    print("Training Data: {}".format(training_data))
    print("Testing Data:  {}".format(testing_data))
    print("Test Results:  {}".format(test_results))
    plot_neighbors(training_data, testing_data, test_results, "System Test",
                  x_label="X Position", y_label="Y Position", inches=6)

################################################################################
#                               END OF MODULE                                  #
################################################################################
