'''
문 : 사용자로부터 전화번호 입력받아 하이픈 제거
'''
user = input('전화번호를 입력해 주세요 : ')
tel = user.replace('-','')

print('숫자로만 구성되어 있는지? ',tel.isdecimal())
print('숫자 0의 갯수 : ',tel.count('0'))