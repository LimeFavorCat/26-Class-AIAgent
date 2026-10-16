# 클래스(static) 메서드
#   공동으로 사용

'''
* self를 안 쓸때
    - 정적 메서드로 사용시 @(annotaion) 사용해서 staticmethod 부여 
    
    class Car:
        @staticmethod
        def [메서드 이름]
    
    - 호출시
    Car.[메서드 이름]
    객체 생성 이름.[메서드 이름]
        
'''

class Calc:
    def plus(self, x,y):
        print('인스턴스 메서드 호출')
        return x + y

    @staticmethod # <- 해당 annotation 안 넣으면 매개변수 첫자리에 객체를 받는 self를 포함시키기 때문에 에러남(매개변수 부족)
    def plus_static(x,y):
        print('static 메서드 호출')
        return x + y

    def minus(self, x, y):
        return x - y

    def result(self, x, y):
        result1 = Calc.plus_static(x,y)
        result2 = self.plus(x,y)
        return result1 + result2   

# print(Calc.plus_static(100,50))

# cal1 = Calc()
# print(cal1.plus(1,2))

# print(cal1.plus_static(5,5))

cal2 = Calc()
print(cal2.plus_static(100,50))