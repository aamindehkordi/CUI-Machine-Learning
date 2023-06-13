import math
import sys
import collections
import pandas as pd
import kplot2d

def knn_pred(query=tuple, k=int, data=list):
    """
    Predicts the type of a queried point with a training dataset by comparing the type
    of the k nearest neighbors to the query and taking the mode of them to predict the query type.

    Args:
        query: First point
        k: Number of nearest neighbors
        data: Training Data (must include labels at the last index)

    Returns:
        Returns the required label of prediction
    """
    distances = []
    for i,x in enumerate(data):
        d = findEucDist(query, x)
        distances.append((d, i))#appends distance to neighbor and correlated data index
    distances = sorted(distances)[:k]
    knnLabels = []
    for dist, idx in distances:
        knnLabels.append(data[idx][-1])#searches data with neighbor distance idx
    predType = mode(knnLabels)
    return predType


def mode(labels):
    """
    This is from Onel Harrison from TowardsDataScience.com AKA the article linked with the assignment:
    https://towardsdatascience.com/machine-learning-basics-with-the-k-nearest-neighbors-algorithm-6a6e71d01761

    Args:
        labels = list of labels

    Returns:
        Returns the most common label
    """
    return collections.Counter(labels).most_common(1)[0][0]

def knn_fit(filename = str, labels = list):
    """
    K-Nearest-Neighbors Fit:
    Loads and Cleans the data

    Args:
        filename = The name of the file to import data from
        labels = Desired list of Labels to train on from the user

    Returns:
        Returns a Tuple list of training and test data from Train Test Split Function
    """
    df = loadData(filename)
    df = df[labels]
    df[labels[-1]] = df[labels[-1]].map({'Wine': 0,'Beer':1})
    data = df.values
    #print(df)
    return ttSplit(data, 0.2)

def ttSplit(data, testSize=float):
    """
    Train Test Split:
    Splits clean data into training and test data in a very rudimentary way

    Args:
        data: Clean data columns
        testSize: Relative % of total data that will be used for testing

    Returns:
        Returns two lists of tuples, A training list and a smaller testing list
    """
    pData = []
    tData = []

    #from 0 to testSize % of length of data
    for i in range(int(len(data)*testSize)):
        tData.append(data[i])
    #start from length of test data and go to length of data
    for i in range(len(tData), len(data), 1):
        pData.append(data[i])
    return tData, pData

def loadData(filename):
    """
    Loads most file formatted data into a dataframe

    Args:
        filename: the name of the file

    Returns:
        Returns a dataframe of the data
    """
    extension = filename[-3:]
    if extension == 'csv':
        data = pd.read_csv(filename)
    elif extension == 'son':
        data = pd.read_json(filename)
    elif extension == 'xsl':
        data = pd.read_excel(filename)
    return data

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


if __name__ == '__main__':
    fName = sys.argv[1]
    k = int(sys.argv[2])
    labels = sys.argv[3:]
    pData, tData = knn_fit(filename=fName, labels=labels)

    knnLabels = []
    for i in range(len(tData)):
        knnLabels.append((*tData[i], knn_pred(tData[i], k, pData)))


    print(f"Prediction data: {pData} \n")
    print(f"Testing Data: {tData} \n")
    print(f"Testing Result: {knnLabels} \n\n")

    print(len(labels))
    if len(labels) < 4:
        kplot2d.plot_neighbors(pData, tData, knnLabels)

    vals = []
    for lab in labels[:-1]:
        vals.append(int(input(f"Enter a {lab}:")))

    print(f"Values: {vals}")
    print(knn_pred(vals, k, pData))