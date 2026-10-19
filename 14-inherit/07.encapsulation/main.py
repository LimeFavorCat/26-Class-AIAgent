'''
1. 각 클래스의 모든 인스턴스 변수는 private로 변경
2. 추상클래스를 제외한 모든 클래스에서 추상 클래스의 인스턴스 변수를 호출하여 
'''

from programmer import Programmer
from farmer import Farmer
from actor import Actor

people = [Programmer('홍길동', 25, 'Python'), Actor('톰 홀랜드', 48, '오딧세이아'), Farmer('안나', 27, '옥수수')]
for person in people:
    person.introduce()
