class Calculator:

    def plus(self,x,y):
        return x + y
    
    def minus(self,x,y):
        return x - y
    
    def multi(self,x,y):
        return x * y
    
    def divide(self,x,y):
        return x / y

if __name__ == '__main__':
    cal1 = Calculator()
    print(cal1.plus(5,5))
    print(cal1.minus(5,5))
    print(cal1.multi(5,5))
    print(cal1.divide(5,5))