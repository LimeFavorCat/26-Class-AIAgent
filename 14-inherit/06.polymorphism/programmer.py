from person import Person

class Programmer(Person):
    def __init__(self, name, age, language):
        super().__init__(name, age, job='프로그래머')
        self.language = language

    def introduce(self):
        super().hello()
        print(f'{self.language} 언어를 사용합니다.')