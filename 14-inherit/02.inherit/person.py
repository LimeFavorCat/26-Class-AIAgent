class Person:
    def __init__(self, name, age, job = None):
        self.name = name
        self.__age = age
        self.job = job

    def __str__(self):
        return f'Name : {self.name}\nAge : {self.__age}\nJob : {self.job}\n'

    def hello(self):
        print(f"Hello, I'm {self.name}")

    def update_age(self, age):
        if age < 0:
            print('나이는 음수일 수 없습니다.')
        else:
            self.__age = age
            print(f'현재 나이는 {self.__age}세 입니다.')

if __name__ == '__main__':
    p1 = Person('홍길동', 25, '의적')
    print(p1)

    p1.hello()
    print(dir(p1)) # 기존 self.__age -> 맹글링으로 인해 p1 객체 안에 _Person__age 형태로 인스턴스 변수 생성
    p1.__age = -7 # 오류x -> 객체에 새로운 인스턴스 변수 __age 생성
    print(f'나이는{p1.__age}세') # 지역변수의 값이 출력됨
    print(dir(p1)) # 클래스의 private 변수는 그대로
    print(p1)
    p1.update_age(-4)
    p1.update_age(30)
    __age = -8 # 오류x -> 새로운 객체 생성
    print(id(__age),id(p1.__age))
    print(dir(p1))

# print(dir(p1)) 
# print(p1.__age)
# print(__age) # if문 밖에서도 객체는 그대로 (if문 자체는 )