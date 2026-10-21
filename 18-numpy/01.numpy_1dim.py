'''
* numpy
    python에서 배열과 행렬 같은 수치데이터를 효율적으로 처리하고
    다양한 수학,통계 계산을 수행하는 라이브러리

    - 장점 : N-dimensional array 다차원 배열을 다룸
'''
import numpy as np

data1 = [1,2,3,4,5]
data2 = [1.7, 2, 5.5, 8.8]
data3 = [1, 2.3, '3.1', 41]

#  array() : 리스트나 튜플을 넘파이 배열로 만들어줌
arr1 = np.array(data1)
arr2 = np.array(data2)
arr3 = np.array(data3)

print(arr1.shape, arr1.dtype, ':', arr1)
print(arr2.shape, arr2.dtype, ':', arr2)
print(arr3.shape, arr3.dtype, ':', arr3)

# 배열의 특징은 단일 데이터만 취급
# 정수와 실수가 섞여있으면 모두 실수로 변환하여 저장

