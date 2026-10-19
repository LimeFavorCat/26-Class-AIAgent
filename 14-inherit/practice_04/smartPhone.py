from camera import Camera
from phone import Phone

class SmartPhone(Phone, Camera):
    def __init__(self, phone_number, megapixels, model_name):
        Phone.__init__(self, phone_number)
        Camera.__init__(self, megapixels)
        self.model_name = model_name

    def show_info(self):
        print(f'모델명 : {self.model_name}\n전화번호 : {self.phone_number}\n카메라 화소수 : {self.megapixels}만 화소\n')


