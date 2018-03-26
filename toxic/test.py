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
# print(k[0])
alpha = np.array([2,2,3])
# y = np.array([1,1,2])
x = np.array([[1,2,4,4,4],[2,3,5,5,5],[3,4,5,5,5]])
# print(alpha * y * x)
print(np.dot(alpha, x))
# print(np.dot(a,b.T))
# print(hex(65))
