"""
2차원 리스트로

과정    파이썬 AI 빅데이터 디자인 합계 평균
홍길동
아무개
이순신
------------------------------------
합계
평균
"""

"""일반적인 풀이"""
"""
students = [['홍길동',10,10,10],['아무개',80,97,90],['이순신',99,95,98]]
class_name = ['파이썬', 'AI', '디자인']

# 평균 및 총점 계산
for student in students:
    if len(student) == 4:
        # 총점 추가하기
        student.append(0)
        for i in range(len(class_name)): student[4] += student[i+1]
    # 평균 추가하기
    student.append(student[4]/len(class_name))

# 결과 출력
print('과정', end='  ')
for i in class_name:
    print(i, end='  ')
print('합계  평균')
print('-' * 50)

for student in students:
    for content in student:
        print(content, end = '   ')
    print()
print('-' * 50)

print('합계', end='     ')
for i in range(len(class_name)):
    score_sum = 0
    for student in students:
        score_sum += student[i+1]
    print(score_sum, end='     ')
print()


print('평균', end='   ')
for i in range(len(class_name)):
    score_sum = 0
    for student in students:
        score_sum += student[i+1]
    print(format(score_sum/len(students),'.2f'), end='   ')
print()
"""

"""클래스를 활용한 풀이"""

"""
class Student:
    def __init__(self, name, score):
        self.name = name
        self.score = score
        self.sum = sum(score)
        self.average = sum(score) / len(score)

    def print_score(self):
        print(self.name, end=' ')
        for each in self.score:
            print(format(each,'6d'),end='  ')
        print(format(self.sum,'7d'), end='  ')
        print(format(self.average,'6.2f'))
        return

students = [Student('홍길동',[10,10,10]), Student('아무개',[95,72,88]), Student('이순신',[100,100,100])]
class_name = ['파이썬', 'AI', '디자인']


print("\n과정   파이썬   빅데이터   AI     합계    평균\n" + '-' * 50)

for student in students:
    student.print_score()
print('-' * 50)

# 합계 점수 및 평균 구하기
result = [0, 0, 0]
for student in students:
    for i in range(len(class_name)):
        result[i] += student.score[i]
print(f'합계      {result[0]}     {result[1]}     {result[2]}', )
print(f'평균    {result[0]/len(class_name):.2f}   {result[1]/len(class_name):.2f}   {result[2]/len(class_name):.2f}', )
"""

"""확장 : random 활용하여 과목수 제한x, 양식 유지"""
import random


class Student:
    def __init__(self, name, score):
        self.name = name
        self.score = score
        self.sum = sum(score)
        self.average = sum(score) / len(score)

    def print_score(self):
        print(format(self.name,'4s'), end='')
        for each in self.score:
            print(format(each,'8d'),end='   ')
        print(format(self.sum,'7d'), end='  ')
        print(format(self.average,'9.2f'))
        return
    
# 랜덤 성적 만들기 (양식 테스트용)
def randscore() -> list[int]:
    return [random.randint(1,100) for i in range(len(class_name))]

# 과목 점수 합계 구하기
def calculate_total(std:list[Student]) -> list[int]:
    result = [0 for i in range(len(class_name))]
    for student in std:
        for i in range(len(class_name)):
            result[i] += student.score[i]
    return result


class_name = ['파이썬', 'AI', '디자인', '수학', 'REA', '테니스', ' 사격']
students = [Student('홍길동',randscore()), Student('아무개',randscore()), Student('이순신',randscore())]

# 출력부
print('\n'+'-' * 120)
for i in ['과정'] + class_name + ['합계', '평균']:
    print(format(i,'9s'), end='')
print('\n'+'-' * 120)

for student in students:
    student.print_score()
print('-' * 120)


result = calculate_total(students)

print('합계', end='   ')
for i in result: print(format(i,'8d'), end='   ')

print('\n평균', end='   ')
for i in result: print(format(i/len(students),'8.2f'), end='   ')

