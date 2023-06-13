#euclidean distance p1, p2
#finds the ID of the closest centroid easy to find min distance
#harder to find ID of centroid of min distance
#assigns every sample to closest centroid
#calculate the position of a single centroid as mean avg location in each dimension
#calculate position of all centroids
#give calculate initial centroids
#do loop
import math


def distance(p1, p2):
    """
    Get distance of 2 points and return the value.
    """
    distance = 0.0
    sum = 0.0
    #2d and beyond
    for i in range(len(p1)):
        sum += (p1[i] - p2[i]) ** 2
    distance = math.sqrt(sum)

    return distance

def createClusters(centroids, data, k):
    """
    Create or change clusters based on centroid positions.
    Basically sorted data
    """
    dArray = []
    clusters = [[] for i in range(k)]

    for i in data:
        dArray = [distance(i, c) for c in centroids]
        #add data point to respective centroid list [[centroidList1], [centroidList2], etc.]
        clusters[findClosestRoid(dArray)].append(i)
    return clusters

def findClosestRoid(distanceArray):
    """
    helper for finding the closest centroid since .index() doesn't work for tuples
    returns index of the closest centroid
    """
    min = 99999999999
    index = 0
    for i, d in enumerate(distanceArray):
        if d <= min:
            min = d
            index = i
    return index

def changeCentroids(data, clusters):
    """
    Change centroid location based on Clusters
    returns centroids with updated coords.
    """
    dimensions = len(data[0])
    #make centroid list correct size
    centroids = [[] for i in clusters]

    for i, c in enumerate(clusters):
        sum = 0.0
        for d in range(dimensions):
            #go through cluster and get the sums of current dimension
            for j, data in enumerate(c):
                sum += c[j][d]
            sum = sum / len(c)

            centroids[i].append(sum)
        #Turn list of x, y, (z) to tuple
        centroids[i] = tuple(centroids[i])

    return centroids

def runKmeansAlgorithm(data, k):
    """
    Main program
    returns centroids and clusters.
    """
    #might not need a few of these lines but I don't want to break anything

    #starting centroid is the first k points so there aren't any repeats
    centroids = [data[i] for i in range(k)]
    clusters = createClusters(centroids, data, k)
    prevClusters = clusters

    changing = True
    while changing:
        clusters = createClusters(centroids, data, k)
        centroids = changeCentroids(data, clusters)
        if clusters == prevClusters:
            #if the cluster is the same as the last iteration then it's done
            changing = False
    return centroids, clusters
"""
Main
"""
if __name__ == "__main__":
    expected = 8
    if findClosestRoid([10,29,13,200,12,53,531,912,2]) == expected:
        print('findClosestRoid ---------- Passed')
    else:
        print('findClosestRoid ---------- Failed')
    expected = 5.0
    if distance((7, 0), (12, 0)) == expected:
        print('distance        ---------- Passed')
    else:
        print('distance        ---------- Failed')
