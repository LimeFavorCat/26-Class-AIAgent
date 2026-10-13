dic1 = {'a':1, 'b':3.141592, 'c':'hello', 'd':'파이썬'}

# key가 없을 경우 대비
target = 'c'
if target in dic1:
    print('키가 존재함 :', dic1[target])
else:
    dic1[target] = 'neo Namu'
    print('새 값 추가됨')

target = 'e'
if target in dic1:
    print('키가 존재함 :', dic1[target])
else:
    dic1[target] = 'neo Namu'
    print('새 값 추가됨')
print(dic1)
print('-' * 30)

# 키, 값 확인하기
print(dic1.keys())
print(dic1.values())
print(dic1.items())
print('-' * 30)

for key in dic1.keys():
    print(key)

for key, value in dic1.items():
    print(f'키 값 : {key}, 벨류 값 : {value}')

for key in sorted(dic1.keys(),reverse=True):
    print(key, dic1[key], end=', ')

dic1 = {'a':1, 'b':3, 'c':2, 'd':5}

# 값을 기준으로 오름차순 정렬
for val in sorted(dic1.values()):
    print(val)

# len : 길이 출력
print(len(dic1))

# 데이터 추가
dic2 = {'e':'파이썬', 'f':'딥러닝'}
# dic1['g'] = dic2 -> 딕셔너리 안에 value로 딕셔너리가 들어감

dic1.update(dic2)

print(dic1)