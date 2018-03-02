import numpy as np
x = np.array([(1, 2), (3, 4)], dtype=[('a', '<i4'), ('b', '<i4')])
print(x['b'])
