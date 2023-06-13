import math
import random
import statistics
from numpy import float64
import pandas as pd
import os

# ----------------------------------------------------------------------------------------------------
# Helper Functions
# ----------------------------------------------------------------------------------------------------


def _pretty_print(*info, title: str = ""):
    """
    Helper func for printing debug info to the terminal thats easier on the eyes.

    Args:
        info: Info to have formatting wrapped around.
        info: Optional param for giving a title before printing.

    Returns:
        None
    """

    term_size = os.get_terminal_size()
    if title:
        print("\n" + title.center(term_size.columns))
    print("="*term_size.columns)
    print(info)
    print("="*term_size.columns)


def _get_euclidean_distance(point1: list, point2: list) -> float:
    """
    Helper func for calculating Euclidean between given points.

    Args:
        point1: First point to use in formula
        point2: Second point to use in formula

    Returns:
        Returns distance between the two points
    """

    # Euclidean distance Formula: https://www.cuemath.com/euclidean-distance-formula/
    sum = 0.0
    for i, _ in enumerate(point1):
        sum += (point1[i] - point2[i])**2
    
    return math.sqrt(sum)


def _generate_random_centroids(data, k):
    """
    Helper Func for generating a list of random centroids of length k
    to use

    Args:
        data:         Dataset to work off on
        k:            Amount of centroids to create 

    Returns:
        Returns a list of centroids to use for Kmeans
    """
    centroids = []
    # Store the indexes of centroids used to prevent from repeats occuring
    previous_centroids_indexes = []

    # Until we make a list that meets our specified length of k,
    # Pick random indexes, make sure they were not used, and then
    # add them for our centroid testing
    while len(centroids) < k:
        datapoint_index = data.index(random.choice(data))
        if datapoint_index not in previous_centroids_indexes:
            centroids.append(data[datapoint_index])
            previous_centroids_indexes.append(datapoint_index)
    return centroids


def _generate_clusters(data: list, centroids: list) -> list:
    """
    Helper Func to define new clusters based off given centroids

    Args:
        data:         dataset to generate clusters from 
        centroids:    Centroids to group clusters off of 
    Returns:
        Gives a 2d list of clusters generated from calculations    
    """
    clusters = [[] for i in range(len(centroids))]
    # Go through each datapoint and see the distance to each
    # centroid, whichever is closest, assign to relevant cluster
    for _, datapoint in enumerate(data):
        distances = []
        for _, centroid in enumerate(centroids):
            # Calculate distances and store the in a list
            distances.append(_get_euclidean_distance(datapoint, centroid))

        # Get the index of the centroid and then put the datapoint
        # inside the cluster of the same index
        shortest_centroid_index = distances.index(min(distances))
        for i, _ in enumerate(clusters):
            if i == shortest_centroid_index:
                clusters[shortest_centroid_index].append(datapoint)
    return clusters


def _generate_centroids(data: list, clusters: list) -> list:
    """
    Helper Func to define new centroids based off current Clusters

    Args:
        Clusters:    2d list of clusters that are used to get centroids 
    Returns:
        Gives a list of tuples that contains new centroids 
    """
    #Generally will only have 2d x and y to worry about, but you never know
    graph_dimension = len(data[0])

    centroids = [] 

    for cluster in clusters:
        centroid = []
        dim_sum = 0.0
        for dim in range(graph_dimension):
            #Get the mean of our current dimension
            for i, datapoint in enumerate(cluster):
                dim_sum += cluster[i][dim]
            dim_sum = dim_sum / len(cluster)

            centroid.append(dim_sum)
        #Keeping our data a tuple, so wrap centroid from list to tuple before appending
        centroids.append(tuple(centroid))

        
            

    return centroids
    

def run_kmeans_algorithm(data: list, k, debug: bool = False):
    """
    Naive k-means cluster algorithm that takes in pre-defined k and 
    generates clusters off amount of given k-means desired

    Args:
        data:     Dataset to calculate clusters and centroids off of
        k:        The amount of centroids to generate
        debug:    optional flag for printing calculations to terminal

    Returns:
        Tuple of Centroids and Clusters calculated from dataset and given k
     """
    # 1. Create Random Initial k-mean
    previous_centroids = _generate_random_centroids(data, k)
    #_pretty_print(previous_centroids, title="Randomized Centroids")

    # Loop to run centroid and cluster calculations
    loop_count = 0
    is_stabelized = False
    while is_stabelized == False and loop_count < 10:
        # 2. Cluster all datapoints to nearest k-mean
        clusters = _generate_clusters(data, previous_centroids)
        if debug:
            for i, _ in enumerate(clusters):
                _pretty_print(clusters[i], title=f"Cluster {i} with Centroids {previous_centroids}")

        # 3. Relocate centroid based off new cluster
        new_centroids = _generate_centroids(data, clusters)

        if new_centroids == previous_centroids:
            return (new_centroids, clusters)
        previous_centroids = new_centroids

        loop_count += 1


# ----------------------------------------------------------------------------------------------------
# A debuged version of the run_kmeans_algorithm with debug prints
# ----------------------------------------------------------------------------------------------------
if __name__ == '__main__':

    # Put CSV data into a Panda Dataframe, then convert Specified Columns to Tuples
    geyser_df = pd.read_csv('old_faithful_geyser.csv')
    list_of_column_names = ["Eruption time", "Waiting time"]
    geyser_tuples = list(
        map(tuple, geyser_df[list_of_column_names].to_records(index=False)))
    #_pretty_print(geyser_tuples, title="Raw Geyser Data")

    # Using k size of 2 for this project
    k = 2
    run_kmeans_algorithm(geyser_tuples, k, debug=True)
