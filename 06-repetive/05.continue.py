# break와 달리 continue는 루프를 탈출하지 않는다
# continue 아래는 실행하지 않고 다시 반복문으로 올라감

x = 1
while True:
    print(x)
    x += 1

    if x == 6:
        x += 2
        continue
    if x == 10:
        break

# 1~100까지 합계를 구하는데 4의 배수 제외

sum = 0
for i in range(1,101):
    if i % 4 == 0:
        continue
    sum += i
print(sum)