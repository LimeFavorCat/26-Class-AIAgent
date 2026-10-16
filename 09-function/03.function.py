# def [함수명]([매개변수], [매개변수], ...) -> 함수를 정의하여 사용 가능

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