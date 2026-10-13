# 타입 변환

a = [1,2,3,4,5]
b = (6,7,8,9,10)
c = {11,12,13,14,15}
d = {16:'a',17:'b',18:'c',19:'d',20:'e'}


# 리스트를 set과 tuple로 변환
set1 = set(a)
tuple1 = tuple(a)

print(type(set1), set1)
print(type(tuple1), tuple1)


# 튜플을 리스트로 변환
list1 = list(c)

print(type(list1), list1)

print(a + list(b) + list(c) + list(d.keys()))




a = [1,2,3,4,5,1,1,1]
print(a)
print(set(a))
