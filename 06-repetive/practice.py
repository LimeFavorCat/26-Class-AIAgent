"""
문
1~100까지의 합계 구하기 (조건 : 사용자가 넣은 숫자의 배수만 합계 구하기)
"""
# 답변 1
num1 = int(input('합계를 구할 배수 입력하기 : '))
sum = 0
for i in range(num1, 101, num1):
    sum += i
print(f'1~100 사이 {num1}의 배수의 총합 : {sum}, 배수의 갯수 : {len(range(num1, 101, num1))}')

# 답변 2
sum = 0
count = 0
for i in range(1,101):
    if i % num1 == 0:
        sum += i
        count += 1
print(f'총합 : {sum}, 갯수 : {count}')

# class 활용 답변
class Multiple:
    def __init__(self, step, max):
        self.step = step
        self.max = max

    def sum(self):
        sum = 0
        for i in range(self.step, self.max, self.step):
            sum += i
        return sum

    def size(self):
        return len(range(self.step, self.max, self.step))

num1 = int(input('합계를 구할 배수 입력하기 : '))
num2 = int(input('합계를 구할 최댓값 입력하기 : '))
mul = Multiple(num1,num2)
print(f'1~{mul.max} 사이 {mul.step}의 배수의 총합 : {mul.sum()}, 배수의 갯수 : {mul.size()}')