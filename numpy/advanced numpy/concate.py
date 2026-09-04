"""
Docstring for numpy.advanced numpy.concate
np.concate((array1,array2),axis=0)
"""
import numpy as np
arr1= np.array([1,2,3])
arr2 = np.array([4,5,6])
new_arr = np.concatenate((arr1,arr2))
print(new_arr)
arr_2d=np.array([[1,2,3],[4,5,6]])
new_arr2d=np.delete(arr_2d,0,axis=0)
print(new_arr2d)
new = np.delete(arr1,1)
print(new)