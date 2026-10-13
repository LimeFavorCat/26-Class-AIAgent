str_tup = ('국어', 'Python', 'AI', '수학', '영어')

print(str_tup[2])
print(str_tup[::2])
print(str_tup[::-1])

print(str_tup.index('Python')) # 없는 걸 참조하면 오류

tup1 = (1,2,3,4,5)
print('%d %d %d %d'%(tup1[0],tup1[4],tup1[2],tup1[1]))
print(f'{tup1[0]} {tup1[4]} {tup1[2]} {tup1[1]}')
print('{0} {3} {2} {1}'.format(tup1[0],tup1[1],tup1[2],tup1[4]))

# 언팩킹 : 튜플의 포장을 풀어서 안의 내용만 출력
# *변수명
# print('{} {} {}'.format(tup1,1,1)) # 에러난다 (튜플 하나만 들어있어서 두번째 중괄호가 읽으려다 뭐가 없음) IndexError: Replacement index 1 out of range for positional args tuple
print('{} {} {}'.format(*tup1))
print('{} {} {}'.format(tup1,2,3))
print(*tup1[:3]) # 싹다 쪼개서 가져온다
print(tup1[:3]) # 튜플을 유지한채 가져온다
print('-' * 30)

tup2 = (34.234, 2.222, 45.452, 1421.31421, 9911.1123)
print('{:.2f} {:.2f} {:.2f} {:.2f}'.format(*tup2))
print('{1:.2f} {0:.2f} {2:.2f} {3:.2f}'.format(*tup2))

for i in range(len(tup2)):
    if i < len(tup2) -1:
        print('{:.2f}'.format(tup2[i]), end=', ')
    else:
        print('{:.2f}'.format(tup2[i]))
print('-' * 30)

# join() : 여러개의 문자열을 하나로 합칠 때 사용하는 문자열 메서드(함수)
#         '구분자'.join(문자열이 담긴 리스트나 튜플)

words = ['python', 'is', 'fun']
print(" ".join(words))

print('-'.join(words))
print(', '.join(f'{x:.2f}' for x in tup2))
print('-' * 30)

tup3= (10,20,30)
a,b,c = tup3
print(tup3)
print(a,b,c)