st1 = 'In the depth of winter, I finally learned that there was in me an invincible summer'

# 특정문자 기준으로 문자열 분리
# 기본값 공백문자.
# str.split() -> list[str]
st2 = st1.split()
print(st1)
print(st2)
print('-' * 100 + '\n')

st2 = st1.split(',')
print(st1)
print(st2)
print('-' * 100 + '\n')

st2 = st1.split(' ', 3) # 3번만 분리
print(st1)
print(st2)
print('-' * 100 + '\n')


st3 = " ".join(st2)
print(st2)
print(st3)
print('-' * 100 + '\n')