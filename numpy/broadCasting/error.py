import numpy as np
arr1 = np.array([[1,2,3],[4,5,6]])
arr2= np.array([1,2]) #shape is not same
result=arr1+arr2
print(result)
#solution we can use .reshape