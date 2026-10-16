class HelloWorld:
    msg = 'Python' # 클래스 변수
    def setEng(self):
        self.msg = 'Hello Python' # 인스턴스 변수
        
    def setKor(self):
        self.msg = '안녕하세요 파이썬' # 인스턴스 변수

    def setLocal(self):
        msg = '파이썬 수업' # 지역 변수 - 메서드 안에서만 사용가능
        return msg
    
    def sayHello(self):
        print(HelloWorld.msg)
        print(self.msg)
        print()
        # print(msg) # 지역변수 호출 안됨

hell = HelloWorld()
hell.sayHello()

hell.setEng()
hell.sayHello()

hell.setKor()
hell.sayHello()

print(hell.setLocal())