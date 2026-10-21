# 나만의 '커스텀 에러'를 만들어 사용하기

# 방법 1 : 에러 메세지를 던질 때 직접 입력받도록
class BankBalanceError(Exception):
    def __init__(self, message = '계좌의 잔액이 부족하여 출금 불가'):
        super().__init__(message)

'''def deposit(balance, money):
    if money <= 0:
        raise BankBalanceError(f'{money}원 입금 불가 (0원 이하 불가)')

    balance += money
    print(f'입금완료 현재 잔액 {balance:,d}원')
    return balance

def withdraw(balance, money):
    if balance < money:
        raise BankBalanceError()

    balance -= money
    print(f'출금완료 현재 잔액 {balance:,d}')
    return balance

def test():
    balance = 0
    try:
        balance = deposit(balance, -1)
    except BankBalanceError as e:
        print('[계좌 오류]',e)

    try:
        balance = deposit(balance, 1000)
    except BankBalanceError as e:
        print('[계좌 오류]',e)

    try:
        balance = withdraw(balance, 5000)
    except BankBalanceError as e:
        print('[계좌 오류]',e)

    try:
        balance = withdraw(balance, 500)
    except BankBalanceError as e:
        print('[계좌 오류]',e)

    print('\n\n')

test()
'''
# 방법 2
# 출금용과 입금용 커스텀 에러 클래스를 따로 정의
class BankDepositError(Exception):
    def __init__(self):
        super().__init__('0이하의 금액 출금 불가')

class BankWithdrawError(Exception):
    def __init__(self):
        super().__init__('계좌의 잔액이 부족하여 출금 불가')

def deposit(balance, money):
    if money <= 0:
        raise BankDepositError()

    balance += money
    print(f'입금완료 현재 잔액 {balance:,d}원')
    return balance

def withdraw(balance, money):
    if balance < money:
        raise BankWithdrawError()

    balance -= money
    print(f'출금완료 현재 잔액 {balance:,d}')
    return balance

def test():
    balance = 0
    try:
        balance = deposit(balance, -1)
    except (BankDepositError,BankBalanceError) as e:
        print('[계좌 오류]',e)

    try:
        balance = deposit(balance, 1000)
    except (BankDepositError,BankBalanceError) as e:
        print('[계좌 오류]',e)

    try:
        balance = withdraw(balance, 5000)
    except (BankDepositError,BankBalanceError) as e:
        print('[계좌 오류]',e)

    try:
        balance = withdraw(balance, 500)
    except (BankDepositError,BankBalanceError) as e:
        print('[계좌 오류]',e)

    print('\n\n')

test()