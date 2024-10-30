# get_clusters.py
import numpy as np
from sklearn.cluster import KMeans
from scipy.spatial.distance import cdist
from scipy.optimize import linear_sum_assignment

def get_even_clusters(X, cluster_size):
    n_clusters = int(np.ceil(len(X) / cluster_size))
    kmeans = KMeans(n_clusters=n_clusters)
    kmeans.fit(X)
    centers = kmeans.cluster_centers_
    centers = np.repeat(centers, cluster_size, axis=0)
    distance_matrix = cdist(X, centers)
    clusters = linear_sum_assignment(distance_matrix)[1] // cluster_size
    return clusters
