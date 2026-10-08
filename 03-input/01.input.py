# 사용자로부터 입력 받기
'''
# input() 함수를 사용해 사용자로부터 문자열을 입력받을 수 있다
var1 = input('이름을 입력하세요')
print(f'{var1}님 환영합니다!')

# str형끼리 더한 뒤 int 변환
kor = input('국어 점수를 입력하세요 : ')
com = input('컴퓨터 점수를 입력하세요 : ')
print(f'두 점수의 총합은 {int(kor + com)}점 입니다.')
print('%s + %s = %d',format(kor, com, int(kor) + int(com)))

# input 함수의 결과는 무조건 문자열로 들어옴
kor = int(input('국어 점수를 입력하세요 : '))
com = int(input('컴퓨터 점수를 입력하세요 : '))
print(f'두 점수의 총합은 {kor + com}점 입니다.')

print('%d + %d = %d',format(kor, com, kor + com))
print('%s + %s = %s',format(kor, com, kor + com))
print(f'{kor} + {com} = {kor + com}')
'''

