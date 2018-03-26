import scipy.io as sio
import numpy as np 
f = sio.loadmat('f:\\matlab\Hw2-package\spamTrain.mat')
X = f['X']
y = f['y']

x = y.reshape(1,-1)[0]
print(x)
