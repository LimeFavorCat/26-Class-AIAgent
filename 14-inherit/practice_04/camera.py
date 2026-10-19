class Camera:
    def __init__(self, megapixels):
        self.megapixels = megapixels

    def take_photo(self):
        print(f'{self.megapixels}만 화소로 사진을 촬영합니다.')