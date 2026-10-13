# {key:value} 쌍으로 이루어져 있다. 키는 유일해야 됨
dic1 = {'a':1, 'b':3.141592, 'c':'hello', 'd':'파이썬'}
dic2 = {1:1, 2:3.141592, 3:'hello', 4:'파이썬'}
dic3 = {1.1:1, 2.2:3.141592, 3.1:'hello', 412:123132}
print(dic1)
print(dic2)
print(dic3)
print('-' * 30)
print(dic1['a'],dic1['c'])
print(dic2[2])
print(dic3[2.2])

# 새로운 값 넣기
dic1['더조은'] = '02-1234-5678'
dic1['더조은'] = '강남' # 있는 key를 넣으면 덮어쓰기 됨
print(dic1)

# 데이터 개별 삭제
del(dic1['더조은'])
print(dic1)
dic1.clear()
print(dic1)