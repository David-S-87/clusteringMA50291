# Even_Clustering.py

from my_clustering_package import (
    generate_and_combine_clusters, 
    get_even_clusters, 
    plot_clusters_and_histogram) 


if __name__ == "__main__":
    n = 1000
    new_random_plots = 500
    total_points = n + new_random_plots
    k = 10

    cluster_size = total_points / k  # Ensure size is an integer

    X_combined = generate_and_combine_clusters(n, k, new_random_plots)
    
    clusters = get_even_clusters(X_combined, cluster_size)
    plot_clusters_and_histogram(X_combined, clusters)

