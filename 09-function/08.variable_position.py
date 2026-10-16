# 가변 위치 인자: 매개변수 갯수가 정해져 있지 않을 때 사용
# *args : 튜플이 전달되고 저장됨
# 마찬가지로 args는 변수명이나 관습적으로 *args로 사용함

def total(*args):
    print(type(args))
    sum = 0
    for i in args:
        sum += i
    return sum
print(total())

def add_mul(op,*args):
    if op == 'add':
        result = 0
        for i in args:
            result += i
    elif op == 'mul':
        result = 1
        for i in args:
            result *= i
    return result
print(add_mul('add',1,2,3,4,5))
print(add_mul('mul',2,2,2,2,2))

def calc_sum(name, *args, academy):
    print(f'Name : {name}, Academy : {academy}')
    sum = 0
    for i in args:
        sum += i
    return sum
print('합계 : ', calc_sum('홍길동',1,2,3,4,5, academy='더조은'))