"""
reshape(rows,columns) specify new shape
if dimensions match then we can reshape
"""
import numpy as np
arr = np.array([10,20,30,40,50,60])
reshaped_arr = arr.reshape(2,3)
print(reshaped_arr)
