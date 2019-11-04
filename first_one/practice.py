from scipy import sparse
import numpy as np
import matplotlib.pyplot as plt
from sklearn.datasets import load_breast_cancer
cancer = load_breast_cancer()
print("cancer.keys(): \n{}".format(cancer.keys()))
print(cancer.feature_names)
print(cancer.data[0])
print("Sample counts per class:\n{}"
      .format({n: v for n, v in
               zip(cancer.target_names, np.bincount(cancer.target))}))
# # Create a 2D NumPy array with a diagonal of ones, and zeros everywhere else
# eye = np.eye(4)
# #print("NumPy array:\n{}".format(eye))
# import matplotlib.pyplot as plt
# # Generate a sequence of numbers from -10 to 10 with 100 steps in between
# x = np.linspace(-10, 10, 100)
# # Create a second array using sine
# y = np.cos(x)
# # The plot function makes a line chart of one array against another
# plt.plot(x, y, marker="x")
# #plt.show()
# import pandas as pd
# from IPython.display import display
# # create a simple dataset of people
# data = {'Name': ["John", "Anna", "Peter", "Linda"],
#  'Location' : ["New York", "Paris", "Berlin", "London"],
#  'Age' : [24, 13, 53, 33]
#  }
# data_pandas = pd.DataFrame(data)
# # IPython.display allows "pretty printing" of dataframes
# # in the Jupyter notebook
# display(data_pandas[data_pandas.Age > 30])
#
# import sys
# print("Python version: {}".format(sys.version))
# import pandas as pd
# print("pandas version: {}".format(pd.__version__))
# import matplotlib
# print("matplotlib version: {}".format(matplotlib.__version__))
# import numpy as np
# print("NumPy version: {}".format(np.__version__))
# import scipy as sp
# print("SciPy version: {}".format(sp.__version__))
# import IPython
# print("IPython version: {}".format(IPython.__version__))
# import sklearn
# print("scikit-learn version: {}".format(sklearn.__version__))
# X, y = mglearn.datasets.make_forge()
# # plot dataset
# mglearn.discrete_scatter(X[:, 0], X[:, 1], y)
# plt.legend(["Class 0", "Class 1"], loc=4)
# plt.xlabel("First feature")
# plt.ylabel("Second feature")
# plt.show()
# print("X.shape: {}".format(X.shape))
# from collections import Counter
#
# # Create a list
# z = ['blue', 'red', 'blue', 'yellow', 'blue', 'red']
# col_count = Counter(z)
# print(col_count)
#
# col = ['blue', 'red', 'yellow', 'green']
#
# # Here green is not in col_count
# # so count of green will be zero
# for color in col:
#     print(color, col_count[color])

