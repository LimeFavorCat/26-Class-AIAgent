"""
한 과일 가게의 현재 과일 재고 수량이 다음과 같이 저장되어 있다
inventory = {'apple':15, 'banana':8, 'orange':20, 'melon':3}

문1. 가게에 포도가 12개 새로 들어왔다
문2. 손님이 망고가 있는지 물어보았다
문3. 오늘 마감 전 현재 가게에 남아있는 모든 과일의 이름과 재고 수량을 아래 보기와 같은 형식으로 한줄씩 출력하는 코드를 작성
"""

# 조건
inventory = {'apple':15, 'banana':8, 'orange':20, 'melon':3}


# 일반적인 풀이
inventory['mango'] = 12

print(f'재고가 {inventory['mango']}개 있습니다' if inventory.get('mango') else '재고가 없습니다')

for fruit, count in inventory.items(): print(f'과일 : {fruit} | 재고 : {count}')


# 클래스를 써보기
class Shop:
    def __init__(self,name, inventory, cash):
        self.name = name
        self.inventory = inventory
        self.cash = cash

    def add_item(self,item,count):
        if item in self.inventory:
            self.inventory[item] += count
        else:
            self.inventory[item] = count

    def check_item(self,item):
        if item in self.inventory:
            print(f'현재 {item}은 {inventory[item]}개 있습니다.')
            return item, inventory[item]
        else:
            print(f'현재 {item}의 재고가 없습니다.')
            return item, 0

    def items(self):
        print(f"현재 {self.name} 가게의 재고")
        return

class Fruit_shop(Shop):
    def __init__(self, name, inventory, cash):
        super().__init__(name, inventory, cash)

    def items(self):
        super().items()
        for fruit, count in self.inventory.items(): print(f'과일 : {fruit} | 재고 : {count}')
        return 

building1 = Fruit_shop('과일장수', inventory, 30)
building1.add_item('apple',15)
building1.add_item('apple_mango',15)
building1.check_item('shine_musket')
building1.check_item('apple_mango')
building1.items()