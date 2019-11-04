import pandas as pd
import matplotlib.pyplot as plt
import numpy as np
df = pd.read_csv('iris.csv')
y = df.iloc[0:100, 4].values
#print(y)
#print(df.head())
y = np.where(y == 'Iris-setosa', -1, 1)
print(y)
X = df.iloc[0:100, [0, 2]].values
#print(X)
plt.scatter(X[:50, 0], X[:50, 1],color='red', marker='o', label='setosa')
plt.scatter(X[50:100, 0], X[50:100, 1],color='blue', marker='x', label='versicolor')
plt.xlabel('petal length')
plt.ylabel('sepal length')
plt.legend(loc='upper left')
plt.show()