from person import Person

class Farmer(Person):
    def __init__(self, name, age, crop):
        super().__init__(name, age, job = '농부')
        self.crop = crop

    def introduce(self):
        super().hello()
        print(f'내 주종 작물은 {self.crop}야')
    