# 문1 : 삼각형의 넓이 구하는 파일(class) 생성
from practice_math import Square

sq1 = Square(100, 50)
print(sq1.calc_extent())

# 문2 : 별도의 클래스에 메소드 2개 만들기
#           메소드 1 : 이름, 파이썬 점수, AI 점수를 사용자로부터 입력받기
#           메소드 2 : 출력문

from practice_math import Student

st1 = Student()
st1.set('김수영',{'파이썬':98,'AI':79})
st2 = Student()
st2.set('홍길동',{'파이썬':100,'AI':99})


st1.display_score()
st2.display_score()