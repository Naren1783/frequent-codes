import pandas as pd
#it prints entered list with index number
data=[100, 102, 104] #For Integer
series=pd.Series(data)
print("Integers:\n",series)
#Pandas are simple as Microsoft excel on STEROIDS

print("\n")

data1=[100.1, 102.2, 104.3] #For Float
series1=pd.Series(data1)
print("Float:\n",series1)

print("\n")

data2=["A", "B", "C"]
series2=pd.Series(data2) #For Object
print("String:\n",series2)

print("\n")

data3=[True, False, True] #For Boolean
series3=pd.Series(data3)
print("Boolean:\n",series3)

print("\n")

#For changing Index
data4=[18, 10, 45, 7, 33]
series4=pd.Series(data4, index=["1st", "2nd", "3rd", "4th", "5th"])
print("GOAT: \n",series4)
#Video=5:39
