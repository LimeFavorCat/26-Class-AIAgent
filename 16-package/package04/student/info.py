from .score import average
from .grade import grade

class Student:
    def __init__(self, name, score):
        self.name = name
        self.score = score

    def info(self):
        score = average(*self.score)
        print(f'이름 : {self.name}\n평균점수 : {score}\n학점 : {grade(score)}')