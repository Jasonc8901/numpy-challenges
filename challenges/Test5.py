import numpy as np

'''Q. Replace all odd numbers in arr with -1'''

arr = np.array([0, 1, 2, 3, 4, 5, 6, 7, 8, 9])


def test():
    arr[arr % 2 == 1] = -1
    print(arr)
