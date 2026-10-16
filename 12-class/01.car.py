'''
함수와 모듈명은 숫자로 시작할 수 없기 때문에 임포트 과정이 복잡해진다 -> mymodule = __import__('11-file/07.json_read.py')

* 파일명은 소문자로 시작, 객체는 대문자로 시작

* 클래스 선언
    class 클래스명:
        메서드 생성
        or
        pass -> 빈 상태로 만들 때 사용(임시 점유용 키워드)

* 매개변수 self
    자기 자신의 객체를 의미
    클래스 안에서 함수를 호출할 때

    이름이 반드시 self일 필요는 없다.
    그러나 보통 self를 많이 사용
'''
class vehicle:
    def __init__(self):
        self.material = 'iron'

class Car(vehicle):
    def set1(self):
        self.model = 'sm7'
        self.color = 'blue'
        self.speed = 10

    def changeSpeed(self, speed):
        self.speed = speed

    def output(self):
        print('재질 :',self.material)
        print('모델 :',self.model)
        print('색상 :',self.color)
        print('속도 :',self.speed)
        print()

myCar = Car()
myCar.set1() # 호출할 때 변수가 생성되면서 초기화가 됨
myCar.output()
myCar.changeSpeed(50)
myCar.output()

print(myCar.model)
print(myCar.color)
print(myCar.speed)
print(myCar.material)