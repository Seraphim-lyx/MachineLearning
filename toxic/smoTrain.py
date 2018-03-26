import numpy as np
import random
import scipy.io as sio

class smoTrain(object):
    """docstring for smoTrain"""

    def __init__(self, kernel='linear', degree=2, C=0.1, gamma=None, tol=1e-3):
        self.kernel = kernel
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
        # X = np.array(X)
        # y = np.array(y)
        self.X = X
        self.y = y
        k = self._kernel(X)
        self.alpha = np.zeros(len(y))
        self. b = 0.0
        count = 0
        while count < 5: 
            print(count)
            alpha_change = 0  
            for i in range(len(self.alpha)):
                #Calculating error for i
                Ei = self.b + np.sum(self.alpha * y * k[i])-y[i]
                if((Ei*y[i] < - self.tol) and (self.alpha[i] < self.C)) or \
                  ((Ei*y[i] > self.tol) and (self.alpha[i] > 0)):
                    print('inside')
                    j = random.randint(0,len(self.alpha)-1)
                    while i == j:
                        j = random.randint(0, len(self.alpha)-1)
                    #Calculating error for j    
                    Ej = self.b + np.sum(self.alpha * y * k[j])-y[j]

                    ai = self.alpha[i] #old alpha i
                    aj = self.alpha[j] #old alpha j

                    #calculating bounding area for alpha
                    if y[i] == y[j]:
                        L = max(0, self.alpha[j] + self.alpha[i] - self.C)
                        H = min(self.C, self.alpha[j] + self.alpha[i])
                    else:
                        L = max(0, self.alpha[j] - self.alpha[i])
                        H = min(self.C, self.C + self.alpha[j] - self.alpha[i])

                    if L == H:
                        #next iteration if no area
                        print("L==H")
                        continue

                    eta = 2 * k[i, j] - k[i, i] - k[j, j]
                    if eta >= 0:
                        print("eta out")
                        continue

                    #clip new value
                    self.alpha[j] = aj - y[j] * (Ei-Ej) / eta

                    #bound new value
                    self.alpha[j] = min(H, self.alpha[j])
                    self.alpha[j] = max(L, self.alpha[j])

                    if abs(self.alpha[j]-aj) < self.tol:
                        #if change less than tol
                        self.alpha[j] = aj
                        print("too small")
                        continue

                    #tune alpha i accroding to alpha j
                    self.alpha[i] = ai + y[i] * y[j] *(aj - self.alpha[j])

                    bi = self.b - Ei - y[i] * (self.alpha[i] - ai) * k[i, i] + \
                                       y[j] * (self.alpha[j] - aj) * k[i, j]

                    bj = self.b - Ej - y[i] * (self.alpha[i] - ai) * k[i, j] + \
                                       y[j] * (self.alpha[j] - aj) * k[j, j]

                    if 0 < self.alpha[i] and self.alpha[i] < self.C:
                        self.b = bi
                    elif 0 < self.alpha[j] and self.alpha[j] < self.C:
                        self.b = bj
                    else:
                        self.b = (bi + bj) / 2.0

                    alpha_change += 1
                    
                    print("iter:{0}, change:{1}".format(i, alpha_change))

            print(alpha_change,i)
            #iteration until alpha converge
        
            if alpha_change == 0:
                # print("count + 1")
                count += 1
            else:
                # print("reset count")
                count = 0   
            print(count)     
            print("whole iter number {0}".format(count))

        self.w = np.dot(self.alpha * y, self.X)
        self.alpha = self.alpha[self.alpha > 0]
        index = np.where(self.alpha>0)[0]
        self.X = self.X[index]
        self.y = self.y[index]

    def predict(self, px):
        err = 0
        for i in range(len(self.px[i])):
            err += self.alpha[i] * self.y[i] * self._kernel(px, self.X[i])
        err = err + self.b

        if err >= 0:
            return 1
        else:
            return 0
        return 

    def evaluate(self, ry, py):
        accracy = 0
        # for i in range(len(py)):

        

    def linearKernel(self, x, z):
        return np.dot(x, z.T)

    def polyKernel(self, x, z):
        return np.power(np.dot(x, z.T + 1.0), 2)

    def GaussianKernel(self, x, z):
        xx = np.sum(x * x, axis=1)
        zz = np.sum(z * z, axis=1)
        res = - 2.0 * np.dot(x, z.T) + \
        xx.reshape(-1, 1) + \
        zz.reshape(1, -1)
        return np.exp(-self.gamma * res) # 0< gamma < 1

f = sio.loadmat('f:\\matlab\Hw2-package\spamTrain.mat')
XX = f['X']
yy = f['y']
XX = XX[0:1000]
yy = yy[0:1000].reshape(1,-1)[0].astype(int)
yy[yy==0] = -1
print(yy)


smo = smoTrain('linear')
smo.train(XX, yy)
print(yy[0])
print(smo.predict(XX))