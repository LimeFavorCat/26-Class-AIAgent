# 클래스, 튜플 사용
class Student():
    def __init__(self):
        self.subject = []

    def add_subject(self, subject, credit, score):
        self.subject.append((subject, credit, score))

    def total_point(self):
        sum = 0
        for i in self.subject:
            sum += i[1] * i[2]
        return sum

    def total_credit(self):
        sum = 0
        for i in self.subject:
            sum += i[1]
        return sum

    def avg_credit(self):
        return self.total_point() / self.total_credit()
    
kim = Student()
kim.add_subject('python', 3, 4.5)
kim.add_subject('os', 2, 3.0)
kim.add_subject('AI', 3, 4.0)


print(kim.total_credit())
avg = kim.avg_credit()
t = int(avg//0.5)*2
print(format(avg,'.2f'), '(' + ' F FD0D+C0C+B0B+A0A+'[t:t+2] + ')') # ㅋㅋㅋ



"""

# 일반적 풀이

python = 3
os = 2
ai = 3

A = 4.5
A0 = 4.0
B = 3.5
B0 = 3

total_points = (python * A) + (os * B0) + (ai * A0)
total_credits = python + os + ai
avg_credits = total_points / total_credits

print(f'총 이수 학점 : {total_credits}')
print('평균 학점 :',format(avg_credits,'.2f'), end = ' ')

t = int(avg_credits//0.5)

grade = ' F FD0D+C0C+B0B+A0A+'
print(f'({grade[t*2:t*2+2]})')

"""