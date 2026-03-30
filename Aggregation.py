import numpy as np
#Aggregate funvtions
array=np.array([[1, 2, 3, 4, 5],
               [6, 7, 8, 9, 10]])

#Sum
print(np.sum(array))

#Mean
print(np.mean(array))

#Standard Deviation
print(np.std(array))

#Variance
print(np.var(array))

#Minimum ans Maximum
print(np.min(array))
print(np.max(array))

#Median
print(np.median(array))

#Argmin and Argmax
print(np.argmin(array))
print(np.argmax(array))

#Sum of individual character inside two list
print(np.sum(array, axis=0))

