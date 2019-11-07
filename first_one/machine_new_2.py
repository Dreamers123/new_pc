import mglearn
from sklearn.model_selection import train_test_split
X, y = mglearn.datasets.make_forge()
# print(X)
# print(y)
X_train, X_test, y_train, y_test = train_test_split(X, y, random_state=0)
from sklearn.neighbors import KNeighborsClassifier
clf = KNeighborsClassifier(n_neighbors=3)
clf.fit(X_train, y_train)
print("Test set predictions: {}".format(clf.predict(X_test)))
print("Another predict",clf.predict([[11,3.3389402]]))