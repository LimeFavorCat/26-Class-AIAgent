class Car:
    def __init__(self, speed = 15, color = 'white', model = 'E-class'):
        self.speed = speed
        self.color = color
        self.model = model

    def output(self):
        print('속도 :',self.speed)
        print('색상 :',self.color)
        print('모델 :',self.model)
        print()

    def __str__(self):
        result = f'속도 : {self.speed}, 색상 : {self.color}, 모델 : {self.model}'
        return result


myCar = Car()
myCar.output()

print(myCar)