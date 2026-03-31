import numpy as np

ages=np.array([[21, 17, 19, 20, 16, 30, 18, 65],
               [39, 22, 15, 99, 18, 19, 20, 21]])

teenagers=ages[ages < 18]
adults=ages[(ages>=18) & (ages<60)]
senior_citizens=ages[ages>=60]
even_ages=ages[ages%2==0]
odd_ages=ages[ages%2!=0]
print("Teenagers : ",teenagers)
print("Adults : ",adults)
print("Senior Citizens : ",senior_citizens)
print("Even Ages : ",even_ages)
print("Odd Ages : ",odd_ages)
print("\n","\n")


import numpy as np

ages=np.array([[21, 17, 19, 20, 16, 30, 18, 65],
               [39, 22, 15, 99, 18, 19, 20, 21]])

#When age is below or equal to 18 it gives 0 in he place of age
adults=np.where(ages>=18,ages,"NA")
print("Not allowed in case of below 18\n",adults)