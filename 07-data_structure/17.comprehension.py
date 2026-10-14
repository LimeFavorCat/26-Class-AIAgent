# Comprehension
# for문이나 if문을 한줄로 표현
#   특히 리스트에서 많이 사용 -> list comprehension 라고 함

# 기본적인 사용법
result = [0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,'...'] # 0 x 100개
result = [0 for i in range(100)] # 한번에 표현
print(len(result),result,'\n')

result = ['&' for i in range(100)]
print(len(result),result,'\n')

result = [i+1 for i in range(100)]
print(len(result),result,'\n')

data = [3, 5, 7, 9]
result = [i**2 for i in data]
print(len(result),result,'\n')

# comprehension에 input이나 random같은 함수를 넣을 수 있다.
# numList = [int(input('숫자 입력 : ')) for x in range(5)]
# print('합계 : ', sum(numList))

# if와 for문이 함께 들어 있을 때 무조건 for문부터 실행
# if만 있는 경우는 맨 뒤에
# if - else 있는 경우는 맨 앞에
result = []
for num in range(1,20):
    if num % 2 == 0:
        result.append(num*3)


# if문 + 반복문 comprehension
result = [ num*3 for num in range(1,20) if num%2 == 0 ]
print(len(result),result,'\n')


# if - else로 배열 만들기
result = []
for num in range(1,20):
    if num % 2 == 0:
        result.append(num)
    else:
        result.append(0)

# if - else comprehension
result = [num if num % 2 == 0 else 0 for num in range(1,20)]


# 3항 연산자 + 반복문 comprehension
result = ['짝수' if i % 2 == 0 else '홀수' for i in range(1,6)]
print(len(result),result,'\n')

# for문이 중첩으로 들어갈 때
result = []
for x in [1,2,3]:
    for y in [10,20]:
        result.append((x,y))
result = [(x,y)for x in [1,2,3] for y in [10, 20]]
print(len(result),result,'\n')

result = [i*j for i in range(1,6) for j in range(1,6)]
print(len(result),result,'\n')


# for 문 중첩 + if
result = []
for x in range(1,4):
    for y in range(1,4):
        if (x+y) % 2 == 0:
            result.append((x,y))
print(len(result),result,'\n')

result = [(x,y) for x in range(1,4) for y in range(1,4) if (x+y) % 2 == 0]
print(len(result),result,'\n')

# for 문 중첩 + if-else
result = [(x,y) if (x+y) % 2 == 0 else (0,0) for x in range(1,4) for y in range(1,4) ]
print(len(result),result,'\n')


# unpacking
list1 = [(1,11), (2,21), (3,31)]
total = 0
for first, last in list1:
    total += first + last
    print(total)

list1 = [(i,i*10 + 1) for i in range(1,4)]
print(len(list1),list1,'\n')

result = [first + last for first, last in list1]
print(len(result),result,'\n')

# enumerate() : index 번호와 데이터를 tuple의 형태로 반환
t = [1,3,141,5,2,12,4,121,314]
for index, Value in enumerate(t):
    print(f'index : {index}, value : {Value}')

# zip() : 리스트들을 동일한 위치값을 묶어서 관리
#         두 리스트의 길이가 다를 경우 짧은 길이로 묶음

name = ['red_hair', 'raven', 'niri']
hp = [100,90,75]
mp = [100,0,250]

for i in zip(name,hp,mp):
    print(i)

for a, b in zip(name,hp):
    print(a*b)