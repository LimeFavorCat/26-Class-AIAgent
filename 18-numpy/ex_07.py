import numpy as np
arr = []
# 1번 - 1차원 배열 만들기
arr.append(np.array([10,20,30,40,50])) 

# 2번 - 2차원 배열 만들기
arr.append(np.array([[1,2,3],[4,5,6]]))

# 3번 - arange를 사용하여 배열 만들기
arr.append(np.arange(5,21,3))

# 4번 - arange사용하여 만든 배열 reshape
temp = np.arange(1,13)
arr.append(temp.reshape(3,4))

# 5번 linespace
arr.append(np.linspace(0,1,6))

# 6번 모든 원소 0
arr.append(np.zeros((4,4), dtype=int))

# 7번 모든 원소 1
arr.append(np.ones((4,4), dtype=int))

# 8번 다음 조건을 만족하는 배열 생성
# 2부터 24까지 짝수를 생성
# 생성한 배열을 3행 4열
temp = np.arange(2,25,2)
arr.append(temp.reshape(3,4))

# 9번
temp = np.linspace(10,50,9, dtype=int)
arr.append(temp.reshape(3,3))

# 10 번
temp = np.arange(1,17).reshape(4,4)
temp2 = np.zeros((4,4), dtype=int)
temp3 = np.ones((4,4), dtype=int)

arr.append(np.array([temp,temp2,temp3]))

# 11번
arr.append(np.eye(4, dtype=int))

# 12번
arr.append(np.eye(3,5,1, dtype=int))



# 생성 결과 출력
for i, each in enumerate(arr):
    print(f'\n# {i+1}번 문제')
    print(each)