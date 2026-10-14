st1 = '12345'
st2 = 'PythonAI'
st3 = 'Python Ai'
st4 = "삶에 대한 절망 없이는 삶에 대한 사랑이 없다"
st5 = '1234abcd'

# 숫자만으로 구성되어 있는지 검사
print('숫자로만 구성되어 있는가? ', st1.isdigit())
print('숫자로만 구성되어 있는가? ', st2.isdigit())
print('숫자로만 구성되어 있는가? ', st5.isdigit())
print()

# 문자만으로 구성되어 있는지 검사
print('문자로만 구성되어 있는가? ', st1.isalpha()) # 숫자라 False
print('문자로만 구성되어 있는가? ', st2.isalpha()) # True
print('문자로만 구성되어 있는가? ', st3.isalpha()) # 공백이 있어서 False
print('문자로만 구성되어 있는가? ', st4.replace(' ','').isalpha()) # 한글도 True
print()

# 숫자나 문자로 구성되어 있는지 검사
print('숫자나 문자로만 구성되어 있는가? ', st1.isalnum())
print('숫자나 문자로만 구성되어 있는가? ', st2.isalnum())
print('숫자나 문자로만 구성되어 있는가? ', st3.isalnum())
print('숫자나 문자로만 구성되어 있는가? ', st5.isalnum())
print()

# 문자열이 소문자 /대문자인지 검사
print('aaa'.islower()) # True
print('aaa'.isupper()) # False
print(st3.lower().islower()) # True

# 문자열이 공백문자인지 검사
st6 = '            '
print('문자열이 공백문자인가? ', st6.isspace())
print('문자열이 공백문자인가? ', st3.isspace())

# 단어의 첫 문자만 대문자인지 검사
print('단어의 첫 글자만 대문자인가? ',st2.istitle())
print('단어의 첫 글자만 대문자인가? ',st3.istitle())
print('단어의 첫 글자만 대문자인가? ',st4.istitle())
print()

# 빈자리를 0으로 채우기
st1 = 'Hello Python!!!'
st2 = st1.zfill(20)
print(st1)
print(st2)
