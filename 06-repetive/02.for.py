# 1 ~ 100까지의 합계 구하기
sum = 0
for i in range(1,101):
    sum += i

print(f'sum of 1~100 is : {sum}')
print('-' * 30)

# 1~100까지 5의 배수의 합을 구하시오
sum = 0
for i in range(5, 101, 5):
    sum += i

sum = 0
for i in range(1, 101):
    if i % 5 == 0:
        sum += i

sum = 0 
for i in range(21):
    sum += i

print(sum*5)
