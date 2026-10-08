price_sell = {'캔 커피':500, '삼각김밥':900, '바나나 우유':800, '도시락':3500, '콜라':700, '새우깡':1000}
price_buy = {'캔 커피':1800, '삼각김밥':1400, '바나나 우유':1800, '도시락':4000, '콜라':1500, '새우깡':2000}

class Counter:
    def __init__(self, price_sell, price_buy):
        self.price_sell = price_sell
        self.price_buy = price_buy
        self.sell = 0
        self.buy = 0
        self.money = 100000

    def item_sell(self, item, count = 1):
        self.money += self.price_sell[item] * count
        self.sell += self.price_sell[item] * count

    def item_buy(self, item, count = 1):
        self.money -= self.price_buy[item] * count
        self.buy += self.price_buy[item] * count

    def print_result(self):
        print(f'오늘의 지출은 {self.buy}원, 매출은 {self.sell}으로 총 잔고는 {self.money}원 입니다.')


pos = Counter(price_sell, price_buy)
pos.item_buy('삼각김밥', 10)
pos.item_sell('바나나 우유', 2)
pos.item_buy('도시락', 5)
pos.item_sell('도시락', 4)
pos.item_sell('콜라')
pos.item_sell('새우깡', 4)
pos.item_sell('바나나 우유', 5)
pos.print_result()

'''
# 일반적인 풀이
money = 100000
sell = 0
buy = 0

buy += 900 * 10
sell += 1800 * 2
buy += 3500 * 5
sell += 4000 * 4
sell += 1500
sell += 2000 * 4
sell += 1800 * 5
money -= buy 
money += sell

print(f'오늘의 지출은 {buy}원, 매출은 {sell}으로 총 잔고는 {money}원 입니다.')
'''