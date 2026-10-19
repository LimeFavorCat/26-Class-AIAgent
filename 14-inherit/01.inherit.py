# 상속 : 부모 클래스의 메서드와 변수를 자식도 사용할 수 있다.

class CalcParent:
    def plus(self,x,y):
        print('부모 클래스의 plus()')
        return x + y
    
    def minus(self,x,y):
        print('부모 클래스의 minus()')
        return x - y

class ClacChild(CalcParent): # CalcParent를 상속받음
    def multi(self,x,y):
        print('자식 클래스의 multi()')
        return x * y
    
    def divide(self,x,y):
        print('자식 클래스의 divide()')
        return x / y

    def plus(self,x,y):
        print(f'{super().plus(x,y)}')
        print('자식 클래스의 plus()')
        return (x + y) * 2

cal1 = ClacChild()
print(cal1.multi(2,3))
print(cal1.minus(5,4))
print(cal1.plus(2,4))

cal2 = CalcParent()
print(cal2.plus(3,5))