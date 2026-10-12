# 중첩 for문

for i in range(3):
    for j in range(2):
        print(f'i = {i}, j = {j}')
print('-' * 30)

for dan in range(2,10):
    print('  ', dan, '단')
    for mul in range(1,10):
        print(dan, 'x', mul, '=', dan * mul)
    print('-' * 10)

# 세로로 출력하기
line = '\n|' + '--------------|' * 8

print(line)
for i in range(1, 10):
    print('| ', end=' ')
    for j in range(2, 10):
        print(j, 'x', i, '=', format(i * j,'2d'), end='  |  ')
    print(line)