from person import Person

class Programmer(Person):
    def __init__(self, name, age, language):
        super().__init__(name, age, job='프로그래머')
        self.__language = language

    def introduce(self):
        print(f'전 {super().get_job()} {super().get_name()}이고, {self.__language} 언어를 사용합니다.\n')