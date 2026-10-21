import numpy as np

# 정방행렬 = 단위행렬
# 행과 열의 길이가 같은 n x n 행렬의 대각선이 모두 1이고, 나머지는 0인 행렬
print(np.identity(3))

print(np.identity(15))

# 직사각 행렬
# eye(N, M=None, k=0, dtype=float)
# N(필수) : 행(row)의 개수
# M(선택) : 열(column)의 개수, 지정하지 않으면 정방행렬 생성
# k(선택) : 1을 채울 대각선의 위치(기본값=0=주대각선)
# dtype(선택) : 배열의 데이터 타입

# 3x3 단위행렬
arr1 = np.eye(3)
print(arr1, arr1.shape, '\n')

# 2x4 단위행렬
arr2 = np.eye(2, 4)
print(arr2, arr2.shape, '\n')

# 대각선의 위치 변경하기
# k가 양수이면 위로, 음수이면 아래로
arr3 = np.eye(6, 8, 2, dtype=int)
print(arr3, arr3.shape, '\n')
arr3 = np.eye(6, 8, -2)
print(arr3, arr3.shape, arr3.dtype, '\n')



