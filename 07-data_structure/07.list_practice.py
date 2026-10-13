"""
kim = [100, 98, 68]
park = [89, 67, 99]
lee = [int(input('숫자 입력 : '))for i in range(3)]

sumList = [0,0,0]

sumList[0] = sum(kim)
sumList[1] = sum(park)
sumList[2] = sum(lee)

print(sumList)

"""

users = []
sumList = []

class User:
    def __init__(self, name, score = [0,0,0]):
        users.append(name)
        sumList.append(sum(score))
        self.score = score
        self.name = name
        self.index = users.index(name)

    def update(self, score = [0,0,0]):
        self.score = score
        sumList[self.index] = sum(self.score)
        print(f'업데이트된 점수 : {self.score}, 업데이트된 총점 : {sumList[self.index]}, 평균 : {sumList[self.index]/len(score)}')

    
kim = User('kim',[100,100,100])
lee = User('lee')

print(users)
print(sumList)

lee.update([80,98,100])


print(users)
print(sumList)