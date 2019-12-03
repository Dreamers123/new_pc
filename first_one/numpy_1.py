import numpy as np
from sklearn.model_selection import train_test_split

a, b = np.arange(10).reshape((5, 2)), range(5)
#print(train_test_split(a, b,random_state=42))
#np.sum((inches > 0.5) & (inches < 1))

x = np.array([1, 2, 3])
y = np.array([3, 2, 1])
#print(np.concatenate([x, y]).reshape(3,2))
L = np.random.random(100)
# print(L)
# print(sum(L))
rng = np.random.RandomState(2)
x = rng.randint(10, size=(3, 4))
#print(np.count_nonzero(x < 6))
#print(x)

###########Fancy Indexing##################
A= np.arange(12).reshape((3, 4))
row = np.array([0, 1, 2])
col = np.array([2, 1, 3])
#print(A[row, col],A[2, [2, 0, 1]])
####################################
c = np.arange(15)
i = np.array([2, 1, 8, 4])
c[i] = 99
c[i] -= 10
#print(c)
rand = np.random.RandomState(42)
X = rand.randint(0, 10, (4, 6))
X = rand.rand(10, 2)
import matplotlib.pyplot as plt
import seaborn; seaborn.set() # Plot styling
plt.scatter(X[:, 0], X[:, 1], s=100)
plt.show()













