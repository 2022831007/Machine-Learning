import numpy as np
arr = np.array([1,2,3,4])
print(arr)
#another way to create array
# with using default values 
#creation of array using 0
import numpy as np
zeros_array = np.zeros(3)
print(zeros_array)
#ones function ,creation of array using 1
import numpy as np
ones_array = np.ones((2,3))
print(ones_array)
# creation of array using specic number 
import numpy as np
filled_array= np.full((2,2),7)
print(filled_array)
#creating sequence of numbers in numpy
#arange(start,stop,step)
import numpy as np
arr = np.arange(1,10,2)
print(arr)
#creating identity matrices
#eye(size)
import numpy as np
identity_matrix=np.eye(3)
print(identity_matrix)