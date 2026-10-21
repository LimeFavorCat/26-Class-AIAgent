import numpy as np

data1 = ['people', 'boy,', 'girl', 'man', 'woman']
data2 = ['1.5','2.0','2.5','3.0','3.5','4.0','4.5','5.0']
data3 = ['10','20','30','40','50']

arr1 = np.array(data1)
arr2 = np.array(data2)
arr3 = np.array(data3)

print(arr1)
print(arr2)
print(arr3)

print(arr2.astype(float))
print(arr3.astype(int))