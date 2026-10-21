import numpy as np

data1 =[1,2,3,4,5]
data2 =[100,200,300,400,500]

list1 = data1 + data2
print(list1)

arr1 = np.array(data1)
arr2 = np.array(data2)

r1 = arr1 + arr2
print(r1)

print(arr1-arr2)

print(arr1 * arr2)

print(arr1 / arr2)

print(arr1 + 5)

print(arr1 ** 2)