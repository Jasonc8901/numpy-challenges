import numpy as np

'''Q. Get the common items between a and b'''

a = np.array([1,2,3,2,3,4,3,4,5,6])
b = np.array([7,2,10,2,7,4,9,4,9,8])


def test():
    print(np.intersect1d(a, b))


