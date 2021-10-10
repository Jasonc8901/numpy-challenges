import numpy as np

'''Q. Extract all odd numbers from arr'''

arr = np.array([0, 1, 2, 3, 4, 5, 6, 7, 8, 9])


def test():
    print(arr[1::2])
    # or
    print(arr[arr % 2 == 1])
