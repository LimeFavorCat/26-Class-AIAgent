# 사용자로부터 정수 2개, 연산자를 입력받아 연산 결과를 출력

"""
# 일반적인 풀이
num1 = float(input('첫 번째 숫자를 입력해주세요 : '))
num2 = float(input('두 번째 숫자를 입력해주세요 : '))
operator = input('연산자를 입력해주세요 : ')

if operator == '+':
    print(f'{num1} + {num2} = {num1 + num2}')
elif operator =='-':
    print(f'{num1} - {num2} = {num1 - num2}')
elif operator =='*':
    print(f'{num1} * {num2} = {num1 * num2}')
elif operator =='/':
    print(f'{num1} / {num2} = {num1 / num2}')
elif operator =='//':
    print(f'{num1}을 {num2}로 나눈 몫 = {num1 // num2}')
elif operator =='%':
    print(f'{num1}을 {num2}로 나눈 나머지 = {num1 % num2}')
elif operator =='**':
    print(f'{num1}의 {num2}제곱 = {num1 ** num2}')


# 자습
def calc(num1, num2, operator):
    if operator == '+':     print(f'{num1} + {num2} = {num1 + num2}')
    elif operator =='-':    print(f'{num1} - {num2} = {num1 - num2}')
    elif operator =='*':    print(f'{num1} * {num2} = {num1 * num2}')
    elif operator =='/':    print(f'{num1} / {num2} = {num1 / num2}')
    elif operator =='//':   print(f'{num1}을 {num2}로 나눈 몫 = {num1 // num2}')
    elif operator =='%':    print(f'{num1}을 {num2}로 나눈 나머지 = {num1 % num2}')
    elif operator =='**':   print(f'{num1}의 {num2}제곱 = {num1 ** num2}')

while True:
    try:
        num1 = float(input('첫 번째 숫자를 입력해주세요 : '))
        num2 = float(input('두 번째 숫자를 입력해주세요 : '))
        operator = input('연산자를 입력해주세요 : ')
        calc(num1, num2, operator)
    except:
        print('형식에 맞는 값을 입력해주세요')

"""


# 숫자를 입력받아 
# 양수, 홀수인지 -> sign
# 음수, 홀수인지 -> parity

# 일반적인 풀이
num1 = int(input('숫자를 입력해주세요 : '))
if num1 == 0:
    print('0은 양수/음수로 구분할 수 없습니다.')
else:
    print(f'해당 숫자는 {'양수이고'if num1 >= 0 else '음수이고'}, {'짝수입니다' if num1 % 2 == 0 else '홀수입니다'}')

# class 활용한 풀이
class Number:
    def __init__(self, number):
        self.number = int(number)

    def isEven(self):
        return True if self.number % 2 == 0 else False
    
    def isPositive(self):
        return True if self.number >= 0 else False

n1 = Number(input('숫자를 입력해주세요 : '))

print(f'해당 숫자는 {'양수이고' if n1.isPositive() else '음수이고'}, {'짝수입니다' if n1.isEven() else '홀수입니다'}')
