import numpy as np

arr1 = np.arange(10,61,10)
print(arr1)

# 각 메서드는 함수로도 사용할 수 있다 ex) arr1.cumsum -> np.cumsum(arr1)
print(f'합계 : {arr1.sum()}')
print(f'평균 : {arr1.mean()}')
print(f'분산 : {arr1.var()}')
print((f'표준편차 : {arr1.std()}'))
print(f'최솟값 : {arr1.min()}')
print(f'최솟값 : {arr1.max()}')
print()
print(f'누적합 : {arr1.cumsum()}')
print(f'누적곱 : {arr1.cumprod()}')

arr2 = arr1.reshape(2,3)
print(arr2)
print(f'전체 평균 : {arr2.mean()}')
print(f'행의 평균 : {arr2.mean(axis=1)}')
print(f'열의 평균 : {arr2.mean(axis=0)}')


print(f'전체 최솟값 : {arr2.min()}')
print(f'행의 최솟값 : {arr2.min(axis=1)}')
print(f'열의 최솟값 : {arr2.min(axis=0)}')

arr3 = [1,2,100]
print(f'중앙값 : {np.median(arr3)}')
arr3 = [1,2,3,100]
print(f'중앙값 : {np.median(arr3)}')

arr5 = np.array([[1,2,3],[10,20,30]])
print(f'전체 중앙값 : {np.median(arr5)}')
print(f'행별 중앙값 : {np.median(arr5, axis=1)}')
print(f'열별 중앙값 : {np.median(arr5, axis=0)}')