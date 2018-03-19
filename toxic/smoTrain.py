import numpy as np


class smoTrain(object):
    """docstring for smoTrain"""

    def __init__(self, kernel, degree=2, C, gamma=None, tol=1e-4):
        self.kernel = kenel
        self.gamma = gamma
        self.C = C
        self.tol = tol
        self.degree = degree

    def _kernel(self, x, z=None):
        if z is None:
            z = np.copy(x)
        if self.kernel == 'linear':
            return np.dot(x, z)
        elif self.kernel == 'poly':
            return np.power(np.dot(x, z.T + 1.0), 2)
        elif self.kernel == 'rbf':
            xx = np.sum(x * x, axis=1)
            zz = np.sum(z * z, axis=1)
            res = - 2.0 * np.dot(x, z.T) + \
                xx.reshape(-1, 1) + \
                zz.reshape(1, -1)
            return np.exp(-self.gamma * res)
        else:
            print("kernel error")

    def train(self, X, y):
        X = np.array(X)
        y = np.array(y)
