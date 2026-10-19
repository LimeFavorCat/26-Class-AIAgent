from person import Person

class Actor(Person):
    def __init__(self, name, age, film):
        super().__init__(name, age, job = '배우')
        self.film = film

    def introduce(self):
        super().hello()
        print(f'나의 대표작은 {self.film} 입니다')