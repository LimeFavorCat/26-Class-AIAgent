import numpy as np
from numpy import random

f1 = random.rand()
print(int(f1* 100))

f2 = np.random.rand(5)
print(f2)

f3 = random.rand(2,3)
print(f3)

f4 = np.random.rand(3,2,3)
print(f4)

# randint() -> 정수생성 
n1 = random.randint(10)
print(n1)

n2 = random.randint(1,10,size=(5,))
print(n2)

n3 = random.randint(1,9, size=(5,5))
print(n3)

n4 = random.randint(1,9,size=(2,3,4))
print(n4)

# randn() 표준정규분포의 난수 생성

weights = random.randn(2,3)
print(weights)