score = 81

if score >= 90: # 90이상인 모든 값 (91, 100, 100000)
    print('A학점')
else :          # 90미만인 모든 값 (89, 62, 0, -1, -142.231)
    if score >=80: # 90미만 ~ 80이상
        print('B학점')
    else:
        if score >= 70:
            print('C학점')
        else:
            if score >= 60:
                print('D학점')
            else:
                print('F학점')

# 더 직관적인 표기법
if score >= 90:
    print('A학점')
elif score >= 80:
    print('B학점')
elif score >= 70:
    print('C학점')
elif score >= 60:
    print('D학점')
else:
    print('F학점')

# 자율 - match-case 써보기
score //= 10
match score:
    case 10, 9:
        print('A학점')