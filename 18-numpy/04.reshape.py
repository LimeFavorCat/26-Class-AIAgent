'''
* reshape -> 배열의 차원을 변경하는 메서드 np.array.reshape(row, column)
'''

import numpy as np

arr1 = np.arange(1, 13)
print(arr1, arr1.shape, '\n')

arr2 = arr1.reshape(3,4)
print(arr2, arr2.shape, '\n')


# 행 또는 열 자동계산 -> 매개변수에 -1 넘겨주기
arr3 = arr1.reshape(2, -1)
print(arr3, arr3.shape, '\n')

arr3 = arr1.reshape(-1, 3)
print(arr3, arr3.shape, '\n')


# 3차원 배열로 바꾸기
arr4 = arr1.reshape(2, -1, 3)
print(arr4, arr4.shape, '\n')


# 돌려놓기
arr5 = arr4.reshape(arr2.shape)
print(arr5, arr5.shape, '\n')

arr5 = arr4.reshape(12)
print(arr5, arr5.shape, '\n')
