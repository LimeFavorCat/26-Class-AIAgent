from error import SeatErr1, SeatErr2

class Screen:
    def __init__(self, movie:str, max_seat:int):
        self.movie = movie
        self.max_seat = max_seat
        self.remain_seat = [0 for i in range(max_seat)]

    def reserve_seat(self, seats:list[int]) -> tuple:
        # 좌석 확인
        complete = []
        for seat in seats:
            if not 0 <= seat < self.max_seat:
                raise SeatErr1(f'{seat} - 존재하지 않는 좌석입니다.')
            if self.remain_seat[seat] == 1:
                raise SeatErr2(f'{seat} - 이미 예약된 좌석입니다')
            else:
                print(f'{seat}번 좌석 예약가능')
                complete.append(seat)

        # 예약 반영
        try:
            for i in complete:
                self.remain_seat[i] = 1
            print(f'예약완료! 영화 : {self.movie}')
            return tuple(complete)
        except:
            raise SeatErr1('예약 정보 반영중 에러발생')