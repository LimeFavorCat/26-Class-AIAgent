students = []
with open('11-file/data/test.csv','r', encoding = 'utf-8') as f:
    # lines = f.read().splitlines()
    # lines = f.readlines()
    # print(lines)

    # for line in lines:
    #     line = line.strip()
    #     line = line.split(',')
    #     students.append(line)

    students = [line.strip().split(',') for line in f.readlines()]

print(students)

result =''
for student in students:
    name, kor, eng, math = student
    total = int(kor) + int(eng) + int(math)
    avg = total / 3
    result += f'이름 : {name}, 국어 : {kor}, 수학 : {math}, 영어 : {eng}, 총점 : {total}, 평균 : {avg:.2f} \n'

print(result)
with open('11-file/data/result.txt','w',encoding='utf-8') as f:
    f.write(result)



# 이름:더조은, 국어:90, 영어:80, 수학: 80, 컴퓨터:78, 총점:358, 평균:87