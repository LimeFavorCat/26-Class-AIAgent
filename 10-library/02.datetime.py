from datetime import datetime

# 현재시간
print(datetime.now())

d = datetime(2026, 10, 8, 10, 0, 0)
print(d)

d = datetime(2026, 10, 8)
print(d)

d = datetime(2026, 10, 8, 10, 30, 12)
print(d)
print('-'*30)

print(f'{d.hour}:{d.minute}:{d.second}')

# H : 24시간제
print(f'{d:%Y/%m/%d}')

# I : 12시간제, p:AM, PM
print(f'{d:%H:%M:%S}')

# I : 12시간제, p:AM, PM
print(f'{d:%I:%M:%S %p}')
print('-'*30)


day1 = datetime(2026, 10, 1)
day_num = datetime.now() - day1
print(day_num)

day_num = (datetime.now() - day1).days # datetime.days -> 일수
print(f'경과한 일 수 : {day_num}일')