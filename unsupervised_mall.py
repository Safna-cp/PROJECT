import pandas as pd
from sklearn.cluster import KMeans
import matplotlib.pyplot as plt
import seaborn as sns   
import numpy as np

customer_data = pd.read_csv(r"Mall_Customers.csv",encoding='latin1')
print(customer_data.head())

print(customer_data.isnull().sum())

X = customer_data.iloc[:, [3, 4]].values #annual income and spending score
print(X)

wcss=[]  # within cluster sum of squares(to find optimal number of clusters)
for i in range(1,11):
    kmeans=KMeans(n_clusters=i,init='k-means++',random_state=42)
    kmeans.fit(X)
    wcss.append(kmeans.inertia_)

# Plotting the results onto a line graph, allowing us to observe 'The elbow'
sns.set()
plt.plot(range(1,11),wcss)
plt.title('The Elbow Method')   
plt.xlabel('Number of clusters')
plt.ylabel('WCSS')
plt.show()

##This array y contains cluster labels assigned by KMeans to each data point in your dataset.
# For example, if y[0] is 3, it means the first data point belongs to cluster 3.
# If y[10] is 4, the 11th point belongs to cluster 4, and so on.

clusters = 5
kmeans = KMeans(n_clusters=i, init='k-means++', random_state=0)   
y = kmeans.fit_predict(X)
print(y)

clusters = 0,1,2,3,4

plt.figure(figsize=(8, 8)) #Creates a square figure of size 8x8 inches.
#X is your dataset (likely 2D features, for example Annual Income and Spending Score).
#y is the array of cluster labels you got from KMeans (y == 0 means points in cluster 0, etc.).
plt.scatter(X[y == 0, 0], X[y == 0, 1], s = 100, c = 'red', label = 'Cluster 1')   # Marker size s=100 for visibility.
plt.scatter(X[y == 1, 0], X[y == 1, 1], s = 100, c = 'blue', label = 'Cluster 2')
plt.scatter(X[y == 2, 0], X[y == 2, 1], s = 100, c = 'green', label = 'Cluster 3')
plt.scatter(X[y == 3, 0], X[y == 3, 1 ], s = 100, c = 'cyan', label = 'Cluster 4')
plt.scatter(X[y == 4, 0], X[y == 4, 1 ], s = 100, c = 'magenta', label = 'Cluster 5')


# Plotting the centroids of the clusters
#It plots these centroids as big yellow dots (s=300 makes them larger).
#These show the “center points” of each cluster on the graph.
#kmeans.cluster_centers_ gives the coordinates of the cluster centers found by KMeans.
plt.scatter(kmeans.cluster_centers_[:, 0], kmeans.cluster_centers_[:, 1], s = 300, c = 'yellow', label = 'Centroids')
plt.title('Clusters of customers')
plt.xlabel('Annual Income (k$)')
plt.ylabel('Spending Score (1-100)')
plt.legend()    
plt.show()