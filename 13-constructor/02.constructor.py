# constructor의 매개변수에도 기본값을 넣을 수 있다
class Car:
    def __init__(self, speed=10, color='black', model='sonata'):
        self.speed = speed
        self.color = color
        self.model = model
    def output(self):
        print('모델 :', self.model)
        print('색상 :', self.color)
        print('속도 :', self.speed)
        print()

mycar = Car()
mycar2 = Car(model='E-class')

mycar.output()
mycar2.output()