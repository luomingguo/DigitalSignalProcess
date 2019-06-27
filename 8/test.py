import numpy as np

a = np.array([1,2,3])
b = np.array([[1,2],
              [3, 4]])
c = np.array([1,2,3])
d = np.zeros(1,3)[0]
x = np.hstack((a,c, d))
print(x)