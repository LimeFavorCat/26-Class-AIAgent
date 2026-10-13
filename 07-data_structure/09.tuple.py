# tuple : 리스트와 동일하지만 변경 불가
# 소괄호() -> 안써도 됨

tup1 = (10,20,30,40)
tup2 = 'python', 4.67, 90, True

print(tup1)
print(tup2)
print(type(tup2))
print('-' * 30)

# 데이터가 1개 일때
tup3 = (10,)
tup4 = 10,
tup5 = (10)
print('tup3의 type =', type(tup3))
print('tup4의 type =', type(tup4))
print('tup5의 type =', type(tup5))
print('-' * 30)

# 배열과 마찬가지로 인덱스/슬라이싱 사용 가능
print(tup1[0])
print(tup1[1])
print(tup1[::-1])
print('-' * 30)

# tup1[0] = 100 # TypeError : tuple object does not support item assignment
# tup1.clear() # AttributeError : 'tuple' object has no attribute 'clear'
del(tup1) # 삭제는 가능