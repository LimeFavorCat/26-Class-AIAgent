st1 = "The struggle itself toward the heights is enough to fill a man's heart."

st2 = st1.center(100)
print(st1)
print(st2 + '*')
print('-' * 80 + '\n')

# 공백대신 '-'로 채움
st2 = st1.center(100,'-')
print(st1)
print(st2)
print()

st2 = st1.rjust(100,'-')
print(st1)
print(st2)
print()

st2 = st1.ljust(100,'-')
print(st1)
print(st2)
print()

# expandtaps - 탭 문자를 공백 문자로 바꿔주는 함수, 매개변수로 공백문자 갯수를 받을 수 있다.
st3 ='1\tand\t2'
print(st3)
print(st3.expandtabs(15))