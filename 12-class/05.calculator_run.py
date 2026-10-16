# 다른 클래스를 사용할 때 파이썬의 변수 작명규칙을 따르지 않으면 불편해진다.
# 이름 = __import__("모듈 경로") 형식으로 임포트는 가능하다

# 1) import 파일명
import calculator05
cal1 = calculator05.Calculator()
print(cal1.plus(10,40))

# 2) from 파일명 import 클래스명
from calculator05 import Calculator
cal2 = Calculator()
print(cal2.plus(5,5))
print(cal2.plus(10,20))

# 3) from 파일명 import 클래스명 as 별칭
from calculator05 import Calculator as c
cal3 = c()
print(cal3.plus(9, 11))