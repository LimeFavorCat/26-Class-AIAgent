# 영화관 좌석예약 프로그램
from random import randint
from screen import Screen
from error import SeatErr1, SeatErr2

MOVIE = '오딧세이아'
MAX_SEET = 120

screen5 = Screen(MOVIE, MAX_SEET)
while True:
    try:
        user = input('예약할 좌석을 콤마로 구분하여 입력해주세요 : ').replace(' ','').split(',')
        if user == ['']:
            reservation = [randint(-5,MAX_SEET+5) for each in range(5)]
        else:
            reservation = [int(each) for each in user]
    except Exception as e:
        print(f'형식 에러 : {e}')
    else:
        try:
            print(f'예약한 좌석 : {screen5.reserve_seat(reservation)}')
        except (SeatErr1, SeatErr2) as e:
            print(f'[부적절한 좌석] : {e}')