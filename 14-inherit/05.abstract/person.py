from abc import ABC, abstractmethod

class Person(ABC):
    def __init__(self, name, age, job=None):
        self.name = name
        self.age = age
        self.job = job

    def hello(self):
        print(f"안녕하세요 저는 {self.name}입니다.")

    @abstractmethod
    def introduce(self):
        pass


    # 추상메소드는 자식클래스에서 오버라이딩 했는지만 검사. 부모 클래스에서 기능을 구현해도 실행가능
    # @abstractmethod
    # def info(self):
    #     print('이 메서드는 자기소개 입니다')