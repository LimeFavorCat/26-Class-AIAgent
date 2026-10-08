# 비교 연산자 : 비교 결과가 True, False로 출력
# >, <, >=, <=
# ==, !=

num1 = int(input("정수 1을 입력해 주세요 : "))
num2 = int(input("정수 2를 입력해 주세요 : "))

print(f'{num1}이 {num2}보다 큰가? {num1 > num2}')
print(f'{num1}이 {num2}보다 작은가? {num1 <num2}')
print(f'{num1}이 {num2}보다 크거나 같은가? {num1 >= num2}')
print(f'{num1}이 {num2}보다 작거나 같은가? {num1 <= num2}')

print('-' * 30)
print(f'{num1}과 {num2}는 같은가? {num1 == num2}')
print(f'{num1}과 {num2}는 다른가? {num1 != num2}')