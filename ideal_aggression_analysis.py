import pandas as pd
import numpy as np
import random
import matplotlib.pyplot as plt

random.seed(10)
team_id = 8203 # wait to be replaced by real data
data = pd.read_csv("CLEANED1_european_soccer_dataset-MATCH.csv") # wait to be replaced by real data


#fake data
data['home_team_aggression']=np.random.randint(20,100,len(data))
data['away_team_aggression']=np.random.randint(30,100,len(data))

plt.hist(data['home_team_aggression'], bins=30, color='blue')
plt.show()

#separate if the opponents loss in the home game or away game
home_team = [[data['home_team_aggression'][i],data['away_team_aggression'][i]]for i in range(len(data)) if data['home_team_api_id'][i] == team_id and data['home_team_goal'][i]<data['away_team_goal'][i]]
away_team = [[data['away_team_aggression'][i],data['home_team_aggression'][i]]for i in range(len(data)) if data['away_team_api_id'][i] == team_id and data['away_team_goal'][i]<data['home_team_goal'][i]]



X_home_team = np.array(home_team)
X_away_team = np.array(away_team)
weights_home_test = np.array([random.uniform(1, 5) for i in range(len(X_home_team))])
weights_away_test = np.array([random.uniform(1, 5) for i in range(len(X_away_team))])


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




k_test = 1

labels, centroids = weighted_kmeans(X_home_team, k_test, weights_home_test)

print(centroids)