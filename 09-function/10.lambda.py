# 함수명 = lambda 매개변수 : 수행코드

# 일반적인 함수 표기법
def square1(x):
    return x ** 2

# 람다 함수 표기법
square1 = lambda x : x ** 2

print(square1(10))

# 람다 함수 - 매개변수 없는 버전
test1 = lambda : print('test1')
test1()

# 람다 함수 - 기본값 넣기
a = (lambda x : x**2)(3)
print(a)
print((lambda x : x**2)(3))

# 맨 뒤의 ()는 앞의 함수를 실행하라는 명령어
(lambda : print('test2'))()

# 람다함수 사용법
list1 = [(lambda x,y,z: x + y * 2 + z ** 2)(1,2,3) for i in range(15)]
print((lambda x,y,z: x + y * 2 + z ** 2)(1,2,3))
print(list1)

print([(lambda x : x**2)(a) for a in range(5)])