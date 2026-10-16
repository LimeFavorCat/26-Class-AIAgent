import calendar

# 달력 출력
print(calendar.calendar(2026))
print(calendar.calendar(2025))
print(calendar.calendar(2026,4))
print(calendar.month(2025,10))

# 윤년 확인
year = int(input('년도 입력 : '))
if calendar.isleap(year):
    print(f'{year}년은 윤년입니다')
else:
    print(f'{year}년은 평년입니다.')