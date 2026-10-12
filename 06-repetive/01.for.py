str = 'abcdefg'
for x in str:
    print(x)

num = [0,91.2,4,159]

for i in num:
    print(i)
print('-' * 30)

# range 함수 
# range(시작값, 종료값, step)
# range(종료값) -> default 시작값 = 0, step = 1
for i in range(5):
    print(i)

for i in range(5,10):
    print(i)
print('-' * 30)

for i in range(0,10,2):
    print(i)

for x in range(1, 20, 2):
    print(x, end=', ')
print()

for x in range(1, 20, 2):
    if x != 19:        
        print(x, end=', ')
    else:
        print(x)

