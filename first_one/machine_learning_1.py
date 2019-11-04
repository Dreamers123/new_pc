import seaborn as sns
import matplotlib.pyplot as plt
iris = sns.load_dataset('iris')
# #print(iris.head())
# sns.set()
# sns.pairplot(iris, hue='species', size=1.5)
# plt.show()
from sklearn.model_selection import train_test_split
from sklearn.metrics import accuracy_score

X_iris = iris.drop('species', axis=1)
y_iris = iris['species']
Xtrain, Xtest, ytrain, ytest = train_test_split(X_iris, y_iris,random_state=1)
from sklearn.naive_bayes import GaussianNB # 1. choose model class
model = GaussianNB() # 2. instantiate model
model.fit(Xtrain, ytrain) # 3. fit model to data
from sklearn.decomposition import PCA # 1. Choose the model class
model = PCA(n_components=2) # 2. Instantiate the model with hyperparameters
model.fit(Xtrain,ytrain) # 3. Fit to data. Notice y is not specified!
X_2D = model.transform(X_iris)
iris['PCA1'] = X_2D[:, 0]
iris['PCA2'] = X_2D[:, 1]
sns.lmplot("PCA1", "PCA2", hue='species', data=iris, fit_reg=False);
plt.show()
# y_model = model.predict([[6.9,3.2,4.7,0]])
# print(y_model)
# print(accuracy_score(ytest, y_model))