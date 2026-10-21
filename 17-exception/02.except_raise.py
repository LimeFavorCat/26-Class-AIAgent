# 원하는 시점에 강제로 에러를 발생시킴

def set_age(age):
    if age<0:
        raise ValueError('나이는 0보다 작을 수 없습니다')
    print(f'나이가 {age}로 업데이트 되었습니다')

try:
    set_age(-5)
except ValueError as e:
    print(f'경고 발생 : {e}')
