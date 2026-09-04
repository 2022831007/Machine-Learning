"""
np.insert(array,index,value,axis=None)
array - original array
index-
value-
axis-none,1d array
axis=0,row wise
axis=1,column wise
"""
import numpy as np
arr = np.array([10,20,30,40,50,60])
print(arr)
new_arr = np.insert(arr,2,100)
print(new_arr)
arr_2d = np.array([[1,2],[3,4]])
new_arr_2d=np.insert(arr_2d,1,[5,6],axis=1)
print(new_arr_2d)
