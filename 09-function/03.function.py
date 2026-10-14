nn = [i for i in range(5)]
print(nn)

def inputNum(n):
    for x in n:
        n[x] = int(input(f'{x+1}번째 정수 입력'))

inputNum(nn)
print(nn)

def outputNum(n):
    print('----------출력----------')
    for i, v in enumerate(n):
        print(n[i], end='')
        print(v, end='')