# 생성자를 사용해 클래스를 바로 초기화할 수 있다.

class Car:
    def __init__(self, model, color, speed):
        print('생성자 호출')
        self.model = model
        self.color = color
        self.speed = speed

    def output(self):
        print('모델 :',self.model)
        print('색상 :',self.color)
        print('속도 :',self.speed)
        print()

myCar1 = Car('sm5', 'red', 20)
myCar1.output()

myCar2 = Car('E-class', 'blue', 20)
myCar2.output()

myCar2.__init__('H-class', 'white', 20)
myCar2.output()