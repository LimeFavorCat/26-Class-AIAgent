
score = 89


if score >= 80 and score < 90 : print(f'점수 : {score}, 학점 : B학점')

while score >= 0:
    score = int(input('점수를 입력하세요 : '))
    if score >= 90 and score <= 100 :
        print('A학점')
    if score >= 80 and score < 90 :
        print('B학점')
    if score >= 70 and score < 80 :
        print('C학점')
    if score >= 60 and score < 70 :
        print('D학점')
    if score >= 0 and score < 60 :
        print('F학점')