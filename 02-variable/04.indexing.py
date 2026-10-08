st1 = 'abcdefghijklmnopqrstuvwxyz'
# 인덱싱
print(st1[0], end = '')
print(st1[1], end = '')
print(st1[2])

print(st1[-1], end= '')
print(st1[-2], end= '')
print(st1[-3])
print('-' * 30)

# 슬라이싱
print(st1[:10])
print(st1[1:10:2])
print(st1[1:10:3])

print(st1[::-1])
print(st1[::-2])
print(st1[5:1:-2])
print(st1[-1:-6:-1])
print('-' * 30)

# 문자열 연결하기 : +
st2 = 'xyz'
st3 = st1 + st2
print(f'{st1} + {st2} = {st3}')
st4 = st2 * 3
print(st4)
print('-' * 30)

# 문자열의 문자 갯수 확인
print(f'length of st4 = {len(st4)}')

# indexing에서는 문자를 변경 못함
# st1[0] = 'z' -> 에러 발생
st1 = 'z' + st1[1:] 
print(st1)

st1 = st1[0:4] + 'z' + st1[5:]
print(st1)