import numpy as np
import random

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
            return self.linearKernel(x, z)
        elif self.kernel == 'poly':
            return self.polyKernel(x, z)
        elif self.kernel == 'rbf':     #K(x,z)=exp(− gamma*|x−z|**2)
            return self.GaussianKernel(x, z)
        else:
            print("kernel error")

    def train(self, X, y):
        X = np.array(X)
        y = np.array(y)
        self.alpha = np.zeros(len(y))
        count = 0
        while count < 5:
            alpha_change = 0
            for i in self.alpha:
                Ei = np.sum(np.dot(self.alpha*y[i],self._kernel(X,X[i])))-b
                if():
                    j = random.randint(0,len(self.alpha))
                    while i == j:
                        j = random.randint(0, len(self.alpha))
                        
                alpha_change += 1

    def predict(X):
        pass

    def evaluate(X, y):
        pass

    def linearKernel(x, z):
        return np.dot(x, z)

    def polyKernel(x, z):
        return np.power(np.dot(x, z.T + 1.0), 2)

    def GaussianKernel(x, z):
        xx = np.sum(x * x, axis=1)
        zz = np.sum(z * z, axis=1)
        res = - 2.0 * np.dot(x, z.T) + \
        xx.reshape(-1, 1) + \
        zz.reshape(1, -1)
        return np.exp(-self.gamma * res) # 0< gamma < 1