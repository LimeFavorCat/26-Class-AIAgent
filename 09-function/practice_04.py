'''
문 1 : 매개변수로 2개의 숫자와 연산자를 입력받아 출력
문 2 : 국어, 영어 점수를 사용자로 부터 입력받아 평균 받기 -> 또 다른 함수로 학점 리턴하기
문 3 : 로또를 함수로
'''

# 문제 1
def calc(a, b, operator = '+'):
    if operator == '+':
        return a + b
    if operator == '-':
        return a - b
    if operator == '*':
        return a * b
    if operator == '/':
        return a / b

print(calc(1,5,'+'))


# 문제 2
def average(korean, math):
    return (korean + math) / 2

def grade(score):
    if score < 0 or score > 100 : return '에러'
    elif score < 60 : return 'F'
    else:
        result = int((score - 60) // 5)
        return "D0D+C0C+B0B+A0A+A+"[result*2:result*2+2]

print(grade(average(100,100)))

# 문제 3

import random
def roto():
    result = [random.randint(1,99) for i in range(6)]
    print(result)

roto()

# 문제 4 : 입력한 비밀번호가 규칙에 맞으면 생성되고 규칙에 맞지 앟으면 다시 생성
def isVaild(password:str):
    return True if len(password) > 7 and password.isalnum() else False

while True:
    password = input('비밀번호를 입력해주세요 : ')
    if isVaild(password):
        print('올바른 비밀번호입니다.')
        break
    else:
        print('비밀번호 규칙에 맞지 않습니다.')