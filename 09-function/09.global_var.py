# 지역변수와 전역변수

# 지역변수 / 전역변수 호출 함수
def func1():
    a = 10 # 지역변수 - 함수 안에서만 사용가능
    print('func1()의 a =', a)

def func2():
    print('func2()의 a =', a)


a = 20 # 전역변수 a 선언
func1() # 지역변수 a 출력
func2() # 전역변수 a 출력


# global [함수이름] -> 함수 내부에서 전역변수 선언하기
def func3():
    global b 
    b = 10
    print('func3()의 b =', b)

def func4():
    print('func4()의 b =', b)
    
func3()
func4()

def clac_area(radius):
    global area
    area = 3.14 * radius**2
    return area

clac_area(5)
print(area)