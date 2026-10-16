'''
* 클래스 변수 : 모든 객체가 변수를 공유
    - class 바로 밑에서 선언
    - 사용할 때 : 클래스이름.변수명

* 인스턴스 변수 : 자기자신의 객체에서만 사용
    - 함수 안에서 선언 : self.변수명
    - 사용법 : 객체명.변수명
'''

class Car:
    maker = '삼성르노'
    num = 0
    def __init__(self):
        Car.num += 1
        self.model = 'sm5'
        self.color = 'blue'
        self.speed = 15

    def speedUp(self):
        self.speed += 10

    def speedDown(self):
        self.speed -= 10

    def output(self):
        print('제조사 : ', self.model)
        print('제조사 : ', self.color)
        print('제조사 : ', self.speed)
        print()

print(f'제조사는 {Car.maker}입니다. 현재 {Car.num}대 출차')

mycar = Car()
mycar.output()

print(f'제조사는 {Car.maker}입니다. 현재 {Car.num}대 출차')

yourcar = Car()
yourcar.speedUp()
yourcar.output()

print(f'제조사는 {Car.maker}입니다. 현재 {Car.num}대 출차')

mycar.speedDown()
yourcar.speedUp()
mycar.output()
yourcar.output()


Car.maker = '기아'
print(f'제조사는 {Car.maker}입니다. 현재 {Car.num}대 출차')
print(mycar.maker)
mycar.maker = '삼성'
print(Car.maker)
print(mycar.maker)