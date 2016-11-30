from sklearn.datasets import load_iris
from sklearn.cluster import KMeans
data=load_iris()
X=data.data
y=data.target
cl=KMeans(3)
cl.fit(X)
print(cl.cluster_centers_)
print(cl.inertia_)
print(cl.labels_)
print(y)
from sklearn.metrics import adjusted_mutual_info_score
print(adjusted_mutual_info_score(y,cl.labels_))

