from abc import ABC, abstractmethod

class Person(ABC):
    def __init__(self, name, age, job=None):
        self.__name = name
        self.__age = age
        self.__job = job

    # getter 메서드 --- 조회용
    def get_name(self):
        return self.__name
    
    def get_age(self):
        return self.__age
    
    def get_job(self):
        return self.__job

    # setter 메서드 --- 설정용
    def set_age(self, age):
        if age < 0:
            print('나이에는 0 이상의 값을 넣어주세요')
        else:
            self.__age = age
            print(f'{self.__name}의 나이가 {self.__age}세로 업데이트 되었습니다.')

    def set_job(self,job):
        self.__job = job
        print(f'{self.__name}의 직업이 {self.__job}으로 업데이트 되었습니다.')


    def hello(self):
        print(f"\n안녕하세요 저는 {self.__name}입니다.")

    @abstractmethod
    def introduce(self):
        pass


    # 추상메소드는 자식클래스에서 오버라이딩 했는지만 검사. 부모 클래스에서 기능을 구현해도 실행가능
    # @abstractmethod
    # def info(self):
    #     print('이 메서드는 자기소개 입니다')