import numpy as np

'''Q. Create a 3×3 numpy array of all True’s'''


def test():
    print(np.ones([3, 3], dtype=bool))
    # or
    print(np.full([3, 3], True))
