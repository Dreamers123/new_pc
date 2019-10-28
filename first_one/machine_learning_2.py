from sklearn.datasets import load_digits
# import matplotlib.pyplot as plt
# digits = load_digits()
# print(digits.images.shape)
# import matplotlib.pyplot as plt
# fig, axes = plt.subplots(10, 10, figsize=(8, 8),
# subplot_kw={'xticks':[], 'yticks':[]},
# gridspec_kw=dict(hspace=0.1, wspace=0.1))
# for i, ax in enumerate(axes.flat):
#  ax.imshow(digits.images[i], cmap='binary', interpolation='nearest')
#  ax.text(0.05, 0.05, str(digits.target[i]),transform=ax.transAxes, color='green')
# plt.show()
import seaborn as sns
from sklearn.neighbors import KNeighborsClassifier
from sklearn.metrics import accuracy_score
from sklearn.datasets import load_iris
model = KNeighborsClassifier(n_neighbors=1)
iris = load_iris()
X = iris.data
y = iris.target
#print(X,y)
from sklearn.model_selection import cross_val_score
print(cross_val_score(model, X, y, cv=5))

from sklearn.model_selection import train_test_split

X1, X2, y1, y2 = train_test_split(X, y, random_state=0,train_size=0.5)
# fit the model on one set of data
model.fit(X1, y1)
# evaluate the model on the second set of data
y2_model = model.predict(X2)
#print(y2_model)
#print(accuracy_score(y2, y2_model))