from sklearn.datasets import load_iris
iris = load_iris()
X, y = iris.data, iris.target
from sklearn.svm import SVC
clf=SVC()
from sklearn.cross_validation import train_test_split
X_train,X_test,y_train,y_test= train_test_split(X,y, test_size=0.5)
clf.fit(X_train,y_train)
y_hat=clf.predict(X_test)
from sklearn.metrics import accuracy_score,classification_report
# print(accuracy_score(y_test, y_hat))
# print(classification_report(y_test, y_hat))

from sklearn.feature_selection import SelectKBest
selection = SelectKBest(k=2)
#print(selection.fit_transform(X,y))

from sklearn.decomposition import PCA
pca = PCA(n_components=4)
pca.fit(X)

from sklearn.pipeline import FeatureUnion
combined_features = FeatureUnion([("pca", pca),
        ("univ_select", selection)])
combined_features.fit(X, y)
X_features = combined_features.transform(X)

from sklearn.pipeline import Pipeline
pipeline = Pipeline([("features", combined_features),
                     ("clf", clf)])
param_grid = dict(features__pca__n_components=[1, 2, 3],
                  features__univ_select__k=[1, 2],
                  clf__C=[0.1, 1, 10])
from sklearn.grid_search import GridSearchCV
grid_search = GridSearchCV(pipeline, param_grid=param_grid,
                           verbose=10)
grid_search.fit(X, y)
print(grid_search.best_estimator_)
#
# # print(X_features)