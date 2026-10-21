# 다른 모듈 import
import random
import math

# 전역변수
count = 0

# 상수
PI = 3.141592
MAX_SIZE = 100

# 자료구조
fruits = ['사과', '배', '포도']
student_info = {'name':'더조은',
                'age': 20
                }

# 함수
def add(x,y):
    return x + y

def sub(x,y):
    return x - y

def random_num():
    return random.randint(1,9)

# 클래스
class Student:
    def __init__(self, name, age):
        self.name = name
        self.age = age

    def introduce(self):
        print(f'이름 : {self.name}, 나이 : {self.age}세')

    @staticmethod
    def hello():
        print('안녕')

# 클래스 상속
class Tjoeun(Student):
    def __init__(self, name, age, language):
        super().__init__(name, age)
        self.language = language

    def program(self):
        print(f'{self.name} 은 {self.language} 언어를 사용 가능합니다.')


# 람다함수 / comprehension 등등
lm = [(lambda x : x**2)(5) for i in range(10)]

