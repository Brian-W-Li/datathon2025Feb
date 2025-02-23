import pandas as pd
import numpy as np
import random

random.seed(10)
data = pd.read_csv("CLEANED1_european_soccer_dataset-MATCH.csv") # wait to be replaced by real data
home_team=data['home_team_aggression']
away_team=data['away_team_aggression']

for i in range(len(combined_list)): #keep the data for matches that a specific team is losing
    if data['home_team_goal']>data['away_team_goal']:
        combined_list[i][0]=1


combined_list = [[x , y] for x, y in zip(home_team, away_team)]
X = np.array(combined_list)
#weights = np.array(data["newColumn"])  wait to be replaced by real data
weights_test=[random.uniform(1,5) for i in range(len(X))]

def weighted_kmeans(X, k, weights, max_iter=100, RNG=None):
    if RNG is not None:
        np.random.seed(RNG)

    n_samples, n_features = X.shape

    # Initialize centroids by randomly selecting k points
    initial_indices = np.random.choice(n_samples, k, replace=False)
    centroids = X[initial_indices, :]

    for _ in range(max_iter):
        # Assignment step: calculate distances to each centroid
        distances = np.sqrt(np.sum((X[:, np.newaxis, :] - centroids[np.newaxis, :, :]) ** 2, axis=2))
        labels = np.argmin(distances, axis=1)

        # Update step: calculate new centroids as weighted means
        for j in range(k):
            cluster_points = X[labels == j]
            cluster_weights = weights[labels == j]

            if np.sum(cluster_weights) == 0:  # Handle empty cluster or all zero weights
                centroids[j] = X[np.random.choice(n_samples)]
            else:
                # Calculate weighted mean manually
                numerator = np.sum(cluster_points * cluster_weights[:, np.newaxis], axis=0)
                denominator = np.sum(cluster_weights)
                centroids[j] = numerator / denominator

    return labels, centroids




X_test = np.array([[1.0, 2.0],
                   [1.5, 1.8],
                   [5.0, 8.0],
                   [8.0, 8.0],
                   [1.0, 0.6],
                   [9.0, 11.0]])


weights_test = np.array([1, 1, 1, 1, 1, 1])


k_test = 2

labels, centroids = weighted_kmeans(X_test, k_test, weights_test)

print(labels,centroids)