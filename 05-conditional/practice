# 사용자로부터 정수를 입력받아서 짝수인지 홀수인지 판별
"""
# 일반적인 풀이
num = int(input('정수를 입력해주세요 :'))
if num % 2 == 0 :
    print('짝수')
else :
    print('홀수')

# def 활용
def isOdd(num) -> None :
    if num % 2 == 1 :
        print('홀수')
        return True
    else :
        print('짝수')
        return False

num = int(input('정수를 입력해주세요 :'))
isOdd(num)


# class 활용
class Calc:
    def __init__(self):
        pass

    def isEven(self, num):
        if num % 2 == 0:
            return True
        else:
            return False

calc = Calc()
num = int(input('정수를 입력해주세요 :'))
if calc.isEven(num):
    print('짝수입니다')
else :
    print('홀수입니다')
"""

"""
# 문2 두개의 정수를 입력받아 큰값 작은값 판별 출력
num1 = int(input('첫 번째 정수를 입력해주세요 : '))
num2 = int(input('두 번째 정수를 입력해주세요 : '))

if num1 > num2:
    print(f'큰값 : {num1}, 작은 값 : {num2}')
elif num2 > num1:
    print(f'큰값 : {num2}, 작은 값 : {num1}')
else:
    print('두 수의 크기가 같습니다')


if num1 < num2 :
    num1, num2 = num2, num1
print(f'큰값 : {num1}, 작은 값 : {num2}')

"""
st1 = "안녕"
num1 = 10

print(f'{id(st1), id(num1)}')

st1, num1 = num1, st1
print(f'{id(st1), id(num1)}')