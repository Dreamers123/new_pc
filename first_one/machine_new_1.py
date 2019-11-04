from sklearn.datasets import load_iris
import pandas as pd
import numpy as np

from pandas.plotting import scatter_matrix
import matplotlib.pyplot as plt

iris_dataset = load_iris()
print("Keys of iris_dataset: \n{}".format(iris_dataset.keys()))
print(iris_dataset.feature_names)
from sklearn.model_selection import train_test_split
X_train, X_test, y_train, y_test = train_test_split(
 iris_dataset['data'], iris_dataset['target'], random_state=0)
# print("X_train shape: {}".format(X_train.shape))
# print("y_train shape: {}".format(y_train.shape))
# print("X_test shape: {}".format(X_test.shape))
# print("y_test shape: {}".format(y_test.shape))
iris_dataframe = pd.DataFrame(X_train, columns=iris_dataset.feature_names)
from sklearn.neighbors import KNeighborsClassifier
knn = KNeighborsClassifier(n_neighbors=1)
knn.fit(X_train, y_train)
X_new = np.array([[5, 2.9, 1, 7.2]])
print("X_new.shape: {}".format(X_new.shape))
prediction = knn.predict(X_new)
print("Prediction: {}".format(prediction))
print("Predicted target name: {}".format(iris_dataset['target_names'][prediction]))
y_pred = knn.predict(X_test)
print("Test set predictions:\n {}".format(y_pred))
print("Test set score: {:.2f}".format(np.mean(y_pred == y_test)))

# create a scatter matrix from the dataframe, color by y_train
# plt.plot(iris_dataset['data'],label="You know nothing,Abeer")
# plt.show()
# grr = scatter_matrix(iris_dataframe, c=y_train, figsize=(15, 15), marker='o',
#  hist_kwds={'bins': 20}, s=60, alpha=.8)
# tumy=pd.DataFrame(np.random.randint(1,100,size=24).reshape((3,8)),
#                   index=['a','b','c'],
#                   columns=['First','Second','Third','Fourth','Fifth','Sixth','Seventh','Eighth'])
# print(tumy)
# plt.plot(tumy,label="You know nothing,Abeer")
# #plt.legend()
# plt.show()

