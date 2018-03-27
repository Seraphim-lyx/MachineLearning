import numpy as np 
gamma = 0.02
x = np.array([[1,2],[3,4],[5,6]])
z = x
xx = np.sum(x * x, axis=1)
zz = np.sum(z * z, axis=1)
res = - 2.0 * np.dot(x, z.T) + \
xx.reshape(-1, 1) + \
zz.reshape(1, -1)
k = np.exp(-gamma * res)

