# 2차원 리스트 : [[],[],[]]
# [10,[3,4,5],8,[4,5]] -> 1차원

name = ['이차원', '박수영', '최명길']
score = [[] for i in range(3)]

print(name)
print(score)


score[0].append(96)
score[0].append(78)
score[0].append(40)

score[1].append(88)
score[1].append(80)
score[1].append(90)

score[2].append(99)
score[2].append(100)
score[2].append(96)

print(score)

total = [0 for i in range(len(score))]
for i in range(3):
    total[i] = sum(score[i])
    print(f'{name[i]} : 총점 = {total[i]}, 평균 = {total[i]/len(score[i]):.2f}')