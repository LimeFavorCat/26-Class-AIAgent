class SeatErr1(Exception):
    def __init__(self, err = '알 수 없는 좌석 에러'):
        super().__init__(err)

class SeatErr2(Exception):
    def __init__(self, err = '알 수 없는 좌석 에러'):
        super().__init__(err)