# 파이썬의 변수는 내부적으로 객체로 생성되기 때문에 자료형을 지정할 필요가 없다.
# 실제로는 주소만 저장되기 때문에 변수 크기가 2byte로 일정하다

data = 'value'
print(f'value stored in class = {data}, real value sotored in data is {id(data)}')

a = '안녕하세요'
b = 3.141592
c = 100
print(a)
print(b)
print(c)
print(f'a type = {type(a)}')
print(f'b type = {type(b)}')
print(f'c type = {type(c)}')

d = 7
e = 8
f = 9

g, h, i = 10, 11, 12
print(d,e,f,g,h,i)

j, k, m = '문자열', True, 2.19
print(j, k, m)
