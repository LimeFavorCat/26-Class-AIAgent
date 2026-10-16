'''
import 모듈명
    -> 모듈명.명령어

from 모듈명 import 함수, 클래스명
'''
"""
import random
print(random.__file__) # 패키지의 __file__ 메서드는 파일 위치를 출력한다
"""
from random import random, randint, randrange, sample


print(random())
print(randint(1,100))
print(randrange(2,100,2))
print(sample(['사과', '바나나', '오렌지', '망고'],2))

for i in range(1000):
    print(chr(randint(65,90)),end='')