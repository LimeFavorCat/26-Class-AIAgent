st1 = '     He likes apples, and she likes mango, I like it both     '

# 좌우 공백 제거
st2 = st1.strip()
print(st1+'--')
print(st2+'--')

# 오른쪽 제거
st2 = st1.rstrip()
print(st2+'--')

# 왼쪽 제거
st2 = st1.lstrip()
print(st2+'--')
print('-' * 50)

# 문자열 바꾸기
st2 = st1.replace('like','love')
print(st1)
print(st2)
print('-' * 50)

st2 = st1.replace('like','love',1)
print(st1)
print(st2)
print('-' * 50)

st2 = st1.replace(' ','')
print(st1)
print(st2)
print('-' * 50)