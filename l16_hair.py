import pandas as pd
from sklearn.decomposition import PCA
from sklearn.cluster import KMeans
df1=pd.read_csv('Hair_6th_data.csv',';')
data=df1.ix[:,:6].join(df1.ix[:,-18::2])
col1=data.X1
print('print 3', col1)
k=2
cl=KMeans(k)
cl.fit(data)
y_pred=cl.labels_
print(y_pred)

pca = PCA(n_components=2)
X=pca.fit_transform(data)
#print(X)

import matplotlib.pyplot as plt
plt.scatter(X[:, 0], X[:, 1], c=y_pred)
plt.show()
