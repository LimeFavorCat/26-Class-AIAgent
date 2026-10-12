"""
19세 이상 -> 성년
15세 ~ 18세 -> 청소년
15세 미만 -> 어린이
"""

age = int(input('나이를 입력해주세요 : '))
if age >= 19: print('성인')
elif age >= 15: print('청소년')
elif age >= 0: print('어린이')