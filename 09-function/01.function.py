# 함수 : 클래스 밖에 독립적으로 존재, 이름만으로 호출할 수 있다.
# 매서드 : 클래스 내부에 정의되어 있고, 객체를 통해 호출하는 함수

# def 함수명(매개변수들):
#   실행할 내용
#   return

# 매개변수가 없고 반환값이 없는 함수
def address():
    print('서울특별시 강남구')
    print('삼오빌딩 704호')

address() 

def add():
    a = 3 + 8
    print(a)

add()
print('-' * 30)

# 매개변수가 없고 반환값이 있는 함수
def add2():
    a = 3 + 8
    return a

result = add2()
print(add2())
print('-' * 30)

# 매개변수가 있는 함수
def multi(x,y):
    result = x * y
    print(f'{x} x {y} = {result}')

multi(4,5)

def multi2(x,y):
    result = x * y
    return result

num = multi2(4,5)
print(f'num : {num}')
print('-' * 30)

def star(n):
    for x in range(n):
        print('*', end='')
    print()

star(5)
star(15)
star(25)
