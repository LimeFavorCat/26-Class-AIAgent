# 학점 출력기의 예외처리
def print_grade(score) -> None:
    if score > 100:   print('100 이하의 값을 입력해 주세요')
    elif score >= 90: print('A 학점')
    elif score >= 80: print('B 학점')
    elif score >= 70: print('C 학점')
    elif score >= 60: print('D 학점')
    elif score >= 0:  print('F 학점')
    elif score < 0:   print('0 이상의 값을 입력해 주세요')
    else: print('정상적인 값을 입력해 주세요')

while True:
    score = input('학점을 입력해주세요 : ')
    
    try:
        score = int(score)
        print_grade(score)
    except:
        print('정수 형식으로 입력해주세요')
        