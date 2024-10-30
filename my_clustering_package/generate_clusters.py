# generate_clusters.py
import numpy as np
from sklearn.datasets import make_blobs


def generate_and_combine_clusters(n, k, num_points, scale=25):
    random_state = np.random.randint(0, 1000)
    if n > 0:
        X, _ = make_blobs(n_samples=n, centers=k, n_features=2, random_state=random_state)
    else:
        X = np.empty((0, 2))
    X_new = np.random.uniform(-scale / 2, scale / 2, size=(num_points, 2))
    return np.concatenate((X, X_new), axis=0)

