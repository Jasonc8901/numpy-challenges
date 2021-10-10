import numpy as np

'''Q. Convert a 1D array to a 2D array with 2 rows'''


def test():
    a = np.arange(10).reshape(2, -1)
    b = np.repeat(1, 10).reshape(2, -1)

    print(np.concatenate([a, b]))
    # or
    print(np.vstack([a, b]))
