'''
* set : 중복불가
        순서가 없다( index 없음 )
        {중괄호 사용}

    *** 주의 : 빈 set을 만들때 {} -> 딕셔너리가 됨
        set() -> 이렇게 만들 것

'''

a = {1,2,3,1,1,2,3,3}
print(a)
print(len(a))

b = {'홍길동', 3, 5, True, (4,3)}
print(b)
print('-' * 30)

c = {}
print(type(c))
print(c)
c = set()
print(type(c))
print(c)