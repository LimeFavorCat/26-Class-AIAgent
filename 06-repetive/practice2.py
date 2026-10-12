# 문 : 2개의 숫자를 입력받아 합계 구하기. 무한반복
#   사용자가 첫번째 값에 0을 넣으면 종료

# 답변 1
while True:
    num1 = int(input("첫 번째 값을 입력해주세요(0 입력시 종료) : "))
    if num1 == 0 :
        break
    num2 = int(input("두 번째 값을 입력해주세요 : "))
    print(f'{num1}과 {num2}의 합 : {num1 + num2}\n')
print('프로그램이 종료되었습니다.')