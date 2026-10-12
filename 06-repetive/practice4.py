# random 클래스
import random
x = random.random()
i = random.randint(1, 6)
print(x, i)


# 문 : 주사위를 3개를 동시에 던져서 동일한 숫자가 나오면 탈출하기
"""

dice = [0,1,2]
count = 0
reroll = 0
while True:
    user_input = input('엔터키를 눌러 다시 시도')
    try:
        user_input = int(user_input)
        if user_input > 0 and user_input < 4:
            dice[user_input] = random.randint(1,6)
            print(f'{i+1}번째 주사위 다시 굴린 결과 : {dice[i]}')
            if dice[0] == dice[1] == dice[2]:
                print(f'잭팟! {count}번 만에 탈출 성공!')
                break
            else:
                print('탈출 실패...\n')

    except:
        pass
    for i in range(3):
        dice[i] = random.randint(1,6)
        print(f'{i}번째 주사위 결과 : {dice[i]}')

    count += 1
    if count % 3 == 0 : reroll += 1
    if reroll > 0 :
        print(f'현재 다시 굴림 가능 횟수 : {reroll}\n 1~3 입력시 해당 주사위 리롤 : ')
    print(f'현재 시도 횟수 {count}회\n')
    if dice[0] == dice[1] == dice[2]:
        print(f'잭팟! {count}번 만에 탈출 성공!')
        break

"""

# 문 : 주사위의 숫자 맞추기
"""

rand = random.randint(1,6)
retry = 1
while True:
    user_input = int(input('주사위의 눈을 맞춰보세요 : '))
    if user_input == rand:
        print(f'{retry}번 만에 성공')
        break
    else:
        print(f'실패 {retry}번째 시도 중')
        retry += 1


"""

# 자습 : 숫자야구
"""
rand = [random.randint(1,9),random.randint(1,9),random.randint(1,9)]
while True:
    strike = 0
    ball = 0
    miss = 0
    index = 0
    try:
        user = input('세 자리 숫자를 입력하세요 (x 입력시 포기): ')
        if user.lower() == 'x':
            print('포기하셨습니다.')
            break
        if len(user) != 3 :
            print('형식 오류')
            continue
        for i in user:
            num = int(i)
            if rand[index] == num:
                strike += 1
            elif num in rand:
                ball += 1
            else:
                miss += 1
            index += 1
        print(f'{strike}스트라이크, {ball}볼\n')
        if strike == 3:
            print('축하합니다 성공!')   
            break
    except:
        print('형식 오류')
        continue
"""