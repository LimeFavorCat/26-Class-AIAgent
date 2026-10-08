# 파이썬은 실수 나눗셈의 나머지 연산도 가능하다
print(f'3.14 % 1.2 = {3.14 % 1.2}')

# 산술 연산자
num1 = int(input('정수 입력 : '))
num2 = int(input('정수 입력 : '))

r1 = num1 + num2
print(f'{num1} + {num2} = {r1}')

r2 = num1 - num2
print(f'{num1} - {num2} = {r2}')

r3 = num1 * num2
print(f'{num1} * {num2} = {r3}')

r4 = num1 / num2
print(f'{num1} / {num2} = {r4}')

r5 = num1 % num2
print(f'{num1}을 {num2}로 나눈 나머지 = {r5}')

r6 = num1 // num2
print(f'{num1}을 {num2}로 나눈 몫 = {r6}')

r7 = num1 ** num2
print(f'{num1}의 {num2}제곱 = {r7}')