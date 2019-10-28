
import matplotlib.pyplot as plt
import seaborn as sns; sns.set()
import numpy as np
from sklearn.linear_model import LinearRegression
model = LinearRegression(fit_intercept=True)
rng = np.random.RandomState(1)
x = 10 * rng.rand(50)
y = 2 * x - 5 + rng.randn(50)
model.fit(x[:, np.newaxis],y)
#predict=model.predict([x[:, np.newaxis]][0])
xfit = np.linspace(0, 10, 1000)
yfit = model.predict(xfit[:, np.newaxis])
print(yfit)
plt.scatter(x, y)
plt.scatter(xfit, yfit)
plt.show()