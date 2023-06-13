################################################################################
# Takes clean, numerical data for input and is responsible for                  #
# calculating all centroids and clustering each datapoint about a centroid.    #
# Uses the simple KMeans algorithm that repeatedly recalculates the centroids  #
# and clusters until reaching stability (e.g., the clusters stop changing).    #
# To avoid the rare model that never stabilizes,                               #
# the model should never continue past 10 rounds of calculations.              #
# You must write the kmeans.py module yourself.                                #
# It should have a __main__ section that unit tests your functions.            #
# You program should run on data of arbitrary dimension,                       #
# although we will only use 2D data for this homework assignment.              #
#                                                                              #
#                                                                              #
#                                                                              #
#   file:   kmeans.py                                                          #
#   author: Ali Amin                                                           #
################################################################################


################################################################################
#                                   IMPORTS                                    #
################################################################################

import math
import random


################################################################################
#                                 FUNCTIONS                                    #
################################################################################


def findEucDist(point1, point2):
    """
    Finds the Euclidean Distance between two points

    Args:
        point1: First point
        point2: Second point

    Returns:
        Returns the euclidean distance between the two points
    """
    distance = 0
    dimsSum = 0
    # Possibly multiple dimensions
    for i in range(len(point1)):
        dimsSum += (point1[i] - point2[i]) ** 2
    distance = math.sqrt(dimsSum)

    return distance


def closestCentroid(point, centroids):
    """
    Finds the closest centroid for a given point
    to identify which cluster the point belongs to.

    Args:
        point: The point in question
        centroids: The list of centroids that the point's distance will be compared to.
    Returns:
        The closest centroid index
    """
    # Create a list of distances to each of the different centroids
    distance = []
    for i in range(len(centroids)):
        x = findEucDist(point, centroids[i])
        distance.append(x)

    # Which centroid is closest? Get its index
    min_distance = min(distance)
    closestIdx = distance.index(min_distance)
    return closestIdx


def initRandomCentroids(data, k):
    """
    Randomly places the centroids to begin the kmeans algorithm

    Args:
        data: the set of data in question
        k: number of centroids/ groups
    Returns:
        Returns list of centroids
    """
    centroids = []
    x = 0
    used = []
    # Initializes list of centroids
    for j in range(k):
        x = int(random.random() * len(data))
        while x in used:
            x = int(random.random() * len(data))
        used.append(x)
        centroids.append(data[x])

    return centroids


def initClusters(data, centroids):
    """
    Creates and calcuulates the list of clusters
    that which data will be categorized in which cluster.

    Args:
        data: the set of data in question.
        centroids: the centroids that will be used to calculate which cluster the data belongs in.

    Returns:
        Returns List of Clusters.
    """
    clusters = [[] for i in range(len(centroids))]
    for sample in data:
        closest = closestCentroid(sample, centroids)
        clusters[closest].append(sample)
    return clusters


def allCentroidPos(centroids, clusters):
    """
    Recalculates all centroid positions

    Args:
        centroids: list of current centroids
        clusters: list of current clusters
    Returns:
        Returns List of newly placed centroids
    """
    droids = []
    for i in range(len(centroids)):
        pos = calcSinglePos(centroids[i], clusters[i])
        droids.append(pos)
    return droids


def calcSinglePos(centroid, cluster):
    """
    Helper function for allCentroidPos function;
    Recalculates the position of a single centroid.

    Args:
        centroid: a single centroid
        cluster: a single cluster
    Returns:
        The new position of the centroid.
    """
    droid = []
    dims = len(cluster[0])
    centroids = [[] for i in range(dims)]

    for sample in cluster:
        for i in range(len(sample)):
            centroids[i].append(sample[i])

    for dim in range(dims):
        dimSum = 0
        for i in range(len(cluster)):
            dimSum += centroids[dim][i]
        mean = dimSum / len(centroids[dim])
        droid.append(mean)

    return droid


def run_kmeans_algorithm(data, k):
    """
    The main kmeans Algorithm; initializes random centroids based on the data, calculates
    and recalculates which cluster the data belongs in based on the centroids, which
    also get recalculated in a loop until either a centroid doesn't move or 10 loops occurs.

    Args:
        data: the data set te algorithm is running on
        k: number of centroids/clusters
    Returns:
        Returns the location of the centroid and clusters
    """
    prevRoids = initRandomCentroids(data, k)
    num = 0
    stable = False
    while not stable or num < 10:
        clusters = initClusters(data, prevRoids)
        centroids = allCentroidPos(prevRoids, clusters)
        if centroids == prevRoids:
            stable = True
        prevRoids = centroids
        num += 1

    return centroids, clusters


################################################################################
#                               Testing                                        #
################################################################################
testData = [(7, 68, 1), (5, 54, 1), (1, 193, 0), (0, 157, 0), (3, 45, 1), (3, 37, 1), (3, 141, 0), (15, 43, 1),
            (18, 110, 0), (26, 242, 0), (56, 244, 0), (4, 35, 1), (38, 218, 0), (16, 229, 0), (18, 48, 1), (2, 243, 0),
            (16, 226, 0), (22, 44, 1), (6, 196, 0), (3, 40, 1), (75, 238, 0), (5, 173, 0), (46, 202, 0), (96, 129, 1),
            (41, 67, 1), (7, 33, 1), (5, 42, 1), (8, 136, 0)]

if __name__ == '__main__':
    # initializes centroids
    Centroids = initRandomCentroids(testData, 2)
    Clusters = initClusters(testData, Centroids)
    # tempCluster = [[(1,2,3), (4,5,6)], [(6,7,8), (10,11,12)]]
    # tempCluster = [(1,2,3), (4,5,6)]
    # temp = calculateCentroidPosition(Centroids, tempCluster)
    print(Centroids)

    Centroids = allCentroidPos(Centroids, Clusters)

    print(Centroids)
    print(Clusters)
