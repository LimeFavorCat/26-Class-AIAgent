from person import Person

class Actor(Person):
    def __init__(self, name, age, film):
        super().__init__(name, age, job = '배우')
        self.__film = film

    def introduce(self):
        print(f'안녕하세요 {super().get_job()} {super().get_name()}입니다. 이번에 {self.__film}로 인사드리게 되어 대단히 반갑습니다.\n')