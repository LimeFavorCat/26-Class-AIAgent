from datetime import date

# 오늘 날짜 출력
print(date.today())

# 데이트형 변수
start_d = date(2026, 10, 8)
print(start_d)

# 각 요소 가져오기
print(f'이 수업은 {start_d.year}년 {start_d.month}월 {start_d.day}일에 시작되었습니다.')

# 포맷 바꾸기
print(f'{start_d:%Y/%m/%d}')
print(f'{start_d:%y/%m/%d}') # y 소문자 표기시 두 자리만 출력