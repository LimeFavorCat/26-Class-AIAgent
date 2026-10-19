'''
* Abstract Class - 추상 클래스
    - 추상 메서드(구현하지 않은 메서드)가 포함되어있는 클래스
    - 추상클래스를 상속받는 클래스는 반드시 추상메서드를 구현해야 한다.
    - 추상클래스는 객체 생성을 할 수 없다.

* 추상클래스를 만드는 방법
    - abc : Abstract Base Class (추상 기본 클래스)의 약자
        파이썬에서 추상 클래스를 정의할 때 사용하는 내장 모듈
        
    - 추상클래스는 import를 반드시 해야한다
        from abc import ABC, abstractmethod
    
        - ABC : 추상클래스는 ABC 클래스를 상속받아야한다.
        - abstractmethod : 추상메소드 위에 @abstractmethod 어노테이션을 달아야 한다
'''

from programmer import Programmer
from farmer import Farmer
from actor import Actor

# 다형성 -> 같은 메서드를 호출했지만 클래스의 종류에 따라 다른 결과가 나오는 것
# p = Programmer('홍길동', 25, 'Python')
# p.introduce()
# p = Actor('고길동', 48, 'sword-master')
# p.introduce()
# p = Farmer('나무', 27, 'tomato')
# p.introduce()

people = [Programmer('홍길동', 25, 'Python'), Actor('고길동', 48, 'sword-master'), Farmer('김철수', 27, 'seeweed')]
for person in people:
    person.introduce()

# 추상클래스는 초기화 불가능
# from person import Person
# p = Person()s

