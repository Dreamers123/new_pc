import pandas as pd
import matplotlib.pyplot as plt
import numpy as np
import warnings
warnings.filterwarnings("ignore", category=FutureWarning)
from pandas.plotting import scatter_matrix
iris = pd.read_csv('iris.csv')
from sklearn.metrics import classification_report
from sklearn.metrics import confusion_matrix
from sklearn.metrics import accuracy_score
from sklearn.linear_model import LogisticRegression
from sklearn.tree import DecisionTreeClassifier
from sklearn.neighbors import KNeighborsClassifier
from sklearn.discriminant_analysis import LinearDiscriminantAnalysis
from sklearn.naive_bayes import GaussianNB
from sklearn.svm import SVC
from sklearn import model_selection

#print(df.groupby('species').size())
# plt.figure(figsize=(10, 7))
# x = iris["sepal_length"]
# plt.hist(x, bins=20, color="green")
# plt.title("Sepal Length in cm")
# plt.xlabel("Sepal_Length_cm")
# plt.ylabel("Count")
#iris.plot(kind='box',subplots=True,layout=(2,2),sharex=False,sharey=False)
#iris.hist()
scatter_matrix(iris)
models = []
models.append(('LR', LogisticRegression()))
models.append(('LDA', LinearDiscriminantAnalysis()))
models.append(('KNN', KNeighborsClassifier()))
models.append(('CART', DecisionTreeClassifier()))
models.append(('NB', GaussianNB()))
models.append(('SVM', SVC()))

# Spot Check Algorithms

array = iris.values
X = array[:,0:4]
Y = array[:,4]
validation_size = 0.30
seed = 7
X_train, X_validation, Y_train, Y_validation = model_selection.train_test_split(X, Y, test_size=validation_size, random_state=seed)
# Test options and evaluation metric
seed = 7
scoring = 'accuracy'
# evaluate each model in turn
results = []
names = []
for name, model in models:
    kfold = model_selection.KFold(n_splits=10, random_state=seed)
    cv_results = model_selection.cross_val_score(model, X_train, Y_train, cv=kfold, scoring=scoring)
    results.append(cv_results)
    names.append(name)
    msg =(name, cv_results.mean(), cv_results.std())
    #print(msg)
#plt.show()
knn = KNeighborsClassifier()
knn.fit(X_train, Y_train)
predictions = knn.predict(X_validation)
#print(predictions)
# print(accuracy_score(Y_validation, predictions))
print(confusion_matrix(Y_validation, predictions))
# print(classification_report(Y_validation, predictions))