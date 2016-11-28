import numpy as np
rng = np.random.RandomState(0)
n_samples_1 = 1000
n_samples_2 = 100
X = np.r_[1.5 * rng.randn(n_samples_1, 2),
          0.5 * rng.randn(n_samples_2, 2) + [2, 2]]
y = [0] * (n_samples_1) + [1] * (n_samples_2)
# # fit the model and get the separating hyperplane
from sklearn.svm import SVC
clf = SVC(kernel='linear', C=1.0)
clf.fit(X, y)

w = clf.coef_[0]
a = -w[0] / w[1]
xx = np.linspace(-5, 5)
yy = a * xx - clf.intercept_[0] / w[1]
# # get the separating hyperplane using weighted classes
wclf = SVC(kernel='linear', class_weight={0:1,1:10},
           probability=True)
wclf.fit(X, y)
ww = wclf.coef_[0]
wa = -ww[0] / ww[1]
wyy = wa * xx - wclf.intercept_[0] / ww[1]

# # plot separating hyperplanes and samples
from matplotlib import pyplot as plt
h0 = plt.plot(xx, yy, 'k-', label='no weights')
h1 = plt.plot(xx, wyy, 'k--', label='with weights')
# plt.scatter(X[:, 0], X[:, 1], c=y, cmap=plt.cm.Paired)
# plt.legend()
# plt.axis('tight')
# plt.show()
# print(wclf.predict_proba(X))

# from sklearn.metrics import classification_report
# from sklearn.datasets import load_breast_cancer
# data = load_breast_cancer()
# print(data.data.shape)

# classification_report(y_true, y_pred)