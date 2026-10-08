# str() 함수 : 데이터를 문자열로 변환

num1 = 5
num2 = 5.1
b1 = True

print(num1, num2, b1, sep=", ")
# print('num1 = '+ num1) -> 자료형 불일치
print('num1 = ' + str(num1))
print(f'num1 = {num1}')

y = 2.5 * 2 ** 2
print(y)
help(print)