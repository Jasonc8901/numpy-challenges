import numpy as np

'''Q. Create the following pattern without hardcoding. Use only numpy functions and the below input array a.'''

a = np.array([1,2,3])

# > array([1, 1, 1, 2, 2, 2, 3, 3, 3, 1, 2, 3, 1, 2, 3, 1, 2, 3])


def test():
    print(np.r_[np.repeat(a, 3), np.tile(a, 3)])


