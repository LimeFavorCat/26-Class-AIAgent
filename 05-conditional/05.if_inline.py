# 삼항 연산식

"""
if num1 == 2:
    print('2입니다')
else:
    print('2가 아닙니다')
"""

"""
num1 = 2
print('2입니다') if num1 == 2 else print(('2가 아닙니다.')) # (참이면 앞에 실행) (if-else문) (거짓이면 뒤에 실행)
print(('2입' if num1 == 2 else '2가 아닙')+ '니다.') # ??

# 합격, 불합격
score = 75

# 일반 조건문
# if score >= 60:
#     result = '합격'
# else:
#     result = '불합격'

# print('합격' if score >= 70 else '불합격')

result = '합격' if score >= 60 else '불합격'
print(f'결과는 {result}입니다.')


"""
# 2수 중 큰 수 찾기

# num1 = int(input('첫 번째 정수를 입력해주세요 : '))
# num2 = int(input('두 번째 정수를 입력해주세요 : '))

# max = num1 if num1 > num2 else num2
# print(f'{num1}과 {num2}중 큰 숫자는 {max}입니다')

# 회문 : 왼쪽에서 읽은것과 오른쪽으로 읽었을 때 같은 문자열
str1 = 'abcdcba'
if str1 == str1[::-1]:
    print(f'{str1} : 회문입니다.')
else:
    print(f'{str1} : 회문이 아닙니다.')

print(str1, '회문입니다.' if str1 == str1[::-1] else '회문이 아닙니다.')
print(f'{str1} : {'회문입니다.' if str1 == str1[::-1] else '회문이 아닙니다.'}')