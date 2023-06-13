from math import sqrt
import random
import matplotlib.pyplot as plt


def EuclidDist(point1, point2):

    distance = 0
    sum_of_dimensions = 0
    for idx in range(len(point1)):
        sum_of_dimensions += (point1[idx]-point2[idx])**2
    distance = sqrt(sum_of_dimensions)
    
    return distance


def FindClosestCentroid(point, centroid_list):
    
    # Create a list of distances to each of the different centroids
    distance_to_centroid = []
    for cluster_index in range(len(centroid_list)):
        distance = EuclidDist(point, centroid_list[cluster_index])
        distance_to_centroid.append(distance)
        
    # Which centroid is closest? Get its index
    min_distance = min(distance_to_centroid)
    closest_indx = distance_to_centroid.index(min_distance)
    min_centroid = centroid_list[closest_indx]
    #print("Point {} is closest to centroid #{} which is at location {}".format(point, closest_indx+1, min_centroid))
    
    return closest_indx


def InitEmptyClusters(k):
    clusters = []
    for i in range(k):
        clusters.append([])
    return clusters


def AssignItemsToClosestCluster(data_list, centroid_list):
    
    # k should be the same as len(centroids)
    cluster_list = InitEmptyClusters(len(centroid_list))
        
    # Step through each of the items and calculate its closest centroid
    for key, data_point in data_list.items():

        # Add this item's key to the cluster whose centroid is closest...
        # ...this works because the 'centroid_list', 'distance_to_centroid', and 'cluster_list' are parallel
        closest_indx = FindClosestCentroid(data_point, centroid_list)
        cluster_list[closest_indx].append(key)
    
    return cluster_list
    
def ChooseRandomCentroids(data, k):
    
    centroids = [] # our k centroids will go in here
    used_keys = []
    
    # Keep looping until we have k number of centroids
    while len(centroids) < k:
        
        # Choose a random key from the data AND MAKE SURE IT'S A UNIQUE CHOICE
        key = random.choice(list(data.keys()))
        if key not in used_keys:
            print(" Randomly chose {} {} as initial centroid".format(key, data[key]))
            centroids.append(data[key])
            used_keys.append(key)
        
    return centroids
    
def CaclulateCentroidLocation(data, cluster, dimension_count):
    
    # Initialize this centroid to be all zeros    
    # We typically use a tuple to store the coordinates of each centroid
    # But we use a list in this case because list are mutable
    # We'll convert it from the list back to a tuple later on
    # Most of our data will be two-dimensional (x- and y-coordinates)
    centroid = [0] * dimension_count
    centroid = [0,0]
    print(cluster)
    
    # Avoiding empty clusters that would cause a divide-by-zero error
    if len(cluster) > 0:

        # Go through the x-dimension and then y-dimension
        # The code can handle more dimensions, if necesary
        for idx in range(dimension_count):
            
            # Sum all of x-coordinates in this cluster (or y-coordinates)
            # Then divide by the number of datapoints in the cluster to get the average
            centroid[idx] = sum(data[cluster[i]][idx] for i in range(len(cluster)))  # SUM OF ALL POINTS[idx]
            centroid[idx] /= len(cluster)  # Divide centroid[idx] by the # of points
            
    return tuple(centroid)
    
def UpdateCentroidsKMeans(data, cluster_list):

    # Determine how many dimensions our data has (it will be 2-D for simple problems)
    artibrary_cluster = cluster_list[0]
    arbitrary_key = artibrary_cluster[0]
    dimension_count = len(data[arbitrary_key])

    centroid_list = []

    # CALCULATES A NEW CENTROID FOR EVERY ONE OF THE CLUSTERS
    for cluster in cluster_list:
        centroid_list.append(CaclulateCentroidLocation(data,cluster,dimension_count))

    return centroid_list
    
def PlotClusters2D(data, cluster_list, centroid_list, color_list, x_label=None, y_label=None, inches=5):

    plt.figure(figsize=(inches, inches))

    data_x = [data[key][0] for cluster in cluster_list for key in cluster] # index 0 of student's grade
    data_y = [data[key][1] for cluster in cluster_list for key in cluster] # index 1 of student's grade
    data_c = [color_list[i] for i, cluster in enumerate(cluster_list) for key in cluster] # cluster_list, centroid_list, and color_list are parallel
    #data_c = []
    #for i in range(len(cluster_list)):
    #    for key in cluster_list[i]:
    #        data_c.append(color_list[i])
            
    plt.scatter(data_x, data_y, c=data_c) 

    centroids_x = [centroid[0] for centroid in centroid_list]
    centroids_y = [centroid[1] for centroid in centroid_list]
    centroids_c = color_list
    plt.scatter(centroids_x, centroids_y, c=color_list, s=[1000, 1000, 1000], alpha=0.3)    

    plt.xlabel(x_label, fontsize=16, labelpad=15)
    plt.ylabel(y_label, fontsize=16, labelpad=15)

    plt.show()
    return
    
def CreateKMeansClusters(k, data, colors, x_label=None, y_label=None, max_passes=10, show_debug=True):

    # These two variables help us know when to finish the algorithm
    stable_clusters = False
    pass_count = 0
    
    # Choose our initial centroids
    prev_centroids = ChooseRandomCentroids(data, k)
    
    # Loop until the clusters are stable or we exceed the number of rounds
    while stable_clusters == False and pass_count < max_passes:
    
        # Run a single round of the algorithm
        clusters = AssignItemsToClosestCluster(data, prev_centroids)
        centroids = UpdateCentroidsKMeans(data, clusters)

        # Plot the results
        if show_debug:
            PlotClusters2D(data, clusters, centroids, colors, x_label, y_label)

        # Check for stability and update variables
        if prev_centroids == centroids:
            stable_clusters = True
        prev_centroids = centroids
        pass_count += 1
        
        
        
    return (centroids, clusters)

student_grades = {"Alice":(93, 88), "Bob":(55, 55), "Charles":(90, 87), "Dave":(63,57), "Ellen":(89,88), 
                  "Frita":(90,91), "Grant":(70,86), "Heidi":(98,96), "Isabelle":(77,87), "Jack":(80,94), 
                  "Kate":(60,86), "Lisa":(85,86), "Mary":(90,89), "Nancy":(63,58), "Orville":(88,61),
                  "Peter":(95,58), "Quinton":(83,89), "Ralph":(57,65), "Sally":(67,65), "Trent":(62,62),
                  "Ursala":(65,53), "Violet":(82,90), "Wally":(91,93), "Xavier":(81, 84), "Yolanda":(90, 63),
                  "Zack":(85,56)}

colors = ["royalblue", "forestgreen", "maroon"]
CreateKMeansClusters(3, student_grades, colors, "Homework Scores", "Final Exam Scores")