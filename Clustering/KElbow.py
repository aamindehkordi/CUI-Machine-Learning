import sklearn.cluster._kmeans as KMeans


def kElbow(X: list, cluster_count: int):
    # CALCULATE WSSE FOR A RANGE OF POSSIBLE K-VALUES
    i = 1
    wsses = []
    for i in range(i, cluster_count + 1, 1):
        km = KMeans(n_clusters=i, max_iter=10)
        km.fit(X)
        wsse = km.inertia_
        wsses.append(wsse)

    return wsses
