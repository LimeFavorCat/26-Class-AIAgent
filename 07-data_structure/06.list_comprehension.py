'''
문 : 사용자로부터 정수 4개를 입력받아 리스트에 넣고
리스트를 출력하기
'''


# numList = [0 for i in range(5)]
# print(numList)

# 자습
numList = []
for i in range(4):
    numList.append(int(input(f'리스트에 넣을 {i+1}번째 정수를 입력해주세요 : ')))
print(sum(numList))

# naive한 풀이
sum = 0
numList = [0,0,0,0]
numList[0] = int(input('숫자1 : '))
numList[1] = int(input('숫자2 : '))
numList[2] = int(input('숫자3 : '))
numList[3] = int(input('숫자4 : '))

sum = numList[0] + numList[1] + numList[2] + numList[3]
print(f'합계 : {sum}')

# for문 적용
numList = [0,0,0,0]
sum = 0
for x in range(4):
    numList[x] = int(input('숫자 : '))
    sum += numList[x]
print('합계 :',sum)

#comprehension
numList = [int(input(f'{i}번째 숫자를 입력해주세요 : ')) for i in range(4)]
print(numList)
print(type(numList))


numList =[]
sum = 0
for x in range(4):
    num = int(input('숫자 : '))
    numList.append(num)
    sum += num
print(sum)