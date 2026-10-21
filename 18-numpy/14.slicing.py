import numpy as np

arr1 = np.array([10,20,30,40,50,60])
arr2 = np.arange(10,91,10).reshape(3,3)
print(f'arr1 : {arr1}')
print(f'arr2 : \n{arr2}')

# 1차원 배열의 슬라이싱
print(arr1[1:4]) # 1,2,3
print(arr1[::-1]) # 5,4,3,2,1,0
print(arr1[:5:2])

arr1[1:4] = [100,200,300]
print(f'arr1 : {arr1}')

arr1[1:4] = 300
print(f'arr1 : {arr1}')


# 2차원 배열의 슬라이싱
# 배열명[행슬라이싱, 열슬라이싱]
# 배열명[0:2,1:3]
arr2[1:4,2:3] = 300
print(f'arr2 : \n{arr2}')
arr2[1:4,0] = 4
print(f'arr2 : \n{arr2}')

# 특정 열만 추출
print(arr2[:,2])

# 특정 행만 추출
print(arr2[2,:])
