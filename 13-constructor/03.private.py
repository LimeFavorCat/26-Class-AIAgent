# private : 외부에서 접근 못하게 막음
# getter 메서드 : private로 막힌 변수를 외부에서 조회 가능하도록 해주는 메서드
# setter 메서드 : private로 막힌 변수를 외부에서 설정 가능하도록 해주는 메서드

# private - getter, setter는 보통 세트메뉴

class Cat:
    def __init__(self, speed = 15, color = 'orange', model ='long-nose', maker = 'cheeze'):
        self.speed = speed
        self.color = color
        self.model = model
        self.__maker = maker
        pass

    def ouput(self):
        print('속도 :',self.speed)
        print('색상 :',self.color)
        print('품종 :',self.model)
        print('어미 :',self.__maker)

    def get_maker(self):
        return self.__maker

    def secret_of_birth(self, maker):
        self.__maker = maker

myCat = Cat()
myCat.ouput()

print(myCat.speed)
print(myCat.color)
print(myCat.model)
# print(myCat.__maker) # private라 접근불가
print(myCat.get_maker()) # getter 메서드를 추가해서 접근

myCat.speed = 50
myCat.__maker = 'navi' # private라 변경 불가
print(myCat.get_maker())
myCat.secret_of_birth('navi')
print(myCat.get_maker())
