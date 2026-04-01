import numpy as np
array=np.array([[1,2,3,4],          #0
                [5,6,7,8],          #1
                [9,10,11,12],       #2
                [13,14,15,16]])     #3
#array[start:end:step]
print(array[1])
print(array[-1])#last one
print(array[-2])#last but one
print(array[0:])#it prints everything


print("selected",array[0:4:2])
print("s",array[::2])    #both same

#for reversing 
print("rev",array[::-1])
print("2nd rev",array[::-2])  #these are row selections

#for every characters like matrix
print("Matrix",array[2:, 0:2])