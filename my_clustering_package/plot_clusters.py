# plot_clusters.py
import numpy as np
import matplotlib.pyplot as plt


def plot_clusters_and_histogram(X, clusters):
    fig, (ax1, ax2) = plt.subplots(1, 2, figsize=(12, 6))

    scatter = ax1.scatter(X[:, 0], X[:, 1], c=clusters, s=5)
    ax1.set_title("Clustered Data Points")

    unique_clusters, counts = np.unique(clusters, return_counts=True)
    colors = [scatter.cmap(scatter.norm(cluster)) for cluster in unique_clusters]
    ax2.bar(unique_clusters, counts, color=colors)
    ax2.set_title("Cluster Sizes")
    ax2.set_xlabel("Cluster")
    ax2.set_ylabel("Number of Points")
    ax2.set_xticks(unique_clusters)

    # Display the size of each cluster below the plot
    for i, count in enumerate(counts):
        ax2.text(unique_clusters[i], count, str(count), ha='center', va='bottom')
    # Display the total number of points below the graph
    total_points = len(X)
    plt.figtext(0.5, 0.01, f'Total number of points: {total_points}', ha='center', fontsize=12)
    plt.tight_layout()
    plt.show()