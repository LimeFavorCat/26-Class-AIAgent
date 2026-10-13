'''
문
로또 프로그램 만들기
사용자로부터 몇 회분을 살 건지 물어보고
그 횟수만큼 번호를 랜덤으로 추출하여 출력하기
'''
import random

# ========================================================= setting
ROTO_LEN = 6
ROTO_RANGE = (1,12)
ROTO_PRICE = 10000
ROTO_COMMENTS = [
    "일주일 동안 기다려온 설렘의 순간! 로또복권 당첨 번호를 지금 공개합니다.",
    "인생 역전의 꿈, 과연 오늘 밤 그 주인공은 누가 될까요? 로또 추첨 방송 지금 시작합니다.",
    "여러분의 간절한 소망이 기적으로 바뀌는 시간, 로또 당첨 번호 안내입니다."]
ROTO_REWARD = [0, 500, 2000, 5000, 8000, 100000, 99999999]
REVEAL_COUNT = 3
START_MONEY = 100000

# ========================================================= fuction / class

def print_ticket():
    print('\n구매한 로또\n' + '-' * 40)
    for i in range(amount):
        print(f'{i+1:2d}번 티켓 - ', end='')
        for j in range(ROTO_LEN):
            print(format(roto_ticket[i][j],'2d'), end=' ')
        print()
    print('-' * 40)

# ========================================================= main


money = START_MONEY
roto_ticket = []
turn = 1

while True:
    # 유저 입력
    amount = int(input(f'\n현재 잔고 : {money:3,d}원\n몇 회분의 로또를 구매하시겠습니까? '))

    # 로또 구입
    money -= ROTO_PRICE * amount
    print(f'\n{amount}장의 로또를 구매했습니다. 현재 잔액 : {money:3,d}원(-{amount * ROTO_PRICE:3,d})원\n')

    # 티켓 생성 및 출력
    roto_ticket = []
    for i in range(amount): roto_ticket.append([random.randint(*ROTO_RANGE) for j in range(ROTO_LEN)])
    print_ticket()

    if money < 0 :
        print(f'\n!! 경고!! 현재 빛이 {money * -1:3,d}원 있습니다. 이번턴에 모두 값지 못할 시 파산합니다. !! 경고 !!\n')

    # 로또 결과 공개
    roto_result = []
    input('엔터키를 연타해서 다음 숫자를 공개하세요')
    for x in range(ROTO_LEN):
        for i in range(REVEAL_COUNT):
            input()
        result = random.randint(*ROTO_RANGE)
        roto_result.append(result)
        print(format(result,'2d'), end=' ')
    print()
    print(ROTO_COMMENTS[random.randint(0,len(ROTO_COMMENTS)-1)])
    print(f'로또 추첨 결과 : {roto_result}')
    print('"확인한다"를 입력하면 결과를 확인하고 당첨금을 수령합니다.')

    while True:
        user = input("")
        if user == '확인한다':
            break

    # 로또 결과 계산
    print('엔터키를 눌러서 하나씩 결과 확인')
    reward = 0
    for i in range(amount):
        hit = 0
        for j in range(ROTO_LEN):
            if roto_result[j] == roto_ticket[i][j]:
                hit += 1
            else:
                roto_ticket[i][j] = 'X'
        input()
        print(f'{i+1:2d}번 티켓 - {hit:2d}개 일치 - 보상금 {ROTO_REWARD[hit]}원')
        reward += ROTO_REWARD[hit]

    print(f'\n\n최종 보상 : {reward}원')
    money += reward
    if money < 0:
        print(f'{turn}턴 만에 빛을 못값아 사망하셨습니다.')
        break
    else:
        print('도박은 계속됩니다....')
        turn += 1
