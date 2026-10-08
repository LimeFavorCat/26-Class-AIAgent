'''
bool() 변환

False가 되는경우
    : 완전히 비어 있거나 0인 경우 (0, 0.0, '', None, [])
True가 되는 경우
    : 그 외에 데이터가 하나라도 들어있는 경우 ([''])
'''

print(0 == False)
print(1 == True)
print('-' * 30)

print(bool(0))
print(bool(0.0))
print(bool([]))
print(bool(''))
print(bool(None))
print('-' * 30)

print(bool(1))
print(bool(0.1))
print(bool(['']))
print(bool(' '))


name = input("이름 입력 : ")
print(bool(name))
print('name =',name)