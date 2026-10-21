class A:
    def method(self):
        print('A method')

class B(A):
    def method(self):
        print('B method')

class C(A):
    def method(self):
        print('C method')

class D(B,C):
    def method(self):
        print('D method')

class E(B,C):
    pass

d = D()
e = E()

# MRO(Method Resolution Order) : 다중 상속시 메서드를 찾는 순서
print(D.mro()) # D -> (B, C) -> ((A),)

d.method() # 메서드 검색순서 (1. 자식)
e.method() # 메서드 검색순서 (2. 부모 첫번째 인자부터)
e.method() # 메서드 검색순서 (1. 자식)
e.method() # 메서드 검색순서 (1. 자식)