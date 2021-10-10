import numpy as np

'''Q. Convert a 1D array to a 2D array with 2 rows'''


def test():
    arr = np.array([0, 1, 2, 3, 4, 5, 6, 7, 8, 9])
    arr = arr.reshape(5, -1)
    print(arr)
