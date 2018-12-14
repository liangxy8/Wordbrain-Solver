#!/user/bin/python
import numpy as np
from numpy import array

a = np.array([['y', 's', 'o', 'n'], ['e', 'l', 'n', 'n'], ['h', None, 'c', 'a'], ['o', 'l', None, 'b']])

def drop_letters(matrix):
    '''Drop the used letters in the matrix'''
    result = np.copy(matrix)
    previous = [None] * matrix.shape[0]
    for j in range(0, matrix.shape[1]):
        temp_mat = np.array(previous)
        index = matrix.shape[0] - 1
        for i in range(matrix.shape[0] - 1, -1, -1):
            if result[i][j] != None:
                temp_mat[index] = result[i][j]
                index = index - 1
        result[:, j] = temp_mat
    return result
b = drop_letters(a)
print(b)

