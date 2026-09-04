"""
.ravel() it returns a view ,original array
.flatten() return a copy ,not original array
"""
import numpy as np
arr_2d = np.array([[1,2,3],[4,5,6]])
print(arr_2d.ravel())
print(arr_2d.flatten())