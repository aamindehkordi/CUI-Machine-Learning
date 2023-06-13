##############################################
#   Author: Robby La Tourette
#   Date  : 1/20/22
#   email : robby.latourette@eagle.cui.edu
##############################################
from json.tool import main
import math
import statistics
import random
from tracemalloc import StatisticDiff
import matplotlib
import pandas

MARQUEE = "======================================"
testData = [(7, 68, 1), (5, 54, 1), (1, 193, 0), (0, 157, 0), (3, 45, 1), (3, 37, 1), (3, 141, 0), (15, 43, 1),
            (18, 110, 0), (26, 242, 0), (56, 244, 0), (4, 35, 1), (38, 218, 0), (16, 229, 0), (18, 48, 1), (2, 243, 0),
            (16, 226, 0), (22, 44, 1), (6, 196, 0), (3, 40, 1), (75, 238, 0), (5, 173, 0), (46, 202, 0), (96, 129, 1),
            (41, 67, 1), (7, 33, 1), (5, 42, 1), (8, 136, 0)]


#########################
#   FUNCTIONS
#########################

def printHeader():
    print(MARQUEE +
          "\nHello and Welcome to Kmeans Calculator\n" +
          MARQUEE + "\n")


# Gets User Input for the number of centroids (K)
def getK():
    K = 0
    while (K > 10 or K < 1):
        K = int(input("Enter Number of Centroids(K): "))
        if (K > 10 or K < 1):
            print("K must be a number between 1-10!!")

    return K


# initializes list of centroids
def initializeCentroids(samples, k):
    centroids = []
    temp = 0
    usedSamples = []

    # creates k amount of centroids
    for x in range(k):
        # picks random point from data set
        temp = int(random.random() * len(samples))

        # checks if a point was already used
        while (temp in usedSamples):
            temp = int(random.random() * len(samples))
        usedSamples.append(temp)
        # adds
        centroids.append(samples[temp])

    return centroids


def createClusters(sample, centroids):
    clusters = [[] for i in range(len(centroids))]
    for i in sample:
        clusters[findClosestCentroid(i, centroids)].append(i)
    return clusters


def findEuclideanDistance(point1, point2):
    distance = 0
    sumOfDimensions = 0
    for x in range(len(point1)):
        sumOfDimensions += (point1[x] - point2[x]) ** 2
    distance = math.sqrt(sumOfDimensions)

    return distance


def findClosestCentroid(point, Centroids):
    # Create a list of distances to each of the different centroids
    distance = []
    for i in range(len(Centroids)):
        dist = findEuclideanDistance(point, Centroids[i])
        distance.append(dist)

    # Which centroid is closest? Get its index
    min_distance = min(distance)
    closeCentroid = distance.index(min_distance)
    # min_centroid = Centroids[closeCentroid]
    # print("Point {} is closest to centroid #{} which is at location {}".format(point, closest_indx+1, min_centroid))

    return closeCentroid


# Recalculates posistions of all centroids
def calculatePositionOfAllCentroids(centroids, clusters):
    newCentroids = []
    for x in range(len(centroids)):
        newCentroids.append(calculateCentroidPosition(centroids[x], clusters[x]))

    return newCentroids


# Recalculates Postions of a Centroid
def calculateCentroidPosition(centroid, cluster):
    newCentroid = []
    dimensions = len(cluster[0])
    tempArray = [[] for i in range(dimensions)]
    for x in cluster:
        for y in range(len(x)):
            tempArray[y].append(x[y])

    for x in range(dimensions):
        collector = 0
        for y in range(len(cluster)):
            collector += tempArray[x][y]
        newCentroid.append(collector / len(tempArray[x]))

    return newCentroid


def run_kmeans_algorithm(data, k):
    Centroids = initializeCentroids(data, k)
    for i in range(10):
        Clusters = createClusters(data, Centroids)
        Centroids = calculatePositionOfAllCentroids(Centroids, Clusters)

    return (Centroids, Clusters)


#########################
#   MAIN
#########################
if __name__ == "__main__":
    printHeader()

    # gets number of clusters from user
    k = getK()

    # initializes centroids
    Centroids = initializeCentroids(testData, k)
    Clusters = createClusters(testData, Centroids)
    # tempCluster = [[(1,2,3), (4,5,6)], [(6,7,8), (10,11,12)]]
    # tempCluster = [(1,2,3), (4,5,6)]
    # temp = calculateCentroidPosition(Centroids, tempCluster)
    print(Centroids)

    Centroids = calculatePositionOfAllCentroids(Centroids, Clusters)

    print(Centroids)
    print(Clusters)
