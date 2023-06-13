import pandas as pd
import matplotlib.pyplot as plt
from sklearn.cluster import KMeans
from sklearn.preprocessing import MinMaxScaler
import random
from sklearn.datasets import make_blobs

cluster_count = random.randint(5, 15)
print("Original Cluster Count: {}".format(cluster_count))

# In machine learning, the input features are usually called "X" and the output labels are called "y"
# Note that X may have many dimensions... it is not the same as the x-axis (a single dimension)

plt.figure(figsize=(7,7))
(X, y) = make_blobs(n_samples=500, n_features=2, cluster_std=0.6, centers=cluster_count)
plt.scatter(X[:,0], X[:,1], c=y)
plt.show()
# TALLMAN CODE ^^^^^^
# MY CODE below

#For all Weighted Sums of Squared Errors (WSSE's) of all data points for each cluster is calculated and added to a List
i = 1
wsses = []
for i in range(i, cluster_count + 1, 1):
    km = KMeans(n_clusters=i, max_iter=10)
    km.fit(X)
    wsse = km.inertia_
    wsses.append(wsse)

#The Graph of Errors and Iterations is graphed so we can check if the correct number of iterations was found
plt.plot(wsses)
plt.show()

#Finding the proper k value
i=2 #Essentially cutting off the last and first two data points as they are in the extremes and will never be the correct k value and will not run into an error because the minimum cluster size that is generated is 5. Not the best solution but the best me and Hunter could come up with.
for i in range(i, len(wsses)-1, 1):
    a1 = wsses[i - 1] - wsses[i]
    b1 = wsses[i] - wsses[i + 1]
    if (a1) > 2*(b1):
        cluster_count = i
        break

print(cluster_count)

