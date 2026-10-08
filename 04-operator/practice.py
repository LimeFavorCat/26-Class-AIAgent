'''
문
파운드와 킬로그램을 상호 변환하는 프로그램 만들기
'''
# 한줄로 만들기
print('킬로그램(kg)을 파운드(b)로 변환한 결과 : {} b\n파운드(b)를 킬로그램(kg)으로 변환한 결과 : {} kg'.format(float(input("킬로그램 단위를 입력해주세요 : ")) * 2.204623, float(input("파운드 단위를 입력해주세요 : "))* 0.453592))

# 정상적인 결과물
kg = float(input("킬로그램 단위를 입력해주세요 : "))
b = float(input("파운드 단위를 입력해주세요 : "))

result = f'킬로그램(kg)을 파운드(b)로 변환한 결과 : {kg * 2.204623} b\n파운드(b)를 킬로그램(kg)으로 변환한 결과 : {b * 0.453592} kg'
print(result)

# 클래스 활용
class Convert:
    def __init__(self, kg, b):
        self.kg = kg
        self.b = b

    def kg2b(self):
        result = self.kg * 2.204623
        return result

    def b2kg(self):
        result = self.b * 0.453592
        return result
        
conv = Convert(float(input("킬로그램 단위를 입력해주세요 : ")), float(input("파운드 단위를 입력해주세요 : ")))
print(f'킬로그램을 파운드로 변환한 결과 : {conv.kg2b()}')
print(f'파운드를 킬로그램으로 변환한 결과 : {conv.b2kg()}')