import numpy as np
x = np.array([1, 2, 3])
y = np.array([3, 2, 1])
print(np.concatenate([x, y]).reshape(3,2))
