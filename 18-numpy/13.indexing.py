import numpy as np

arr1 = np.array([10,20,30,40,50,60])
arr2 = np.arange(10,91,10).reshape(3,3)

print(f'arr1 : {arr1}')
print(f'arr2 : \n{arr2}')

# 1차원 배열 인덱싱
print(arr1[0])
print(arr1[[1,3,5]]) # 인덱스 1,3,5를 배열에 넣어서 반환

print(arr1[arr1>30]) # 인덱스 대신에 조건식을 넣어서 배열로 반환

arr1[2] = 555
print(f'arr1 : {arr1}')

arr1[[1,3,5]] =[[555,777,999]]
print(arr1)


# 2차원 배열 인덱실
print(arr2)

print(arr2[0, 2]) # 이 방법을 권장
arr2[0,2] = 1000
print(arr2[0][2])

# 행을 통째로 변경
arr2[0] = [1,2,3]
print(f'행을 통째로 변경 \n{arr2}')

print(arr2[[0,2],[1,1]])
arr2[[0,1,2],[1,1,1]] = [100,200,300]
print(arr2)
