'''
은행 : 개설할 때 계좌주 이름과 초기 예금액을 넣어줌
        입금하면 잔고 변경
        출금 잔고 변경
'''

class Account:
    def __init__(self, user_name, money):
        self.user_name = user_name
        self.__money = money

    def deposit(self, amount):
        self.__money += amount
        print(f'{amount:3,d}원 입금되었습니다.\n잔액 : {self.__money:3,d}\n')

    def exposit(self, amount):
        if amount > self.__money:
            print('잔액 부족')
            return
        else:
            self.__money -= amount
            print(f'{amount:3,d}원 출금되었습니다.\n잔액 : {self.__money:3,d}\n')

user1 = Account('홍길동', 1000000)
user1.deposit(100000)
user1.exposit(1000000)
user1.exposit(1000000)
