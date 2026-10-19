from person import Person

class Farmer(Person):
    def __init__(self, name, age, crop):
        super().__init__(name, age, job = '농부')
        self.__crop = crop

    def introduce(self):
        print(f'안녕 난 {super().get_name()}라고 해! 나는 {self.__crop}을 기르는 {super().get_job()}야\n')
    