import numpy as np

'''Q. Stack the arrays a and b horizontally'''


def test():
    a = np.arange(10).reshape(2, -1)
    b = np.repeat(1, 10).reshape(2, -1)

    print(np.hstack([a, b]))
