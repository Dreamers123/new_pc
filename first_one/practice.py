import numpy as np
import pprint
import matplotlib.pyplot as plt
x = np.array([1, 2, 3, 4, 5])
y = np.array([4, 2, 1, 3, 7])
#plt.scatter(x, y);
#plt.show()
from sklearn.linear_model import LinearRegression
X = x[:, np.newaxis]
model = LinearRegression().fit(X, y)
yfit = model.predict(X)
# plt.scatter(x, y)
# plt.plot(x, yfit);
# plt.show()

