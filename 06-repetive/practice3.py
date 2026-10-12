# 무한반복으로 돌면서 구구단 중 출력할 단수를 입력받아
# 출력 후 구구단을 계속할 것인지 확인

while True:
    dan = int(input('출력할 단 수를 입력하세요 : '))
    for i in range(1,10):
        print(f'{dan} x {i} = {i * dan}', end = '   ')
    print('\n' + '-' * 120)
    cont = input('계속하시겠습니까? Y or N : ')
    if cont != 'Y' and cont != 'y': # cont.lower() 사용하면 더 깔끔
        print('종료되었습니다.')
        break
    else:
        print('-' * 120)
