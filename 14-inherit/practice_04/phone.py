class Phone:
    def __init__(self, phone_number):
        self.phone_number = phone_number

    def call(self, target_number):
        print(f'{target_number} 번호로 전화를 겁니다.')